# Segment Object — Template

**The handoff contract.** One completed object per recommended segment. This is what downstream skills consume: **Positioning → Offer → Partnership → Acquisition.**

**The rule that makes it work:** every field carries an evidence level from `../knowledge/evidence-ladder.md`. A field without a level is not filled — it is asserted, and asserting is how fiction enters a strategy.

**Empty is legitimate. Invented is not.** `[NOT RESEARCHED]` is a valid value and belongs in the research-tasks list at the bottom.

---

## Header

```
SEGMENT OBJECT
Name:            ______________________________  (name by circumstance, not by demographic)
Object ID:       seg-__
Created:         ____-__-__      Engagement: ______________
TAS score:       __._ / 5        Rank: __ of __
Gate check:      PASS / FAIL     (failed gate, if any: ______________)
Overall evidence: L_             Assumption count: __ / 45
Obvious or unexpected: ________  Generator that produced it: ______________
```

---

## Block A — Identity

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 1 | **Segment** — one sentence, circumstance-first | | | |
| 2 | **Situation** — the stable context they are in | | | |

> Field 2 is load-bearing. If it describes a person type rather than a circumstance, stop and return to `../knowledge/jtbd-engine.md` §2.

---

## Block B — The job

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 3 | **JTBD** — *When ___, I want to ___, so I can ___* | | | |
| 12 | **Functional job** — the practical task | | | |
| 13 | **Emotional job** — what they want to feel / stop feeling | | | |
| 14 | **Social job** — how they want to be seen | | | |

---

## Block C — Demand

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 4 | **Trigger** — the discrete, observable event | | | |
| 5 | **Pain** — verbatim, in their words | | | |
| 6 | **Pain severity** — 1–10, with the reason for the number | | | |
| 7 | **Frequency** — how often the circumstance recurs | | | |
| 37 | **Urgency** — what happens if they do nothing for 6 months | | | |

> Field 5 must be a quote, not a summary. Field 6 without a stated reason is a guess wearing a number.

### Pain, split by type

**Three types, three different responses.** An obstacle needs *removal*; a risk needs *reassurance*; you cannot reassure away an obstacle.

| Type | Value — **quantified** | Verbatim | Severity | L |
|---|---|---|---|---|
| **Undesired outcome** — functional / social / emotional / ancillary | | | extreme / moderate | |
| **Obstacle** — what prevents starting or slows it down | | | extreme / moderate | |
| **Risk** — what could go wrong, with consequences | | | extreme / moderate | |

> **Quantify or it does not count.** Not *"takes too long"* — after how many minutes does it become "too long" **for them**? Not *"too expensive"* — above what figure? An unquantified pain cannot be ranked, compared across segments, or used to size economic value in Block F.

### Gains — the four levels

| Level | Value — **quantified** | Verbatim | L |
|---|---|---|---|
| **Required** — without it the solution does not work | | | |
| **Expected** — substantial, could technically do without | | | |
| **Desired** — beyond expectation; surfaces when asked | | | |
| **Unexpected** — they do not know they want it | | | |

> **Required and expected gains are table stakes.** They must be delivered and **never** claimed as differentiation — the same object as McDonald's non-discriminating features. **Differentiation lives at *desired* and *unexpected*.**

### Supporting jobs — the three roles

| Role | Jobs | L |
|---|---|---|
| **Value buyer** — comparing, deciding, queueing, paying, taking delivery | | |
| **Value co-creator** — reviews, feedback, co-development | | |
| **Value transferrer** — cancelling, disposing, passing on, reselling | | |

> **The transferrer row is the one nobody fills, and it is where switching friction hides:** the dining room table, the old mattress at the kerb, *"what happens to my data if we cancel?"* asked before anyone has signed.

### Four Forces

```
Push    ▓▓▓▓▓▓▓░░░  __/10   L_    Pull    ▓▓▓▓▓░░░░░  __/10   L_
Anxiety ▓▓▓▓▓▓▓▓░░  __/10   L_    Habit   ▓▓▓▓▓▓░░░░  __/10   L_

Push+Pull = __   vs   Anxiety+Habit = __   →  SWITCH / NO SWITCH
Binding constraint: ______________  →  strategy: ______________
```

---

## Block D — Competitive reality

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 8 | **Existing solution** — what they use today | | | |
| 9 | **Alternatives** — including "do nothing" and non-obvious substitutes | | | |
| 10 | **Switching trigger** — what makes them willing to change | | | |
| 36 | **Competition** — who else targets this segment, how heavily | | | |

> Field 9 must contain "nothing / status quo" unless you have evidence it is not an option. Inertia is usually the market leader.
> Did they **build their own workaround**?  ☐ yes ☐ no — if yes, flag as a lead-user signal.

---

