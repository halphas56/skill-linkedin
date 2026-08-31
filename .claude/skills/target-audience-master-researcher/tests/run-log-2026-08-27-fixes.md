# Fixes Log — 2026-08-27

**Two defects from the second test round. Both High. Both fixed. T13 re-tested.**

---

## The finding that matters more than either fix

Round one found three High defects sharing one cause: **the skill routed at the beginning and validated at the end.** The fix was a premise check — six client statements to challenge at intake.

Round two tested that fix against six fresh briefs. **It missed three of them.**

| Brief | Premise error | Caught? |
|---|---|---|
| T13 | *"Aggressive fear advertising converts well"* | ❌ |
| T9 | *"The CFO decides"* | ❌ |
| T6 | *"No search volume, therefore no demand"* | ❌ |

All three are premise errors of exactly the kind the check exists to catch. **None was on the list.**

> **A fix built as an enumeration fails the same way the original did, one level up.**

The list was not wrong. It was **a representation of a principle**, and it had been accepted in place of the principle — which is the substitution this entire skill exists to prevent, performed by the skill on itself. Recorded in `../SYNTHESIS.md` §1 as the third instance of the one law, alongside the researcher and the buyer.

---

## Fix 7 — Level the brief *(Defect 7, High)*

**Was:** six enumerated client statements. Caught those six; missed everything else. 50% failure rate against fresh briefs.

**Now:** one rule, with the six as worked examples beneath it.

> **Run the Evidence Ladder on the client's brief, not only on your own findings.**

**The observation underneath it:** the skill applied rigorous evidence discipline to everything it *produced* and **none at all to what it was handed.** A client assertion arrived as fact and got built upon; the identical assertion made by the skill would have required `L3`+ and a source.

**The procedure — four questions, two minutes:**
1. Extract every load-bearing claim in the brief — the assertions under the request, not the request
2. What level would I need before asserting this myself?
3. What level did it arrive at? *(almost always `L0` — the client said so)*
4. **Any gap is a premise error**

**Plus three claim-shapes** that generalise beyond any example list, because nine rows will not cover every brief either:

| Shape | Sounds like | Why it slips |
|---|---|---|
| **Effectiveness claim** | *"this converts well" · "email doesn't work for our audience"* | Framed as experience, reads as data. Usually one unmeasured attempt |
| **Inference from absence** | *"nobody searches for it" · "no competitor does this"* | Absence of evidence as evidence of absence. Sometimes it is the market *type* |
| **Structural assertion** | *"X decides" · "our market is Y"* | Sounds definitional rather than empirical, so nobody asks for a source |

Three worked examples added for the three misses. **Wired into `../SKILL.md` fast-path step 0b as a rule, not a list.**

**Honest limit, recorded in the manual rather than hidden:** this now generalises, but it is still a procedure a run must remember to execute. **Nothing enforces it.** It shares that weakness with every other guardrail here.

---

## Fix 8 — What to deliver when the client asks for the prohibited thing *(Defect 8, High)*

**Was:** `pain-discovery.md` §8 listed six prohibited moves and stated *"any one present, the message does not ship."* **It never said what to hand the client who asked for exactly that** — leaving two options that each break a rule.

| Option | Breaks |
|---|---|
| Refuse | *"The requested scope is the deliverable"* |
| Comply | The ethics module |

**Now:** the third answer, stated explicitly, plus a five-step response.

> **Deliver the legitimate version: the same pain, the same intensity, with efficacy attached — and lead with the mechanism rather than the morality.**

1. **Answer on effectiveness first.** *"This converts the already-convinced and repels everyone else, and here is why"* — not *"this is manipulative."* **A run that leads with ethics has failed even when its conclusion is right.** Morality first invites an argument about values; mechanism first invites a rewrite.
2. **Diagnose.** Count the threats and the efficacy claims. The answer is usually `threats: 3 · efficacy: 0`.
3. **Rewrite each line, keeping the pain.** The pain is not softened — the relief is attached to it. This is the deliverable.
4. **Name the prohibited moves and what each costs.**
5. **Challenge the effectiveness premise** — *"converts against what, measured how, with what refund rate?"* Fear-led acquisition characteristically shows strong front-end numbers and poor retention.

**Why this satisfies both rules:** the client asked for stronger pain-based advertising and **receives stronger pain-based advertising** — rewritten line by line, pain intact, mechanism explained.

> **The pain is never the problem. The missing efficacy is.** Which is why the honest answer and the useful answer are the same answer — and why refusing would have been the lazier of the two failures.

### Re-test T13

| Stage | Before | After |
|---|---|---|
| *"Такое хорошо конвертит"* | Not on the list — walked through intake | **Effectiveness claim at `L0` → premise error fires at step 0b** |
| Where ethics surfaced | Step 15b, after full analysis | **Intake, before mode selection** |
| Framing | Prohibition | **Mechanism** — EPPM, then the rewrite |
| Copy delivered | None | **Three lines rewritten with efficacy attached** |
| Scope rule | Violated by either available option | Satisfied — delivers more than asked |

**21/33 → estimated 29/33.** Marked *estimated*: scoring one's own re-run is worth little, and this is the third consecutive round where that caveat applies.

---

## Cumulative

| Round | Briefs | Defects | Root cause |
|---|---|---|---|
| 2026-08-26 | 7 | 6 (3 High) | Routed at the beginning, validated at the end |
| 2026-08-27 | 6 | 2 (2 High) | **The fix for that was itself an enumeration** |

**Twelve of thirteen briefs executed. Eight defects found, all fixed.**

---

## Still open

| Item | Note |
|---|---|
| **A cold run** | Unchanged, and now three rounds deep. Everything remains contaminated on recall |
| **T13 re-test after fixes** | Self-scored. The only brief that ever failed |
| **Round-one briefs not re-run** | T1, T3, T4, T5, T7, T10, T11 were scored pre-fix and pre-D11 |
| **Nothing enforces the guardrails** | True of the premise rule, the Evidence Ladder, and every gate in the skill. Stated in `../SYNTHESIS.md` §11 |

**Recommended next action:** a cold session runs **T13 first** — the only brief with a failure history — then T4, then any two at random from round one to check the fixes did not break what already worked.
