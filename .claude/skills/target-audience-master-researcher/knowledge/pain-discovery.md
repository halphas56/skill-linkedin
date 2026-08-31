# Pain Discovery, Validation and Closing

**The module for working with customer pain properly** — finding it, telling it apart from things that resemble it, decomposing it, proving it is real, and addressing it in messaging without manipulation.

**Paired file:** `pain-opportunity.md` answers the separate question of whether a business can be built on it — cost of inaction, the two scores, concentration, threshold, evolution, and the Pain × Segment matrix. **The two questions were previously conflated in a single score; they are not the same question.**

---

## §0 — Why this file exists, honestly

**Pain was already everywhere in this skill and nowhere in particular.** An audit on 2026-08-26 found ~200 mentions across 20 files — pain as a scoring criterion, as the Push force, as a VOC language type, as a comment tag, as the first gate — but:

| Checked | Found |
|---|---|
| A pain **taxonomy** beyond the three structural types | Only VPD's outcome/obstacle/risk + the five pressures |
| Prioritisation of pains **within** a segment | Only "extreme / moderate" |
| **Surface complaint vs. root pain** | **No coverage at all** |
| **Ethics of pain-based messaging** | **No coverage at all** — the single hit was about competitors faking reviews |

The last two were genuine holes, and the fourth was the serious one: a skill that teaches you to find and amplify pain, with nothing about where amplification stops being legitimate, is incomplete in a way that matters.

**This file consolidates what was scattered and fills what was missing. It does not replace the existing treatments** — `customer-profile.md` §3 still owns the structural split, `willingness-to-pay.md` still owns Pain ≠ Demand ≠ WTP, `jtbd-engine.md` §6 still owns the four forces. This is the connective layer plus the two missing halves.

---

## §0b — The quotation-mark rule

**A hard prohibition, stated separately because it is the one an LLM is most likely to break while trying to be helpful.** `[S]`

> **If no one actually said it, it does not go in quotation marks.**

A language model producing pain research will generate customer quotes that are vivid, idiomatic, emotionally precise and completely invented — because a good quote is exactly what the surrounding text calls for. The fabrication is not malicious; it is stylistic completion. **It is still fabrication, and it is the single fastest way to make a research document worthless.**

| Permitted | Prohibited |
|---|---|
| **Paraphrase, marked as such:** *Users report difficulty reconciling two systems* | *User quote: "I'm exhausted from spending hours every week…"* — when nobody wrote that |
| **A real quote with source and date:** *"I have no idea where my ad money is actually going"* — Reddit r/PPC, 2026-03 | A composite quote assembled from several real ones |
| **An illustrative example, explicitly labelled:** *[constructed example, not a real quote]* | A "typical" quote written to demonstrate a point |
| **A blank:** `[VERBATIM NEEDED]` | Filling the blank because the table looked incomplete |

**Preserve the original wording exactly**, including the language it was said in. If a customer wrote *"I have no idea where my ad money is actually going"*, that is the quote — not *"the user experiences difficulty attributing advertising spend."* The second is a summary of the first with everything useful removed.

**The check before delivery:** every quotation mark in the document must trace to an artefact with a source and a date. **Any that cannot, loses its quotation marks and becomes a paraphrase, or is deleted.**

---

## §1 — Four orthogonal axes, not competing lists

The skill already carried three classifications of pain and treated them as alternatives. **They are not alternatives. They are independent axes, and every pain has a value on each.** `[S]`

| Axis | Values | What it determines |
|---|---|---|
| **Structural** — what kind of thing it is | outcome · obstacle · risk | **The response.** Fix it, remove it, or reassure against it |
| **Domain** — what area of their life it hits | fourteen types, §2 | **The language.** Which words land |
| **Conversion** — whether money will move | compliance · time · risk · status · money | **Whether it converts** at all |
| **Articulation** — do they call it a problem? | articulated · **latent** | **Whether asking will ever find it.** See §2 |

**A fully classified pain is a 4-tuple**, e.g.:

> *"I lose the whole of Sunday evening reconciling two exports by hand"*
> → **obstacle** (structural) · **time + operational** (domain) · **time pressure** (conversion) · **articulated**

**Why the tuple matters.** Each axis answers a question the others cannot, and skipping one produces a characteristic failure:

- Skip **structural** → you reassure against an obstacle, or try to remove a fear. Neither works.
- Skip **domain** → your copy is in your vocabulary, not theirs.
- Skip **conversion** → you build for a pain nobody pays to fix. See `willingness-to-pay.md`.
- Skip **articulation** → you search only for what people call problems, and every latent pain stays invisible.

---

## §2 — The domain taxonomy: fourteen types

`[S — a practitioner synthesis; the categories are a working classification, not a sourced model. Their value is coverage, not authority.]`

