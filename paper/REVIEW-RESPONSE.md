# Response to the review of `olgc.tex`

*Drafted 2026-09-12. The review is correct on every mathematical point. This file
triages it, and works out the one place where two of its points combine into a
result rather than a repair.*

---

## 1. Triage

| # | Point | Verdict | Cost |
|---|---|---|---|
| 1 | Gauge freedom between `Φ` and `G`; they are not separately identifiable | **Correct.** Becomes Theorem below | A theorem and a definition |
| 2 | `C − t` is not intrinsic on a Riemannian manifold | **Correct.** Resolved by the same theorem rather than by fiat | A restriction stated in Section 2 |
| 3 | Proposition 3 is too easy | **Correct.** Needs the capacity bound, which is Open 6 | Open, and the hardest item |
| 4 | Proposition 5 conflates the induced order with observed behaviour | **Correct.** Two layers, and `π` is decorative unless stated | A rewrite of one proposition |
| 5 | Falsifiers that rest on observing no effect are not falsifiers | **Correct.** Each needs an equivalence bound `δ_min` | One number per falsifier, before registration |
| 6 | Positioning against the existing literature | **Correct, and both citations check out** | A paragraph, and a narrowed claim |
| 7 | Whitney stratification is conjectural and must not carry the theory | **Correct, and already the programme's own position** | Nothing. Keep it at Phase IV |

On 6, both works the review names are real and both are close. Jurewicz,
Sleezer, Mehta, Hayden and Ebitz, "Irrational choices via a curvilinear
representational geometry for value", *Nature Communications* 15, 2024,
doi:10.1038/s41467-024-49568-4, reports value encoded on a curved manifold in
vmPFC and shows the curvature predicts a specific decoy-dependent irrationality.
That is the nearest neighbour to this paper's core move and it is empirical,
which this paper is not yet. arXiv:2512.12225, "A Geometric Theory of Cognition",
December 2025, puts cognition on a learned Riemannian manifold as gradient flow
of a scalar potential. Neither carries a rank budget, an observer-relative read
operator, or modular identification. The review is right that novelty has to be
staked on the conjunction and not on cognition being geometric.

On 7, this is already the programme's position and it was reached independently
on the economics side. See `geometric-economics/stratification-thesis.md`, which
says in its own words that the four results reading naturally as stratification
are the discovery set and cannot test the thesis, and that a registered
prediction is needed. The reviewer's "no discriminating measurement yet" and that
document's "none of them is evidence for it" are the same sentence.

---

## 2. Points 1 and 2 are the same point, and together they give a theorem

The review treats the gauge freedom and the non-intrinsic `C − t` as two separate
problems. They are coupled, and the coupling is the useful part.

**The unbudgeted evaluation really is invariant under any diffeomorphism.** The
review's construction is right. For any smooth invertible `h`, setting
`Φ' = h∘Φ`, `t' = h(t)` and `G' = (h⁻¹)*G` leaves every geodesic distance and
therefore every prediction unchanged. Taken alone this is bad news, because the
gauge group is infinite dimensional and almost nothing is identified.

**The budgeted evaluation is not.** The rank budget is built from

```
M_ω = E_ω[ G^{1/2} (C − t)(C − t)ᵀ G^{1/2} ]
```

and `C − t` is a coordinate difference. Under a general diffeomorphism `M_ω` is
not carried to anything in particular, so `d_k` is not invariant. This is exactly
the review's second point, and it means the two objects in the paper have
different gauge groups.

That is the result. **The budget is what cuts the gauge group down.**

> **Observer equivalence.** Let `Y` be a vector space with `G` positive definite.
> For an invertible affine `h(y) = Ay + b`, put `Φ' = h∘Φ`, `t' = h(t)`,
> `C' = h(C)` and `G' = A⁻ᵀ G A⁻¹`. Then
>
> 1. `d_{G'}(Φ'(w), t') = d_G(Φ(w), t)` for every `w`, and
> 2. `M'_ω = Q M_ω Qᵀ` for an orthogonal `Q`, so the two have the same
>    eigenvalue spectrum, and
> 3. `d_k` is unchanged for every `k`.
>
> Conversely, for `h` not affine, (1) still holds and (2) and (3) fail in general.
> So the gauge group of the budgeted theory is the affine group, not the
> diffeomorphism group.

