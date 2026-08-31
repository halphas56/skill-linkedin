# Willingness to Pay

**The module almost every audience generator skips.** Finding a person with a problem is the easy half. The hard half is establishing that money will move.

**The governing distinction:**

```
PAIN  ≠  DEMAND  ≠  WILLINGNESS TO PAY
```

Three separate variables. They fail independently, and confusing them produces the most demoralising outcome in commerce: enthusiastic conversations, grateful users, no revenue.

---

## §1 — The three-way distinction

| Variable | Question | Failure looks like |
|---|---|---|
| **Pain** | Does the problem hurt? | Everyone agrees it's a problem; nobody does anything |
| **Demand** | Are they actively trying to solve it? | Real pain, but tolerated indefinitely — chronic, not acute |
| **Willingness to pay** | Will they hand *you* money for *this* solution at *this* price? | Active search, then "we'll build it internally" or "isn't there a free one?" |

Each is a separate gate. A segment must clear all three.

### The counter-intuitive comparison

| Segment | Pain | Money at stake | Verdict |
|---|---|---|---|
| **A** — extreme pain, no budget | 10/10 | ~0 | **Bad segment.** Applause, gratitude, no revenue |
| **B** — moderate pain, problem touches $100k of revenue | 5/10 | $100k | **Potentially excellent** |

This inverts the intuition that drives most audience research. **You are not selecting for how much it hurts. You are selecting for how much it costs.**

Segment B's moderate annoyance sits on top of a large number, which means a solution has obvious economic justification and an easy internal business case. Segment A's agony sits on top of nothing, and no amount of empathy converts that into a purchase order.

> The corollary for segment selection: **prefer the segment where your solution touches the largest amount of money**, even if the emotional intensity is lower. Emotional intensity tells you the *message*; economic exposure tells you the *price*.

---

## §2 — Ability vs. willingness

Two different variables, and treating them as one is a standard error.

| | **Ability to pay** | **Willingness to pay** |
|---|---|---|
| Question | Do they have the money? | Will they spend it on *this*? |
| Blocked by | No budget, no revenue, no approval route | Category norms, free alternatives, priorities, "we'll build it" |
| Evidence | Funding, headcount, existing vendors, job postings | What they already pay for **in this category** |
| Fails as | "We'd love to, but we can't afford it" | "We could, but we won't" |

**Enterprises with millions in budget refuse to pay $50 for a category they have decided should be free.** Developers who spend thousands on hardware resist paying for tooling. Photographers spend four figures on a lens and balk at $9/month for backup.

**Ability is about the wallet. Willingness is about the category's norms.** Check both, separately, with different evidence.

### The third variable nobody checks: approval route

A segment can have ability *and* willingness and still be unbuyable because the **process** costs more than the price. A ₽200k purchase requiring a tender, three signatures and a security review is a different business from a ₽200k purchase a founder makes on a call.

**Always ask: "who has to approve a purchase this size, and what does that take?"** The answer determines your sales motion, your cycle length, and whether the segment is viable at your price point at all.

---

## §3 — Economic Value Estimation

The rigorous way to price against a problem rather than against your own costs. From Nagle's *The Strategy and Tactics of Pricing*: `[E]`

```
TOTAL ECONOMIC VALUE  =  REFERENCE VALUE  +  DIFFERENTIATION VALUE
```

| Component | Definition |
|---|---|
| **Reference value** | The price of the customer's **best alternative** |
| **Differentiation value** | The worth of everything that distinguishes your offering from that alternative |

An EVE model is a set of **value drivers**, each with a short written description and an equation estimating its impact on the customer's P&L. `[E]`

### Worked example — the CPA case

Continuing the running example from `jtbd-engine.md`: an online store spending ₽500k/month on ads, whose CPA has risen ~40%, who does not know why.

**Step 1 — Size the problem.**
```
Monthly ad spend                    ₽500,000
CPA inflation                       ~40%
Monthly value destroyed             ≈ ₽140,000
Annualised                          ≈ ₽1,700,000
```

**Step 2 — Reference value (best alternative).**
```
Freelance audit, one-off            ₽80,000
OR in-house marketer                ₽150,000/month
OR do nothing → keep burning        ₽140,000/month
```

**Step 3 — Differentiation value.**
```
Time-to-answer: 3 days vs ~6 weeks alone
Weeks of burn avoided:  5 × ~₽35,000  ≈ ₽175,000
Confidence to resume scaling: unlocks growth they've frozen
```