| # | Type | What it is | Typical verbatim | Converts when |
|---|---|---|---|---|
| 1 | **Functional** | The task doesn't get done, or gets done badly | *"It just doesn't work with our file format"* | The task is required, not optional |
| 2 | **Emotional** | How it makes them feel — dread, shame, anxiety, exhaustion | *"I dread Mondays because of this report"* | Intensity is high **and** an outlet exists |
| 3 | **Financial** | Direct money lost, leaked, or not earned | *"We wrote off ₽400k in unbilled hours last year"* | The number is known. If it isn't, quantify it first |
| 4 | **Social / status** | How they are seen by peers, clients, boss, family | *"I look like an amateur when I send that"* | An audience exists whose opinion has consequences |
| 5 | **Time** | Hours consumed, deadlines threatened | *"Two evenings a week, every week"* | Their time has a price they can state |
| 6 | **Operational** | The process is fragile, manual, dependent on one person | *"If Marina's on holiday, nothing ships"* | A failure has already happened, or is imminent |
| 7 | **Strategic** | It blocks something bigger — growth, a market, a raise | *"We can't take enterprise clients without this"* | The blocked thing is already funded or committed |
| 8 | **Identity** | It conflicts with who they believe they are | *"I'm supposed to be the organised one"* | Rarely stated directly. Surfaces in tone, not content |
| 9 | **Risk** | Something could go badly wrong | *"If we get audited on this we're finished"* | The consequence is named and dated |
| 10 | **Opportunity cost** | What they can't do because of this | *"I haven't taken on a new client in eight months"* | They can name the specific thing forgone |

### Four more types, added 2026-08-27

| # | Type | What it is | Typical verbatim | Why it was missing |
|---|---|---|---|---|
| 11 | **Process** | The result *is* achievable — the process to get it is awful | *"Every Monday, three hours pulling one report out of five systems"* | Distinct from functional: nothing is broken, everything is horrible |
| 12 | **Control / uncertainty** | They have the information and cannot decide | *"I have the data. I don't know what to do with it"* | **The most under-mapped B2B pain.** Nothing is missing; confidence is |
| 13 | **Friction** | Steps, switches and handoffs between tools | *"Open four tools and move the numbers by hand"* | A subtype of process, kept separate because the fix differs — remove steps, don't redesign the workflow |
| 14 | **Alternative** | The pain is caused by the current *solution*, not by the task | *"The CRM does solve it — implementation takes two months"* | **This is what makes switching possible.** Without it you only ever see greenfield demand |

**Type 12 deserves particular attention.** Dashboards, analytics and reporting products routinely solve a *functional* pain (the data was unavailable) and leave the *control* pain untouched (the buyer still cannot decide). The customer's own summary is usually some version of *"we have reports nobody acts on."*

**Type 14 is the switching engine.** A prospect happy with the task and unhappy with their tool is the easiest sale in the market and is invisible to research that only asks about the job.

### Latent pain is not a type — it is a state

The brief that prompted this section listed **latent pain** alongside the domain types. It does not belong there: `[S]`

> *"I just copy the enquiries from Telegram into Excel every morning."*

That is **operational + time + friction** by domain. What makes it *latent* is that **the person does not name it as a problem at all** — and that property cuts across every one of the fourteen types.

**Treat it as a flag on the fourth axis — articulation:**

| State | The person… | Research consequence |
|---|---|---|
| **Articulated** | Names it as a problem, unprompted | Findable by asking, by search, by review mining |
| **Latent** | Describes the behaviour without calling it a problem | **Invisible to every question containing the word "problem."** Found only by observing what they *do* |

**How to detect latent pain:** listen for a **repeated manual behaviour described neutrally**. *"Every morning I…"*, *"I just…"*, *"it's not a big deal, I only…"* — the diminutive is the tell.

**The chain:** repetitive workaround → candidate problem → **verify the consequence before calling it a pain.** A latent pain that costs nothing when examined is a habit, not an opportunity.

### The three that get missed

**Identity pain (8)** is the most under-detected and often the most powerful. It is almost never stated as a pain — it appears as over-explanation, defensiveness, or a joke. When someone says *"I know, I know, I should have a system"*, that is identity pain wearing self-deprecation.

**Opportunity cost (10)** is invisible to complaint-based research entirely, because nobody complains about the thing that never happened. It surfaces only if asked for directly: *"What have you not been able to do because of this?"*

**Strategic (7)** is where B2B budget actually lives. Functional pain gets a workaround; strategic pain gets a line item.

### Reconciliation with what the skill already had

- The **five pressures** (compliance · time · risk · status · money) are the conversion axis, not a competing taxonomy. Map: compliance ⊂ risk(9) + operational(6) · time = 5 · risk = 9 · status = 4 · money = 3.
- **JTBD's three dimensions** (functional/emotional/social) are the same distinction applied to *jobs* rather than pains. Types 1, 2 and 4 correspond. The other seven have no JTBD equivalent and that is the gap this taxonomy fills.

---

## §3 — Surface complaint → root pain

**Previously absent from the skill entirely.** The most common research failure is treating the first thing someone says as the finding.

> *"What might appear as the problem on the surface may actually be only a symptom of a much larger, underlying issue."* `[E]`

### The four layers

