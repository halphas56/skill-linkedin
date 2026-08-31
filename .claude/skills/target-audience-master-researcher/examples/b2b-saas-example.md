# Worked Example — B2B SaaS

> **⚠ This is a constructed demonstration, not a case study.** The company does not exist. The reasoning, the structure and the method are what you should copy; the specific findings are illustrative. Numbers marked `[A]` are assumptions inserted to show how the analysis behaves, not research results.

---

## The brief as received

> "We built **Threadline** — it turns customer support conversations into structured product feedback. Support tickets in, themed insight reports out. $299–999/month. We have 14 customers, mostly SaaS companies, mostly through founder network. Our audience is product managers at B2B SaaS companies. We need to know who to actually go after, because founder network is exhausted."

**Intake gaps:** no CRM analysis provided, no interviews done, competitors named only vaguely, budget stated as "under $2k/month," founder hours "maybe 8 a week."

---

## 1. Offer summary

- **What is sold:** structured product-feedback reports generated from existing support conversations
- **Job:** *When my support volume outgrows my ability to read it personally, I want to know what customers are actually struggling with, so I can defend roadmap decisions with evidence instead of anecdote.*
- **Genuinely better at:** working from *existing* support text with no tagging discipline required — competitors need clean taxonomies that nobody maintains
- **Model / price:** B2B SaaS, $299–999/mo · **Preset:** B2B SaaS
- **Geography:** English-speaking, remote-first
- **Regime:** **Focus** — challenger, no distribution, needs a beachhead

**Note on the stated audience.** "Product managers at B2B SaaS companies" is a role plus a vertical with no circumstance and no habitat. It fails Tier 5 of the ideal-audience checklist on both counts. It is the starting point, not the answer.

---

## 2. Key assumptions

| # | Assumption | Why | If wrong | How to check | Cost |
|---|---|---|---|---|---|
| 1 | The 14 existing customers contain a pattern nobody has named | Standard in every business at this stage | The engine has no empirical anchor; everything drops to inference | ABCDX on all 14 | 2 hours |
| 2 | Support-volume growth is the trigger, not roadmap planning | Inferred from the job statement | Trigger monitoring targets the wrong event entirely | 5 switch interviews | 1 week |
| 3 | Buyer and user are the same person `[A]` | Assumed from price point | Buying group is larger; the sales motion must change | Ask in the same 5 interviews | included |
| 4 | Founder can produce written content weekly | Stated 8 hours/week | Free acquisition is unavailable; must go paid on $2k | Confirm with founder | 5 minutes |

**Confidence: medium-low.** The load-bearing assumption is #1. Checking costs two hours and would change the ranking below. **It should be checked before anything else in this document is acted on.**

---

## 3. Audience universe map

| Role | Who | Wants | Fears | Blocks? | Pays? |
|---|---|---|---|---|---|
| User | PM, support lead, UX researcher | Evidence for roadmap arguments | Being contradicted by sales' anecdotes | no | no |
| Buyer | Head of Product / VP Product | Fewer roadmap fights | Another tool nobody adopts | no | yes |
| Economic DM | CPO or CEO at this size | Faster, defensible decisions | Tool sprawl | yes | yes |
| Influencer | Head of Support | Their tickets finally mattering | Being blamed for ticket quality | no | no |
| **Blocker** | IT / security | No new data processor | **A support-data processor triggers review** | **yes** | no |
| Champion | Whoever loses roadmap arguments | Ammunition | Looking like they need a crutch | no | no |

**Finding.** The blocker is structural and was not in the brief. A product that ingests customer support text will meet a data-processing review in most companies above ~100 staff. **This is not a marketing problem — it is a segment boundary**, and it appears in the scoring below.

---

## 4. Generated segments (14 after deduplication)

