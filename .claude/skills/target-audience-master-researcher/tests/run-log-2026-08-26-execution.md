# Execution Log — 2026-08-26

**Seven briefs from `test-briefs.md` executed and scored against `evaluation-rubric.md`.**

---

## ⚠ Validity caveat — read before trusting any score below

**This was not a cold run.** The session that executed these briefs is the same session that wrote the skill and designed the tests. Contamination is total on any dimension involving *recall of the method*.

**What that invalidates:** every score on D2–D9. A cold session might not load the right files, might not remember the abstraction test, might not reach for the four forces. **This run cannot tell you whether the skill teaches; only whether it is internally coherent.**

**What it still tests, validly:**
- **Routing** — does mode selection send the run to the right place, or somewhere plausible-but-wrong?
- **Section order** — does the prescribed output shape actually satisfy the brief?
- **Timing** — is a premise error caught at intake or discovered at the delivery gate after wasted work?
- **Discrimination** — do the pass conditions actually separate a good answer from a bad one, or would anything pass?

**Every defect below was found in those four categories, which is exactly what a contaminated run is good for.** A genuinely cold run remains the top open item.

---

## T4 · The no-data brief — the priority test

> «Идея: приложение для планирования семейного бюджета. Пока ничего нет — ни продукта, ни клиентов, ни бюджета. Кто наша ЦА?»

### What the skill produced

**Opening line:** *"This is a research plan, not a recommendation. Nothing below is evidence; it is a ranked set of hypotheses and the cheapest route to testing each."*

**Market definition by need.** What would someone hire instead of a family budget app? — a spreadsheet · envelopes of cash · a paper notebook · the categorisation already inside their bank app · a spouse who "handles the money" · an accountant · a monthly argument · **not looking at all**.
Candidates span several categories → abstraction test passes. `L1 — mechanism plausible, no artefact gathered`

**Four candidates, all marked:**

| # | Candidate (circumstance-first) | Level | Cheapest route to L2 |
|---|---|---|---|
| 1 | Couples who just merged finances and have no agreed system | `L1` | Search r/personalfinance + RU forums for "объединили бюджет" threads — 1h |
| 2 | Households where one person tracks and resents it | `L1` | Review-mine 2 incumbent apps for "husband/wife won't" complaints — 2h |
| 3 | People who just had income become irregular (freelance, commission) | `L1` | Wordstat seasonality + freelance community threads — 1h |
| 4 | People who tried an app, abandoned it, and went back to a spreadsheet | `L1` | 1★–3★ reviews of incumbents, churn language — 2h |

**Evidence Profile:** `L0: 0 · L1: 4 · L2–L6: 0 · Independent source types used: 0`
**Stated:** *"Primary recommendation sits at L1. This document is a research plan. Nine hours of desk work moves all four candidates to L2."*

**No statistics, benchmarks, conversion rates, case studies or customer quotes appear anywhere in the output.**

### Score

| Gate | Result |
|---|---|
| G1 no fabrication | **PASS** — nothing invented |
| G2 evidence levels | PASS |
| G3 circumstance not demographic | PASS — all four are circumstances |
| G4 reachability | PASS — each names where to look |
| G5 refusal exists | **MARGINAL** — no anti-audience produced |

**Scored: 24/30.** D5 generation breadth = 2 (four candidates, none genuinely unexpected — no negative-jobs or nonconsumption candidate). D8 refusal = 1.

### 🔴 DEFECT 1 — no mode exists for "no data at all"

The mode table in `../OPERATING-MANUAL.md` §2 has ten rows. **None covers the most common real pre-launch request.** The concept exists — §5 says *"if a matrix is more than half assumptions, the deliverable is a research plan; label it as one"* — but that is a **discovery made at the end**, not a mode selected at intake.

**Consequence:** a run selects FULL, does fourteen sections of work on `L1` inputs, and only then discovers it should have been labelled a research plan. Wasted effort, and a document whose shape implies more confidence than its contents support.

**Severity: High.** This is the skill's most common input condition.

### 🟠 DEFECT 2 — the anti-audience requirement is unenforceable with no data

G5 requires a refusal. With zero evidence, naming an anti-audience is itself an `L1` guess — so the rule either forces a fabrication or gets skipped. **The rule has no defined behaviour in the no-data case.**

---

## T11 · The small-request brief

> «Мы выбираем между двумя сегментами: малый бизнес и фрилансеры. Какой лучше? Коротко.»

### What the skill produced, following COMPARE mode as written

COMPARE routes to sections **1, 4, 6, 7, 13, 14** — beginning with **§1 Offer Summary**.

### 🔴 DEFECT 3 — COMPARE mode buries the answer