```
COMPLAINT      "Your export is slow"
    ↓ why does that matter?
FRICTION       "I have to wait around instead of finishing"
    ↓ why does that matter?
CONSEQUENCE    "I stay late on Thursdays"
    ↓ why does that matter?
ROOT PAIN      "I promised my family I'd stop doing this"
```

**Only the bottom layer explains the purchase.** The top layer explains a support ticket.

### Laddering — the method

Grounded in **Means-End Chain theory**: move the respondent from features → benefits → motivational and emotional criteria. `[E]` Practitioners describe it as *"the annoying back-seat child technique"* — continually asking *why?*

**Procedure:**
1. Start from the stated complaint, verbatim.
2. Ask *"why does that matter to you?"* — not *"why?"*, which reads as a challenge.
3. Repeat until the answer stops changing, or becomes a **life theme** (`jtbd-engine.md` §2) — that is one rung too far; step back up one.
4. Record every rung. The middle rungs are your content; the bottom rung is your positioning.

**Stopping rules — both matter:**
- **Too shallow:** the answer is still about the product. Keep going.
- **Too deep:** the answer is *"I want to be a good parent"* — a life theme, true of everyone, triggers no purchase. Step back up.

**The right depth is one rung above the life theme**, which is where the abstraction test also lands (`jtbd-engine.md` §3). Two instruments, one altitude.

### Two directions, not one — and the skill previously had only one

**Laddering goes *up*, toward meaning. Pain chains go *down*, toward cost.** They are different operations answering different questions, and the skill was missing the second. `[S]`

```
            ROOT PAIN  ("I promised my family I'd stop")
                 ↑
                 │   LADDERING — "why does that matter to you?"
                 │   Finds:  meaning · motivation · positioning
                 │
            COMPLAINT  ("your export is slow")
                 │
                 │   PAIN CHAIN — "and what does that lead to?"
                 │   Finds:  consequence · economics · who else is affected
                 ↓
        BUSINESS CONSEQUENCE  (lost deals, no sense of control)
```

**Worked example, downward:**

```
Leads have to be moved across by hand
   ↓ and what does that lead to?
Time is lost
   ↓
Enquiries are occasionally missed
   ↓
Prospects never get a reply
   ↓
The company loses sales
   ↓
The owner starts checking the sales team's work personally
   ↓
No sense of control over the business
```

Read what happened to the **type** as it descended:

> **operational → productivity → financial → management → emotional**

**The commercially decisive link is frequently the last or second-to-last, not the first.** The first link — *"leads are moved by hand"* — sells a data-transfer feature. The last — *"no sense of control"* — is what the owner will actually pay to fix, and it is what the message should name.

**Run both directions on every serious pain.** Upward gives you the positioning; downward gives you the price.

### The full seven-link decomposition

Combining both directions produces the chain that downstream skills actually need:

| Link | The question | Example |
|---|---|---|
| **Signal** | What was literally observed? | A comment, a ticket, a review line |
| **Symptom** | What is measurably off? | *"CPA rose from $20 to $37"* |
| **Problem** | What can't they do? | *"Doesn't know which creatives stopped working"* |
| **Root problem** | Why does that keep happening? | *"No systematic process for creative testing"* — **must be confirmed, not assumed** |
| **Consequence** | What follows behaviourally? | *"Afraid to raise the ad budget"* |
| **Cost of inaction** | What does that cost, per period? | *"Store doesn't scale; profit foregone"* + hours spent guessing |
| **Desired outcome** | What do they want instead, in their metric? | *"Know within a day which creative to cut"* |

**Only links 2, 3, 5 and 7 are typically observable.** Link 4 (root) is an inference and must be labelled as one; link 6 (cost) must be calculated with sourced multipliers — see `pain-opportunity.md` §1.

**The confidence discipline across the chain:** `[S]`

```
confirmed fact   →   inference   →   hypothesis
```

Each link is labelled with which it is. **A chain presented entirely as fact, when links 4 and 6 were reasoned, is the most common way a pain analysis becomes fiction while looking rigorous.**

### Where the "5 Whys" fails here

The 5 Whys is a **root-cause tool for defects**, built to find a single mechanical cause. Human motivation is not a fault tree — it branches, and different people ladder from the same complaint to different roots. `[S]`

**Use laddering, not 5 Whys, and expect a tree rather than a chain.** If ten people ladder from one complaint to three distinct roots, **that is three segments**, not noise to average away.

---

## §4 — What is not a pain

**The differential diagnosis.** The brief for this module named exactly the right confusion set, and each mistake produces a different downstream failure. `[S]`

| It looks like a pain but it's… | Test | If you treat it as a pain you get |
|---|---|---|
| **A desire** — "I want more clients" | Is there a *current negative state*, or only an absent positive? | Aspirational messaging that engages and never converts |
| **An objection** — "It's too expensive" | Does it appear *before* considering you, or only in response to your offer? | You rebuild the product to answer a pricing conversation |
| **A demographic** — "small businesses struggle" | Can you name the *moment*? | A segment with no *when*; nothing to time a campaign to |
| **A generic problem** — "inefficiency" | Would a real person say this sentence out loud about their own life? | Copy that fits any company and describes nobody |
| **A feature request** — "you need a Zapier integration" | Ladder it: what breaks without it? | You build a roadmap from the loudest customer |
| **Your own hypothesis** — one you arrived with | Where is the artefact? What did they actually say? | Confirming data (`evidence-ladder.md` §10b) |