| # | Gen | Segment | Pain | Pay | Urgency | Where | Free? | Main risk |
|---|---|---|---|---|---|---|---|---|
| 1 | B3 | Heads of Product, 50–200 staff | Med | High | Low | LinkedIn, PM communities | Med | No trigger; crowded |
| 2 | B2 | Teams who just hired their **first** PM | High | Med | **High** | Job boards | **High** | Small window |
| 3 | B2 | Teams whose support volume doubled after a funding round | High | High | **High** | Funding news | High | Hard to detect precisely |
| 4 | B10 | *The pattern in the existing 14* | ? | ? | ? | ? | ? | **Unresearched — assumption #1** |
| 5 | B4 | Developer-tool companies | Med | Med | Low | Dev communities | High | Build-it-ourselves culture |
| 6 | B7 | Teams already using a tagging tool and failing at it | **High** | High | Med | G2 reviews of competitors | Med | Incumbent inertia |
| 7 | C3 | **Support leads** who cannot get product to listen | **High** | **Low** | High | Support communities | **High** | User ≠ buyer |
| 8 | C9 | Heads of Support who own budget in support-led orgs | High | **High** | Med | Support leadership groups | Med | Different message entirely |
| 9 | C1 | Teams maintaining a manual "ticket themes" spreadsheet | **High** | High | Med | Notion/Sheets templates, PM forums | High | Hard to find at scale |
| 10 | C10 | Companies with a **churn spike** and no explanation | **High** | **High** | **High** | Hard to detect externally | Low | Detection problem |
| 11 | C6 | Refusers: evaluated the category, found it too much setup | High | High | Low | Competitor review threads | Med | Why they refused may be unfixable |
| 12 | C12 | People repeatedly asking "how do you turn support tickets into roadmap input?" | Med | Med | Low | PM Slack groups, Reddit | **High** | Question ≠ budget |
| 13 | B8 | Non-English support teams whose tools only parse English `[A]` | High | Med | Med | Regional communities | Med | Product may not support it |
| 14 | **D1** | **ANTI: seed-stage startups under 15 staff** | Low | **None** | Low | Everywhere | — | 3 of 14 customers; heaviest support load; lowest price |

**Generator coverage:** B2, B3, B4, B7, B8, B10 (obvious) · C1, C3, C6, C9, C10, C12 (unexpected) · D1 (anti). **Requirement met:** 6 unexpected candidates, 1 anti-audience.

---

## 5. Detailed analysis — the two that matter

### Segment 2 — Teams who just hired their first PM

**Obvious / unexpected:** obvious · **Generator:** B2 trigger events · **Evidence:** `[S]` reasoning + `[A]` on conversion

- **Description.** Companies of roughly 40–150 staff that have just posted or filled their first dedicated Product Manager role, where support has been handled informally by founders until now.
- **Pain.** The new PM arrives with no evidence base, inherits a roadmap built on the loudest voices, and must produce a credible plan in their first quarter.
- **Outcome wanted.** Walk into the first roadmap review with data nobody can dismiss.
- **Trigger.** The job posting itself — public, dated, with a company name attached.
- **Alternatives.** Reading tickets manually for a week; asking the support team's opinion; a spreadsheet.
- **Ability to pay.** Strong — they just committed to a salary. **The salary is the budget signal.**
- **Willingness.** Medium. A new hire has limited spending authority in their first 90 days. `[A]`
- **Where they live.** Job boards (the trigger) · PM communities · new-PM onboarding content.
- **Free channels.** Content aimed at "your first 90 days as the first PM" — a question with a large, dated, recurring audience. Direct outreach on the vacancy.
- **Paid channels.** LinkedIn targeting by title + tenure < 6 months + company size.
- **Trust requirement.** Low. A demo on their own data would close most of it. Blocker risk is low at this size.
- **Objections.** *Anxiety:* "will this look like I can't do the job myself?" *Habit:* "I'll just read the tickets."
- **Positioning hook.** *"Your first roadmap review, with evidence instead of opinions."*
- **Risks.** The window is short (weeks). New hires have limited authority. Company size caps ACV.

