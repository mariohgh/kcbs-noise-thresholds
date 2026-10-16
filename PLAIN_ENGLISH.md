# Plain English Guide — What You Are Actually Looking For

No jargon. If something is still confusing, ask.

---

## The one-sentence version of your research question

> "How much of a specific type of noise can you add to a quantum system before it stops
> behaving quantum and starts looking classical — and can you work out the exact answer
> mathematically for a type of noise that nobody has done this for yet?"

---

## What is a quantum system doing that is "special" here?

Imagine you have a coin. Classically, before you look at it, it is either heads or tails —
you just don't know which. A quantum system is different: before you measure it, it is
genuinely in a mixture of possibilities, not just an unknown fixed answer.

Contextuality is a specific, provable way that quantum systems are different from classical
ones. It says: you cannot explain the measurement results by pretending the system had
hidden pre-set answers all along. The KCBS inequality is a mathematical test for this.
If the number K comes out bigger than 2, the system is behaving quantum. If K ≤ 2,
a classical explanation exists.

---

## What is noise doing to the system?

Noise is anything that disturbs the quantum system — interaction with the environment,
imperfect equipment, heat, vibration, etc.

As you add more noise, the system gets "blurred." The quantum specialness fades.
Eventually K drops below 2 and the system looks classical.

The **noise threshold** (called p*) is the exact amount of noise where K crosses 2.
Below p*: still quantum. Above p*: looks classical.

Your baseline already has this for one type of noise (depolarization):  p* ≈ 0.4146

---

## What is depolarization vs a non-depolarizing channel?

Think of noise as a type of damage to the quantum state.

**Depolarization** — the "lazy" noise model.
It smears the state equally in every direction. Like taking a sharp photo and blurring
it uniformly in all directions. It is the simplest noise to calculate with, which is
why everyone uses it first.

**Dephasing** — a physically different type of damage.
It destroys the "phase" of the quantum state — the timing relationships between
different parts of the state — without destroying the energy. Like a photo where
the colours are washed out but the shapes are still sharp. This happens in real
quantum computers when qubits interact with their environment over time.

**Amplitude damping** — another physically different type.
It models energy loss — like a quantum system slowly losing energy to its surroundings,
the way an excited atom eventually emits a photon and drops to the ground state.
This is non-unital (explained below).

**Why does the distinction matter?**
These are physically different situations. A real quantum device experiences dephasing
and amplitude damping, not just depolarization. If the noise threshold is different
for dephasing vs depolarization, that tells you something real about which quantum
systems are more or less robust. Nobody has published the analytic (exact mathematical)
threshold for dephasing in the KCBS scenario. That is the gap.

---

## What does "analytic threshold" mean vs "experimental" or "numerical"?

| Type | What it means | Example |
|---|---|---|
| Analytic | You derive an exact formula with pen and paper (or algebra). It works for all values, not just ones you tested. | p* = (√5 − 2) / (√5 − 5/3) — exact, always true |
| Numerical | You run the calculation on a computer for many values of p and see where K crosses 2. Approximate. | "K drops below 2 somewhere around p = 0.41" |
| Experimental | You build the physical system in a lab, add real noise, and measure. Subject to equipment error. | Shaham 2014 — they actually did the experiment |

Your baseline already has the analytic threshold for depolarization.
The goal is to derive the analytic threshold for dephasing the same way.

---

## What is a "unital" channel and why does it matter for Shaham 2014?

A unital channel is one that maps the maximally mixed state (total chaos, I/3) to itself.
Depolarization is unital. Dephasing is unital. Amplitude damping is NOT unital.

Shaham 2014 tested KCBS experimentally under "unital channels with controlled noise."
This means they probably tested depolarization and dephasing (both unital), but in a lab,
not with an analytic formula. Their result was: "KCBS contextuality is more fragile to
noise than nonlocality." They did not publish an exact formula for the dephasing threshold.

So even if they tested dephasing experimentally, the analytic threshold is still open.

---

## What did the literature search actually find?

Four papers found. Here is what each one did and whether it blocks your question:

**Dutra, Baldijão, Terra Cunha (2026) — arXiv:2604.24735**
- What they did: Studied depolarizing noise in KCBS mathematically and carefully.
  Both before measurements and between measurements. Very thorough for depolarization.
- Does it block you? NO.
- The smoking gun: Footnote 4 on page 6 says, word for word:
  *"Naturally Dp is not the only channel that captures decoherence. For instance,
  the dephasing map would also represent a decoherence process in which a pointer
  basis is perfectly selected by the environment."*
  Then they never mention dephasing again. No analysis. No threshold. No future work section.