**The single sharpest test:** *"Has this already cost them something specific, that they can name?"* A desire costs nothing yet. A pain has already taken money, hours, sleep, or standing.

---

## §5 — Evidence signals

### Strong-pain indicators — in rough order of weight

| Signal | Why it weighs | Level it can reach |
|---|---|---|
| **They built a workaround** | Paid in hours. A free specification and proven willingness to pay | `L5` |
| **Money already spent** on a partial fix | Budget exists and has been released before | `L6` |
| **A hire posted** to do this work | An approved salary is an approved budget, with a number | `L5` |
| **Repeated across independent source types** | Survives the independence test | `L4` |
| **Emotional intensity** — profanity, hyperbole, caps | Proxy for urgency, therefore for WTP | `L2–L3` |
| **A dated consequence** — audit, launch, renewal, season | Urgency with a clock | `L3–L4` |
| **Abandoned alternatives** — "we tried X and Y" | Active search already happened | `L3` |
| **Contrast stated unprompted** — "it should just…" | They hold a clear model of the after-state | `L2` |
| **The same phrase recurring** across people | Shared vocabulary implies shared circumstance | `L3` |
| **They ask about it before you raise it** | The pain is top-of-mind, not prompted | `L2` |

### Weak-pain indicators — treat as disqualifying until proven otherwise

| Signal | What it usually means |
|---|---|
| **Stated only when prompted** | You created it with the question |
| **Tolerated for years** | Chronic, not acute. Looks like urgency in a transcript, behaves nothing like it in a pipeline |
| **No workaround exists** | Not worth the effort of improvising — so probably not worth paying for |
| **Nobody has spent anything** | Neither money nor hours have moved |
| **Phrased in your vocabulary** | You supplied the frame; they agreed to be polite |
| **Everyone agrees it's a problem** | Universal agreement without universal spending = table stakes, not opportunity |
| **Only the founder reports it** | `L0` until an artefact exists |
| **It disappears when you ask for a specific instance** | *"When did this last happen?"* — hesitation here is the finding |

### The invented-pain tell

**A pain that only exists in the analysis has three markers:** `[S]`
1. No verbatim quote attached
2. Perfectly symmetrical with a product feature
3. Nobody has ever been observed doing anything about it

**Any two of these and it is `L0`.** Delete it or label it.

---

## §5b — Workaround mining

**A named technique, because a workaround is frequently stronger evidence than a direct complaint.** `[S]`

A complaint costs seconds. **A workaround costs hours, repeatedly, and nobody builds one for a problem they do not have.**

### The eleven workaround forms

Any of these is a signal that the market's existing solutions do not adequately close the job:

| Form | What it tells you |
|---|---|
| **Built a spreadsheet** | The canonical form. Its columns are your feature spec |
| **Wrote a script** | Technical user, high pain, will evaluate you on rigour |
| **Chained several tools** | The gap is *between* products — an integration or a category |
| **Hired an assistant** | Pain quantified at a salary. `B7` on the behavioural ladder |
| **Moves data by hand** | Recurring, measurable, easy to price against |
| **Checks something manually every day** | A control pain (type 12) wearing operational clothes |
| **Keeps a parallel Notion / doc** | The system of record is not trusted |
| **Pays a freelancer** | Budget already released. `B6` |
| **Wrote an elaborate SOP** | The process is fragile and person-dependent |
| **Uses a product off-label** | Unusual-use generator — see `segment-generation-lenses.md` C17 |
| **Deliberately does nothing, with a coping story** | *"We just accept some leads slip"* — tolerated pain. Check severity honestly |

### How to mine them

**You cannot find these by asking about problems.** People do not describe their workarounds as problems — they describe them as *how things work here*.

**Ask about the process instead:**
- *"Walk me through what happens after a lead comes in."*
- *"What do you do on Monday mornings?"*
- *"Show me the file."* — the single highest-yield request in this entire skill
- *"What's the thing you'd be embarrassed to show me?"*

**Then ask what it cost to build**, and what it costs to maintain. Both numbers go straight into cost of inaction.

> **The workaround is a free specification written by the customer.** It shows what they need, in what order, at what tolerance — with every compromise they were willing to accept already visible.

---

## §5c — Trigger mining: why *now*

**Pain existing and pain being acted on are different states**, and the gap between them is usually months or years.

> The pain existed for a year. Then something happened — and it became active demand.

**The typical converters:**

| Trigger | Why it flips the state |
|---|---|
| Headcount grew — three more staff | Crossed the threshold (`pain-opportunity.md` §6) |
| Ad budget went from $2k to $20k | The cost of the pain scaled with it |
| Lost a major client | The consequence became concrete |
| New manager demanded reporting | A person with authority now cares |
| The incumbent raised its price | The comparison changed |
| Someone resigned | The manual process lost its owner |
| An audit, a deadline, a regulation | An external clock started |