### Segment 8 — Heads of Support with budget

**Obvious / unexpected:** **unexpected** · **Generator:** C9 hidden B2B buyers · **Evidence:** `[S]`

- **Description.** Support leaders in organisations where support owns a real budget line, who are measured on deflection and CSAT and need product changes to move either.
- **Pain.** They see the same issues every day, report them, and nothing happens — because their reports read as anecdote to the product team.
- **Outcome wanted.** Turn "support keeps complaining" into "support brought us the data."
- **Trigger.** Quarterly review where support metrics did not move; or a new Head of Support arriving.
- **Alternatives.** Manual tagging in the helpdesk; a spreadsheet; escalation meetings.
- **Ability to pay.** **High** — support tooling budgets are established and unglamorous, therefore uncontested.
- **Willingness.** High, at a lower price point than product budgets.
- **Where they live.** Support leadership communities, helpdesk vendor ecosystems, support conferences — **entirely different venues from PM communities.**
- **Free channels.** Support-leader communities; helpdesk marketplace listings; content about "getting product to act on support data."
- **Paid channels.** Support-role targeting on LinkedIn — cheaper than PM targeting, because fewer vendors compete for it.
- **Trust requirement.** Medium. Integration with their helpdesk matters more than any case study.
- **Objections.** *Anxiety:* "will this be used to blame my team?" — **a serious and specific fear that must be answered directly.** *Habit:* existing tagging scheme.
- **Positioning hook.** *"Support already knows what's broken. This is how product finally listens."*
- **Why unexpected.** The entire category markets to product. Support is an equally affected, separately budgeted buyer that nobody addresses.
- **Risks.** Different message, different venues, possibly a different price tier — this is a second go-to-market, not a variation.

---

## 6. Scoring (abbreviated — preset: B2B SaaS)

| # | Criterion | W | S2 first PM | S8 support leads | S6 failed tagging | S1 stated audience |
|---|---|---|---|---|---|---|
| 1 | Pain | 8 | 4 | 5 | 5 | 3 ⚠ |
| 2 | Urgency | 5 | 5 | 3 | 3 | **1** ⚠ |
| 3 | Ability to pay | 12 | 4 | 5 | 4 | 4 |
| 4 | Willingness | 6 | 3 ⚠ | 4 | 4 | 3 ⚠ |
| 5 | Reachability | 11 | 5 | 4 | 4 | 3 |
| 6 | Concentration | 4 | 3 | 4 | 3 | 3 |
| 7 | Trust access | 5 | 4 | 3 | 3 | 3 |
| 8 | Existing demand | 5 | 3 | 3 | **5** | 3 |
| 9 | Competition (inv) | 4 | 3 | **5** | 2 | 2 |
| 10 | Differentiation | 3 | 3 | 4 | **5** | 2 |
| 11 | Free acquisition | 3 | 5 | 4 | 3 | 2 |
| 12 | Paid acquisition | 5 | 4 | 4 | 3 | 3 |
| 13 | Content | 2 | 5 | 4 | 4 | 3 |
| 14 | Sales cycle (inv) | 7 | 4 | 3 | 3 | 3 |
| 15 | Retention | 10 | 3 | 4 | **5** | 3 |
| 16 | Referral | 2 | 3 | 4 | 3 | 3 |
| 17 | Strategic fit | 2 | 3 | 2 | 4 | 4 |
| 18 | Positioning | 3 | 4 | 5 | 5 | 2 |
| 19 | Risk (inv) | 3 | 4 | 3 | 3 | 3 |
| | **Weighted total** | | **3.85** | **3.98** | **3.87** | **2.91** |
| | **Gates** | | PASS | PASS | PASS | **FAIL — urgency = 1** |
| | **Assumption cells** | | 1 | 0 | 0 | 2 |