**Step 4 — The conclusion.**
```
Total economic value  ≈  ₽80,000 (reference) + ₽175,000 (differentiation)
Defensible price band:  ₽100,000 – ₽150,000
```

**What this changes.** Priced against your own effort ("three days of work"), the number is ₽40–60k. Priced against the problem, it is ₽100–150k for the identical work. **Same deliverable, 2.5× the price, and easier to sell** — because the buyer's arithmetic now favours it obviously.

### Why a job-fitting solution commands a premium

The EVE arithmetic explains what a solution is *worth*. Christensen explains why customers will actually **pay** it: `[E]`

> *"The reason why we are willing to pay premium prices for a product that nails the job is because the **full cost of a product that fails to do the job** — wasted time, frustration, spending money on poor solutions — is significant to us. The 'struggle' is costly — you're already spending time and energy to find a solution and so, even when a premium price comes along, your internal calculus makes that look small compared with what you've already been spending, not only financially, but also in personal resources."*

**The implication for segment ranking:** the longer and more expensively a segment has been struggling, the *less* price-sensitive it is — because your price is compared against a running cost they have already normalised, not against zero.

**QuickBooks is the proof case.** It shipped with **half the functionality of existing accounting software at twice the price** and became the global category leader. Competitors were building the best *accounting software*. Intuit was solving the job — small business owners who *"just wanted to get money in and out of their business"* and did not want to understand debits, ledgers and closings at all. `[E]`

> *"A clear view of customers' jobs means an organization should never overshoot what those customers are actually willing to pay for. On the contrary, when customers find the right product to respond to their Job to Be Done, they're often willing to pay more."*

### Grateful premium vs. resentful premium

**Not all premium pricing is the same, and the difference decides retention.** `[E]`

| | **Job-based premium** | **Lock-in premium** |
|---|---|---|
| Example | IKEA when you must furnish a flat today; American Girl | Printer ink · proprietary chargers · phone cases |
| Mechanism | Solves the job better than any alternative | No better option *at this moment*, because you already bought the base product |
| What it does to anxiety | **Resolves** it | **Causes** it |
| Customer feeling | Grateful | *"We will give in and pay... but we will simultaneously despise the company for taking us to the cleaners"* |
| Durability | Survives competition | Collapses the moment an alternative appears |

**Diagnostic for a candidate segment:** if your price premium depends on the customer having no exit rather than on doing the job better, you are building resentment and modelling it as margin.

### Why this belongs in an audience skill

EVE is usually taught as a pricing tool. Here it is a **segment-selection tool**: run the calculation for each candidate segment and the ranking often reorders completely. The segment with the largest economic exposure to your solution wins, regardless of which one felt most enthusiastic in interviews.

---

## §4 — The value metric

**What you charge *per*.** Per seat, per transaction, per location, per GB, per campaign, per employee. `[E — Ramanujam & Tacke, *Monetizing Innovation*]`

The value metric must scale with the value the customer receives. When it does, price stops being an argument and becomes arithmetic.

**Why it matters for segment selection:** two segments may need *different value metrics* for the same product. When they do, they are genuinely different segments and probably different products — not a single market to be averaged.

| Segment | Natural value metric | Consequence |
|---|---|---|
| Solo operator | Flat monthly | Simple, low, predictable |
| Small agency | Per client account | Scales with their revenue |
| Enterprise | Per seat + volume | Procurement-compatible, expansion built in |

**Diagnostic:** if you cannot name what the price should scale with for a segment, you do not yet understand what value they get.

---

## §5 — WTP research methods

| Method | What it measures | Best for | Cost | Evidence ceiling |
|---|---|---|---|---|
| **Van Westendorp PSM** | Perceived acceptable price *range* | **New or innovative** offers — reveals expectations where no reference exists | Low | `L2–L3` |
| **Gabor-Granger** | Purchase likelihood at specific price points → a demand curve | **Established** categories — how demand responds to price changes | Low–med | `L3` |
| **Conjoint / discrete choice** | Feature-price trade-offs, competitive simulation | Optimising price *and* features together | High | `L3–L4` |
| **Observed competitor pricing** | What the market already sustains | Always — free | Free | `L5` |
| **Actual transactions** | What people really paid | Always the tiebreaker | — | `L6` |