**Buyer Persona Institute calls these Priority Initiatives** — the events that make a buyer start looking *now* rather than remaining with the status quo. `[E]`

### The two questions that separate pain from demand

> **1. How long has this been true?**
> **2. What changed recently that made you start looking?**

**If question 2 has no answer, you have a pain and not a buyer.** That is a legitimate finding — it means the segment is real but untimed, and the acquisition strategy must wait for triggers rather than push messages.

**And the operational payoff:** most converters above are **externally observable** — headcount, funding, job postings, price changes, regulatory dates. A trigger inventory turns a static segment into a monitored queue. See `habitat-research-playbook.md`.

---

## §5d — Lost-deal mining, and the source hierarchy

### Lost deals: the richest B2B source, almost never mined

Ask, for every deal that did not close, **which of four things happened**:

| Outcome | What it reveals |
|---|---|
| Bought nothing | The pain lost to inertia — **Push was too weak** |
| Bought a competitor | Your differentiation failed on a criterion you can name |
| Built it themselves | Their cost of building < your price, or trust was missing |
| Stayed with the status quo | **Habit and Anxiety beat Push and Pull** — the four-forces diagnosis |

Each surfaces something research on *won* deals cannot: **barriers · risk · switching cost · missing capability · budget constraint · trust deficit · priority conflict.** `[E — BPI: perceived barriers and decision criteria are studied alongside triggers]`

**The question that pays for the whole exercise:** *"What would have had to be true for you to buy?"*

### Source hierarchy — weight sources by what they cost the person

| Tier | Sources | Why this tier |
|---|---|---|
| **A — strongest** | Customer interviews · sales-call transcripts · support tickets · **lost deals** · cancellation reasons · churn interviews · customer emails | Real people, real stakes, specific circumstances. Usually already in the client's possession and unmined |
| **B — scale** | G2 · Capterra · Amazon · app stores · competitor reviews · Reddit · professional communities | Volume and independence. Buyers only — no non-customers |
| **C — behavioural / commercial** | Search data · Google Trends · **Upwork and Fiverr postings** · **job boards** · comparison and alternative searches · competitor pricing | **Someone already decided the problem was worth money.** Reaches `B6`–`B8` on the behavioural ladder |
| **D — signal** | Quora · YouTube comments · X · Facebook groups · Discord · Slack | Cheap, noisy, good for language and for finding where to look next |

**Tier C is the one most often skipped and the only free tier that reaches transaction-grade evidence.** A job posting or a freelance brief is a person who has already converted the pain into a budget line, in public, with a number attached.

**The triangulation rule applies across tiers, not within one.** Thirty Reddit threads is one source type at Tier B, however many there are.

---

## §6 — Validation: six tests

A pain is commercially real when it survives all six. Each maps to a level on `evidence-ladder.md`.

| # | Test | The question | Fails when |
|---|---|---|---|
| 1 | **Frequency** | How many times in the last 12 months? | Once, ever |
| 2 | **Intensity** | What did it cost, in a number they state? | Only adjectives |
| 3 | **Urgency** | What happens if they do nothing for six months? | Nothing much |
| 4 | **Spend** | What have they already paid — in money or hours? | Nothing |
| 5 | **Independence** | Does it appear across ≥3 *different kinds* of source? | Three review sites is one type |
| 6 | **Revealed behaviour** | Does what they *did* match what they *said*? | Stated only |

### Test 6 is the one that catches most fiction

**Stated pain and revealed behaviour diverge in a consistent direction** — people overstate pains that are socially creditable to have (*"we're very focused on security"*) and understate ones that are embarrassing (*"I don't actually understand our numbers"*). `[E — consistent with the Mom Test and SparkToro's "people are terrible at reporting their own behavior"]`

**The check:** for every stated pain, name one thing they would have *done* if it were true. Then look for it.

---

## §6b — Question library

**Five sets, because they do different jobs.** Mixing them is why most pain interviews produce polite fiction: a validation question asked during discovery contaminates the answer, and a discovery question asked during validation wastes the slot.

**The rule that governs all five** — ask about **what already happened**, never about opinions or predictions. `[E — Mom Test]`

### 1 · Discovery — surfacing pain that exists

**Interviews**
- Walk me through the last time [circumstance] happened. Start from the beginning.
- What were you doing right before you started looking for a solution?
- What did you try first? What happened?
- What part of this do you dread?
- If you could delete one step from this process entirely, which one?
- What have you just stopped doing because it wasn't worth the hassle?
- Who else gets pulled in when this goes wrong?
- What does this cost you when it goes badly — money, hours, or something else?