### Reading it

- **The stated audience fails a gate.** "Product managers at B2B SaaS companies" scores 2.91 *and* fails on urgency. It is not a weak segment; it is not a segment. That is the headline finding of this engagement.
- **S2, S6 and S8 are within 0.13 of each other.** By the tie rule, analysis cannot separate them. **Break the tie with an experiment, not with more argument.**
- **Segment 4 is absent from this table**, because it was never researched. If assumption #1 holds, it may outrank everything here — which is why the ABCDX pass is the first recommended action, ahead of any campaign.

---

## 7. Top recommendations

**1. Segment 8 — Heads of Support with budget (3.98)**
Attractive because the category ignores it entirely: lowest competition (5), strongest positioning (5), and an established, unglamorous budget line. Loyal because the tool becomes the mechanism by which their team's work is finally taken seriously. Reachable through support-leader communities nobody else is working. **Must validate first:** that support genuinely owns budget in enough organisations — and how loudly the "will this be used to blame my team?" fear speaks.

**2. Segment 2 — First-PM hires (3.85)**
Attractive because the trigger is public, dated and self-replenishing from job boards, and free acquisition is unusually strong (the "first 90 days as first PM" content question is asked constantly). **Must validate first:** whether a new hire can actually authorise $299/mo in their first quarter.

**3. Segment 6 — Teams failing at tagging (3.87)**
The best retention (5) and differentiation (5) of the three — they have already tried and failed, so they understand the value and their alternative has visibly failed. Slower to reach; the evidence sits in competitor review threads.

**Rejected runner-up worth stating:** **Segment 10 — churn spike, no explanation.** Highest pain, highest urgency, highest ability to pay of anything generated. It ranks nowhere because it **cannot be detected from outside.** If a detection method ever appears — a partner integration, a churn-analytics alliance — this becomes the best segment on the list. Keep it named.

**Anti-audience: seed-stage startups under 15 staff.** 3 of 14 current customers, lowest price, heaviest support load `[A]`. Decline politely and route to a self-serve tier or a competitor.

---

## 8. Where to find them

| Habitat | Segment | Size | Match | Rules | Route in | Free? |
|---|---|---|---|---|---|---|
| Support-leadership Slack communities | S8 | ~thousands | **High** | No selling; contribution welcome | Apply, contribute 2 weeks | **Yes** |
| Helpdesk vendor marketplaces | S8 | — | High | Listing usually free | Build integration, list it | **Yes** |
| Support conferences (speaker + sponsor lists) | S8 | — | High | — | Read the lists for free; speak if possible | Research free |
| Job boards, "first Product Manager" postings | S2 | Continuous | **High** | Public | Monitor duty keywords | **Yes** |
| PM communities and newsletters | S2, S6 | Large | Medium | Varies | Contribute | Yes |
| G2/Capterra review threads on tagging tools | S6 | — | **High** | Public | Read; write comparison content | **Yes** |
| LinkedIn (support-leader titles) | S8 | Large | High | — | Organic + targeted | Partly |

**Friday test.** *To reach 100 of them by Friday:* monitor job boards for "first PM" postings (≈continuous supply, S2) and post one genuinely useful answer in each of the three support-leadership communities (S8). Both are free and both start today.

---

## 9. Free acquisition

**Verdict: realistic for S2, conditionally realistic for S8.**

| Channel | Segment | Required asset | Time-to-signal | Fails if |
|---|---|---|---|---|
| Trigger outreach on job postings | S2 | A list + a reason to write | **1–3 weeks** | Framed as "don't hire, buy us" |
| Content: "first 90 days as the first PM" | S2 | Founder writing 1×/week | 2–4 months | Cadence not sustained past month 3 |
| Support-community contribution | S8 | Credible expertise + patience | 4–8 weeks | Delegated to someone with no standing |
| Helpdesk marketplace listing | S8 | An integration | 6–12 weeks | Integration not built |
| Comparison content vs. tagging tools | S6 | Honest competitive knowledge | 3–6 months | Written as a hit piece |

