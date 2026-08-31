# CA — Target Audience Master Skill

A Claude / Claude Code skill for finding the target audience that will actually **pay, stay and spread** — including the non-obvious segments nobody else is marketing to — plus the research corpus it was built from.

Built 2026-08-25. Follows the conventions of the sibling skills in `D:\Cloude Skills\` (`offer`, `position`, `leadgen`, `partner-channel`, `funnel-agent`): a named skill folder containing `SKILL.md`, an operating manual, research, knowledge, templates, checklists and worked examples.

---

## What this skill does

Given any offer — SaaS, course, agency, local business, consumer product, consulting, marketplace, app, info product, subscription — it:

1. Restates the offer as a **job in a circumstance** — the full six-link chain, four forces, and the binding constraint
2. Maps the **situations** that bring people into the category (7Ws), which surfaces segments people-first analysis cannot see
3. Maps everyone who touches the problem — users, buyers, decision-makers, influencers, **blockers**
4. Generates **10–20 candidate segments**, of which **at least 3 must be non-obvious**
5. Harvests the audience's **actual words** — seven language types, verbatim, never paraphrased
6. Turns **complaints into pains** — laddered *up* for meaning and chained *down* for cost, classified on four axes, validated on six tests
7. Scores each pain **twice** — how much it hurts, and whether a business can be built on it — because a blend hides real suffering with no budget
8. Tests the money separately: **Pain ≠ Demand ≠ Willingness to pay**, with the economic value of the problem quantified
9. **Levels every claim L0–L6** and refuses to call anything validated without **3+ independent source types**
10. Scores with the **TAS formula**, reported alongside gates, evidence level and assumption count
11. Applies **six gates** that disqualify a segment regardless of its total score
12. Maps **exactly where each segment gathers** — named venues, ranked by over-index rather than raw share
13. Builds a **citation-enforced avatar from real comments** — the only free source that contains non-buyers
14. Judges whether they can be reached **for free**, with the required asset and time-to-signal
15. Builds **positioning** around the winner, and stress-tests it with the swap test
16. Names an **Anti-ICP** — who to refuse, and the questions that disqualify them on the first call
17. Closes pain **ethically** — never threat without efficacy in the same breath, because the alternative is predicted to fail as well as being manipulative
18. Designs **5–10 validation experiments**, each with a declared falsifying result
19. Emits a **45-field segment object** for handoff to positioning, offer, partnership and acquisition skills

It is deliberately built to **work on incomplete input**, to **distinguish "interested" from "ready to buy"**, and to say *"this is an excellent audience you currently cannot reach"* when that is the truth.

**The single rule it is built around:** an LLM doing audience research fails in one predictable way — it invents plausible pains, writes them fluently, and the fluency gets mistaken for evidence. The Evidence Ladder makes that failure visible instead of invisible.

**And the law underneath all of it**, which only became visible once six research passes were laid side by side: *audience research is the practice of refusing convenient representations.* Every instrument in the skill catches one specific substitution — the category name for what the customer would actually do instead, the average for the people, what they say for what they do, engagement for intent, a number with decimals for a finding. `SYNTHESIS.md` is where that argument is made and where the frameworks are organised by the altitude they operate at rather than by the order they were added.

---

## File map

```
target-audience-master-researcher/          ← installed at .claude/skills/ — Claude Code finds it automatically
├── SKILL.md                                ← entry point + tiered routing. The only file with frontmatter
├── SYNTHESIS.md                            ← READ FIRST: the one law, the altitude stack, the two engines,
│                                               the convergence & conflict maps, the four-hour pass
├── OPERATING-MANUAL.md                     ← the operating prompt: role, workflow, gates, critic, ethics
├── README.md                               ← you are here
├── ANALYSIS.md                             ← packaging audit + the ordered work plan
│
├── research/                               ← the evidence layer (why). Tier 5 — consult, don't read
│   ├── INDEX.md                            ← question → file → section. Start here, not in the files below
│   ├── target-audience-research-report.md  ← 2,200-line report, 10 sections
│   ├── source-map.md                       ← ~75 sources, reliability-scored, EN + RU
│   ├── frameworks.md                       ← 53 framework cards + question→framework routing
│   └── examples.md                         ← documented cases, 15 weak→strong rewrites, failure anatomies
│
├── knowledge/                              ← the execution layer (how)
│   ├── evidence-ladder.md                  ← THE CORE PROTOCOL: L0–L6, independence, triangulation
│   ├── jtbd-engine.md                      ← six-link chain, 3 dimensions, 4 forces, 5 Rings
│   ├── category-entry-points.md            ← audiences through situations; 7W + 3C
│   ├── market-mapping.md                   ← market by need, leverage junctions, micro-segments
│   ├── customer-profile.md                 ← jobs/pains/gains recorded, ranked and quantified
│   ├── pain-discovery.md                   ← is the pain real? 4 axes, 14 types, laddering, EPPM
│   ├── pain-opportunity.md                 ← is it a business? cost of inaction, TWO scores
│   ├── voice-of-customer.md                ← 7 language types, verbatim discipline, swipe file
│   ├── willingness-to-pay.md               ← Pain ≠ Demand ≠ WTP; economic value estimation
│   ├── segment-generation-lenses.md        ← 30 generators + the Different-X matrix
│   ├── interview-and-survey-kits.md        ← 8 verbatim scripts, EN + RU
│   ├── avatar-from-comments.md             ← a sourced avatar from comments (≠ reviews)
│   ├── habitat-research-playbook.md        ← research stack, search recipes, the over-index rule
│   └── ru-market-playbook.md               ← RU/CIS operations (in Russian)
│
├── templates/                              ← the output layer
│   ├── scoring-matrix-template.md          ← the TAS formula + 19 criteria, 12 presets
│   ├── segment-object-template.md          ← the 45-field handoff object + YAML
│   ├── pain-matrix-template.md             ← inventory, two scores + 2x2, the full Pain Card
│   ├── avatar-card-template.md             ← citation-enforced avatar, mandatory limitations
│   ├── positioning-template.md             ← 17 components, Dunford order, swap test
│   ├── research-output-template.md         ← the 14-section delivery contract + 7 shapes
│   └── audience-brief-template.md          ← client intake form
│
├── checklists/
│   ├── ideal-audience-checklist.md         ← 43 checks across 7 tiers, gates first
│   ├── red-flags-checklist.md              ← 38 failure patterns, severity-rated, with repairs
│   └── free-acquisition-checklist.md       ← 6-step decision procedure
│
├── tests/                                  ← 12 of 13 briefs run in 2 rounds; 8 defects fixed
│   ├── test-briefs.md                      ← 13 adversarial briefs, each with a documented trap
│   ├── evaluation-rubric.md                ← 6 gates, 11 dimensions, 10 deductions
│   ├── COLD-RUN.md                         ← 10-min kit: paste A to produce, paste B to score.
│                                               NOT YET RUN COLD — the top open item
│   └── run-log-*.md                        ← 6 logs: the structural audit, both rounds, the fixes,
│                                               and run-log-2026-08-27-cold.md — the control group, 18/33
│
├── examples/                               ← 6 worked engagements — constructed, never real case studies
│   ├── 00-reference-engagement.md          ← ★ THE STANDARD. Current instrument set, end to end
│   ├── b2b-saas-example.md                 ← (EN) stated audience fails a gate
│   ├── expert-course-example.md            ← (RU) RU output conventions end to end
│   ├── agency-service-example.md           ← (EN) a gate-blocked segment handled correctly
│   ├── local-business-example.md           ← (RU) radius as the first segmentation axis
│   └── unexpected-audience-example.md      ← (EN) the discovery process, step by step
│                                               ↑ these five predate research passes 3–6; each ends with
│                                                 "Delta to the current method". Read the delta.
│
├── tools/
│   ├── md2pdf.py                           ← markdown → structured A4 PDF. The last step of every engagement
│   └── requirements.txt                    ← `markdown` required; `pypdf`+`reportlab` for page numbers
│
└── reports/                                ← an example of a finished deliverable
    └── 2026-08-27-cold-run.md / .pdf       ← the control-group run