### Choosing

- **New offer, no reference point** → Van Westendorp first. It surfaces what customers *expect* to pay when they have nothing to compare against.
- **Existing category** → Gabor-Granger. It answers the question you actually have: what happens to volume at each price.
- **Price and features interact** → conjoint, if the budget justifies it.
- **Practical guidance from the corpus:** Van Westendorp + Gabor-Granger together deliver roughly *80% of the insight at 30% of the cost* of conjoint. `[E]` Reserve conjoint for when features and price must be optimised jointly.

### Van Westendorp — the four questions

Per segment:
1. At what price would this be **so cheap** you'd doubt its quality?
2. At what price would it be **a bargain**?
3. At what price would it start to seem **expensive**?
4. At what price would it be **too expensive to consider**?

### The hard limit on all stated methods

**Every survey-based WTP method measures stated preference, and stated preference tops out at `L2–L3` no matter how large the sample.** `[E — corpus is explicit that PSM must be triangulated]`

People are unreliable narrators of their own future spending, in a consistent direction: they overstate willingness for things that sound good and understate it for things they'd be embarrassed to admit valuing.

**Always triangulate stated WTP against:**
- what competitors' prices have sustained for years (`L5`)
- ad longevity in the segment — 60–90+ days implies profitable unit economics (`L5`)
- what they already pay for adjacent things (`L5`)
- an actual costly-action test — deposit, pre-order, paid pilot (`L6`)

---

## §6 — Price segmentation: never average

Ramanujam & Tacke's warning, and one of the most expensive mistakes in the discipline: `[E]`

> If two customer groups have willingness to pay of **$20** and **$100**, pricing at the average of **$60** leaves money on the table with the high group and makes the product unaffordable for the low group. **You lose both.** Building two versions — one at $20 and one at $100 — is usually better.

**This is the pricing twin of the milkshake error** (`jtbd-engine.md`): averaging two real segments produces a fictional third one that nobody belongs to.

### Detection

You have a price-segmentation problem, not a pricing problem, when:
- WTP responses cluster bimodally rather than around a mean
- Comment mining shows "too expensive" beside "cheap for what it does" (the contradiction scan — `avatar-from-comments.md` §7)
- Sales calls split into two recognisable conversation types
- Two segments name different value metrics (§4)

**The fix is packaging, not discounting.** Two versions with genuinely different scope, not the same thing at two prices.

### The context for all of this

**72% of innovations fail to meet their financial targets, or fail entirely.** `[E — Ramanujam & Tacke]` The book's core prescription is to have the **willingness-to-pay conversation early** — before building — and to design the product around the price rather than pricing whatever got built.

For audience research, the translation is direct: **WTP is a segment-selection input, not a post-launch afterthought.**

---

## §7 — Budget archaeology

For any candidate segment, find where the money would actually come from. If you cannot trace it, willingness to pay is unproven regardless of how the interviews felt.

| Question | Good answer | Bad answer |
|---|---|---|
| What do they pay for this today? | A named vendor and a number | "Nothing, they do it manually" *(new budget = 3× the cycle)* |
| Whose budget line is it? | A named function with a named owner | "It would depend" |
| What was the last comparable purchase? | Specific, recent, with a price | Nothing comes to mind |
| What would be cut to fund this? | A specific alternative spend | "It would be incremental" *(usually means no)* |
| What approval does this size require? | A known, short route | Tender, committee, annual cycle |

### The strongest ability-to-pay signals, ranked

| Signal | Level | Why |
|---|---|---|
| They already buy from a competitor | `L6` | Ability, willingness and category norms all proven at once |
| **A job posting for a role doing this work** | `L5` | An approved salary is an approved budget — and it names the number |
| Long-running ads targeting them | `L5` | Someone else's money says the economics work |
| Marketplace orders for the same task | `L6` | Completed transactions for exactly this |
| Awarded tenders with contract values | `L6` | Public prices for public problems |
| Funding, headcount growth | `L4` | Capacity, not intent |
| They *say* they'd pay | `L2` | Stated preference |

**The job-posting signal deserves special weight.** A company advertising ₽150,000/month for someone to do what your product does has published, in a dated public document: the problem exists · it is worth at least ₽1.8M/year · budget is approved · and here is who to contact. Very few research artefacts carry that much at once.

---

## §8 — Red flags