**Constraint that governs all of it:** 8 founder hours/week supports **two** of these, not five. Recommend trigger outreach (fastest signal) plus one content stream. Half the cadence sustained beats the full cadence abandoned in month three.

---

## 10. Paid acquisition

- **Channel:** LinkedIn — the only platform whose targeting can express these segments.
- **Targeting:** S8 — support leadership titles, company size 50–500. S2 — PM titles, tenure under 6 months, company size 40–150.
- **Proxy warning:** LinkedIn cannot target "support leaders who own budget." You are targeting title + company size and accepting leakage. Expect a meaningful share of the audience to be non-budget-holders. `[A]`
- **ARPU ↔ CAC:** at $299–999/mo with SaaS retention, a CAC in the low hundreds is fundable. LinkedIn is expensive per click but the audience is precise; the arithmetic is tight but not impossible.
- **Angles to test:** (a) *"Support already knows what's broken"* → S8 · (b) *"Your first roadmap review, with evidence"* → S2 · (c) *"You bought a tagging tool. Nobody tags."* → S6
- **Budget floor for a decision-grade test:** three angles × two segments, run to leave the learning phase. Under $2k/month this means **testing sequentially, not in parallel** — state that constraint rather than pretending otherwise.
- **What would falsify:** cost per booked call above the point where SaaS payback exceeds 18 months.

---

## 11. Positioning — Segment 8

- **Competitive alternatives:** manual helpdesk tagging · a spreadsheet of ticket themes · escalation meetings · doing nothing and complaining
- **Unique attribute:** works on existing unstructured support text, no tagging discipline required
- **Differentiated value:** support gets evidence product cannot dismiss, without the team doing extra work
- **Best-fit customer:** support leaders judged on metrics they cannot move without product changes
- **Category:** support-intelligence tooling, adjacent to the helpdesk (existing category, buyer understands it)

**Statement:** *For heads of support who already know what's broken but can't get product to act, Threadline turns the support inbox into evidence — without asking the team to tag a single ticket. Unlike tagging tools, it needs no discipline to maintain, because it reads what's already there.*

**Swap test:** substitute the leading tagging tool's name → *"needs no discipline to maintain"* becomes false. **Passes.**

**Proof needed:** `[PROOF NEEDED: one support-led customer willing to be named — none of the current 14 qualifies]`

**The objection to answer first, publicly and in the product:** *"will this be used to blame my team?"* An unanswered version of this fear kills the deal silently, and it will not be raised on a call.

---

## 12. Validation plan

| # | Hypothesis | Method | Channel | Success metric | Minimum evidence | Cost | Speed | Risk |
|---|---|---|---|---|---|---|---|---|
| 1 | The existing 14 contain an unnamed pattern | ABCDX on all 14 | Internal | A shared attribute in the top 5 | Clear split | Free | **2 h** | None |
| 2 | Support leaders own budget | 10 manual outreach messages | LinkedIn / communities | 3+ replies, 2+ calls | 2 confirming budget | Free | 1 wk | Low |
| 3 | S2's trigger is real | 20 outreach on live job postings | Email | 3+ conversations | 2 confirming the pain | Free | 1 wk | Low |
| 4 | Blame-fear is decisive for S8 | Ask in every S8 call | Calls | Raised unprompted | 3 of 5 raise it | Free | 2 wk | None |
| 5 | S8 message beats S2 message | Two landing pages, identical structure | LinkedIn ads | Cost per booked call | 2× difference | $600 | 3 wk | Med |
| 6 | Failed-tagging teams will switch | Comparison page + outreach to reviewers | Content | Demo requests | 5 requests | Free | 6 wk | Low |
| 7 | New PMs can authorise $299 | Ask directly in test 3 calls | Calls | Explicit yes/no | 3 answers | Free | included | None |

