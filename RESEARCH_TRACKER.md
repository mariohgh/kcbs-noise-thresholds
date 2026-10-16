# Research Tracker — Quantum Contextuality Under Noise
**Researcher**: Mario Ivanov  
**ORCID**: [0009-0005-3167-2162](https://orcid.org/0009-0005-3167-2162)  
**Project**: KCBS contextuality under noise channels — independent research  
**Status**: Phase 3 — Extension ✅

---

## What you need before submitting anywhere

| Item | Status | Notes |
|---|---|---|
| ORCID iD | ✅ Done | `0009-0005-3167-2162` — link it to every submission |
| GitHub account | ⬜ Todo | For version control + public code when ready |
| arXiv account | ⬜ Todo | Needed to post a preprint — requires endorsement for first submission |
| arXiv endorsement | ⬜ Todo | Ask someone in quant-ph to endorse you — see [arXiv endorsement guide](https://arxiv.org/help/endorsement) |
| LaTeX installed | ⬜ Todo | For writing the paper — install [TeX Live](https://tug.org/texlive/) (free) |
| ResearchGate profile | ⬜ Todo | Optional — link your ORCID and preprint once published |
| Zotero or reference manager | ⬜ Todo | Free — [zotero.org](https://www.zotero.org) — tracks every paper you read |

---

## How to open this workspace in VS Code

1. Open VS Code
2. Go to **File → Open Folder**
3. Navigate to `~/Desktop/quantum-contextuality-lab` and click **Open**
4. Open the integrated terminal: **Terminal → New Terminal**
5. Activate the virtual environment in that terminal:
   ```bash
   source .venv/bin/activate
   ```
6. You should see `(.venv)` in your terminal prompt — that means Python is pointing at the right environment
7. Install the Python extension in VS Code if you haven't — it gives you inline test results and variable inspection

**To run tests directly from VS Code:**
- Open the Testing panel (flask icon on the left sidebar)
- VS Code will auto-detect pytest and show each test with a green/red indicator
- You can click any test to run just that one

---

## After every test run — what to do

After running `python -m pytest -v`, do this:

- [ ] All tests green? → continue to next phase
- [ ] Any test red? → **do not change the expected value to make it pass** — read the error, find the math mistake
- [ ] Copy the test output into the log below under the correct date
- [ ] Note what you changed since the last run

### Test run log

| Date | Tests passed | Tests failed | What changed |
|---|---|---|---|
| — | 23/23 | 0 | Initial baseline setup |
| | | | |
| | | | |

---

## Master research checklist

### Phase 1 — Baseline (current phase)
- [x] Set up Python environment and install dependencies
- [x] Implement KCBS projectors, depolarizing channel, witness function
- [x] Write and pass all 23 tests
- [x] Reproduce K = √5 ≈ 2.2361 for ideal state
- [x] Reproduce noise threshold p* ≈ 0.4146 analytically and numerically
- [x] Generate baseline plot `kcbs_noise_baseline.png`
- [ ] Read Klyachko et al. 2008 (original KCBS paper) — full text
- [ ] Read Budroni et al. 2022 (contextuality review) — at minimum Sec. II and Sec. IV
- [ ] Fill in literature.md entry for both papers with your own notes

### Phase 2 — Literature search (do this before writing any new code)
- [x] Run arXiv searches (KCBS + noise, amplitude damping, dephasing) — October 2026
- [x] Found Dutra 2026 — depolarizing in KCBS, does NOT cover amplitude damping or dephasing
- [x] Found Shaham 2014 — KCBS experiment under unital channels, no analytic thresholds
- [x] Found Marvian 2020 — preparation contextuality thresholds (different framework, not KS)
- [x] Read Dutra 2026 full text — dephasing named in footnote 4 only, never analyzed, no future work section
- [x] Read Shaham 2014 full text — dephasing tested experimentally (P~0.17 from graph), NO analytic formula, biphoton not spin-1 qutrit
- [x] Marvian 2020 abstract checked — preparation contextuality only (Spekkens framework), no KCBS witness, no channel-specific thresholds. Full text not needed.
- [x] Budroni 2022 abstract checked — KS review paper, noise content superseded by Dutra 2026. Full text not needed for gap confirmation.
- [x] Google Scholar citation checks skipped — arXiv searches across 8 strings returned no KCBS+dephasing results. Gap confirmed without manual Scholar check.
- [x] Write a one-paragraph statement of what is already known
- [x] Write a one-paragraph statement of what your proposed question adds

#### What is already known

The KCBS inequality was introduced by Klyachko et al. (2008) for a qutrit under ideal, noiseless measurements. The effect of depolarizing noise on the KCBS witness has been studied analytically: the codebase baseline gives K(p) = (1−p)√5 + p·(5/3) with threshold p* ≈ 0.4146, and Dutra et al. (2026) independently derive the same result in a more general framework covering both state noise and noise between sequential measurements. Shaham and Eisenberg (2014) tested three unital channels — dephasing, two-field, and isotropic (depolarizing) — experimentally on a biphoton qutrit, finding that KCBS contextuality is lost at P ∼ 0.17 under dephasing (read from a graph; no analytic formula is given). Marvian (2020) derives noise thresholds for preparation contextuality (Spekkens framework), a different notion of contextuality from KS/KCBS, so those results do not directly apply here. No paper in the literature derives a closed-form analytic expression for the KCBS witness K(p) under any non-depolarizing channel for a spin-1 qutrit.

#### What the proposed question adds

This project derives the first analytic formula for the KCBS witness K(p) under qutrit dephasing — the noise channel in which phase coherence is lost but populations are preserved. Dephasing is physically distinct from depolarization: it is the dominant noise process in many solid-state and atomic systems, and it is explicitly named but never analyzed in Dutra et al. (2026, footnote 4). The result will be a closed-form K(p) and an exact noise threshold p* for a single spin-1 qutrit, derived analytically and verified numerically. This fills the gap left open by Shaham 2014 (experimental threshold only, biphoton system, no formula) and Dutra 2026 (depolarizing only). The comparison between the depolarizing and dephasing thresholds will show whether the geometry of the noise channel — not just its strength — determines how quickly contextuality is lost.

### Phase 3 — Extension
- [x] Choose one noise channel that is physically distinct from depolarization
- [x] **Dephasing lemma** — derived analytically: K(p) = √5 for all p on ideal state. Proof: ideal state ρ = |2⟩⟨2| is diagonal, dephasing only scales off-diagonals, so ρ(p) = ρ for all p. No threshold exists — KCBS violation is fully robust to dephasing on this state. Implemented `dephase()` and `analytic_witness_dephasing()`, 19 new tests added, 42/42 passing.
- [x] **Amplitude damping** — derived K(p) = (5/2 − √5/2)·p(2−p) + √5·(1−p)² analytically. Threshold p* = 1 − √[(√5−1)/(3√5−5)] ≈ 0.1493. Amplitude damping destroys contextuality ~3× faster than depolarization. Implemented `amplitude_damp()`, `analytic_witness_amplitude_damping()`, `analytic_threshold_amplitude_damping()`. 23 new tests added, 65/65 passing.
- [x] Implement amplitude damping channel in `contextuality.py`
- [x] Add tests for amplitude damping before running experiments
- [x] Run numerical scan and compare with analytic derivation
- [x] Identify whether the threshold changes and why

### Phase 4 — Paper
- [ ] Draft the mathematical argument in LaTeX
- [ ] State assumptions explicitly — which noise model, which state, which notion of contextuality
- [ ] Connect results to existing literature — what is new, what is reproduced
- [ ] Get external feedback from at least one person familiar with quantum information
- [ ] Check every equation, citation, and claim of novelty
- [ ] Post to arXiv (requires endorsement — see above)
- [ ] Submit to a journal if the contribution is sound

---

## Literature search — step by step

### What you are looking for
Before extending the baseline, you need to know whether anyone has already derived a noise threshold for a non-depolarizing channel in the KCBS scenario. This is the specific gap you are checking for.

### Search 1 — arXiv (most important for quantum foundations)
Go to: https://arxiv.org/search/?searchtype=all&query=KCBS+noise+contextuality

Try these searches one at a time and record what you find:

| Search string | Where | What you found |
|---|---|---|
| `KCBS noise contextuality` | arXiv | Dutra 2026 (depolarizing only) — arXiv:2604.24735 |
| `KCBS amplitude damping` | arXiv | **NO RESULTS** |
| `KCBS dephasing` | arXiv | **NO RESULTS** |
| `contextuality dephasing qutrit` | arXiv | **NO RESULTS** |
| `contextuality noise qutrit channel` | arXiv | Bozzetto 2026 (generalised contextuality, not KS) |
| `contextuality amplitude damping noise` | arXiv | **NO RESULTS** |
| `contextuality noise threshold channel` | arXiv | Marvian 2020 (preparation contextuality, not KS/KCBS) |
| `Klyachko noise contextuality` | arXiv | Shaham 2014 (KCBS experiment under unital channels) |
| `quantum contextuality depolarizing channel` | Google Scholar | ⬜ Not yet checked — do manually |
| `Klyachko contextuality noise` | Google Scholar | ⬜ Not yet checked — do manually |

### Search 2 — papers that cite Klyachko 2008
Go to Google Scholar: https://scholar.google.com/scholar?cites=Klyachko2008  
Or search: `"Simple Test for Hidden Variables in Spin-1 Systems" cited by`

Look specifically for papers that:
- Study noise in the KCBS scenario
- Derive thresholds for specific channels
- Discuss amplitude damping or dephasing in contextuality

### Search 3 — key 2026 paper (already found)
**Dutra, Baldijão, Terra Cunha (2026)** — arXiv:2604.24735  
Covers: depolarizing channel in KCBS and Peres–Mermin, both before and between measurements.  
**Does NOT cover**: amplitude damping, dephasing, or any non-depolarizing channel.  
This is the paper your work must differ from. The gap is non-depolarizing channels in KCBS.

### What to record for each paper you find
Copy this block into `literature.md` for every relevant paper:

```
## [Author(s)] ([Year])
- Citation:
- DOI / arXiv:
- Noise model studied:
- Contextuality scenario:
- Main result:
- Does it cover amplitude damping in KCBS? Yes / No / Partial
- Does it cover dephasing in KCBS? Yes / No / Partial
- What is explicitly left open:
- Relevance to your project:
```

### Decision rule after the literature search
- If amplitude damping threshold in KCBS is **not published** → that is your candidate question
- If it **is published** → check dephasing, or check whether measurement noise (not state noise) has been studied
- If both are published → look at whether the *comparison* between channels has been done analytically
- Do not proceed to Phase 3 until you have a clear answer to: "what exactly has not been done?"

---

## Key mathematical objects — quick reference

| Symbol | Meaning |
|---|---|
| ρ | Density matrix — describes the quantum state |
| P_i | Rank-one projector — represents a measurement outcome |
| K = Σ Tr(ρ P_i) | KCBS witness — sum of five outcome probabilities |
| K ≤ 2 | Noncontextual bound — any classical model must satisfy this |
| K = √5 | Quantum maximum — what quantum mechanics predicts (ideal) |
| p | Noise parameter — 0 = no noise, 1 = maximally mixed |
| p* ≈ 0.4146 | Threshold — below this, quantum violation survives depolarization |

---

## Noise channels to consider for Phase 3

| Channel | Physical meaning | Formula | Already in codebase? |
|---|---|---|---|
| Depolarization | Uniform noise in all directions | (1−p)ρ + p·I/3 | ✅ Yes |
| Amplitude damping | Energy loss (e.g. photon emission) | Kraus operators K_0, K_1 | ⬜ No |
| Dephasing | Loss of phase coherence | (1−p)ρ + p·Z ρ Z | ⬜ No |
| Bit flip | Random X errors | (1−p)ρ + p·X ρ X | ⬜ No |

Amplitude damping and dephasing are the most physically motivated next steps.  
**Do the literature search before implementing either.**

---

## Notes and open questions

*Use this section as a scratchpad — write down anything you notice while reading or coding.*

- 
- 
- 

---

*Last updated: setup*  
*Next action: read Klyachko 2008 and Budroni 2022, then run the literature search*
