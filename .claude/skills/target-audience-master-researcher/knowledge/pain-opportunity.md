# Pain Economics & Opportunity

**The second half of pain work: is this a business?**

`pain-discovery.md` answers *"is this pain real, and what is it actually?"* This file answers a different question that the skill previously **conflated with it**: *"can anything be built on it?"*

> **A 9/10 pain with 1/10 willingness to pay is a bad commercial opportunity. A 5/10 pain sitting on ₽100M of exposure may be an excellent one.** A single score cannot express that.

---

## §0 — The correction this file makes

**The previous version of this skill scored pain once, on ten criteria, and that was wrong.** `[S]`

The old PPS mixed two incompatible questions:

| Criterion | Actually measures |
|---|---|
| Frequency · Severity · Urgency · Emotional intensity | **How much it hurts** |
| Willingness to pay · Fit with offer · Solvability · Messaging clarity | **Whether it's a market** |
| Proof availability · Ethical safety | Neither — they are gates |

A single total let a severe-but-unmonetisable pain and a mild-but-lucrative one land on the same number, with the structure that mattered averaged away. **That is the averaging error the rest of this skill spends its time preventing** — committed by the skill's own instrument.

**Superseded by two independent scores.** Old PPS totals in any existing deliverable should be recomputed, not translated.

---

## §1 — Cost of inaction — a mandatory field

**Previously absent entirely.** It is the field that converts a complaint into a number, and without it no economic comparison between pains is possible.

**The question, asked with a horizon:**

> **What happens if this is not solved for the next 3 / 6 / 12 months?**

Ten dimensions. Not all apply; the ones that do must be quantified.

| Dimension | Probe |
|---|---|
| **Money lost** | Direct leakage — write-offs, penalties, refunds, waste |
| **Time lost** | Hours × people × frequency × rate |
| **Revenue lost** | Deals not closed, customers not served, capacity not sold |
| **Opportunity cost** | What they cannot do while this occupies them |
| **Productivity loss** | Output foregone by the people involved |
| **Churn** | Customers who leave because of it |
| **Operational risk** | Probability × consequence of the failure it enables |
| **Reputation risk** | What it costs when someone outside notices |
| **Stress** | Not monetisable, and it drives urgency — record it |
| **Growth constraint** | The ceiling it imposes on scaling |

### Why quantification changes the conversation

```
WEAK:   "Reports are made manually."
STRONG: 3 people × 4 hours/week × 52 weeks = 624 person-hours a year.
```

The first is a complaint. **The second is a budget line**, and it is the same fact.

**And it sets the price.** A solution to a ₽1.7M/year problem is priced against ₽1.7M, not against your delivery cost. See `willingness-to-pay.md` §3.

### The honesty rule

Cost of inaction is **the field most easily fabricated**, because the arithmetic looks authoritative regardless of the inputs. `[S]`

- Every multiplier must be **sourced**: *"4 hours" — from whom, said when?*
- An estimate the client supplied is `L2`, not fact
- **Show the arithmetic, never only the total.** A number without its working is exactly the false precision this skill warns about
- If you cannot source a multiplier, write the formula with the gap visible: `3 people × [HOURS UNKNOWN] × 52`

---

## §2 — The behavioural evidence ladder for pain

The general `evidence-ladder.md` grades *claims*. This grades **what someone has actually done about a pain** — which is the more discriminating question, because talk is free.

| Rung | Signal | Why it weighs | Maps to |
|---|---|---|---|
| **B1** | **Complaining** — *"I hate doing X"* | Free. Says nothing about priority | `L2` |
| **B2** | **Searching** — repeatedly looks for a fix | Cost: attention and intent | `L3` |
| **B3** | **Workaround** — built a sheet, a script, a process | **Cost: hours.** Proven willingness to pay in the only currency that never lies | `L5` |
| **B4** | **Time investment** — sustained weekly effort | Cost: recurring hours, forever | `L5` |
| **B5** | **Switching** — tried and abandoned products | Cost: evaluation effort + change risk | `L5` |
| **B6** | **Paying** — already pays for a partial fix | **Budget released.** Ability and willingness both proven | `L6` |
| **B7** | **Hiring** — employs someone to do this work | An approved salary is an approved budget, **with a number** | `L6` |
| **B8** | **Budget allocated** — a line exists for this category | The strongest single signal available | `L6` |
| **B9** | **Market evidence** — many organisations pay for this category | The problem is proven at market scale, not just at this account | `L6` + prevalence |