## Block E — The decision

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 11 | **Desired outcome** — the after-state in their metric | | | |
| 15 | **Decision criteria** — what they actually compare on (Ring 5) | | | |
| 16 | **Objections** — verbatim, ranked by frequency | | | |
| 17 | **Risk** — what they are afraid of | | | |

---

## Block F — Money

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 18 | **WTP** — price corridor, method used | | | |
| 19 | **Ability to pay** — existing budget line, evidence | | | |
| 33 | **CAC potential** — estimated cost to acquire one | | | |
| 34 | **LTV potential** — value of one customer | | | |

```
ECONOMIC VALUE OF THE PROBLEM
Annual cost of the problem to them:   ______________
Reference value (best alternative):   ______________
Differentiation value (our delta):    ______________
Defensible price band:                ______________
Value metric (what price scales with):______________
Money would come from:                ______________
```

> WTP from stated methods caps at `L3`. Pair with one behavioural source before recommending a price. See `../knowledge/willingness-to-pay.md`.
> `CAC ≪ LTV`? If not, this segment fails channel-model fit regardless of its other scores.

---

## Block G — The buying group

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 20 | **Decision maker** — who chooses between vendors | | | |
| 21 | **User** — who uses it daily | | | |
| 22 | **Influencer** — whose opinion is consulted | | | |
| 23 | **Budget owner** — whose line it comes from | | | |
| — | **Blocker** — who can veto (security, legal, procurement) | | | |

> B2B: assume **6–10 people** in a complex decision. `[E]`
> **Do not build a persona for someone who signs off but does not choose between vendors** — that persona yields nothing usable. `[E — Revella]`
> Is buyer ≠ user? ☐ yes ☐ no — if yes, this is effectively two audiences. See `../knowledge/category-entry-points.md` §5.

---

## Block H — Where they are

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 24 | **Search intent** — actual queries, with volume | | | |
| 25 | **Language / VOC** — 5+ verbatim quotes per language type | | | |
| 26 | **Communities** — named, with size and vendor rules | | | |
| 27 | **Websites** — what they read | | | |
| 28 | **Creators** — who they follow and never skip | | | |
| 29 | **Search channels** — where they look for solutions | | | |
| 35 | **Reachability** — can we reach 100 of them by Friday? How? | | | |

> Fields 26–28 must contain **named instances**, never platform names. "LinkedIn" is not an answer.
> Prefer **over-index** to raw share: 80% on a universal platform tells you nothing; 200% over-index on a niche one tells you where they are distinctively present.

---

## Block I — Acquisition

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 30 | **Organic acquisition** — channel, required asset, time-to-signal | | | |
| 31 | **Paid acquisition** — channel, targeting parameter, angle | | | |
| 32 | **Partners** — who already has this audience | | | |

> Field 30 must state the **required asset** and the **time-to-signal**, or it is a wish. "Free" is never free — it is paid in founder time and credibility.

---

## Block J — Market

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 38 | **Market size** — countable, bottom-up | | | |
| 39 | **Growth** — direction, with evidence | | | |

```
Bottom-up:  ____ reachable customers  ×  ____ price  ×  ____% capture  =  ____
Top-down cross-check: ____    Within 2×? ☐ yes ☐ no
Where the list of these customers physically exists: ______________
```

---

## Block K — Evidence

| # | Field | Value |
|---|---|---|
| 40 | **Evidence** — what supports this segment, by source type | |
| 41 | **Confidence** — overall level + weakest load-bearing assumption | |

```
EVIDENCE PROFILE (this segment)
Independent source types used: ____   (list: ______________________)
L0 __  L1 __  L2 __  L3 __  L4 __  L5 __  L6 __
Highest level supporting the core claim: L__
Triangulated?  ☐ yes ☐ no    (needs 3+ independent types — see evidence-ladder.md §4)
Weakest load-bearing assumption: ______________________
What would falsify this segment: ______________________
```

---

## Block L — Strategic

| # | Field | Value | L | Source |
|---|---|---|---|---|
| 42 | **Why us** — why this specific business fits this segment | | | |
| 43 | **Positioning opportunity** — the angle, swap-tested | | | |
| 44 | **Offer opportunity** — what to package and how | | | |
| 45 | **Unexpected angle** — the non-obvious reason they might choose you | | | |

> Field 43 must survive the swap test: substitute the strongest competitor's name. Still reads true → it is not positioning.

---

## Machine-readable handoff

Emit alongside the human-readable form when passing to another skill.