*Proof of (2).* Write `S = E_ω[(C − t)(C − t)ᵀ]`, so `M_ω = G^{1/2} S G^{1/2}`.
Under the action `S' = A S Aᵀ`, so `M'_ω = (G')^{1/2} A S Aᵀ (G')^{1/2}`. Put
`N = (G')^{1/2} A`. Then `Nᵀ N = Aᵀ G' A = Aᵀ A⁻ᵀ G A⁻¹ A = G`, so by polar
decomposition `N = Q G^{1/2}` with `Q` orthogonal. Hence
`M'_ω = N S Nᵀ = Q M_ω Qᵀ`. Part (3) follows because the top-`k` projector
transforms as `Π'_k = Q Π_k Qᵀ` and `Q` is an isometry. ∎

Checked numerically at `n = 5` over random positive-definite `G`, random
invertible `A` and random `b`. Spectra agree and `d_k` is invariant at
`k = 1, 2, 3`.

### What this buys

**It answers point 2 without an arbitrary choice.** The paper does not have to
*decide* to work on a vector space. The rank budget already requires it. If the
theory keeps the budget in its present form, `Y` is a vector space and `C − t`
is intrinsic to the affine structure. If it wants a general manifold, the budget
must be rebuilt in `T_tY` through the logarithmic map, as the review says, and
then the gauge group is the isometries of the base point's tangent space. Either
way the choice is forced by the budget and is not a matter of taste.

**It converts the identification problem into a quotient.** What is identifiable
is the class `[Φ, G, t]` under the affine action, and concretely the pullback
`g_W = Φ*G` on task space together with the spectrum of `M_ω`. The paper should
state identification on the quotient, which is what the review recommends.

**It retires degrees of freedom, countably.** This is the part that bears on
Open 6. Going from the diffeomorphism group to the affine group takes the
unidentified directions from infinite dimensional to `n² + n`. That is not the
capacity bound Open 6 asks for, and it does not close it. But it is a first
non-trivial statement of the form Open 6 wants, and it says the budget is the
component doing the work. **The budget is not only a psychological assumption.
It is the source of the theory's identification content.** That reading is worth
having in the paper whatever happens to Open 6.

---

## 3. The remaining items, and what each costs

**Proposition 5, the two layers.** The review is right that the proposition
delivers an order and the paper claims behaviour. State it as two arrows,
`(Φ, G, B, K) → preference` and `(preference, π) → behaviour`, and say which one
the proposition covers. Then either `π` is degenerate and should be dropped from
the observer tuple, or it is not and Proposition 5 needs it as a hypothesis. The
paper cannot have it both ways, and the honest version is cheap to write.

**Falsifiers.** Each falsifier that rests on an absence needs a `δ_min` and an
equivalence test, two one-sided tests or an interval, fixed before registration.
This is mechanical and should be done before `PREREG-C1` freezes, not after. The
boundary registration on the economics side has the same structure and is worth
copying.

**Proposition 3b.** The capacity bound is the hard item and is genuinely open.
The theorem above is a down payment and not a solution. A realistic first step is
to bound the realizable choice class under fixed menu-independent `K` and a rank
budget `k`, which is a shattering question about the family of orders induced by
rank-`k` quadratic forms, and that family is small enough to be countable in `n`
and `k`.

---

## 4. What I would not change

The review's closing is right and the paper should not be talked out of its own
framing. "We do not offer a better theory of choice. We offer the condition under
which this one can be wrong" is the correct sentence, and Open 6 stated as
brutally as it is stated now is a feature. The theorem above makes Open 6 sharper
rather than removing it.