### How to use it

**Never report a pain without its highest observed rung.** *"Pain confidence: HIGH — B7 (three job postings found)"* is a finding. *"This is an important pain"* is an opinion.

**The gap between B1 and B3 is where most fictional pains die.** People complain freely about things they have never once tried to fix. **If nobody built a workaround, ask why not** — usually the answer is that it is not worth the effort, which means it is not worth paying for either.

---

## §3 — Frequency is not importance

**A correction with academic grounding, and it invalidates how most pain analysis — including AI-driven analysis — actually works.** `[E — Griffin & Hauser, "The Voice of the Customer", *Marketing Science* 12(1), 1993]`

Griffin & Hauser tested precisely the hypothesis that everyone quietly assumes: that customers mention their most important needs most often, so counting mentions could substitute for measuring importance.

> **The data do not support this hypothesis. High-priority needs do not seem to be mentioned more often than low-priority needs.**

They concluded that formal research is required to establish priority — mention frequency cannot stand in for it.

### What this breaks

```
100 people say:  "The interface is ugly."
 10 people say:  "This bug costs us $10k every month."
```

**Counting mentions ranks the first one higher. It is the less interesting problem by an order of magnitude.**

Every "top 10 pain points" list built by tallying reviews, comments or search volume is measuring **prevalence** and calling it **importance**.

### The rule

**Measure and report the two separately, always:**

| | What it is | How to get it |
|---|---|---|
| **Prevalence** | How many people have it | Counting. Cheap and reliable |
| **Importance / severity** | How much it costs the people who have it | **Asking those people to rank or trade off.** Cannot be inferred from counting |

**In the two scores below:** prevalence sits in the *Commercial* score, severity in the *Strength* score. They are never summed.

**Practical note from the same paper:** roughly 20–30 customer interviews identify about 90% of the needs in a category — and **two analysts should code the transcripts, because one analyst finds only about half.** `[E]` The second point is routinely ignored and is the cheaper of the two fixes.

---

## §4 — Two scores

### Pain Strength Score — *how much does this hurt?*

| Criterion | Weight | 1 | 5 |
|---|---:|---|---|
| **Severity** | 20 | Mild annoyance | Quantified loss they state unprompted |
| **Urgency** | 20 | No consequence to waiting a year | Dated deadline with a penalty |
| **Frequency** | 15 | Once ever | Weekly or continuous |
| **Cost of inaction** | 20 | Nothing measurable | Large, quantified, compounding |
| **Persistence** | 10 | Transient; resolves itself | Structural; worsens without intervention |
| **Emotional intensity** | 5 | Neutral description | Raw, unprompted language |
| **Evidence quality** | 10 | `L0`–`L1` | `L5`–`L6`, triangulated |

`PSS = Σ(score × weight) / 5` → **0–100**

### Commercial Opportunity Score — *can a business be built on it?*

| Criterion | Weight | 1 | 5 |
|---|---:|---|---|
| **Willingness to pay** | 20 | Category norm is "should be free" | Already pays for a partial fix |
| **Ability to pay** | 15 | No budget exists anywhere | Existing line larger than your price |
| **Economic value** | 15 | Cost of inaction ≈ 0 | Cost of inaction ≫ plausible price |
| **Prevalence** | 15 | A handful of people | Large, countable, reachable population |
| **Existing spend** | 10 | Nobody spends anything on this | An established category with real revenue |
| **Dissatisfaction with alternatives** | 10 | Incumbents are fine | Consistent complaints across every provider |
| **Reachability** | 5 | No list, no channel | A named list accessible this week |
| **Product fit** | 5 | We'd build something new | Our existing mechanism addresses it |
| **Evidence quality** | 5 | `L0`–`L1` | `L5`–`L6`, triangulated |

`COS = Σ(score × weight) / 5` → **0–100**

### The 2×2 — the point of splitting them

```
                    COMMERCIAL OPPORTUNITY
                 low                    high
            ┌───────────────────┬───────────────────┐
     high   │   THE CHARITY     │   THE OPPORTUNITY │
            │ Hurts badly, no   │  Build here       │
  PAIN      │ money. Real, and  │                   │
  STRENGTH  │ not your market   │                   │
            ├───────────────────┼───────────────────┤
     low    │      DROP IT      │    CHECK AGAIN    │
            │ Say so plainly    │ Big market, mild  │
            │                   │ pain? Usually the │
            │                   │ pain is mis-      │
            │                   │ measured, not the │
            │                   │ market            │
            └───────────────────┴───────────────────┘
```