Segments that fail WTP in predictable ways:

| Red flag | Why it fails | Test before proceeding |
|---|---|---|
| **Free-culture category** | Norm says this should be free | Does *anyone* charge for this successfully? |
| **"We'd build it internally"** | Their labour looks free to them | Have they built similar things before? Did those get finished? |
| **Students, pre-revenue founders, hobbyists** | Real pain, structurally no budget | Who else benefits and *does* have budget? |
| **Approval costs more than the price** | Process exceeds value | What's the smallest purchase they make without ceremony? |
| **Pain is chronic, not acute** | Tolerated for years already | What would force action within 90 days? |
| **Value accrues to someone other than the payer** | The payer sees only cost | Can you sell to whoever captures the value? |
| **Price is set by a race to the bottom** | Commoditised; the buyer compares on price alone | Is there a segment that buys on something else? |
| **They can only afford you at a price that doesn't work for you** | Model-market misfit | Is there a lighter product, or a different segment? |
| **Large engaged audience, almost no buyers** | **The aspirational pattern** — see below | Score against transactions only, never engagement |

### The aspirational-audience pattern

**Relocated here after test execution found it living only in the research report, which a working run may never load.** `[S]`

**The shape:** courses, coaching, career products, status goods, community products — anything sold on who the buyer wants to *become*. The audience is large, engaged, emotionally invested, and converts badly.

**Why.** People buy the **identity** cheaply — following, watching, saving, joining — and the **transformation** rarely. A subscriber has already got part of what they came for by subscribing.

**The diagnostic that matters:** 60,000 engaged subscribers and 11 buyers is **consistent, not contradictory.** Treating it as a paradox sends the client into funnel optimisation, copy rewrites and price experiments, none of which address the cause.

**Check before diagnosing anything downstream:**
- Is the promised outcome a **life theme** ("become a CFO", "get fit") rather than a job in a circumstance? Life themes generate engagement and no purchase
- Score the **four forces**: aspirational audiences characteristically show high Pull and **weak Push** — no struggling moment, no clock
- Is there a **trigger**? Without one, interest never becomes intent

**The rule:** never score an aspirational audience on engagement. Score it on completed transactions by comparable sellers — and if none exist, that absence is the finding.

**The "value accrues elsewhere" flag is the subtlest.** A tool that saves employees time but costs the company money will be loved by users and refused by buyers. Find who captures the value and sell to them — or accept that this is a consumer product being sold to a business.

---

## §9 — Evidence levels for WTP claims

Applying `evidence-ladder.md` specifically:

| Claim type | Level | Note |
|---|---|---|
| "This segment seems affluent" | `L0` | Speculation |
| "They should be able to afford this" | `L1` | Plausible mechanism |
| "One interviewee said ₽50k felt reasonable" | `L2` | Single stated preference |
| "Van Westendorp across 40 respondents shows a ₽40–70k corridor" | `L3` | Stated preference, larger n — **still stated** |
| "Three competitors have held prices in this band for 2+ years" | `L5` | Behavioural, market-validated |
| "Twelve of our own closed-won deals landed at ₽55–65k" | `L6` | Transactional |

**Never recommend a price on stated preference alone.** The minimum defensible position pairs one stated method (`L3`) with one behavioural observation (`L5`).

---

## §10 — Quality gate

- [ ] **Pain, Demand and WTP assessed separately** — not collapsed into one score
- [ ] **Ability and willingness assessed separately**, with different evidence
- [ ] **Approval route** identified — process cost vs. price
- [ ] **Economic value of the problem** quantified: reference value + differentiation value
- [ ] **Value metric** named — what the price scales with
- [ ] WTP triangulated: at least one **stated** and one **behavioural** source
- [ ] **Bimodality checked** — is this one segment or two averaged?
- [ ] **Budget archaeology** complete: existing spend, budget owner, last comparable purchase
- [ ] **Red flags** screened
- [ ] Every WTP claim carries an **evidence level**
- [ ] Segments ranked by **economic exposure**, not by emotional intensity alone

### The test

For each candidate segment, answer in one sentence: **"This problem costs them approximately ___ per year, they currently spend ___ on it, and the money would come from ___."**

If you cannot complete that sentence with numbers and a named budget line, willingness to pay is `L1` — a hypothesis — and the segment cannot be recommended as primary. It can be recommended for validation, which is a different and honest deliverable.
