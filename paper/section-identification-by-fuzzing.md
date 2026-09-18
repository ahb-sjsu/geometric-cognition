# 9. Identifying the observer before predicting its deliberation

*Drafted 2026-09-18 to replace Sections 9.1 and 9.2 of the working paper. It is written to sit between Section 8 and the measurement strategy of Section 10. The registration it refers to is `experiments/H1/PREREG-H1-DRAFT.md` in the repository.*

Every prediction in Section 8 begins with a boundary that is located before deliberation is measured. The location has to come from the participant's own observer, and it cannot come from a model fitted to the choices it is then used to explain. The foundational paper states that condition as a proposition, and four registered designs in this programme were refused for the same defect, each of them selecting stimuli by the prediction of a metric fitted to the subject under test. This section adopts the construction that replaced them. The observer is not fitted. It is fuzzed.

## 9.1 The structure label comes from the generator

A fuzz perturbation is built in stimulus space before the participant answers. Its axis, its size and the variance of everything around it are set by the generator, so the label that says which direction a trial tests is a fact about the construction rather than a prediction about the participant. That is the label the admission filter found missing when it ruled the earlier instrument inadmissible, and it is available here without any estimation step. Nothing in the design is admitted or rejected on the basis of how the participant is expected to behave.

## 9.2 The unit is a set, and the probe never changes

A trial shows an ideal and a set of options. Two options are the probe, and they differ mainly along one target attribute at a chosen separation. The rest of the set is context, and the context is what the budget is defined on. A finite resolution budget retains the directions that carry workload variance and discards the rest, so the same probe pair is a resolved distinction when its attribute carries high variance in the context and an unresolved one when it carries low variance. The probe is presented byte for byte the same in both roles, at the same positions, with the same labels. Only the context changes.

This gives the exact null the programme's pair designs never had. Any noise that acts on the probe sees identical input in every role of a triplet, so it predicts no difference between roles. So does generic difficulty, since the probe's wording, length and separation are unchanged. A role difference, if one appears, is a property of the context, and the context is the workload.

Attributes are exchangeable. Every attribute spans the same range around the same registered ideal, attribute order and labels are drawn per triplet from a pool, and the four sign patterns that decide whether the nearer option has the smaller value and whether the pair straddles the ideal are stratified exactly in every cell. The construction check of the evaluator version of this design, recorded in the C3 note, reached those stratifications exactly and placed the top eigenvector of the in-context workload within a few degrees of the high attribute in every prompt. The human version reuses that generator.

## 9.3 The calibration block identifies the observer

The first block a participant completes is the fuzz. Each target attribute is presented in each role at a ladder of separations, and the participant reports which probe option is nearer the ideal. The quantity read from this block is the sensitivity profile, one psychometric function per attribute and role, fitted with a lapse rate, a response position term and a free upper asymptote. Geometric Evaluation Theory says the indifference threshold of a finite observer is its budget rather than a free parameter, and the signature of a discarded direction is a low asymptote rather than a shifted threshold. The endpoint is therefore accuracy at the largest separation by role, with the fitted plateau reported beside it, since a fitted plateau is not identified while the function is still rising at the top of the ladder.

Two identified quantities leave this block. The first is the participant's retained subspace, read as the set of attribute and role cells whose asymptote is near ceiling. The second is the separation on each cell at which accuracy reaches a registered criterion, which is the location of the resolution boundary for that participant on that cell. Both are identified on evidence disjoint from every trial in which deliberation is measured.

## 9.4 The test block measures deliberation where the boundary was found

The second block presents new probe sets, constructed and not selected, at separations placed on a grid around each cell's identified boundary. The dependent measures are response latency after reading is complete, confidence, and the number of options inspected when options are revealed on request. The prediction of the Deliberative Recruitment Hypothesis is that each process measure peaks at the identified boundary, and that the peak sits at a larger separation in the low role than in the high role by the amount the calibration block identified.

The null again holds by construction. Under any account in which effort depends on the probe alone, the peak location is the same in every role, because the probe is the same. Under a sequential sampling account with drift set by the probe's separation, the peak location is also the same in every role. The role dependence of the peak location is the quantity the hypothesis is staked on, and it is the one quantity in Section 8 that neither competitor predicts.

## 9.5 The second budget, and its manipulation check

Workload variance is the budget the theory is defined on. A resource load such as a response deadline is a second manipulation, and the programme's record shows that a load can degrade an evaluator's reliability without moving its effective rank. The load therefore enters this design with its own check. Both blocks are repeated under the load. The load has moved the budget only if the difference between roles in the calibration block grows under it, which is a difference of differences on a quantity with no fitted metric in it. Where that check fails, the load's deliberation data are reported and are not read as evidence about budgets. Where it passes, the predicted displacement of the deliberation peak under the load is the strongest test the hypothesis offers, and it is the test that Prediction 3 named.

## 9.6 What the design cannot do

The named-axis fuzz measures sensitivity to the directions it perturbs. A direction the generator never moves is invisible to it. The programme's spectral probe supplies the discovery mode, in which random perturbation directions, the response graph over them and the agreement of three intrinsic dimension estimators certify whether the response landscape has coherent low dimensional geometry at all. That mode is not part of this registration and is the natural follow up if the calibration block returns profiles that no small set of retained directions explains.

Human data are also expensive at psychometric resolution. A usable asymptote per cell needs on the order of tens of trials, and the number of attributes, roles, separations and loads multiplies. The registration fixes the trial counts from a pilot and states the participant number that follows, so that the design is sized on the calibration block and not on the deliberation effect, whose scale is unknown before the pilot.

Finally, the generator can leak a cue. The second rebuild of the evaluator design was refused because its workload created a cue that a position or magnitude heuristic could follow. The human registration inherits the counterbalancing that answered it and adds the pilot check that heuristics following position, label or magnitude predict no role effect on the built stimuli.
