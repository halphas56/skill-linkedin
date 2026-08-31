# Fixes Log — 2026-08-26

**Six defects found by executing seven briefs. All six fixed. Three re-tested.**

Kept separate from `run-log-2026-08-26-execution.md` so that log preserves what the skill looked like **when the defects were found**, rather than being retro-edited into looking clean.

---

## The root cause

Three of the six were High severity, and they shared one cause:

> **The skill routed at the beginning and validated at the end, with nothing checking the client's premise in between.**

Mode selection accepted the brief as stated. The red-flags checklist — which contains the right challenges — runs *"before delivering."* So a wrong premise produced a full analysis, and the error surfaced at the delivery gate with the work already done.

**All three High fixes are the same move: pull validation earlier.**

---

## Fix 1 — RESEARCH PLAN mode *(Defect 1, High)*

**Was:** ten modes, none covering *no product, no customers, no data* — the most common pre-launch condition. Research-plan status was discovered at the end via §5's assumption-count rule.

**Now:** a mode selected **at intake**, with a defined six-part shape: opening disclaimer · market definition by need · 4–8 candidates all marked `L1` · cheapest route to `L2` per candidate with hour estimates · the Evidence Profile shown even though it reads all-`L1` · the first experiment plus what would kill the direction.

**And an explicit prohibition:** *do not score a TAS in this mode.* Ranking `L1` guesses produces false precision — the exact failure the skill exists to prevent.

### Re-test T4

| | Before | After |
|---|---|---|
| Mode selected | FULL | **RESEARCH PLAN, at intake** |
| Research-plan status | Discovered at delivery | **Declared in the opening line** |
| TAS scored | Yes, on `L1` inputs | **Prohibited** |
| Wasted sections | ~10 | 0 |

**Structurally verified.** Routing now sends this brief to a shape that fits it.

---

## Fix 2 — anti-audience with zero evidence *(Defect 2, Medium)*

**Was:** gate G5 requires a refusal. With no data, naming one is itself a guess — so the rule forced either a fabrication or a silent skip. **Undefined behaviour.**

**Now:** in RESEARCH PLAN mode the anti-audience is named **as a hypothesis to disconfirm**, not as a finding — *"we expect X to be a poor fit because [mechanism]; here is what would prove us wrong."* And if even that cannot be stated honestly:

> **An admitted gap satisfies the rule; a fabricated refusal does not.**

This closes the loophole in the direction the skill's own G1 demands.

---

## Fix 3 — COMPARE mode reordered *(Defect 3, High)*

**Was:** COMPARE routed to sections `1, 4, 6, 7, 13, 14` — opening with an offer summary, reaching the answer at 13 of 14. A run following the instruction faithfully **failed T11's first pass condition.**

**Now:** `13 first — the answer — then 6, 7, 4, 1, 14.` **Answer, then working.**

> **An instruction that causes a failure when followed correctly is worse than a missing instruction.** VERDICT mode already carried *"one page, answer first"*; COMPARE simply had not inherited it.

### Re-test T11

| Pass condition | Before | After |
|---|---|---|
| Answers the question first | ❌ §1 offer summary | ✅ §13 leads |
| Fits requested length | ❌ six sections | ✅ answer + working |
| Flags unanswerable comparison | ❌ nothing routed to it | ✅ Fix 4 |

**Score: 16/30 → estimated 26/30.** Marked *estimated* because scoring one's own re-run is worth little.

---

## Fix 4 — "the question as posed is unanswerable" *(Defect 4, Medium)*

**Was:** *"малый бизнес или фрилансеры?"* compares two **sectors**, not segments. Red flag A10 covers it — in the delivery checklist, run at the end.

**Now:** an explicit output shape in §2, reachable from mode selection: what is actually being compared and why it cannot be · the answerable version · the cheapest experiment that settles it · a provisional lean, marked as such.

**Framed deliberately as a delivery, not a refusal:** *"This is not a refusal. It delivers more than the question asked for, in less space."* The skill's own rule is that the requested scope is the deliverable — declining to answer would violate it.

---

## Fix 5 — the premise check at intake *(Defect 5, High — the structural one)*

**Was:** premise errors caught at output (§1 regime naming) or at delivery (red-flags). Correct answers, reached late, after invalidated work.

**Now:** `OPERATING-MANUAL.md` §3 carries a **six-statement premise check that runs before mode selection**:

| Client says | Challenge |
|---|---|
| "Our audience is [demographic]" | Ask for the circumstance |
| "Everyone buys on price" | What proportion, and what evidence? |
| "We want to narrow" *(established brand)* | Name the regime first |
| "Big audience, nobody buys" | Check the aspirational pattern before the funnel |
| "Skip research, just write copy" | Name the broken link — **then deliver anyway** |
| "We won't change anything" | Deliverable becomes an evidence case for change |

Plus a structural check: *is a meaningful share of purchases decided by someone other than the end user?* → draw the market map first.

**The rule now stated in one line:**
> **A premise error caught at intake costs one question. The same error caught at the delivery gate costs the engagement.**

Wired into `SKILL.md` as fast-path step 0b, **before** mode selection.

### Re-test T5

| | Before | After |
|---|---|---|
| Where the regime error surfaced | §1 of the output, after mode selection | **Intake, before mode selection** |
| Analysis performed on a wrong premise | Full narrowing analysis | None |
| Score | 27/30 (correct, late) | 27/30 (correct, early) |

**The score did not move. The waste did.** This is the fix's actual value and it is invisible to the rubric — worth noting as a rubric limitation.

---

## Fix 6 — aspirational pattern relocated *(Defect 6, Low)*

**Was:** the pattern that explains *"60k subscribers, 11 buyers"* lived only in `../research/target-audience-research-report.md` §2.16 — a Tier 5 reference file a working run may never open.

**Now:** in `../knowledge/willingness-to-pay.md` §8 (Tier 2), as a red flag with its own subsection: why identity is bought cheaply and transformation rarely · the check that 60k/11 is **consistent, not contradictory** · the life-theme test · the characteristic four-forces signature (high Pull, weak Push) · and the rule to score on completed transactions by comparable sellers, never on engagement.

---

## What the fixes did *not* address

| Still open | Why |
|---|---|
| **A genuinely cold run** | Every test and re-test came from the session that wrote the skill. Contaminated on recall |
| **T2, T6, T8, T9, T12, T13** | Six of thirteen unexecuted. T8 and T12 test behavioural rules this session judges itself worst on |
| **Whether the fixes hold under a cold run** | Verified structurally — the routing now exists. Not verified behaviourally |
| ~~A rubric blind spot~~ | **Closed in the same session.** Fix 5 improved the skill measurably and moved no score, because the rubric measured output quality and was blind to work wasted reaching it. **Dimension D11 (premise timing) added; rubric is now 33 points.** Recorded here rather than silently corrected, because the rubric failing to see its own blind spot is the same error the skill warns about everywhere else |

---

## Recommended next action

**Re-run T4, T11 and T5 from a cold session**, then T8 and T12 — the two behavioural briefs, in that order, because they are the ones this session is least qualified to have judged.
