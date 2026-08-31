# Audience Scoring Matrix — Template

**Purpose.** Compare candidate audience segments on identical criteria, so that disagreement becomes specific and missing evidence becomes visible.

**What this is not.** A decision machine. The matrix surfaces the criterion nobody checked and the cell nobody researched. The decision is still yours, and the gates below override any total.

**Two layers.** The **TAS** (below) is the headline score — eleven variables, fixed weights, comparable across every engagement. The **nineteen criteria** (Part 2) are the diagnostic layer that explains *why* a TAS variable scored what it did. Report the TAS; use the nineteen to defend it.

---

## Part 0 — The Target Audience Score (TAS)

### The formula

```
TAS = 0.15·P + 0.12·U + 0.12·W + 0.10·A + 0.10·R
    + 0.08·F + 0.08·G + 0.07·L + 0.06·C + 0.06·D + 0.06·E
```

Weights sum to **1.00**. Each variable is scored **1–5**. TAS therefore runs **1.0 – 5.0**.

### The eleven variables

| Sym | Variable | What it measures | Fed by criteria (Part 2) |
|---|---|---|---|
| **P** | Pain intensity | How much the problem actually costs them | #1 |
| **U** | Urgency | Whether there is a clock | #2 |
| **W** | Willingness to pay | Will they hand *you* money for *this* | #4 |
| **A** | Ability to pay | Does the money exist at all | #3 |
| **R** | Reachability | Can you get to them affordably | mean(#5, #6) |
| **F** | Product fit | Does your specific strength match their need | mean(#10, #17) |
| **G** | Market growth | Is the segment expanding or shrinking | growth evidence |
| **L** | LTV potential | Repeat, retention, referral | mean(#15, #16) |
| **C** | Competition advantage | Can you win here, not just compete | mean(#9 inv, #18) |
| **D** | Demand evidence | Is there observable demand today | #8 |
| **E** | **Evidence quality** | **How well-supported this whole row is** | see below |

### E — the honesty variable

`E` is computed directly from `../knowledge/evidence-ladder.md`. It is the **mean evidence level across this segment's load-bearing claims**, mapped:

| Mean level | E |
|---|---|
| L0 – L1 | **1** |
| L2 | **2** |
| L3 | **3** |
| L4 | **4** |
| L5 – L6 | **5** |

This is what stops the matrix from laundering speculation into a confident number. A segment built on guesses cannot score above roughly 4.4 even if every other variable is perfect — and the gap between its TAS and its potential is precisely the value of doing the research.

### Gates still override

The five gates (Rule 1) apply **on top of** the TAS, not inside it. A segment scoring 4.6 with a `1` on Reachability is **disqualified**, and the report says so on the same line.

### Six of the nineteen never feed the TAS — deliberately

| Criterion | Why it is diagnostic-only |
|---|---|
| **#7 Trust accessibility** | A **gate**. It kills segments rather than ranking them |
| **#11 Free acquisition potential** | Feeds the *strategy*, not the *choice*. Two segments can be equally attractive and need different channels |
| **#12 Paid acquisition potential** | Same — and partly captured inside `R` (reachability) |
| **#13 Content potential** | A downstream consequence of the segment, not a property of it |
| **#14 Sales cycle length** | Real, but a cash-flow constraint rather than an attractiveness measure; surfaces in the gate check and in `CAC` |
| **#19 Risk level** | Reported alongside the score, not inside it — averaging risk away is exactly what a weighted total does badly |

**Why this matters:** the TAS is deliberately compact so scores stay comparable across engagements. The six above still get scored in Part 2, still appear in the deliverable, and still change the recommendation — they just do it as **narrative and gates**, not as arithmetic. If one of them is decisive for a given client, say so in words rather than inflating the total.

### Reporting format

Never report a bare number. Always these four together:

```
| Segment | TAS | Gates | Evidence | Assumptions |
|---------|-----|-------|----------|-------------|
| A       | 4.3 | PASS  | L4       | 3/45        |
| B       | 4.1 | PASS  | L3       | 11/45       |
| C       | 4.5 | FAIL — Reachability = 1 | L2 | 24/45 |
| D       | 3.2 | PASS  | L5       | 2/45        |
```

Read that table correctly: **C is out despite the top score. A beats B not on 0.2 points but on evidence. D is the honest one** — low score, but you can trust it, and it may be the right first move precisely because it is real.

### Four rules for using TAS

1. **A difference under 0.3 is not a difference.** Two segments within 0.3 are indistinguishable by analysis. Break the tie with an experiment — parallel smoke tests or WTP research — not with more argument.
2. **Report the working, not the number.** Eleven scores with sources, then the total. A TAS with no visible inputs is astrology with decimals.
3. **Recompute after every research pass.** TAS is a snapshot of current evidence, and `E` in particular should climb as work proceeds. A TAS that never moves means no new evidence was gathered.
4. **Do not tune the weights per engagement.** The fixed weights are what make scores comparable across clients and across time. If a business genuinely needs different weights, use the Part 3 presets as the *diagnostic* layer and keep TAS canonical.

### Worked calculation

```
Segment: "Store owners whose CPA just jumped and who've frozen spend"

P 5 [L4: 11/30 reviews + 3/5 interviews + search vol]   0.15 × 5 = 0.75
U 5 [L5: money burning now; ad spend live]              0.12 × 5 = 0.60
W 4 [L5: 3 competitors hold ₽80–120k audits 2+ yrs]     0.12 × 4 = 0.48
A 5 [L6: already spending ₽500k/mo on ads]              0.10 × 5 = 0.50
R 4 [L4: 3 TG chats + agency partners + intent search]  0.10 × 4 = 0.40
F 4 [L3: our diagnostic method is the differentiator]   0.08 × 4 = 0.32
G 3 [L2: category flat, no strong signal either way]    0.08 × 3 = 0.24
L 3 [L3: audit is one-off; retainer possible not proven]0.07 × 3 = 0.21
C 4 [L4: agencies sell execution, not diagnosis]        0.06 × 4 = 0.24
D 5 [L5: 2,400/mo on "почему вырос CPA" cluster]        0.06 × 5 = 0.30
E 4 [mean level across load-bearing claims = L4]        0.06 × 4 = 0.24
                                                        ─────────────
                                                  TAS =        4.28
Gates: PASS (no 1s on P, U, A, R, Trust)
Evidence: L4 triangulated — reviews + interviews + search + competitor pricing
Assumptions: 6/45
```

Note what the low scores are doing: `G 3` and `L 3` are honest admissions — the category isn't visibly growing and the offer is one-off. They cost 0.28 points and they tell the client exactly what to fix (find the retainer).

---

## Part 1 — Rules of use

### Rule 1 — Gates before weights

Five criteria are **near-veto gates**. A score of **1** on any of them disqualifies the segment regardless of its weighted total, and the report must say so on the same line as the score.

| Gate | Criterion |
|---|---|
| G1 | **Pain intensity** (#1) |
| G2 | **Urgency** (#2) |
| G3 | **Ability to pay** (#3) |
| G4 | **Reachability** (#5) |
| G5 | **Trust accessibility** (#7) |

A weighted average that averages away a fatal flaw is worse than no matrix at all.

### Rule 2 — Weights sum to 100

Per business model. No criterion above 15; none below 2. Above 15 and you have a checklist with extra steps; below 2 and you should delete the criterion.

### Rule 3 — Every score cites a source

Format the cell as `score [source]`:

- `4 [4.9 review mining: 18/30 reviews cite this]`
- `5 [interview 3, 7, 9 — all named a Q4 deadline]`
- `2 [ASSUMPTION — no evidence found]`

**Assumption-scored cells must be visually distinct** (bold, or `⚠`). The count of them is itself a finding: a matrix that is 70% assumptions is a *research plan*, and must be labelled as one.

### Rule 4 — Score column-wise, not row-wise

Score every segment on criterion 1, then every segment on criterion 2, and so on. Scoring one segment across all criteria produces a halo effect — the segment you already like collects 4s. Column-wise scoring forces relative judgement, which is the only kind that is reliable here.

### Rule 5 — Inverse criteria

Criteria marked **(inv)** are scored so that **5 is always good**. A short sales cycle scores 5; a nine-month committee cycle scores 1. Never mix directions inside one matrix.

---

## Part 2 — The nineteen criteria with scoring anchors

Write the anchors down before scoring anything. These are the defaults; adjust them for the engagement and record the change.

| # | Criterion | 1 | 3 | 5 | Evidence that settles it |
|---|---|---|---|---|---|
| 1 | **Pain intensity** ⚠G1 | Mild annoyance, tolerated for years | Real friction, worked around | Quantified loss they state in money or hours | Verbatim complaints; review theme counts |
| 2 | **Urgency** ⚠G2 | No consequence to waiting a year | Wants it "this year" | Dated deadline with a penalty attached | Trigger events; seasonality data |
| 3 | **Ability to pay** ⚠G3 | No budget exists anywhere | Budget exists but must be found | Existing line item larger than your price | Job postings, funding, vendor logos, CRM |
| 4 | **Willingness to pay** | Category norm is "should be free" | Pays reluctantly, haggles | Pays comparable amounts without friction | Van Westendorp + behavioural cross-check |
| 5 | **Reachability** ⚠G4 | No list, no channel, no targeting parameter | Reachable but expensively | A named list or channel accessible this week | The list test |
| 6 | **Concentration** | Scattered; never meet | Some venues, partial coverage | 3 venues cover most of the segment | Habitat map with sizes and activity |
| 7 | **Trust accessibility** ⚠G5 | Needs certifications/references you lack | Needs a case study you could build | A portfolio link or peer intro is enough | What proof buyers actually accepted |
| 8 | **Existing demand** | Nobody searches, nobody buys | Some search, few paying | Active search volume + paying incumbents | Keyword/Wordstat data; competitor pricing |
| 9 | **Competition** (inv) | Several funded specialists own it | Contested but not dominated | Only generalists, serving it badly | Ad libraries, review sites, SERP |
| 10 | **Differentiation potential** | You'd be the eleventh identical claim | Some contrast available | You can say something true nobody else can | Swap test against top competitor |
| 11 | **Free acquisition potential** | No venue, no founder standing, no search | One weak free route | Dense communities + founder with standing | The §6.3 decision rule |
| 12 | **Paid acquisition potential** | No targeting parameter matches | Targetable but ARPU is tight | Precise targeting + ARPU funds the CAC | Platform parameters + ARPU↔CAC check |
| 13 | **Content potential** | No questions asked; nothing to say | Occasional questions | Repeat questions asked monthly for years | Community repeat-question log |
| 14 | **Sales cycle** (inv) | 9+ months, committee, procurement | 1–3 months, 2–3 people | Days; single decision-maker | Observed cycles; buying-group size |
| 15 | **Retention potential** | One-off; no reason to return | Occasional repeat | Recurring need embedded in a workflow | Frequency of the triggering circumstance |
| 16 | **Referral potential** | Private or competitively sensitive | Sometimes shared | Peers routinely share and are rewarded for it | "Who did you tell?" answers |
| 17 | **Strategic fit** | Off-mission; no interest, no network | Acceptable but not natural | Founder's own network and expertise; on-mission | Network overlap; prior experience |
| 18 | **Positioning strength** | Survives the swap test intact | Some defensibility | Incumbents can't copy without breaking themselves | Competitor message homogeneity |
| 19 | **Risk** (inv) | Regulatory / platform / concentration exposure | One manageable risk | No structural exposure | Named risks with likelihood |

---

## Part 3 — Weight presets

Pick the nearest preset. **Adjust no more than three weights**, and document each change with a reason — bespoke weighting per engagement destroys comparability across engagements, which is most of the value of having a matrix.

### Presets 1–6

| # | Criterion | Default | B2B SaaS | Expert course | Agency / service | Local business | Consumer product |
|---|---|---|---|---|---|---|---|
| 1 | Pain intensity | 10 | 8 | 8 | 7 | 7 | 7 |
| 2 | Urgency | 8 | 5 | **11** | 6 | 8 | 5 |
| 3 | Ability to pay | 10 | **12** | 7 | **12** | 6 | 5 |
| 4 | Willingness to pay | 8 | 6 | **12** | 6 | 6 | 7 |
| 5 | Reachability | 10 | **11** | 7 | 7 | **10** | 8 |
| 6 | Concentration | 5 | 4 | **9** | 4 | **13** | 4 |
| 7 | Trust accessibility | 6 | 5 | 5 | **11** | 6 | 3 |
| 8 | Existing demand | 6 | 5 | 5 | 4 | **10** | **12** |
| 9 | Competition (inv) | 4 | 4 | 3 | 3 | 4 | 7 |
| 10 | Differentiation | 4 | 3 | 3 | 3 | 2 | 4 |
| 11 | Free acquisition | 5 | 3 | 6 | 4 | 4 | 4 |
| 12 | Paid acquisition | 4 | 5 | 3 | 2 | 4 | **12** |
| 13 | Content potential | 3 | 2 | 8 | 3 | 2 | 3 |
| 14 | Sales cycle (inv) | 3 | 7 | 2 | 3 | 3 | 2 |
| 15 | Retention | 4 | **10** | 2 | 3 | 4 | 7 |
| 16 | Referral | 3 | 2 | 3 | **9** | 5 | 3 |
| 17 | Strategic fit | 3 | 2 | 2 | 5 | 2 | 2 |
| 18 | Positioning strength | 2 | 3 | 2 | 6 | 2 | 3 |
| 19 | Risk (inv) | 2 | 3 | 2 | 2 | 2 | 2 |
| | **Total** | **100** | **100** | **100** | **100** | **100** | **100** |

### Presets 7–12

| # | Criterion | High-ticket consulting | Marketplace | Mobile app | Info product | Subscription | B2B services / outbound |
|---|---|---|---|---|---|---|---|
| 1 | Pain intensity | 7 | 6 | 6 | 7 | 8 | 8 |
| 2 | Urgency | 6 | 5 | 4 | 8 | 5 | **11** |
| 3 | Ability to pay | **13** | 5 | 4 | 6 | 7 | **11** |
| 4 | Willingness to pay | 6 | 6 | 6 | **11** | 9 | 6 |
| 5 | Reachability | 8 | 9 | 7 | 7 | 7 | **13** |
| 6 | Concentration | 4 | **13** | 4 | 7 | 4 | 5 |
| 7 | Trust accessibility | **12** | 3 | 2 | 4 | 4 | 8 |
| 8 | Existing demand | 3 | **10** | **12** | 9 | 8 | 4 |
| 9 | Competition (inv) | 3 | 4 | 7 | 4 | 5 | 3 |
| 10 | Differentiation | 3 | 2 | 4 | 3 | 3 | 3 |
| 11 | Free acquisition | 3 | 5 | 5 | 8 | 4 | 3 |
| 12 | Paid acquisition | 2 | 4 | **11** | 5 | 6 | 3 |
| 13 | Content potential | 3 | 2 | 3 | 8 | 2 | 2 |
| 14 | Sales cycle (inv) | 3 | 2 | 2 | 2 | 2 | 5 |
| 15 | Retention | 2 | 9 | **11** | 2 | **14** | 3 |
| 16 | Referral | 5 | 8 | 6 | 3 | 6 | 5 |
| 17 | Strategic fit | 7 | 2 | 2 | 2 | 2 | 2 |
| 18 | Positioning strength | 8 | 2 | 2 | 2 | 2 | 3 |
| 19 | Risk (inv) | 2 | 3 | 2 | 2 | 2 | 2 |
| | **Total** | **100** | **100** | **100** | **100** | **100** | **100** |

### Why the presets differ — the reasoning in one line each

| Preset | The thing that kills businesses of this type |
|---|---|
| **B2B SaaS** | CAC recovered over months → retention and cycle length decide viability; ability to pay gates everything |
| **Expert course** | Aspiration converts unreliably → urgency and willingness carry the weight; dense communities are how interest becomes purchase |
| **Agency / service** | Sold on trust and referral → the ceiling is credibility, not demand |
| **Local business** | Radius caps the addressable market before any other criterion applies |
| **Consumer product** | Thin margin per unit → only channels that scale cheaply matter |
| **High-ticket consulting** | One client changes the year → access and credibility dominate everything |
| **Marketplace** | Liquidity is the product → density on both sides decides survival |
| **Mobile app** | Store discovery is winner-take-most → retention determines whether paid installs are affordable |
| **Info product** | Self-serve, no sales conversation → demand and willingness must be pre-existing |
| **Subscription** | Churn is the only number → the need must genuinely recur |
| **B2B services / outbound** | The whole motion depends on a list and a reason to write today |

---

## Part 4 — The working sheet

Copy this. One column per segment. Fill scores with sources.

```
SEGMENT SCORING SHEET
Business model: ______________  Preset used: ______________
Weight adjustments (max 3): ______________________________
Regime: [ ] Focus (challenger / new offer / service)  [ ] Reach (established brand, mass category)
Date: __________   Scored by: __________
```

| # | Criterion | W | Seg A | Seg B | Seg C | Seg D | Seg E |
|---|---|---|---|---|---|---|---|
| 1 | Pain intensity ⚠ | | | | | | |
| 2 | Urgency ⚠ | | | | | | |
| 3 | Ability to pay ⚠ | | | | | | |
| 4 | Willingness to pay | | | | | | |
| 5 | Reachability ⚠ | | | | | | |
| 6 | Concentration | | | | | | |
| 7 | Trust accessibility ⚠ | | | | | | |
| 8 | Existing demand | | | | | | |
| 9 | Competition (inv) | | | | | | |
| 10 | Differentiation | | | | | | |
| 11 | Free acquisition | | | | | | |
| 12 | Paid acquisition | | | | | | |
| 13 | Content potential | | | | | | |
| 14 | Sales cycle (inv) | | | | | | |
| 15 | Retention | | | | | | |
| 16 | Referral | | | | | | |
| 17 | Strategic fit | | | | | | |
| 18 | Positioning strength | | | | | | |
| 19 | Risk (inv) | | | | | | |
| | **Weighted total** | 100 | | | | | |
| | **Gate check** | | PASS / FAIL on ___ | | | | |
| | **Assumption cells** | | __ / 19 | | | | |
| | **Confidence** | | High / Med / Low | | | | |

**Weighted total** = Σ(score × weight) ÷ 100. Range 1.00–5.00.

---

## Part 5 — Reading the result

**Never rank by total alone.** Report three numbers together: **total · gate result · assumption count.**

> A 3.9 with two assumption cells beats a 4.3 with eleven.

### Interpretation bands

| Total | Reading |
|---|---|
| **4.2+** | Strong candidate — proceed to positioning and a validation experiment |
| **3.5–4.2** | Viable — proceed, but name the two weakest criteria as the things to test first |
| **2.8–3.5** | Conditional — usually reachable *later*; name the asset or condition that would lift it |
| **Below 2.8** | Reject, and say why in one sentence |
| **Any gate = 1** | **Disqualified regardless of total.** State the gate and the reason on the same line. |

### Four reading rules

1. **A tie is a signal, not a problem.** Two segments within ~0.3 are not distinguishable by analysis. Break the tie with an experiment — parallel smoke tests, or willingness-to-pay research — not with more argument.
2. **Uniform excellence deserves suspicion.** Real segments have trade-offs. A segment scoring 4–5 across all nineteen criteria usually means uniform assumption, not uniform quality. Check the assumption count.
3. **Report the best segment you are rejecting, and why.** The rejected runner-up is often the more useful finding, because it names the condition under which the strategy should change.
4. **Low confidence is a legitimate output.** If more than half the cells are assumptions, deliver the matrix as a research plan with the five highest-value unknowns ranked — not as a recommendation.

---

## Part 6 — Worked fragment

An abbreviated example of correctly sourced scoring. Preset: **Agency / service**.

**Six of the nineteen rows are shown**, to illustrate cell formatting rather than to demonstrate arithmetic — the weighted totals below come from the full nineteen and cannot be recomputed from what is visible here. In a real deliverable, show all nineteen so the reader can check your maths. **If your stated total does not reconcile with your own table, every other number in the report becomes suspect.**

| # | Criterion | W | Seg A: *inherited-account marketing leads* | Seg B: *"SMBs needing marketing"* |
|---|---|---|---|---|
| 1 | Pain intensity | 7 | 5 [12/15 interviews described a specific failed report] | **2 ⚠ [ASSUMPTION]** |
| 2 | Urgency | 6 | 5 [board review dates named in 9/15] | **1 ⚠ [ASSUMPTION — no trigger identified]** |
| 3 | Ability to pay | 12 | 4 [all had an existing agency retainer] | 3 [varies wildly; no evidence] |
| 5 | Reachability | 7 | 5 [LinkedIn role-change filter + 3 named Slack groups] | **1 [no list exists for "SMBs needing marketing"]** |
| 7 | Trust accessibility | 11 | 4 [case study in-vertical was sufficient in 6/6 won deals] | 3 [unknown] |
| 16 | Referral | 9 | 4 [4/15 named a peer who referred them] | **2 ⚠ [ASSUMPTION]** |
| | **Weighted total** | | **4.4** | **2.1** |
| | **Gate check** | | PASS | **FAIL — gates G2 (urgency) and G4 (reachability) both score 1** |
| | **Assumption cells** | | 1 / 19 | 11 / 19 |

**Verdict.** Segment B is not a low-scoring segment. It is **not a segment** — two gates at 1 and a majority of cells unevidenced. The correct output is not "B scored 2.1"; it is *"B cannot be scored, because it has no trigger and no list. Here is what would have to be true for it to become one."*