**The two diagonal quadrants carry the information:**

- **The Charity** *(high pain, low commercial)* — the trap that feels most like a discovery. Students, pre-revenue founders, hobbyists, and anyone whose defining feature is that they cannot afford the incumbent. Genuine suffering, no budget. **Naming it as a charity is the finding**, not a failure.
- **Check Again** *(low pain, high commercial)* — large market, mild reported pain. **Usually means the pain was measured on B1 complaining rather than B3+ behaviour.** Go back to §2 before believing it.

**Reporting rule:** `PSS · COS · quadrant · evidence rung · gates`. A single blended number is prohibited — blending is what this file exists to correct.

### Gates — they still override

| Gate | Fails when |
|---|---|
| **Evidence** | the pain sits at `L0`–`L1` — you are scoring a guess |
| **Ethical safety** | it only lands by amplifying fear (`pain-discovery.md` §8) |
| **Relievability** | no mechanism **and** no proof — see the fields 10/11 rule |

---

## §5 — Pain Concentration

**Where does this problem become 5–10× worse?** `[S]`

Most pain analysis produces a flat statement — *"companies waste time on reporting"* — which is true, useless, and describes no one in particular.

**The concentration question finds where the same pain is disproportionately severe**, and the answer is frequently a segment nobody has named.

```
FLAT:          "Agencies spend time on client reporting."
CONCENTRATED:  "Performance agencies running 15–50 client accounts
                suffer disproportionately, because reporting effort
                scales linearly with accounts while headcount doesn't."
```

### The eleven concentration axes

Walk each and ask *where does this get much worse?*

**Company size · volume · frequency · role · maturity · industry · regulation · geography · channel · technology stack · life stage**

### Why this belongs in an audience skill, not just a pain skill

**Pain concentration is an unexpected-audience generator.** `[S]` The place where a common pain becomes acute is, by construction:

- a segment defined by **circumstance** rather than demographics
- one with **higher willingness to pay** than the flat average implies
- one competitors serving the flat market are **not addressing specifically**

**This closes the loop back to audience discovery** — pain research improving segmentation rather than merely consuming it. Cross-referenced as a generator in `segment-generation-lenses.md`.

---

## §6 — Pain Threshold

**The point at which the existing solution stops scaling.** `[S]`

A pain often exists at every level and only *converts* above a breakpoint:

```
  20 leads/day  →  a spreadsheet is fine
 100 leads/day  →  the spreadsheet is a nightmare
```

**Find the breakpoint and you have an ICP with a trigger built in.**

| Vague | With threshold |
|---|---|
| "Companies that need a CRM" | "Service businesses past ~5–10 sales staff, where manual lead handoff starts causing systematic lost enquiries" |

### How to find it

1. Ask **switchers**: *"At what point did the old way stop working?"*
2. Look for the **unit that scales** — accounts, leads, staff, SKUs, locations, transactions
3. Find where **effort stops being linear** and starts compounding
4. Check the **non-switchers below the line** — they should report the same pain as tolerable

**The confirmation test:** people below the threshold should describe the same situation and not consider it a problem. **If they do consider it a problem, you have found a different pain, not a threshold.**

### What it gives you

- **A precise ICP boundary** — measurable and observable from outside
- **A trigger** — crossing the threshold *is* the buying event
- **Timing** — monitor the metric, arrive as they cross
- **A disqualifier** — below the line is your anti-audience, and refusing them protects your case studies

---

## §7 — Pain Evolution

**The same business has different pains at different maturity stages.** `[S]`

```
Stage 1   Where do we find customers at all?
Stage 2   How do we get customers predictably?
Stage 3   How do we lower CAC?
Stage 4   How do we scale without CAC rising?
Stage 5   How do we manage attribution across 8 channels?
```

**These are five different segments wearing one company name.** A message built for stage 2 is invisible to stage 4 and vice versa.

### Operational consequences

