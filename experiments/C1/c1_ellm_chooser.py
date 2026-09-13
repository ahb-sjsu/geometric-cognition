# -*- coding: utf-8 -*-
"""The pinned hosted evaluator, and the preflight that checks it is still itself.

C1's evaluator is the NRP managed gateway's `qwen3`. The gateway exposes no
revision, no underlying model name and no weights hash. A model entry carries an
alias, an object type, an owner, and a creation timestamp, and nothing else. The
alias can therefore be repointed at a different model without the identifier
changing, and the timestamp is the only field that would show it.

So the pin is enforced rather than recorded. `preflight_model_pin` refuses to run
when the timestamp has moved, which converts an unverifiable provenance claim
into a check that fails loudly. It does not make the evaluator reproducible. It
makes an evaluator that has silently changed impossible to run against by
accident.

The timeout policy comes from a stall. Under five attempts at a 300 second
timeout, `gpt-oss` held sixteen idle connections for forty three minutes and was
indistinguishable from slow work. A run that cannot finish an item within the
registered deadline records it as failed and moves on.
"""
from __future__ import annotations

import concurrent.futures as cf
import json
import random
import re
import time
import urllib.request


class PinViolation(RuntimeError):
    """The pinned model is not the model the gateway is serving."""


def preflight_model_pin(cfg: dict, token: str) -> dict:
    """Verify the pinned alias still resolves to the pinned creation timestamp.

    Raises rather than warns. A gate whose evaluator has changed underneath it is
    not the gate that was registered.
    """
    ev = cfg["evaluator"]
    req = urllib.request.Request(ev["gateway"] + "/models",
                                 headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    entry = next((m for m in data.get("data", []) if m["id"] == ev["model_id"]), None)
    if entry is None:
        raise PinViolation(
            f"pinned model {ev['model_id']!r} is no longer in the catalog; "
            f"available: {sorted(m['id'] for m in data.get('data', []))}")
    if int(entry.get("created", -1)) != int(ev["created"]):
        raise PinViolation(
            f"pinned model {ev['model_id']!r} has created={entry.get('created')} "
            f"but the registration pinned {ev['created']}. The alias has been "
            f"repointed, so this is a different evaluator and the gate does not "
            f"run against it.")
    return {"model_id": ev["model_id"], "created": entry.get("created"),
            "owned_by": entry.get("owned_by"), "verified_utc":
                time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


class EllmChooser:
    """Asks the pinned hosted model which of two options is nearer.

    Same reading discipline as the local chooser. A single letter, both
    presentation orders shown for every pair, an unparsable answer dropped and
    counted. The deliberation the registration requires is why `max_tokens` is
    large; a reasoning model writes its answer only after it has reasoned.
    """

    def __init__(self, cfg: dict, token: str):
        ev = cfg["evaluator"]
        self.url = ev["gateway"] + "/chat/completions"
        self.model = ev["model_id"]
        self.token = token
        self.max_tokens = int(ev.get("max_tokens", 512))
        self.temperature = float(ev.get("temperature", 0))
        self.timeout = float(ev.get("per_item_timeout_s", 60))
        self.attempts = int(ev.get("max_attempts", 3))
        self.concurrency = int(cfg.get("concurrency", 16))
        self.template = cfg["chooser_prompt_template"]
        self.unparsed = 0
        self.failed = 0
        self.reasoning_tokens: list[int] = []
        # Why an item produced no letter, not only that it did not. Truncation
        # is not missing at random, because it tracks reasoning length and
        # reasoning length tracks difficulty, so drops concentrate on the hard
        # pairs and bias a calibration toward the easy ones.
        self.finish_reasons: dict[str, int] = {}
        self.escalations = 0

    def _one(self, ideal: str, first: str, second: str, budget: int | None = None,
             escalated: bool = False):
        """One comparison, with a single bounded escalation on truncation.

        A reasoning model that runs out of room writes no letter, and the item
        is then dropped. Dropping is not harmless here, because truncation
        tracks reasoning length and reasoning length tracks how hard the pair
        is, so the drops concentrate on the hard pairs and bias a calibration
        toward the easy ones. An item that hit the ceiling is therefore given
        room once rather than discarded. The escalation is single and bounded,
        so a pathological item cannot consume the budget indefinitely.
        """
        budget = int(budget or self.max_tokens)
        body = json.dumps({
            "model": self.model,
            "messages": [{"role": "user", "content": self.template.format(
                ideal=ideal, first=first, second=second)}],
            "max_tokens": budget,
            "temperature": self.temperature}).encode()
        for attempt in range(self.attempts):
            try:
                req = urllib.request.Request(
                    self.url, data=body,
                    headers={"Authorization": f"Bearer {self.token}",
                             "Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    d = json.load(r)
                ch = d["choices"][0]
                rt = ((d.get("usage") or {}).get("completion_tokens_details") or {}
                      ).get("reasoning_tokens", 0)
                content, finish = ch["message"].get("content"), ch.get("finish_reason")
                if finish == "length" and not escalated:
                    self.escalations += 1
                    return self._one(ideal, first, second, budget * 2, True)
                return content, finish, rt
            except Exception:
                if attempt == self.attempts - 1:
                    return None, "deadline", 0
                time.sleep((2 ** attempt) + random.random())
        return None, "deadline", 0

    def prefers_first(self, ideal: str, pairs, batch: int | None = None) -> list[float]:
        """`batch` is accepted and ignored, so this is drop-in for the local
        chooser. Concurrency here is the gateway's fair-use cap, not a batch
        size, and it comes from the registration rather than the caller."""
        out: list[float] = [float("nan")] * len(pairs)
        with cf.ThreadPoolExecutor(max_workers=self.concurrency) as ex:
            futs = {ex.submit(self._one, ideal, f, s): i
                    for i, (f, s) in enumerate(pairs)}
            for fut in cf.as_completed(futs):
                i = futs[fut]
                content, finish, rt = fut.result()
                self.reasoning_tokens.append(rt)
                self.finish_reasons[str(finish)] = (
                    self.finish_reasons.get(str(finish), 0) + 1)
                if finish == "deadline":
                    self.failed += 1
                    continue
                m = re.search(r"\b([AB])\b", content.upper()) if content else None
                if m:
                    out[i] = 1.0 if m.group(1) == "A" else 0.0
                else:
                    self.unparsed += 1
                    k = f"unparsed_{finish}"
                    self.finish_reasons[k] = self.finish_reasons.get(k, 0) + 1
        return out