```

---

## How to use it

### As a Claude skill

Point Claude at `target-audience-master-skill/SKILL.md`. It triggers on requests like:

**English** — "who is our target audience" · "which segment should we focus on" · "where do we find customers like this" · "build our ICP" · "can we reach them without a budget" · "find a non-obvious audience" · "why isn't our marketing converting" · "compare these two niches"

**Russian** — «определи нашу ЦА» · «портрет клиента» · «сегментация аудитории» · «где искать клиентов» · «как найти платёжеспособную аудиторию» · «неочевидная аудитория» · «кому продавать» · «как привлечь клиентов бесплатно» · «выбор ниши»

### Minimum useful input

You do not need to fill in the brief. Five answers are enough:

1. What exactly do you sell, and at what price?
2. Who has already paid you, and which of them was the best customer?
3. What are you genuinely better at than the alternatives?
4. What happens to a customer that makes them start looking?
5. What do you have — budget, founder hours per week, existing audience, case studies?

Everything else is inferred, and every inference is marked as an assumption.

### Typical run

| You ask | You get |
|---|---|
| "Find our target audience" | Full 14-section report |
| "Which of these two?" | Comparison + scoring + a tiebreaking experiment |
| "Where do we find them?" | Habitat map with named venues, sizes, entry routes |
| "Can we do this for free?" | Verdict + channel + required asset + time-to-signal + failure condition |
| "Is this audience any good?" | One page, answer first |
| "Find a non-obvious audience" | Generator run + disqualification tests + evidence |
| "Собери аватар по комментариям" | Citation-enforced avatar card + contradiction log + interview shortlist |

---

## How it was built

**Phase 1 — research.** ~30 targeted searches in English and Russian across market selection, JTBD, positioning, PMF measurement, channel frameworks, research methods, pricing research and Russian-market practice. Seven sources retrieved and read in full; four retrieval failures logged openly; the rest reviewed at search-extract level.

**Phase 2 — report.** A 2,200-line research report covering: what makes an audience good (23 factors) · types of audiences (20 lenses) · finding unexpected audiences (16 generators) · research methods (26) · the habitat atlas (34 surfaces) · free vs paid acquisition (19 methods) · scoring · positioning · rules · the master framework.

**Phase 3–5 — the skill**, its knowledge layer, templates, checklists and five worked examples.

**Second pass (same day) — comment mining.** A dedicated method for building an avatar from *comments* rather than reviews, on the grounds that they are different instruments: reviews contain buyers only, comments contain buyers, near-buyers, refusers and lurkers. Adds the stimulus map, a tagging schema, the awareness tell, the contradiction scan, and a citation-enforced avatar card. Its three distinctive mechanisms are **synthesis, not sourced evidence**, and are labelled as such in `source-map.md` §6.7.

**Sixth pass — the Customer Profile.** *Value Proposition Design* (Osterwalder, Pigneur, Bernarda & Smith), read from a user-supplied Russian edition. Deliberately scoped: the skill takes the **Customer Profile (circle)**; the Value Map belongs to the offer skill. Contributes the sub-taxonomies the skill lacked — **pains split into outcomes / obstacles / risks** (an obstacle needs *removal*, a risk needs *reassurance*), **gains split into required / expected / desired / unexpected** (required and expected are table stakes — the same object as McDonald's non-discriminating features), and **supporting jobs** including the **value-transferrer role** where switching friction hides. Plus three techniques that make a sparse profile fillable — **quantify every adjective**, the **mirror** (gain, inverse pain, obstacle, risk from each job), and **"why?" laddering**. Plus **six buying roles** with the point that only the decision maker is reliably inside the buying organisation; **multi-sided fit**; and **"test the circle before the square"** — validate the audience before the offer, because a failed offer test cannot distinguish a wrong offer from a wrong audience. See `source-map.md` §11.1.

**Fifth pass — systematic segmentation.** Malcolm McDonald & Ian Dunbar's *Market Segmentation: How to Do It and How to Profit from It*, studied via McDonald's own full-length paper (retrieved as PDF and extracted in full). Upgrades what had been a one-line citation into a proper module. Contributes: **market definition by need** (*"the aggregation of all products or services which customers regard as being capable of satisfying the same need"* — independently identical to Christensen's abstraction test, the strongest cross-source agreement in the corpus); the **market map with quantified leverage junctions**, which answers *where in the chain the decision is actually made* — a gap that mattered for anything sold through distributors, contractors or specifiers; **micro-segments** as a bottom-up engine with the **KDF/CPI distinction** and the **100-point constant-sum allocation**; the **four-question segment checklist** whose fourth question tests the organisation rather than the segmentation; and the **commoditisation diagnostic** — "everyone buys on price" is a hypothesis about the client's research, not a fact about their market. See `source-map.md` §10.1.

**Fourth pass — the JTBD primary source.** *Competing Against Luck* (Christensen, Hall, Dillon & Duncan, 2016) read in full from a user-supplied copy, replacing the secondary summaries the JTBD layer had rested on and **resolving the paywall gap flagged in the previous pass**. It contributed four mechanisms no secondary source in the corpus contained — the **abstraction test** (if every alternative comes from one product category, it is a spec, not a job), **Big Hire vs Little Hire** (a purchase proves persuasion; repeated use proves the job), **negative jobs** (what customers wish they did not have to do at all — flagged by Christensen as often the best opportunities), and the **Three Fallacies of Innovation Data** — plus one direct correction: *cluster before you segment*, since deconstructing customer episodes into binary attributes too early destroys the meaning. See `source-map.md` §9.1.

**Third pass (same day) — depth on the four weakest modules.** Commissioned against a 17-point brief. Added: a dedicated **JTBD engine** (Christensen's circumstance-and-progress definition, the six-link chain, three dimensions, Moesta's four forces, the HBS recruitment→interview→analysis→application arc, Revella's Five Rings and the "demographics are a dangerous distraction" critique); **Category Entry Points** as a situation-based segment generator (Romaniuk's 7Ws, the LinkedIn B2B Institute's 3C screen); **Voice of Customer** as its own module (seven language types, the paraphrase decay chain, competitor quote patterns, `DATA → OBSERVATION → INSIGHT → HYPOTHESIS`); **willingness to pay** (Pain ≠ Demand ≠ WTP, Nagle's EVE, Ramanujam's price-segmentation warning, method selection across Van Westendorp / Gabor-Granger / conjoint); the **Evidence Ladder** L0–L6 with the independence test; the **Different-X transformation matrix**; the **TAS** scoring formula; the **45-field segment object**; and the **Anti-ICP** as a deliverable. New sources are catalogued in `source-map.md` cluster 9.

### Evidence discipline

Every substantive claim in the research carries a marker: **[E]** evidence with a traceable source · **[S]** synthesis across sources · **[A]** assumption by analogy. Source reliability is scored 1–5, and depth of review is stated per source (read in full / search extract only / retrieval blocked).

**No conversion benchmarks appear anywhere in this skill.** Nothing in the corpus supports portable benchmark numbers, and inventing them is the fastest way to make a skill untrustworthy.

**Counter-evidence is included rather than smoothed over.** Byron Sharp's finding that established consumer brands grow by broad reach — not narrow targeting — contradicts the premise of most of the rest of the corpus. The skill is required to name which regime it is operating in before it recommends anything.

### Key sources

Aulet (beachhead) · Blank (market types) · Kim & Mauborgne (noncustomer tiers) · Hormozi (market criteria) · Christensen (JTBD) · Ulwick (ODI) · Moesta (four forces, switch interview) · Fitzpatrick (Mom Test) · von Hippel (lead users) · Dunford (positioning) · Schwartz (awareness stages) · Revella (buyer personas) · Sharp (mass reach — the counterweight) · Vohra & Ellis (PMF engine) · Krasinsky (ABCDX) · Balfour (four fits) · Weinberg & Mares (Bullseye) · Fishkin (audience intelligence) · Gartner (B2B buying groups) · van Westendorp (WTP) · Sherrington (5W) · Hunt's ladder · vc.ru, Habr, Kontur and the RU free-research stack.

Full accounting with URLs, reliability scores and limitations: `target-audience-master-skill/research/source-map.md`.

---

## What still needs manual validation

Stated openly so it can be fixed rather than discovered later.

| Item | Status | What to do |
|---|---|---|
| **Four blocked sources** — Zamesin and Product Focus on ABCDX, Yandex Practicum, Weinberg's own Bullseye post | Covered via other sources, but at one remove from the originating author | Re-fetch from a different network, or use printed sources |
| **Non-Meta ad libraries** (Google Ads Transparency, TikTok Creative Center, VK/Yandex) | Mechanism assumed by analogy, marked `[A]` | Verify each library's actual capabilities before recommending |
| **Tender / procurement platforms as a habitat** | Included on reasoning, not on sourced evidence | Validate with someone who sells this way |
| **Podcast and newsletter audience research** | Covered only indirectly via SparkToro | Research directly if a client needs it |
| **Comment-mining method** | The **thinnest cluster relative to the weight placed on it.** Stimulus map, contradiction scan and awareness tell are `[S]` synthesis, constructed from other frameworks — not found in any source | Attack them on first use; they are reasoning, not evidence |
| **The TAS weights** | A **specified design decision, not a calibrated model.** They sum to 1.00 and encode a defensible priority order, but no outcome dataset backs them | Use for relative ranking, never as an absolute quality measure |
| ~~Two paywalled JTBD sources~~ | **Resolved.** *Competing Against Luck* read in full; the JTBD layer now rests on the primary source. Only the HBS *Toolbox* note remains abstract-only, cited solely for four stage names | — |
| **Christensen's case outcomes** | Retold by the authors advocating their own theory, not independently audited. Christensen concedes the retrofit risk himself | Report as figures the authors state, not as verified results |
| **McDonald & Dunbar** | The **book itself was not read** — only the author's own full-length summary paper, which is self-published advocacy by the method's author and consultancy co-founder. The "85% of 30,000 products failed" stat has **inconsistent attribution within the source itself** | Method is sound and CIM-taught; buy the book if an engagement turns on exact clustering procedure. Cite the 85% figure with care, or not at all |
| **The market-map / micro-segment method** | **Heavyweight.** Presumes sales data, volumes, often commissioned research — resources most users of this skill lack | Positioned as the rigorous tier, not the default. The JTBD engine remains the fast path |
| **Cluster-vs-segment tension** | The primary source warns that slicing episodes into binary attributes "destroys meaning" — and this skill scores and ranks | Carried openly: cluster during discovery, segment during prioritisation, ship a narrative with every scored segment |
| **`DATA → OBSERVATION → INSIGHT → HYPOTHESIS`** | Framed in the brief as CXL/ResearchXL, but **not found stated in that form** in any source reviewed | Marked `[S]`. Do not attribute the phrasing to CXL |
| **SparkToro outside US/CA/UK** | First-party docs confine coverage to English-language audiences in three countries | **Never extrapolate it to RU, UA or most of Europe.** No equivalent tool was found; the RU stack is manual |
| **Marketplace pre-purchase questions** as a research surface | Searched, **nothing relevant found**. Included on reasoning alone, marked `[S]` | Verify with a seller before recommending |
| **Named tools** | Decay fastest of anything here. **GummySearch is reported to be shutting down** | Treat every named tool as a category example; verify it is alive before recommending |
| **Test coverage** | 12 of 13 briefs across two rounds; 8 defects found and fixed. ** now makes the cold run a 10-minute paste.** **But the session that ran them wrote the skill** — contaminated on recall. It verified routing, section order, timing and whether pass conditions discriminate; it cannot verify whether the skill *teaches* | **A cold run is the top open item.** Start with T4, then T8 and T12 |
| **RU regional differences** within Russia and across CIS | Described in general terms | Verify per project |
| **The worked examples** | **All five are constructed demonstrations, not case studies.** Companies do not exist | Never present them to a client as precedent |

---

## Recommended next improvement

**Run the skill against three real briefs and log where it fails.** Everything here is internally consistent and evidence-marked, but it has not yet met a real client with incomplete data, a defensive founder and a deadline.

The three most likely failure points, in order:

1. **Segment generation may produce plausible-sounding but unevidenced candidates** when the client has no existing customers and no market access. Watch the assumption count — if it exceeds half the cells, the skill should be labelling the output a research plan, and it needs testing that it actually does.
2. **The scoring matrix may reward segments that are easy to research over segments that are valuable.** Evidence availability and commercial attractiveness are not the same thing, and the matrix does not currently separate them.
3. **The regime check may be applied too rarely.** It sits in Step 1 and is easy to skip; a mass-market brand receiving beachhead advice would be a silent, confident failure.

Suggested method: three briefs — one with customers, one pre-launch, one Russian-language — then compare the outputs against `target-audience-master-skill/checklists/red-flags-checklist.md` and record which gates the skill failed to apply to itself.
