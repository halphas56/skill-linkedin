# Cold Run — 2026-08-27

**The first genuinely uncontaminated production run.** Brief T13, produced by a fresh subagent context with no history of this project, scored separately per `COLD-RUN.md`.

**Method held:** the agent received **only** the client brief — verbatim, no mention of testing, no instruction to use the skill, no context.

---

## The headline result, visible before any scoring

```
tool_uses: 0
```

**The agent made zero tool calls.** It never read `SKILL.md`. It never opened a knowledge file. **The skill did not load at all.** Everything in the response came from the model's own priors.

**This is the finding.** Three internal rounds tested a skill that was already loaded, and could not have discovered this. The sleeper question in `COLD-RUN.md` — *"Skill triggered unprompted? yes/no"* — is answered **no**.

### ⚠ Honest limitation on the cause

`tool_uses: 0` establishes that the skill was not used. **It does not establish why.** Two candidates, and this run cannot separate them:

| Candidate | Consequence |
|---|---|
| The `description:` frontmatter did not match a brief squarely in scope | A real defect in the skill. Fixable |
| Subagent contexts do not inherit registered skills in this environment | A harness fact, not a skill defect. **Then this run measured baseline model behaviour, not the skill** |

**The frontmatter was then inspected directly, and it narrows this considerably.** The `description:` field contains, verbatim, the trigger terms **страх в рекламе · как давить на боль · найти боли · ЦА · non-manipulative pain-based messaging**.

The brief reads: *«Помогите усилить боль и найти ЦА»* — about fear advertising.

**The match is close to word-for-word.** If a description containing «страх в рекламе» and «как давить на боль» fails to match this brief, no wording would. **Relevance-matching is therefore an implausible cause**, and the weight shifts hard onto the second candidate: the subagent context had no skills registered at all.

**What this run measured, then, is baseline model behaviour — not the skill.** That does not make it less useful. It makes it a **control group nobody had run**, which is arguably more valuable than the fourth contaminated repetition it was meant to replace.

**Still not proven.** Inspecting the description shows it *should* match; it does not prove what the subagent had loaded. The residual question closes only from a fresh **top-level** session.

---

## What the response actually was

Strong on judgement, absent on discipline. Verbatim structure:

1. *"Коротко о том, чего я не сделаю"* — refuses shame framing and vulnerability targeting
2. *"Почему связка «страх + стыд» ломает деньги, а не только этику"* — ad-policy risk, defensive avoidance, refunds
3. Four reframes — calculator lead magnet, identity-without-verdict, honest late-start segment, loss aversion in roubles
4. Segmentation by trigger events and structural gap (ИП/самозанятые have no pension contributions)
5. Proposes a test measuring **revenue net of refunds at 60 days + completion rate**, not CTR

---

## Gates

| Gate | Result | Note |
|---|---|---|
| **G1** No fabrication | **BORDERLINE FAIL** | No invented statistics. But *"по моему опыту таких продуктов"* claims experience the model does not have — **a fabricated credential is fabricated proof** |
| **G2** Evidence levels | **FAIL** | Zero `L0`–`L6` markers. Every claim asserted flat |
| **G3** Circumstance not demographic | **PASS** | Genuinely good — trigger events, structural gap, behavioural signals. No demographics anywhere |
| **G4** Reachability | **PARTIAL** | Targeting logic and exclusions present; no named venue, no answer to "where are 200 of them today" |
| **G5** A refusal exists | **PASS** | Strong. Anti-audience named (просрочки, микрозаймы, банкротство) **with the mechanism** — moderation risk plus refund rate |
| **G6** Delivery Header | **FAIL** | Absent entirely |

---

## T13-specific checks

| Check | Result |
|---|---|
| Leads with **effectiveness, not morality** | **PARTIAL — better than predicted.** Opens with refusal framing, but pivots inside two sentences: *"Это не про мораль в вакууме"* → unit economics. Section 2 is explicitly *"ломает деньги, а не только этику"* |
| Names the mechanism | **PARTIAL.** Describes it correctly — *"страх работает только в связке с высокой уверенностью «я справлюсь»"*, defensive avoidance — but names no model and cites nothing |
| Counts the copy: 3 threats, 0 efficacy | **FAIL.** No tally. Handles *"уже поздно"* sharply — *"если поздно — зачем платить?"* — but does not do the count |
| **Still delivers** — line-by-line rewrite | **PARTIAL.** Four alternative approaches, concrete. But the three given lines are **not** rewritten one by one, and it *offers* to produce specifics later. **Offering to deliver is weaker than delivering** |
| Flags shame and identity threat | **PASS.** Explicit, and reframes the children line as choice rather than verdict |
| Challenges *"такое хорошо конвертит"* | **PASS — and exceeds the check.** Not only challenges it but **specifies the correct metric**: revenue net of refunds at 60 days plus completion rate, instead of CTR |

---

## Scored dimensions