**Run order:** 1 → 2, 3, 4 in parallel → 5. Test 1 costs two hours and may reorder everything below it. **Do not run any paid test before test 1.**

**Declared falsifier:** if S8 outreach produces zero budget-holding replies from 10 well-researched messages, S8 drops below S2 and the plan changes.

---

## 13. Final recommendation

1. **Best audience to start with:** **Heads of Support with budget** — uncontested, funded, and the strongest positioning available to this product.
2. **Backup:** **First-PM hires** — promote if support-budget ownership proves rare, or if the blame-fear proves decisive.
3. **Audience to avoid:** seed-stage startups under 15 staff. Stated in resource terms.
4. **First experiment:** ABCDX on the existing 14 customers. Two hours. Before anything else.
5. **First message angle:** *"Support already knows what's broken."*
6. **First channel:** manual outreach into three support-leadership communities.

**Trade-off accepted:** going after support means the product team is *not* the primary buyer, which will feel wrong to a founding team that built a product-feedback tool. The positioning, the pricing tier and the integration roadmap all shift with it. That is the cost of the recommendation, and it should be decided deliberately.

**What would make this wrong:** if the existing 14 customers turn out to share an attribute pointing somewhere else entirely. **Which is exactly why test 1 comes first.**

| Horizon | Action | Success signal |
|---|---|---|
| Week 1 | ABCDX on 14 customers; join 3 support communities; 10 outreach messages | Pattern found; 3 replies |
| Month 1 | 5 support-leader calls; blame-fear tested; comparison page live | 2 confirm budget ownership |
| Quarter 1 | One named support-led customer; helpdesk integration listed | 3 inbound from communities |

---

## Self-critique

- **Weakest part:** segment 4 is a hole in the middle of the analysis. Everything here is provisional until the ABCDX pass runs.
- **Could not verify:** whether support leaders control budget at these company sizes. It is the assumption the top recommendation rests on.
- **Reasoned by analogy:** the LinkedIn CPM and leakage estimates. Marked `[A]`, and they should not survive contact with a real test.
- **A sceptic would attack:** the 0.11 gap between the top three, presented as a ranking. It is not a ranking — it is a tie, and the document says so.
- **Next, given one more day:** the ABCDX pass, then five switch interviews with the three customers who bought fastest.

---

## ⚠ Delta to the current method

**This example was written in research pass 1 and predates passes 3–6.** The reasoning is sound; the instrument set is partial. The reference implementation is [`00-reference-engagement.md`](00-reference-engagement.md).

What the current method would add **to this specific case**:

| Instrument | What it changes for Threadline |
|---|---|
| **Abstraction test** | List what a support lead would hire *instead*: a PM reading tickets on Friday · a shared spreadsheet · a monthly review meeting · an intern · **nothing**. If every alternative had been another feedback tool, the altitude was wrong. Here it passes — and it reveals that the real incumbent is *the monthly meeting*, which no feature comparison would surface |
| **Big Hire vs Little Hire** | Decisive for SaaS. Signups prove persuasion; **a report actually opened each week proves the job.** Any adoption claim here should be re-read as `L6-big` and downgraded until usage data exists |
| **Buying roles** | Support lead (user) ≠ product manager (chooser) ≠ VP Product (signs). Per VPD, the **recommender may sit outside the company** — an advisor or fractional consultant. Only the decision maker is reliably internal |
| **Four forces** | Likely binding constraint: **Anxiety** — *"another dashboard nobody looks at"*. If so, the budget belongs in proof and pilot design, not in more capability messaging |
| **Gain levels** | "Integrates with Zendesk" is a **required** gain — table stakes. It must be delivered and must never be claimed as differentiation |
| **Evidence levels** | No claim in this example carries `L0`–`L6`. Re-read every finding as unlevelled and assume `L2` unless a source is shown |