- What this means for you: They literally pointed at dephasing and walked away.
  That is your paper.

**Shaham & Eisenberg (2014) — arXiv:1410.3640**
- What they did: Built the KCBS experiment in a real lab using biphotons (two photons
  in the same mode). Tested three unital channels: dephasing, two-field, and isotropic
  (which is depolarization). Measured KCBS and CHSH values as noise increased.
- Does it block you? NO — for two reasons:
  1. Experimental only. The dephasing threshold P~0.17 is read off a graph. No formula.
  2. Their system is a biphoton qutrit, not a spin-1 qutrit. The noise acts on each
     photon separately, not on the qutrit as a whole. Physically different.
- Key finding: They DID test dephasing and found KCBS contextuality dies at P~0.17.
  But they never wrote down why, or what the exact formula is.
- What this means for you: Your paper derives the analytic formula that explains
  their experimental graph. That is a concrete connection to existing experimental work.

**Marvian (2020) — arXiv:2003.05984**
- What they did: Derived noise thresholds for contextuality — but a DIFFERENT type of
  contextuality called "preparation contextuality" (Spekkens framework), not KCBS.
- Does it block you? NO — completely different framework. Like asking whether a rule
  about football blocks a rule about rugby. Related sport, different game.
- What this means for you: You need one sentence in your paper saying "this is KS
  contextuality, not preparation contextuality — see Marvian 2020 for the other case."

**Bozzetto & Hance (2026) — arXiv:2605.09558**
- What they did: Studied generalised (Spekkens) contextuality under decoherence.
  Again a different framework from KCBS.
- Does it block you? NO — different notion of contextuality.
- What this means for you: Low relevance. Just note it exists.

---

## What is still unknown (the gap you are aiming for)

After all searches, no paper has published:

- An analytic formula for the KCBS witness K(p) under **qutrit dephasing**
- An analytic noise threshold p* for KCBS under **qutrit dephasing**
- A comparison of the dephasing threshold vs the depolarizing threshold in KCBS

This is the candidate gap. It is not confirmed as novel until you also check:
- Google Scholar citations of Klyachko 2008 (can't be done automatically — needs a browser)
- The full text of Dutra 2026 and Shaham 2014 (abstracts only were accessible)
- Budroni 2022 Section IV (the big review paper — surveys all experimental noise work)

---

## What dephasing looks like mathematically (plain version)

Depolarization smears the state in all directions equally:
  ρ → (1−p)ρ + p·(I/3)

Dephasing only destroys the off-diagonal parts of the density matrix
(the parts that encode quantum phase relationships):
  ρ → diagonal parts stay the same, off-diagonal parts shrink by factor (1−p)

In matrix form for a qutrit, dephasing does this:

  [a  b  c]       [a    (1−p)b   (1−p)c]
  [d  e  f]  →    [(1−p)d   e   (1−p)f]
  [g  h  i]       [(1−p)g  (1−p)h   i  ]

The diagonal (a, e, i) — the classical probabilities — are untouched.
Only the off-diagonal entries (the quantum interference terms) shrink.

This is physically what happens when a quantum system interacts with an environment
that "measures" which energy level it is in without absorbing energy.

---

## Your next three actions (plain version)

1. Open https://arxiv.org/abs/2604.24735 in your browser.
   Scroll to the very last section (Conclusion or Discussion).
   Look for any sentence mentioning "dephasing", "amplitude damping", "future work",
   or "other channels." Copy any relevant sentences here.

2. Open https://arxiv.org/abs/1410.3640 in your browser.
   Look at Section II or the Methods section.
   Find the list of channels they actually tested. Write them down here.
   Check whether they give a formula for the threshold or just a measured number.

3. Go to scholar.google.com.
   Search: "Simple Test for Hidden Variables in Spin-1 Systems"
   Click "Cited by" (around 500 papers).
   Filter by year: 2020 to 2026.
   Scan titles for words like: noise, channel, dephasing, damping, threshold, decoherence.
   Write down any titles that look relevant.

Once you have done those three things, you will know whether the gap is real.
If it is, the next step is to derive K(p) for dephasing by hand — which is a
straightforward calculation once you understand how the trace works.

---

*Last updated: after arXiv search, October 2026*
*Status: gap identified but not yet confirmed — manual checks required*