```yaml
segment_object:
  id: seg-01
  name: ""
  tas_score: 0.0
  gate_check: pass          # pass | fail
  gate_failed: null
  evidence_overall: L0      # L0..L6
  triangulated: false
  assumption_count: 0
  obvious_or_unexpected: unexpected
  generator: ""             # which lens/generator produced it

  identity:
    segment: {v: "", L: "L0", src: ""}
    situation: {v: "", L: "L0", src: ""}

  job:
    jtbd: {v: "", L: "L0", src: ""}
    functional: {v: "", L: "L0", src: ""}
    emotional: {v: "", L: "L0", src: ""}
    social: {v: "", L: "L0", src: ""}

  demand:
    trigger: {v: "", L: "L0", src: ""}
    pain: {v: "", L: "L0", src: ""}          # verbatim
    pain_severity: {v: 0, L: "L0", src: ""}  # 1-10
    frequency: {v: "", L: "L0", src: ""}
    urgency: {v: "", L: "L0", src: ""}
    forces: {push: 0, pull: 0, anxiety: 0, habit: 0, binding: ""}

  competitive:
    existing_solution: {v: "", L: "L0", src: ""}
    alternatives: {v: [], L: "L0", src: ""}   # must include "do nothing"
    switching_trigger: {v: "", L: "L0", src: ""}
    competition: {v: "", L: "L0", src: ""}
    built_own_workaround: false

  decision:
    desired_outcome: {v: "", L: "L0", src: ""}
    decision_criteria: {v: [], L: "L0", src: ""}
    objections: {v: [], L: "L0", src: ""}     # ranked by frequency
    risk: {v: "", L: "L0", src: ""}

  money:
    wtp: {v: "", method: "", L: "L0", src: ""}
    ability_to_pay: {v: "", L: "L0", src: ""}
    cac_potential: {v: "", L: "L0", src: ""}
    ltv_potential: {v: "", L: "L0", src: ""}
    problem_annual_cost: ""
    reference_value: ""
    differentiation_value: ""
    price_band: ""
    value_metric: ""
    budget_source: ""

  buying_group:
    decision_maker: {v: "", L: "L0", src: ""}
    user: {v: "", L: "L0", src: ""}
    influencer: {v: "", L: "L0", src: ""}
    budget_owner: {v: "", L: "L0", src: ""}
    blocker: {v: "", L: "L0", src: ""}
    buyer_is_user: true

  habitat:
    search_intent: {v: [], L: "L0", src: ""}
    voc: {v: [], L: "L0", src: ""}            # verbatim, by language type
    communities: {v: [], L: "L0", src: ""}    # named instances only
    websites: {v: [], L: "L0", src: ""}
    creators: {v: [], L: "L0", src: ""}
    search_channels: {v: [], L: "L0", src: ""}
    reachability: {v: "", L: "L0", src: ""}

  acquisition:
    organic: {channel: "", asset_required: "", time_to_signal: "", L: "L0"}
    paid: {channel: "", targeting: "", angle: "", L: "L0"}
    partners: {v: [], L: "L0", src: ""}

  market:
    size: {v: "", method: "bottom-up", L: "L0", src: ""}
    growth: {v: "", L: "L0", src: ""}

  strategic:
    why_us: {v: "", L: "L0", src: ""}
    positioning_opportunity: {v: "", swap_tested: false, L: "L0"}
    offer_opportunity: {v: "", L: "L0", src: ""}
    unexpected_angle: {v: "", L: "L0", src: ""}

  falsification: ""
  research_tasks: []
```

---

## Downstream handoff

Which fields each skill consumes.

| Downstream skill | Fields it needs |
|---|---|
| **Positioning** | 2, 3, 5, 8, 9, 11, 12–14, 15, 16, 25, 36, 42, 43, 45 |
| **Offer** | 5, 6, 11, 15, 16, 17, 18, 19, 33, 34, 44 + economic value block |
| **Partnership / channel** | 22, 26, 27, 28, 32, 35 |
| **Acquisition / leadgen** | 4, 24, 26–31, 33, 35, 37 + Four Forces |
| **Sales enablement** | 15, 16, 17, 20–23 + Blocker + Four Forces |

**Handoff rule:** never pass a segment object whose core claims sit below `L3`, without stating so in the first line of the handoff. A downstream skill that receives assumptions as facts will build confidently on sand, and the error compounds silently through every stage.

---

## Research tasks — the blanks

| # | Missing field | Why it matters | Cheapest way to get it | Cost | Would it change the recommendation? |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

---

## Delivery gate

- [ ] All 45 fields addressed — filled, or explicitly `[NOT RESEARCHED]`
- [ ] Every filled field carries an **evidence level** and a source
- [ ] Field 2 states a **circumstance**, not a person type
- [ ] Field 5 is **verbatim**, not paraphrased
- [ ] Field 9 includes **"do nothing"**
- [ ] Four Forces scored; **binding constraint named**
- [ ] Buying group mapped; **blocker identified**; buyer ≠ user checked
- [ ] Economic value block completed with numbers
- [ ] Fields 26–28 contain **named instances**, not platform names
- [ ] Field 30 states the **required asset** and **time-to-signal**
- [ ] Field 43 **swap-tested**
- [ ] Evidence Profile complete; triangulation status honest
- [ ] **Falsification condition** stated
- [ ] Research tasks ranked by decision impact
- [ ] YAML block emitted if handing off to another skill