**Review and comment mining** *(read for, don't ask)*
- Which complaints appear in **3- and 4-star** reviews? Those people bought and stayed honest.
- Which reviewer is clearly **not the intended customer**? That is an unaddressed segment describing itself.
- What do people say they were doing *instead* before they bought?
- Which complaint recurs across **different vendors**? That is a category-level pain.

**Social listening / communities**
- Which question gets asked in this community every month, forever?
- What are people apologising for when they ask? *(identity pain)*
- What do people say at 11pm that they don't say at 11am?
- Which threads get argued in rather than agreed with?

**Sales calls and support tickets**
- What objection appears before you've said anything about price?
- Which ticket describes a use case nobody designed for?
- What do people ask about *last*, casually, at the end of a call?

**Competitor analysis** — the four patterns
- *"I bought X because…"* → trigger + winning criterion
- *"I switched from X to Y because…"* → **a completed four-forces case**
- *"I like X, but…"* → unmet need inside a satisfied customer
- *"I would use X if…"* → the exact barrier blocking a willing buyer

**Opportunity cost — nobody volunteers this**
- What have you **not** been able to do because of this?
- What would you take on if this weren't in the way?

### 2 · Validation — is it real and commercial

- How many times did this happen in the last twelve months?
- What did the last occurrence cost you? *(push for a number)*
- What have you already spent trying to fix it — money **or** hours?
- What did you build or improvise yourself?
- What happens if you do nothing about this for six months?
- Who else has to agree before something like this gets bought?
- What did you buy most recently in this area, and what did it cost?
- **The revealed-behaviour probe:** *"If this were as bad as it sounds, I'd expect you to have [X]. Did you?"*

### 3 · Prioritisation — which pain leads

- Of everything we've discussed, which one would you fix first?
- If you could only fix one this quarter, which?
- Which of these have you already tried to solve, and which have you just lived with?
- Which one does your boss / partner / client actually ask about?
- Which one would you notice being gone within a week?

> The gap between *"which is worst"* and *"which have you tried to fix"* is where tolerated chronic pain hides.

### 4 · Messaging — turning pain into copy

- What words would **you** use to describe this to a colleague?
- What would have to be true for you to believe someone could fix this?
- What would make you suspicious of a promise to fix it?
- Who would you check with before buying something like this?
- What proof would you need — and **what proof have you actually accepted before?**
- How would you explain this purchase to whoever signs off?
- What would make this an easy yes at three times the price?

### 5 · Ethical check — before anything ships

Asked of the **message**, not the customer:

- Does this name a pain they already had, or one we manufactured?
- Is the relief mechanism named **in the same breath** as the threat — or three scrolls away?
- Have we supplied **both** halves of efficacy — "it works" *and* "you can do this"?
- Does the reader still have full information, emotional space and a clear exit?
- Is any urgency here **real**, with a real date and a real consequence?
- Would I say this to their face, knowing they'd read the fine print afterwards?
- If they act on this and it doesn't work out, will they feel **informed or fooled**?
- Have we said who this is **not** for?

### Weak questions — and why they fail

| Weak | Why it produces fiction | Ask instead |
|---|---|---|
| *"What are your biggest pain points?"* | Invites them to perform a business persona | *"Walk me through the last time it went wrong."* |
| *"Would you pay for a solution to X?"* | Prediction. People are generous with hypothetical money | *"What have you already paid for this?"* |
| *"Do you struggle with X?"* | Leading. You supplied the frame | *"How do you handle X today?"* |
| *"How important is X, 1–10?"* | Everything scores 7–8 and nothing discriminates | *"Which would you fix first?"* |
| *"What features would you like?"* | Gets you a roadmap from the loudest customer | *"What breaks without it?"* — then ladder |
| *"Is this a problem for you?"* | Yes/no, and politeness answers yes | *"When did this last happen?"* |

---

## §7 — Scoring moved, and split in two

**The single PPS that lived here has been superseded.** `[S]`

It scored ten criteria into one number and thereby mixed two incompatible questions — *how much does this hurt* and *can a business be built on it*. A severe-but-unmonetisable pain and a mild-but-lucrative one landed on the same total, with the structure that mattered averaged away. **That is the averaging error the rest of this skill exists to prevent, committed by the skill's own instrument.**

**Replaced by two independent scores** in `pain-opportunity.md` §4:

| Score | Question | Weighted on |
|---|---|---|
| **Pain Strength (PSS)** | How much does this hurt? | Severity · urgency · frequency · **cost of inaction** · persistence · emotional intensity · evidence quality |
| **Commercial Opportunity (COS)** | Can a business be built on it? | WTP · ability to pay · economic value · prevalence · existing spend · dissatisfaction with alternatives · reachability · product fit · evidence quality |

Read together as a **2×2**, which is the point: the *high pain / low commercial* quadrant — real suffering, no budget — is the trap that most resembles a discovery, and a blended score hides it completely.

**Any existing deliverable carrying a PPS total should be recomputed, not translated.**

---

## §8 — Closing pain ethically

**The half of this module that was entirely missing, and the important one.**

### The mechanism that makes the ethical line and the effectiveness line the same line

Kim Witte's **Extended Parallel Process Model** is the best-evidenced answer available. `[E]`

A person receiving a threat message runs two appraisals:

```
THREAT     = severity ("how bad is it?") × susceptibility ("could it happen to me?")
EFFICACY   = response efficacy ("does the fix work?") × self-efficacy ("can I do it?")
```

| | Result |
|---|---|
| **High threat + high efficacy** | **Danger control** → the person acts on the problem. Message accepted |
| **High threat + LOW efficacy** | **Fear control** → the person acts on the *fear*: defensive avoidance, denial, reactance. **Message rejected** |
| Low threat | Nothing happens either way |

> *"Most fear campaigns fail not because fear is the wrong lever but because they crank threat without lifting efficacy."* `[E]`

**Read what this means.** Amplifying pain without simultaneously raising the buyer's belief that something can be done about it does not merely cross an ethical line — **it demonstrably does not work.** The audience defends itself against the message instead of against the problem.

### The operating rule

> **Never raise threat without raising efficacy in the same breath.**

Practically: every sentence that names a pain must be within sight of a sentence that names a credible, achievable relief. Not a promise — a **mechanism**, and one this specific person can plausibly execute.

**This single rule prevents most fearmongering**, because fearmongering is structurally *threat without efficacy*.

### The three conditions test

A message is persuasion rather than manipulation when the buyer retains: `[E]`

| Condition | Violated by |
|---|---|
| **Full information** | Hiding the real price, the real effort, who it isn't for |
| **Emotional space** | Manufactured countdowns, "only 3 left", pressure framing |
| **A clear exit** | Hidden cancellation, dark-pattern opt-outs, guilt on refusal |

> Persuasion *"helps a customer see real value more clearly"*; manipulation *"pushes a customer toward a decision they might not choose if they had full information, emotional space, and a clear exit."* `[E]`

Cross-check with the **TARES** criteria — truthfulness, authenticity, respect, equity, social responsibility. `[E]`

### Six closing moves that are legitimate

| Move | What it does | Example shape |
|---|---|---|
| **Name it in their words** | Recognition, not persuasion | Their verbatim, unedited |
| **Quantify it** | Converts vague dread into a solvable number | *"About 6 hours a week — roughly ₽X a year"* |
| **Show the mechanism** | Raises response efficacy | *"It works by doing Y, which is why Z stops happening"* |
| **Lower the effort** | Raises self-efficacy — **the most neglected half** | *"Setup takes 20 minutes and we do the import"* |
| **Give proof at their level** | Makes efficacy believable | A case from their vertical, at their scale |
| **State who it isn't for** | Restores autonomy; also prevents bad-fit churn | *"If you're under X, this won't pay for itself"* |

**The fourth is the one most often skipped.** Teams raise response efficacy (*"our product works"*) and neglect self-efficacy (*"and you specifically can do this"*). EPPM treats them as equally load-bearing.

### Six moves that are not

| Move | Why it fails |
|---|---|
| **Amplifying a pain the buyer hadn't felt** | Manufacturing threat. Also triggers reactance |
| **Fake urgency** — invented deadlines, false scarcity | Removes emotional space. And it is a lie |
| **Shame** — "still doing it the old way?" | Threat aimed at identity, with no efficacy offered |
| **Catastrophising** — worst case as default case | Inflates severity beyond the evidence |
| **Vagueness about the fix** | Threat without mechanism = fear control by construction |
| **Hiding the exit** | Fails the autonomy test regardless of anything else |

### When the client asks for the prohibited thing

**The module previously said what not to ship and never what to deliver instead.** That leaves a run with two options that each break a rule: `[S]`

| Option | Breaks |
|---|---|
| Refuse | *"The requested scope is the deliverable"* — the skill's own behavioural rule |
| Comply | Everything above |

**There is a third answer, and it delivers more than was asked.**

> **Deliver the legitimate version: the same pain, the same intensity, with efficacy attached — and lead with the mechanism rather than the morality.**

### The five-step response

**1 · Answer on effectiveness first.** Not *"this is manipulative"* — *"this converts the already-convinced and repels everyone else, and here is the mechanism."* Morality first invites an argument about values; mechanism first invites a rewrite. **A run that leads with ethics has failed even when its conclusion is right.**

**2 · Diagnose what is actually missing.** Usually the same thing: threats present, efficacy absent. Count them.

```
"In five years you'll have no pension"      → threat
"Your children will be ashamed of you"      → threat + identity + shame
"It's late, but not too late"               → threat + false reassurance
────────────────────────────────────────────────────────────────
threats: 3     efficacy: 0     predicted outcome: fear control
```

**3 · Rewrite each line, keeping the pain.** This is the deliverable. The pain does not get softened — **the relief gets attached to it.**

| Original | Rewritten | What changed |
|---|---|---|
| *"In five years you'll have no pension"* | *"Here is what your pension looks like on current contributions — and what changes if you add 3% from next month"* | Same threat, made **specific and personal**, with response efficacy in the same sentence |
| *"Your children will be ashamed of you"* | *"Most people avoid this because nobody taught them. Two evenings is enough to stop avoiding it"* | Shame removed; **self-efficacy** added — the half teams routinely skip |
| *"It's late, but not too late"* | *"Starting at 45 changes the number by roughly X. Starting at 50 changes it by Y"* | Vague dread → an arithmetic the reader can act on |

**4 · Name the specific prohibited moves and what each costs.** Shame framing is threat aimed at identity with no efficacy offered. False scarcity removes emotional space. Vagueness about the fix *is* fear control by construction.

**5 · Challenge the effectiveness premise.** *"Такое хорошо конвертит"* is an unevidenced claim arriving as fact — level it (`../OPERATING-MANUAL.md` §3). **Converts against what, measured how, over what horizon, with what refund rate?** Fear-led acquisition characteristically shows strong front-end numbers and poor retention, and a campaign judged on click-through will look excellent while doing this.

### Why this satisfies both rules

The client asked for stronger pain-based advertising. **They receive stronger pain-based advertising** — rewritten copy, line by line, with the pain intact and the mechanism that makes it work explained.

> **The pain is never the problem. The missing efficacy is.** Which is why the honest answer and the useful answer are the same answer, and why refusing would have been the lazier of the two failures.

---

### The self-check, three questions

Run before any pain-based message ships: `[S]`

> **1. Would I say this sentence to this person's face, knowing they'd read the fine print afterwards?**
> **2. If they act on this and it doesn't work out, will they feel informed or fooled?**
> **3. Is the efficacy claim in the same breath as the threat — or three scrolls away?**

Question 3 catches the most failures, because it fails on **layout**, not intent. A landing page can be entirely truthful and still be fear control if the relief lives below the fold.

---

## §9 — Pain-to-offer mapping

The handoff artefact. Full template: `../templates/pain-matrix-template.md`.

**Fourteen fields per pain.** The chain has to be complete — a gap anywhere breaks the message downstream.

| # | Field | Sourced from |
|---|---|---|
| 1 | Segment | Segment object |
| 2 | Pain, verbatim | VOC swipe file |
| 3 | Evidence + level | Evidence ladder |
| 4 | Root pain (post-laddering) | §3 |
| 5 | 3-tuple classification | §1 |
| 6 | Desired outcome, in their metric | Customer profile |
| 7 | Current workaround | Interviews, comments |
| 8 | Failed alternatives | Competitor quote patterns |
| 9 | Objections | Four forces: Anxiety + Habit |
| 10 | Our mechanism | The offer |
| 11 | Proof available | — or `[PROOF NEEDED]` |
| 12 | Message angle | §8 legitimate moves |
| 13 | Content angle | Repeat questions |
| 14 | Ethical risk + mitigation | §8 |

**The rule:** if field 10 or 11 is empty, **do not use the pain in acquisition messaging.** Naming a pain you cannot relieve, or cannot prove you relieve, is threat without efficacy — the exact configuration EPPM predicts will be rejected.

---

## §10 — Anti-patterns

| Anti-pattern | Correction |
|---|---|
| **Complaint taken as finding** | Ladder it. The complaint explains a ticket; the root explains a purchase |
| **Pain list with no numbers** | Every adjective has a number behind it. Ask for it |
| **Pains averaged across a segment** | Ten people, three roots = three segments |
| **Pain inventory with no ranking** | An unranked list is `L1` however long it is |
| **Desire filed as pain** | Is there a current negative state, or only an absent positive? |
| **Objection filed as pain** | Did it exist before you showed up? |
| **Ranking pains with the TAS** | Wrong instrument. TAS ranks segments; PPS ranks pains |
| **Threat without efficacy** | Fear control. Predicted to be rejected, not just unethical |
| **Efficacy three scrolls from the threat** | Same failure, caused by layout |
| **Pain amplified beyond its evidence** | The evidence level caps the intensity of the claim |
| **Every pain rated "extreme"** | Nothing has been ranked |
| **Identity pain read as a joke** | *"I know, I should have a system"* is not self-deprecation |

---

## §11 — Quality gate

- [ ] Every pain carries a **verbatim quote**, not a paraphrase
- [ ] Every pain **quantified** — no adjectives standing in for numbers
- [ ] Every pain **laddered** to root, stopping one rung above a life theme
- [ ] Every pain classified on **all three axes**
- [ ] Screened against **§4** — not a desire, objection, demographic, generic problem, feature request or your own hypothesis
- [ ] **Six validation tests** run; test 6 (revealed behaviour) explicitly checked
- [ ] **PPS scored** with gates checked separately from totals
- [ ] Reported as **four columns**: score · gates · evidence level · source
- [ ] Contradiction scan run — divergent roots **split**, never averaged
- [ ] Every pain intended for messaging has **fields 10 and 11** filled
- [ ] **EPPM check:** no threat raised without efficacy in the same breath
- [ ] **Autonomy check:** full information · emotional space · clear exit
- [ ] The three self-check questions answered in writing
- [ ] At least one pain **declined** as non-commercial, with the reason

### The final test

> **Read the pain back to someone in the segment. If they say "yes, exactly" — you have their words. If they say "yes, I suppose so" — you have your own.**