| Consequence | What to do |
|---|---|
| **Determine the maturity stage before writing anything** | It changes the pain, the vocabulary and the buying process |
| **Your best customers may be at one stage only** | And they age out. Model the churn as graduation, not failure |
| **The next stage is your expansion path — or your ceiling** | If you cannot serve stage 4, stage 3 customers leave when they succeed |
| **Stage-crossing is a trigger** | Same mechanism as §6 |

**The diagnostic question:** *"What was your biggest problem in this area a year ago, and is it the same now?"* A changed answer locates the stage and gives you the trajectory.

---

## §8 — The Pain × Segment matrix

**The artefact that feeds pain research back into audience research.**

Score each pain, in each segment, on Pain Strength. One number per cell.

| Pain | Freelancer | Small agency | 100-person agency |
|---|---:|---:|---:|
| Reporting | 4 | 7 | 8 |
| Attribution | 5 | 8 | **10** |
| Client reporting | 2 | **9** | 9 |
| Creative fatigue | 7 | 8 | 8 |
| Managing permissions | 2 | 5 | **9** |

### How to read it

**Read the rows for concentration.** A row that rises sharply across segments has found a threshold (§6) or a concentration axis (§5). *Attribution* going 5 → 8 → 10 says the pain scales with something.

**Read the columns for positioning.** A column with one standout value tells you what to lead with **for that segment specifically**. Small agencies lead with client reporting; large agencies lead with permissions.

**Read the flat rows sceptically.** *Creative fatigue* at 7-8-8 is either genuinely universal — in which case it is table stakes and cannot differentiate — or it was scored from complaint volume rather than from behaviour. Check the rung (§2).

**Read the gaps.** A cell scoring 2 where its neighbours score 9 is a segment boundary made visible.

### The feedback rule

> **If the matrix shows one pain behaving completely differently across two segments, those segments were correctly separated. If every pain scores identically across two segments, they are one segment.**

That is a **segmentation test derived from pain data** — and it is the loop the brief asked for: pain research improving audience research rather than only consuming its output. `[S]`

---

## §9 — Evidence against

**Mandatory, and previously absent.** `[S]`

Having concluded a pain is important, the run must actively look for reasons it might not be. This is the conforming-data fallacy (`evidence-ladder.md` §10b) applied at pain level, and an LLM is structurally prone to it: having generated a compelling pain narrative, everything subsequently found will appear to confirm it.

**Every pain card carries both columns:**

| Evidence FOR | Evidence AGAINST |
|---|---|
| 20 complaints across 3 communities | Everyone uses a free tool and seems content |
| Emotional language, unprompted | Nobody has ever bought a specialised product for it |
| Two interviewees described it in detail | It occurs once a year |
| | Most say it is annoying but does not block work |

**In that example the pain survives as real and fails as commercial** — exactly the *Charity* quadrant, and visible only because the second column exists.

### Where to look for disconfirmation

- **Is anyone paying?** A category with complaints and no revenue is usually a category with no willingness to pay
- **How often, really?** Annual pains generate loud complaints and no urgency
- **Do free tools already handle it?** Then your price ceiling is near zero
- **Is it blocking, or merely irritating?** Ask what they did *instead* of solving it
- **Who does *not* have this pain, in the same segment?** If plenty of comparable people are fine, the pain belongs to a sub-segment you have not isolated

**The rule:** an "evidence against" column that is empty means nobody looked. **Write "searched, none found" — never leave it blank**, so the reader can tell the difference between a clean bill and an unexamined one.

---

## §10 — Quality gate

- [ ] **Cost of inaction** quantified with the arithmetic shown and every multiplier sourced
- [ ] Highest **behavioural rung** (B1–B9) recorded per pain
- [ ] **Prevalence and severity reported separately** — never summed, never inferred from each other
- [ ] **Two scores** computed; no blended total anywhere
- [ ] **Quadrant** named — including "Charity" where that is the honest answer
- [ ] Gates checked separately from scores
- [ ] **Concentration** examined across the eleven axes
- [ ] **Threshold** sought, and confirmed against people below the line
- [ ] **Maturity stage** identified
- [ ] **Pain × Segment matrix** built where more than one segment is live
- [ ] **Evidence AGAINST** populated for every pain — *"searched, none found"* if that is the truth
- [ ] At least one pain classified as **not a commercial opportunity**, with the reason

### The test

> **Name the pain you found that hurts most and is worth least. If you cannot, you measured only one thing.**
