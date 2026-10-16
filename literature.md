# Literature Log

Use this table for every paper you read. Do not claim a gap is open without
checking papers that cite the one you are reading.

| Field | What to record |
|---|---|
| Research question | Exact problem the paper solves |
| Assumptions | States, measurements, noise models allowed |
| Main result | Theorem, bound, or construction |
| Method | Analytic proof / numerical / experiment |
| Limitations | Cases explicitly excluded or left open |
| Proposed extension | What exact result would differ from this paper |

---

## Klyachko, Can, Binicioglu, Shumovsky (2008)

- **Citation**: A. A. Klyachko, M. A. Can, S. Binicioglu, A. S. Shumovsky,
  "Simple Test for Hidden Variables in Spin-1 Systems,"
  *Physical Review Letters* **101**, 020403 (2008).
- **DOI**: https://doi.org/10.1103/PhysRevLett.101.020403
- **System**: Qutrit (spin-1), five rank-one projectors
- **Inequality**: K = sum_i <P_i> <= 2 (noncontextual bound)
- **Quantum maximum**: K = sqrt(5) ~ 2.2361
- **Noise model**: None (ideal measurements)
- **Main result**: Derives the five-observable inequality and shows quantum violation
- **Limitations**: No noise analysis; ideal projective measurements assumed
- **Notes**: This is the foundational paper for the KCBS scenario

---

## Budroni, Cabello, Gühne, Kleinmann, Larsson (2022)

- **Citation**: C. Budroni, A. Cabello, O. Gühne, M. Kleinmann, J.-Å. Larsson,
  "Kochen-Specker contextuality,"
  *Reviews of Modern Physics* **94**, 045007 (2022).
- **DOI**: https://doi.org/10.1103/RevModPhys.94.045007
- **Scope**: Comprehensive review of KS contextuality definitions, proofs,
  experiments, graph-theoretic connections, and applications
- **Key sections to read**: Sec. II (definitions), Sec. IV (noise and experiments),
  Sec. VI (connections to other areas)
- **Notes**: Read this before proposing any extension — it surveys what is known

---

## Dutra, Baldijão, Terra Cunha (2026)  ← READ THIS FIRST

- **Citation**: A. C. R. Dutra, R. D. Baldijão, M. Terra Cunha,
  "How Quantum Contextuality disappears in the Classical Limit,"
  arXiv:2604.24735 (2026).
- **arXiv**: https://arxiv.org/abs/2604.24735
- **System**: KCBS (qutrit) and Peres–Mermin scenarios
- **Noise model**: Depolarizing channel — applied (a) before measurements and (b) between sequential measurements
- **Method**: Sequential correlators analyzed in both Schrödinger and Heisenberg pictures
- **Main result**: Shows depolarizing noise suppresses correlations required to witness contextuality in both KCBS and Peres–Mermin; resolves apparent paradox between state-dependent and state-independent contextuality
- **Does it cover amplitude damping?**: NO — only depolarizing throughout
- **Does it cover dephasing?**: Mentioned ONCE in a footnote (footnote 4, p.6) as an example of another decoherence channel, but never analyzed. Exact quote: *"Naturally Dp is not the only channel that captures decoherence. For instance, the dephasing map would also represent a decoherence process in which a pointer basis is perfectly selected by the environment."* — then dropped entirely.
- **Does it cover measurement noise (non-depolarizing)?**: NO
- **Conclusion section mentions other channels?**: NO — conclusion only discusses depolarizing. No future work section. No mention of dephasing thresholds.
- **KCBS threshold derived**: p_crit(ρ) = −(4/3) / (Sρ + 5/3) for general state ρ. For maximally violating state: p_max_crit = (5 + 3√5) / 20 ≈ 0.59. NOTE: this uses a different parameterization from your baseline — their p=1 means no noise, your p=0 means no noise. Same physics, opposite convention.
- **What is explicitly left open**: Dephasing channel (named but not analyzed); amplitude damping; any non-depolarizing channel; comparison of thresholds across channels.
- **Relevance**: This is the most directly competing paper. Footnote 4 is the smoking gun — they name dephasing as another valid decoherence model and immediately move on. That is your opening.

---

## Bozzetto, Hance (2026)

- **Citation**: E. Bozzetto, J. R. Hance,
  "Classical Limit: Dissipation of Spekkens' Generalised Contextuality under Decoherence,"
  arXiv:2605.09558 (2026).
- **arXiv**: https://arxiv.org/abs/2605.09558
- **System**: Generalised (Spekkens) contextuality framework — broader than KS contextuality
- **Noise model**: Decoherence (general)
- **Main result**: Studies when a decohering system loses generalised noncontextuality
- **Does it cover KCBS specifically?**: Unclear from abstract — need to read
- **Does it cover amplitude damping in KCBS?**: Unknown
- **Relevance**: Different notion of contextuality (Spekkens vs KS). Confirms the area is active in 2026. Read Sec. I to check overlap.

---

## Nguyen, Doan, Nguyen (2026)

- **Citation**: K. Nguyen, D. M. Doan, H. Q. Nguyen,
  "Coexistence of CHSH Nonlocality and KCBS Contextuality in a Single Quantum State,"
  arXiv:2604.04816 (2026).
- **arXiv**: https://arxiv.org/abs/2604.04816
- **System**: Hybrid qubit–qutrit; qutrit carries KCBS test
- **Noise model**: None mentioned in abstract
- **Main result**: Shows CHSH nonlocality and KCBS contextuality can coexist in one state
- **Relevance**: Low — different question. Confirms KCBS is active research area.

---