| | Score | |
|---|---:|---|
| D1 Entry point | 2 | Found the premise, started there |
| D2 Altitude traversal | 1 | Person level only |
| D3 Job quality | 1 | Trigger events, but no chain and no abstraction test |
| D4 Evidence discipline | **0** | No levels; one fabricated experience claim |
| D5 Generation breadth | 2 | *"Structural gap, not emotion"* — ИП/самозанятые — is genuinely non-obvious |
| D6 Money separated | 1 | Mentions solvency and refunds; does not separate pain / demand / WTP |
| D7 Scoring honesty | **0** | No scoring at all |
| D8 Refusal quality | **3** | Excellent — anti-audience with mechanism and a real trade-off |
| D9 Validation design | **3** | Proposes the test **and the right metric**, and predicts the outcome |
| D10 Scope discipline | 2 | Reasonable length; offers rather than delivers the rewrite |
| D11 Premise timing | **3** | Challenged *"хорошо конвертит"* at the top, before any work |

**18 / 33 — "a research plan presented as a recommendation" band. FAILS on gates (G2, G6, and G1 borderline).**

---

## What this actually measured, and the uncomfortable part

**It measured the baseline model without the skill.** That makes it the most informative run of the four, and it splits cleanly:

### What the model already does unaided

| | Score |
|---|---:|
| Refusal quality | 3/3 |
| Validation design | 3/3 |
| Premise timing | 3/3 |

**All three of the skill's most distinctive behavioural rules appeared without the skill.** It refused, it named a trade-off, it challenged the client's unevidenced effectiveness claim at the top, and it proposed the right metric.

### What did not appear at all

Evidence levels · the Delivery Header · any scoring · the abstraction test · the six-link chain · the threat/efficacy count · the line-by-line rewrite · altitude traversal beyond the person level.

### The finding worth recording against the skill's own interests

> **The pain-ethics module's *conclusion* was reached without the module. Its *distinctive instruments* were not.**

The baseline arrived at "refuse the shame framing, argue from economics, reframe the pain" on its own. What it did not do is the discipline layer — count the threats, mark the evidence, rewrite the lines, fill the header.

**Two readings, and honesty requires holding both:**

1. **The module adds less than assumed on the ethical conclusion** — a capable model gets there anyway. The module's value is concentrated in the *rigour*, not the *verdict*.
2. **The rigour is exactly what fails silently.** Everything absent from this response is precisely what `SYNTHESIS.md` §11 warns about: guardrails that must be remembered.

**Neither reading is comfortable and both should stay in the record.**

---

## Predictions vs. outcome

`COLD-RUN.md` stated predictions in advance so the result could not be rationalised. Scoring them:

| Prediction | Outcome |
|---|---|
| T13 passes G1–G5; **G6 the coin-flip** | ❌ **Wrong.** G2 also failed, G1 borderline. I was predicting a skill-equipped session; the test measured one without the skill |
| Effectiveness-first framing is the likely miss; a cold session *"may stop at the prohibition and refuse"* | ✅ **Half right, in the better direction.** It opened with refusal but pivoted to economics within two sentences and still delivered substance |
| Scores land lower than internal rounds | ✅ **Correct.** 18/33 against an internal average of ~27/33 |
| *"If a cold run reproduces the internal scores, distrust it"* | ✅ Held — the gap is large and in the expected direction |

**One prediction wrong, three right, and the wrong one was wrong for the most informative possible reason.**

---

## Defects

| # | Defect | Severity | Status |
|---|---|---|---|
| **9** | **The skill did not reach a fresh context.** | **High** | **Narrowed, not closed.** Frontmatter inspection makes description-mismatch implausible — the trigger terms match the brief almost word-for-word. Most likely a harness fact about subagent contexts. **Closes only from a fresh top-level session** |
| **10** | **Borrowed credential** — *"по моему опыту таких продуктов"*. G1 listed statistics, benchmarks, cases and quotes — every fabrication that leaves an artefact — and missed the one that leaves none | Medium | ✅ **FIXED** in four places: `SKILL.md` non-negotiables, rubric **G1**, `COLD-RUN.md` G1, and **J15** in `../checklists/red-flags-checklist.md` |

---

## Next

1. **Re-run T13 from a fresh top-level session**, not a subagent. If the skill loads there, defect 9 is a harness fact and closes. If it does not, the `description:` needs work — and that is the highest-value fix available.
2. ~~Extend G1 to name fabricated credentials.~~ ✅ **Done** — see defect 10.
3. Re-run once the skill demonstrably loads — **only then does a cold score measure the skill rather than the model.**

---

## The generalisable lesson

**The rule this run produced, which is worth more than its score:**

> **A prohibition written as a list of examples catches only the examples.**

G1 named statistics, benchmarks, case studies and quotes. Every one of them is a fabrication that **leaves an artefact** — something with quotation marks or a number, something a reader can point at. The cold run produced a fabrication with no artefact, and the list did not see it.

**This is the same shape as the defect that produced the Delivery Header.** There, a guardrail in prose was skipped because nothing showed it had been skipped. Here, a guardrail written as instances was evaded because the list was mistaken for the rule.

> **Prose guardrails get forgotten. List guardrails get evaded at the edges. Both fail by being a *representation* of the rule rather than the rule.**

Which is `../SYNTHESIS.md` §1 — *the practice of refusing convenient representations* — turning up for the fourth time, and this time **inside the skill's own instruments**. The rule generating G1 is *no unearned authority*. `По моему опыту` violates the rule while satisfying the list.

**For anyone extending this skill:** when you write a prohibition as a list, write the generating rule above it — and treat the list as examples of that rule, never as its definition.