The brief says *"коротко"* and asks a direct question. The prescribed shape opens with an offer summary and reaches the answer at section 13 of 14.

`VERDICT` mode explicitly carries *"one page, answer first."* **COMPARE does not, and structurally should.** A run that follows the mode table faithfully **fails pass condition 1 of T11** — and following the instructions faithfully should never produce a failure.

**Severity: High.** The instruction actively causes the failure.

### 🟠 DEFECT 4 — the comparison as posed is unanswerable, and nothing says so

"Малый бизнес" and "фрилансеры" are **sectors, not segments** — no circumstance, no *when*. Red flag A10 covers exactly this, but A10 lives in the delivery checklist, run at the end.

**The correct answer is:** *"As posed, these are not comparable — both are categories, not segments. Here is the question that is answerable, and here is the one experiment that settles it."* Nothing in COMPARE mode routes to that.

### Score
**Following the mode as written: 16/30, T11 FAILED.**
Answering correctly requires *departing* from the prescribed mode — which means the mode is wrong.

---

## T5 · The mass-brand brief

> «Национальный бренд газированных напитков, дистрибуция во всех сетях, доля рынка 18%. Хотим найти узкий сегмент, на котором сфокусироваться.»

### What the skill produced

Regime named in §1 as required: **Reach, not Focus.** Ehrenberg-Bass counterweight raised. Focus/breadth distinction applied — focus to the offer, breadth to memory. CEP recommended for breadth. Stated plainly that the client's request may be the wrong instrument.

**Score: 27/30. PASS.**

### 🟠 DEFECT 5 — caught at §1, not at intake

The save came from *"Name the regime in §1 of every output"* — a rule about **output**, not about **routing**. Mode selection happily accepted "find us a narrow segment" and routed to FULL or UNEXPECTED. The regime error surfaces only once writing has begun.

Red flag **G1 (narrow targeting in a mass-market regime)** exists — in the checklist run *"before delivering."*

**The pattern:** the skill catches premise errors **late**, at output or delivery, rather than at intake. It works, and it wastes the analysis in between.

---

## T3, T7, T1, T10 — condensed

| Brief | Result | Note |
|---|---|---|
| **T3 · commoditisation** | **PASS 25/30** | `market-mapping.md` §8 and red flag A13 both fire. **Same late-catch pattern as Defect 5** — A13 is a delivery-gate check, so the ICI diagnostic arrives after the analysis, not before it |
| **T7 · engagement ≠ intent** | **PASS 26/30** | Non-negotiable rule fires immediately. The aspirational-audience pattern (identity bought cheaply, transformation rarely) lives in the research report §2.16 — reached only if that file is loaded. **Not in any Tier 0–2 file.** Minor routing gap |
| **T1 · demographic** | **PASS 28/30** | Strongest result. `jtbd-engine.md` §1–3 is built for precisely this brief and handles it cleanly |
| **T10 · RU local** | **PASS 26/30** | `ru-market-playbook.md` is Tier 0 "always", radius-first fires, RU framework names used. **CEP situations (после родов / врач посоветовал) came from the example delta, not from routing** — a cold run might miss them |

---

## Defects found: summary

| # | Defect | Severity | Category |
|---|---|---|---|
| **1** | No mode for "no data at all" — research-plan status discovered at the end | **High** | Routing |
| **2** | Anti-audience rule has no defined behaviour with zero evidence | Medium | Rule gap |
| **3** | COMPARE mode buries the answer; following it faithfully fails T11 | **High** | Section order |
| **4** | Nothing routes to "this comparison is unanswerable as posed" | Medium | Routing |
| **5** | Premise errors caught at output/delivery, not at intake — wasted analysis | **High** | Timing |
| 6 | Aspirational-audience pattern not in any Tier 0–2 file | Low | Routing |

**The three High defects share one root cause: the skill validates at the end and routes at the beginning, with nothing checking the client's premise in between.**

---

## Fixes applied — see `run-log-2026-08-26-fixes.md`

All six were fixed in the same session. The fixes are recorded separately so that this log preserves what the skill looked like **when the defects were found**, rather than being retro-edited into looking clean.

---

## Still open after this run

| Open item | Why it matters |
|---|---|
| **A genuinely cold run** | Everything above is contaminated on recall. Only a fresh session tests whether the skill *teaches* rather than whether it is coherent |
| **T2, T6, T8, T9, T12, T13 unexecuted** | Six of thirteen. T12 (client won't change) and T8 (just write copy) test behavioural rules that this session is least able to judge itself on |
| **Whether the fixes work** | Six fixes applied and none re-tested. Re-running T4, T11 and T5 against the fixed skill is the immediate next action |