## Shaham, Eisenberg (2014)  ← FULL TEXT READ

- **Citation**: A. Shaham, H. S. Eisenberg,
  "The Effect of Decoherence on the Contextual and Nonlocal Properties of a Biphoton,"
  arXiv:1410.3640 (2014).
- **arXiv**: https://arxiv.org/abs/1410.3640
- **System**: Polarization biphotons (qutrit subspace) — NOT a clean qutrit. A biphoton is two photons in the same mode; it lives in a 3D symmetric subspace of a 4D two-qubit space. Physically different from a single spin-1 qutrit.
- **Three channels tested**:
  1. **Dephasing** (one-field): E(ρ) = (1−P)ρ + P·σ₁ρσ₁ — single Pauli kick
  2. **Two-field**: E(ρ) = (1−P)ρ + (P/2)σ₁ρσ₁ + (P/2)σ₂ρσ₂
  3. **Isotropic** (three-field): E(ρ) = (1−P)ρ + (P/3)(σ₁ρσ₁ + σ₂ρσ₂ + σ₃ρσ₃) — this is depolarization
- **Method**: Experimental only. Theoretical predictions shown as solid lines on graphs but no analytic formula is derived or stated in the paper.
- **Key result for dephasing**: KCBS violation lost at P ∼ 0.17 (read from graph, Fig. 2a). Nonlocality preserved for all P except P = 0.5.
- **Does it give an analytic threshold formula for dephasing?**: NO. The threshold P ∼ 0.17 is read off a graph. No closed-form expression is written anywhere in the paper.
- **Does it cover amplitude damping?**: NO — all three channels are unital. Amplitude damping is non-unital and is not studied.
- **System difference**: Biphoton qutrit ≠ spin-1 qutrit. The KCBS projectors are constructed differently (Eq. 3 in their paper uses a two-photon decomposition). The noise channels act on each photon independently, not on the qutrit as a whole. This is a physically different noise model from yours.
- **What is left open**:
  - Analytic formula for KCBS threshold under dephasing (for any system)
  - Analysis for a single spin-1 qutrit (not a biphoton)
  - Non-unital channels (amplitude damping)
  - Comparison of thresholds across channels analytically
- **Relevance**: HIGH — confirms dephasing suppresses KCBS contextuality experimentally and gives a rough threshold (~0.17 in their P convention). Your work derives the exact analytic formula for a clean qutrit and explains why the threshold sits where it does.

---

## Marvian (2020)  ← IMPORTANT — read this

- **Citation**: I. Marvian,
  "Inaccessible information in probabilistic models of quantum systems, non-contextuality inequalities and noise thresholds for contextuality,"
  arXiv:2003.05984 (2020).
- **arXiv**: https://arxiv.org/abs/2003.05984
- **System**: General D-dimensional quantum system (qubit and qutrit covered)
- **Noise model**: General noise channel — derives threshold in terms of **average gate fidelity**
- **Main result**: Under sufficiently strong noise any quantum system becomes preparation non-contextual. Threshold: average gate fidelity ≤ 1/D·(1 + 1/2 + ... + 1/D). For D=3 (qutrit): fidelity ≤ 1/3·(1 + 1/2 + 1/3) = 11/18 ≈ 0.611
- **Notion of contextuality**: Preparation contextuality (Spekkens framework) — NOT the same as KS/KCBS contextuality
- **Does it cover KCBS specifically?**: No — different notion of contextuality
- **Does it cover amplitude damping or dephasing in KCBS?**: No
- **What is left open**: KS contextuality thresholds for specific channels; connection between preparation contextuality threshold and KCBS witness threshold
- **Relevance**: MEDIUM — uses a different framework but the threshold result is related. Confirms the area is active. The distinction between preparation contextuality and KS contextuality must be explicit in your paper.

---

## arXiv search results summary (October 2026)

| Search string | Result |
|---|---|
| `KCBS noise contextuality` | Found Dutra 2026 (depolarizing only) |
| `KCBS amplitude damping` | NO RESULTS |
| `KCBS dephasing` | NO RESULTS |
| `contextuality dephasing qutrit` | NO RESULTS |
| `contextuality noise qutrit channel` | Found Bozzetto 2026 (generalised contextuality) |
| `contextuality depolarizing qutrit` | No new results |

**Preliminary gap assessment**: No arXiv paper found studying dephasing or amplitude damping in the KCBS scenario. This is a candidate gap — but requires checking Google Scholar citations of Klyachko 2008 before concluding.

---

## Still to check (manual — requires browser)

- [x] Read Dutra 2026 full text — dephasing named in footnote 4 but never analyzed. No future work section.
- [ ] Read Shaham 2014 full text — confirm exactly which unital channels were tested; check whether dephasing threshold was derived analytically
- [ ] Read Marvian 2020 full text — check whether KCBS-specific results appear anywhere
- [ ] Read Budroni 2022 Sec. IV — check whether non-depolarizing channels in KCBS are discussed
- [ ] Google Scholar: `"Simple Test for Hidden Variables in Spin-1 Systems" cited by` — filter 2020–2026, scan for noise analyses
- [ ] Google Scholar: `KCBS dephasing contextuality threshold`

## Parameterization note — important for your code

Dutra 2026 writes their depolarizing channel as Dp(ρ) = p·ρ + (1−p)·I/d
Your baseline writes it as depolarize(ρ, p) = (1−p)·ρ + p·I/3

These are the same channel with p_theirs = 1 − p_yours.
Dutra's p_max_crit ≈ 0.59 corresponds to your p* ≈ 0.41. Same result, different variable.
When you write your paper, pick one convention and state it explicitly.
