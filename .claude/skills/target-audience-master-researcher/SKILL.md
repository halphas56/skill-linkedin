---
name: target-audience-master-researcher
description: >
  Finds the target audience that will actually pay, stay and spread — including the
  non-obvious ones nobody else is marketing to. Generates 10–20 candidate segments,
  scores them on evidence, maps exactly where each one gathers, judges whether they can
  be reached for free, and builds positioning around the winner. Use when someone asks
  who their audience is, who to sell to, which segment or niche to pick, where to find
  customers, how to reach an audience without a budget, why their marketing isn't
  converting, or wants an ICP, buyer personas, a customer avatar built from real
  comments and reviews, a jobs-to-be-done analysis, customer-pain discovery, validation,
  ranking or non-manipulative pain-based messaging, voice-of-customer
  language, audience segmentation, willingness-to-pay assessment, demand
  validation, a go-to-market hypothesis, or a comparison between
  two audiences. Covers B2B SaaS, expert courses, agencies and services, local business,
  consumer products, high-ticket consulting, marketplaces, mobile apps, info products and
  subscriptions. Works in English and Russian — trigger terms include целевая аудитория,
  ЦА, портрет клиента, сегментация аудитории, кастдев, custdev, где искать клиентов,
  платёжеспособная аудитория, готовность платить, боли клиентов, выбор ниши, ICP, аватар клиента,
  составить аватар, анализ комментариев, анализ отзывов, что пишут в комментариях, JTBD,
  боли клиента, найти боли, проверить боли, приоритизация болей, как давить на боль,
  триггеры боли, копирайтинг через боль, страх в рекламе,
  работа для продукта, язык клиента, неочевидная аудитория, как привлечь клиентов бесплатно,
  кому продавать, кому НЕ продавать.
---

# Target Audience Master Researcher

Find the audience that will pay, stay and spread — and prove it before anyone spends money.

> ### Architecture: one skill, many modules
>
> **This file is the skill.** It is the only file in this folder with YAML frontmatter and a `name:` field, and the only entry point Claude ever loads on its own.
>
> Everything else — `knowledge/`, `templates/`, `checklists/`, `research/`, `examples/`, `tests/` — is a **reference file this file points at**. Reference files have no frontmatter, are never invoked directly, and are loaded on demand when the task calls for them. That is progressive disclosure, and it is what keeps a large body of method usable.
>
> **Adding a module never means adding a skill.** A new module is a new file under `knowledge/` plus a row in the routing table below. The count of skills stays at one, permanently.
>
> **Why not one enormous file:** the method runs to ~17,000 lines. A single file loads all of it on every request, destroys routing, and buries the two or three files a real engagement actually needs. The split is what makes the depth navigable — not a departure from the one-skill rule but the mechanism that lets one skill hold this much.

**Two files before your first engagement:**
- **[`SYNTHESIS.md`](SYNTHESIS.md)** — what all of this is actually about. The one law, the altitude stack, the two engines, where sources converge and where they genuinely conflict, and the four-hour pass. **Read once. Re-read whenever two sources appear to contradict each other.**
- **[`OPERATING-MANUAL.md`](OPERATING-MANUAL.md)** — the operating instructions: role, intake, workflow, gates, critic.

**The one law, if you read nothing else:** *audience research is the practice of refusing convenient representations.* Every instrument here catches one specific substitution — the category name for what they'd actually do instead, the average for the people, what they say for what they do, engagement for intent, a number with decimals for a finding.

---

## Fast path

0. **Size the pass to the decision** (`SYNTHESIS.md` §10). Four hours, a day, a week, a month — each has a defined shape. **Never run a longer pass than the decision deserves, and never present a shorter one as though it were longer.**
0b. **Level the brief** (`OPERATING-MANUAL.md` §3) — **before selecting a mode.** Run the Evidence Ladder on *the client's assertions*, not only on your own findings. Extract every load-bearing claim · ask what level you would need to assert it yourself · note what level it actually arrived at (almost always `L0` — the client said so) · **any gap is a premise error.** Watch especially for the three shapes that hide easiest: an **effectiveness claim** ("this converts well"), an **inference from absence** ("nobody searches for it"), and a **structural assertion** ("X decides"). **A premise error caught at intake costs one question; caught at delivery it costs the engagement.**
1. **Pick the mode** (`OPERATING-MANUAL.md` §2). "Find our audience" is a full engagement. "Is this audience any good?" is one page with the answer first. **No data at all → RESEARCH PLAN mode, selected now, not discovered at the end.** Running 14 sections on a small request is a failure, not thoroughness.
1b. **Find the earliest broken link.** The chain is *market boundary → where decisions happen → whose struggle → profile → their words → offer → message*. Ask: **"what is the earliest link you haven't established with evidence?"** Start there, whatever was requested — the most common wasted engagement is messaging work on top of a wrong market definition.
2. **Test the input for *usability*, not presence** (§3). A filled-in field that could describe anyone counts as missing. If thin, ask the five triage questions once — then **proceed regardless of what comes back.** Never block on intake.
3. **Set the four dials**: business model (selects the scoring preset) · **regime** (focus or reach) · language · founder hours per week (decides whether "free" channels exist at all).
4. **Define the job, not the person** — [`knowledge/jtbd-engine.md`]. The six-link chain: *situation → trigger → struggle → desired progress → alternatives → purchase decision*. **A definition missing any link is a hole in the strategy.** Score the four forces and name the binding constraint.
5. **Map the situations** — [`knowledge/category-entry-points.md`]. Run the 7Ws to generate 10+ CEPs. Situations produce segments that people-first thinking cannot see, and the **With/For Whom** column detects buyer ≠ user for free.
5b. **Check where the decision actually sits** — [`knowledge/market-mapping.md`]. Define the market **by need, not by product**, then map the chain to the final user and record **what share of purchases is decided at each junction**. If contractors, distributors or specifiers decide a meaningful slice, you are about to generate candidates at the wrong junction.
6. **Generate 10–20 segments** — [`knowledge/segment-generation-lenses.md`], then run the **Different-X transformation matrix** on the strongest. **At least 3 unexpected candidates and at least 1 anti-audience.** Non-negotiable. Where sales data exists, prefer the **bottom-up micro-segment engine** instead.
7. **Collect evidence** — [`knowledge/interview-and-survey-kits.md`]. **No access to buyers, or the ask is an avatar? Run [`knowledge/avatar-from-comments.md`]** — comments are the only free source containing *non-buyers*.
7b. **Turn complaints into pains** — [`knowledge/pain-discovery.md`]. Ladder **up** for meaning *and* chain **down** for cost · classify on four axes · differential diagnosis · six validation tests. **Divergent roots from one complaint = more than one segment.**
7c. **Price the pain and rank it** — [`knowledge/pain-opportunity.md`]. Quantify **cost of inaction** with sourced arithmetic · record the **behavioural rung** (complaining is B1; a built workaround is B3; a job posting is B7) · score **twice** — Pain Strength and Commercial Opportunity — and name the quadrant. **Never blend them.**
8. **Harvest the language** — [`knowledge/voice-of-customer.md`]. Verbatim, seven language types, `DATA → OBSERVATION → INSIGHT → HYPOTHESIS`. **Never paraphrase; paraphrasing destroys the asset.**
9. **Test the money separately** — [`knowledge/willingness-to-pay.md`]. **Pain ≠ Demand ≠ WTP.** Quantify the economic value of the problem; a segment with moderate pain over $100k of exposure beats extreme pain with no budget.
10. **Level every claim** — [`knowledge/evidence-ladder.md`]. L0–L6, and **3+ *independent* source types before anything is called validated.**
11. **Score** — [`templates/scoring-matrix-template.md`]. **TAS** headline, column-wise, source per cell, **gates separate from totals.**
12. **Map habitats** — [`knowledge/habitat-research-playbook.md`]. Named instances, never platform names. **Rank by over-index, not by raw share.**
13. **Judge free acquisition** — [`checklists/free-acquisition-checklist.md`]. Channel + required asset + time-to-signal + failure condition. Never encouragement.
14. **Build positioning** — [`templates/positioning-template.md`], Dunford order, swap test.
15. **Emit the segment objects** — [`templates/segment-object-template.md`] for each recommended segment, for handoff downstream.
15b. **Ethical review — any message built on pain** ([`templates/pain-matrix-template.md`] Part 8). Per message, not per campaign: is the relief mechanism in the **same breath** as the threat, or below the fold? Are **both** halves of efficacy present — "it works" *and* "you can do this"? Does the reader keep full information, emotional space and a clear exit? **Any prohibited move present and it does not ship.**
16. **Run the red-flags check + the Anti-ICP** ([`checklists/red-flags-checklist.md`]) and the built-in critic (§7) **before delivering.**
17. **Fill the Delivery Header and put it at the top** ([`templates/research-output-template.md`] §0). **Never delete a row to make it look complete** — an honest blank is a finding. An empty *unwelcome finding* means either the client was right about everything or the pass was shallow; say which.
18. **Ship it as a PDF.** `python tools/md2pdf.py REPORT.md -o REPORT.pdf --title "..." --stats "..."`. A markdown file in a repo is not a deliverable a client reads. **The cover stat strip is not decoration** — put the numbers that decide something there (score, gate failures, evidence level of the primary recommendation), because that is the page everyone actually looks at.

---

## Reference files

**Thirteen knowledge files exist and a real engagement loads two or three.** Load by tier, not by browsing.

### Tier 0 — always

| File | Why |
|---|---|
| [`SYNTHESIS.md`](SYNTHESIS.md) | **Read once before your first engagement.** The one law, the altitude stack, the two engines, the convergence and conflict maps, the refusal principle, and the minimum viable pass. **Re-read whenever two sources appear to contradict each other** |
| [`OPERATING-MANUAL.md`](OPERATING-MANUAL.md) | Role, intake, the 14-step workflow, gates, built-in critic, ethics |
| [`knowledge/evidence-ladder.md`](knowledge/evidence-ladder.md) | **The core protocol.** L0–L6, the independence test, what each level licenses, the Evidence Profile block |
| [`knowledge/ru-market-playbook.md`](knowledge/ru-market-playbook.md) | **Any Russian-language engagement.** RU terminology, habitats, free research stack, ABCDX, ready phrasings |

### Tier 1 — the altitude stack, in zoom order

**Traverse; don't camp at one level** (`SYNTHESIS.md` §2). A defensible pass touches at least three.

| Altitude | File | Answers |
|---|---|---|
| 1 · **Market structure** | [`knowledge/market-mapping.md`](knowledge/market-mapping.md) | Where in the chain is it decided, and who controls what share? **Always when selling through channels** |
| 2 · **Situation** | [`knowledge/category-entry-points.md`](knowledge/category-entry-points.md) | When does the category come to mind? 7Ws, 3C, buyer ≠ user |
| 3 · **Person** | [`knowledge/jtbd-engine.md`](knowledge/jtbd-engine.md) | **Always.** What progress, in what circumstance? Six-link chain, four forces, the two precision tests |
| 4 · **Profile** | [`knowledge/customer-profile.md`](knowledge/customer-profile.md) | What must be written down, ranked and quantified? **Always before handoff** |
| 5 · **Sentence** | [`knowledge/voice-of-customer.md`](knowledge/voice-of-customer.md) | What words did they actually use? Any copy or messaging work |

### Tier 2 — engines and methods

| File | Load when |
|---|---|
| [`knowledge/pain-discovery.md`](knowledge/pain-discovery.md) | **Is the pain real?** Four axes, 14-type taxonomy, laddering *up* + pain chains *down*, latent pain, workaround / trigger / lost-deal mining, source tiers, what is *not* a pain, six validation tests, **ethical closing (EPPM)** |
| [`knowledge/pain-opportunity.md`](knowledge/pain-opportunity.md) | **Is it a business?** Cost of inaction, the behavioural rung B1–B9, **frequency ≠ importance**, the **two scores** and their 2×2, pain concentration / threshold / evolution, the Pain × Segment matrix, evidence AGAINST |
| [`knowledge/segment-generation-lenses.md`](knowledge/segment-generation-lenses.md) | **Generating candidates.** 30 generators, the Different-X matrix, and the bottom-up alternative |
| [`knowledge/willingness-to-pay.md`](knowledge/willingness-to-pay.md) | Any pricing or segment-ranking question. Pain ≠ Demand ≠ WTP, economic value estimation |
| [`knowledge/interview-and-survey-kits.md`](knowledge/interview-and-survey-kits.md) | Collecting evidence. Verbatim scripts, EN + RU |
| [`knowledge/avatar-from-comments.md`](knowledge/avatar-from-comments.md) | **No access to buyers, or an avatar is the ask.** Comments are the only free source containing non-buyers |
| [`knowledge/habitat-research-playbook.md`](knowledge/habitat-research-playbook.md) | Finding where they are. Research stack, per-platform recipes, the over-index rule |

### Tier 3 — outputs

| File | Load when |
|---|---|
| [`templates/scoring-matrix-template.md`](templates/scoring-matrix-template.md) | Scoring. The TAS formula, 19 diagnostic criteria, 12 presets |
| [`templates/pain-matrix-template.md`](templates/pain-matrix-template.md) | Ranking pains inside a segment and mapping them to offers. Inventory · laddering · PPS with gates · the 14-field pain map · the ethical review |
| [`templates/segment-object-template.md`](templates/segment-object-template.md) | Handoff. 45 fields + YAML for downstream skills |
| [`templates/positioning-template.md`](templates/positioning-template.md) | Positioning hypotheses. 17 components, swap test |
| [`templates/research-output-template.md`](templates/research-output-template.md) | The delivery contract — 14 sections plus shorter shapes |
| [`templates/avatar-card-template.md`](templates/avatar-card-template.md) | Delivering an avatar — citation-enforced |
| [`templates/audience-brief-template.md`](templates/audience-brief-template.md) | Asking the client to prepare inputs |

### Tier 4 — gates

| File | Load when |
|---|---|
| [`checklists/red-flags-checklist.md`](checklists/red-flags-checklist.md) | **Before delivering, always.** Also for auditing an existing audience definition. Contains the Anti-ICP |
| [`checklists/ideal-audience-checklist.md`](checklists/ideal-audience-checklist.md) | Before recommending any segment |
| [`checklists/free-acquisition-checklist.md`](checklists/free-acquisition-checklist.md) | Judging whether free acquisition is realistic |

### Tier 5 — reference, consult don't read

| File | Load when |
|---|---|
| [`research/frameworks.md`](research/frameworks.md) | **Quick lookup mid-engagement.** 48 framework cards + a question→framework routing table |
| [`research/source-map.md`](research/source-map.md) | You need a source, its depth marker, reliability score or stated limitation |
| [`research/target-audience-research-report.md`](research/target-audience-research-report.md) | You need the full reasoning, the taxonomies, or a citation |
| [`research/examples.md`](research/examples.md) | You need a comparable — 15 weak→strong rewrites |
| [`examples/00-reference-engagement.md`](examples/00-reference-engagement.md) | **The reference implementation.** A channel business run end to end through the current instrument set — market map with quantified leverage, four forces, evidence levels, TAS with sources, anti-ICP, circle-before-square. **Imitate this one** |
| [`examples/*.md`](examples/) | Worked engagements by business type: B2B SaaS · expert course *(RU)* · agency · local business *(RU)* · unexpected-audience discovery. **These five predate research passes 3–6** — each ends with a *"Delta to the current method"* section stating what the current instruments would change. Read the delta |
| [`tools/md2pdf.py`](tools/md2pdf.py) | **Turns any deliverable in this skill into a structured A4 PDF** — cover with a stat strip, generated contents, repeating table headers across page breaks, coloured PASS/FAIL badges, stamped page numbers. Cyrillic-safe throughout, in both the body and the footer. Run it as the last step of every engagement |
| [`tests/`](tests/) | 13 adversarial briefs with documented traps · the evaluation rubric (6 gates, 11 dimensions) · three audit logs. **[`tests/COLD-RUN.md`](tests/COLD-RUN.md) is a 10-minute copy-paste kit** that separates production from scoring — the only way to test whether the skill *teaches* rather than whether it is coherent. **[`tests/run-log-2026-08-27-cold.md`](tests/run-log-2026-08-27-cold.md) is the control group**: the same brief answered without the skill, scoring 18/33 |

---

## Non-negotiable rules

- **Every audience claim carries a level, L0–L6** ([`knowledge/evidence-ladder.md`]). **The cardinal sin of this skill is laundering an L0 guess into a finding by rewriting it more confidently.** Fluency is not evidence. Any L0 in a delivered report is a defect.
- **Triangulation needs *independence*.** 1 source = hypothesis · 2 = weak evidence · **3+ independent source types = validated**. Three review sites are one source type. Five articles quoting one study are one source. A survey plus an interview plus a poll are all stated preference and will be wrong together.
- **The deliverable is a PDF**, generated by [`tools/md2pdf.py`](tools/md2pdf.py) from the markdown. Write markdown, ship PDF. `PASS` / `FAIL` / `PARTIAL` in table cells are auto-badged, so **write verdicts as those bare tokens** rather than prose equivalents.
- **Every output opens with the Delivery Header** ([`templates/research-output-template.md`] §0) — mode, regime, **premise audit**, evidence profile, gates, anti-audience, trade-off, **unwelcome finding**. A one-line version for short answers. **A short answer is not exempt** — it is the shape most likely to skip the checks.
- **Never block on missing input.** State assumptions and produce work. *"I need more information"* is a failure state.
- **Never fabricate.** No invented statistics, benchmarks, case studies, customer quotes or proof. Use `[PROOF NEEDED: how to obtain it]`. A fabricated benchmark is worse than none — it terminates thinking.
- **Never claim experience you do not have.** *"In my experience"*, *"по моему опыту"*, *"на таких проектах обычно"*, *"I've seen this many times"* — **a fabricated credential is fabricated proof.** It is the same failure as an invented statistic wearing a different coat, and it is harder to spot because it cites nothing a reader can check. If the reasoning is sound, give the mechanism instead: *"this predicts X because Y"* is checkable; *"in my experience X"* is not. `[S]`
- **Mark every claim** `[E]` evidence · `[S]` synthesis · `[A]` assumption. Report the assumption count. **If assumptions outnumber evidence, the deliverable is a research plan — label it as one.**
- **Define by the job and the circumstance, never by the person.** The six-link chain must be complete: situation → trigger → struggle → desired progress → alternatives → purchase decision. **The test: could a marketer write an ad from this definition alone?**
- **Run the abstraction test on every job statement.** List what they could hire instead. **If every candidate comes from the same product category, it is a spec or a preference, not a job — go up a level.** You have arrived when "do something else entirely" appears on the list.
- **Jobs are verbs and nouns.** "Convenience" is not a job. Neither is a need ("they need to grow") nor a life theme ("feel like a good parent") — those are true on most days and trigger no purchase.
- **A purchase proves persuasion; repeated use proves the job.** Ask for usage data, not sales data. High Big Hire with low Little Hire means the job was mis-identified and the buyers will churn.
- **Cluster before you segment.** Discovery works in whole narratives; the scoring machinery comes after. Deconstructing customer episodes into binary attributes too early destroys the meaning you were trying to find. Every scored segment ships with at least one full story attached.
- **Never build a pass on handed-over data alone.** Client data is operations data, organised around products and customer attributes. It will reproduce their existing view of their market. Go and get the passive data: nonconsumers, workarounds, refusers.
- **Always run the negative-jobs generator.** What does this customer wish they did not have to do *at all*? Removal, not improvement, is frequently the product — and nobody asks for the absence of a step, so it never shows up in feature research.
- **Every segment needs a *who*, a *when*, and a *where*.** Missing the *when* makes it a list. Missing the *where* makes it a wish.
- **Demographics are targeting parameters, never a definition.** The same demographic buys the same product for different jobs. Demographics are a dangerous distraction, and they produce roughly twice as many personas as focusing on the decision does.
- **Never build a persona for someone who signs off but does not choose between vendors.** Seniority is not influence over the decision.
- **Verbatim or nothing.** Store the raw string; analyse the raw string. Paraphrasing deletes intensity, frequency, systems and the person — in that order — and each step feels like tidying.
- **Never accept an adjective where a number belongs.** "Takes too long" → *after how many minutes?* "Too expensive" → *above what figure?* An unquantified pain cannot be ranked, compared, or used to size the value of the problem.
- **Separate obstacles from risks.** An obstacle needs *removal*; a risk needs *reassurance*. You cannot reassure away an obstacle, and no amount of friction-reduction cures a fear.
- **Required and expected benefits are table stakes.** Deliver them; never claim them as differentiation. Differentiation lives at *desired* and *unexpected*.
- **Build the profile with the product hidden.** If a stranger could reverse-engineer what you sell from your list of customer pains, you wrote it backwards.
- **Test the audience before the offer.** If an offer test fails you cannot tell whether the offer was wrong or the audience was wrong. Every validation plan includes one experiment on the profile itself, run first.
- **In intermediated and multi-sided models, "the audience" is not one audience.** A profile covering only the end user in a channel business is an incomplete deliverable — say so rather than shipping it.
- **Pain ≠ Demand ≠ Willingness to pay.** Three separate gates that fail independently. **Rank segments by economic exposure, not by emotional intensity**: moderate pain over a large number beats agony over nothing.
- **Score pain twice, never once.** *How much does it hurt* and *can a business be built on it* are different questions. A blended total hides the quadrant that matters most — real suffering with no budget.
- **Frequency is not importance.** Counting mentions measures prevalence. Griffin & Hauser tested whether mention-frequency proxies importance and found it does not. 100 people calling an interface ugly ranks above 10 people losing $10k a month — and is the less interesting problem.
- **Complaining is the weakest signal there is.** A built workaround costs hours; a job posting costs a salary; a purchase costs money. **Record what they did, not what they said.**
- **Quantify cost of inaction, and show the arithmetic.** An unsourced multiplier makes an authoritative number out of a guess.
- **Every pain carries an "evidence against" column.** Empty means nobody looked — write *"searched, none found"* instead.
- **If nobody said it, it does not go in quotation marks.** A fabricated customer quote is the fastest way to make a research document worthless.
- **A complaint is not a pain.** Ladder it — *"why does that matter to you?"* — until the answer stops changing, then stop **one rung above a life theme**. The complaint explains a support ticket; the root explains a purchase.
- **Never raise threat without raising efficacy in the same breath.** High threat with low efficacy produces defensive avoidance, denial and reactance — the audience defends against the *message* instead of the *problem*. This is the ethical rule and the effectiveness rule simultaneously, and it fails on **layout** as easily as on intent: relief below the fold is fear control.
- **Never name a pain you cannot relieve or cannot prove you relieve.** No mechanism or no proof → the pain belongs in research, roadmap and non-selling content. Not in acquisition.
- **A pain is not a desire, an objection, a demographic or a feature request.** The test: *has this already cost them something specific that they can name?*
- **The buyer keeps full information, emotional space and a clear exit.** No fake urgency, no invented scarcity, no shame framing, no hidden exit — regardless of how well it converts.
- **Define the market by need, never by product.** "The pensions market" and "our catering business" hide most of the competitors. Every share and growth figure computed on a wrong definition is meaningless — **never reuse a client's market-share number without asking what market it measures against.**
- **A segment is a need group, not a sector.** If the segment list reads as industry names, no segmentation has happened yet.
- **Never impose a segmentation scheme.** Demographics, socio-economics and firmographics are **descriptors that make a found segment reachable** — never the logic that creates one. "We segment markets by…" is the error.
- **Find out where the decision actually sits before choosing whom to research.** In channel markets a large share of purchases is decided by contractors, distributors or specifiers, not by the end user.
- **"Everyone in our market buys on price" is a hypothesis about the client's research, not a fact about their market.** In the ICI case the whole industry believed it; the genuinely price-driven segment was 10%.
- **Ask "will the company actually change?" during intake, not at delivery.** A segment nobody will reorganise around is a slide. If the answer is no, the deliverable is an evidence case for change — say so up front.
- **Never recommend an unreachable segment.** Say: *"excellent audience, currently closed to you — here is the asset that opens it."* That is a complete, professional answer.
- **Ability to pay ≠ willingness to pay.** They fail independently. Check both, separately.
- **Interest ≠ intent.** Score against completed transactions, never against likes, follows or engagement.
- **Value first, audience second.** Establish what the business is genuinely better at, then find who is structurally forced to care.
- **Gates override totals.** A high weighted score with a failed gate is a disqualification, and it must be stated on the same line.
- **Never report a bare TAS.** Always four columns together: score · gates · evidence level · assumption count. A number without its evidence is astrology with decimals.
- **Never average a contradiction.** "Too expensive" beside "cheap for what it does" is a segmentation boundary, not noise. Averaging two real segments produces a fictional third one that nobody belongs to.
- **Rank habitats by over-index, not raw share.** 80% on a universal platform tells you nothing; a 200% over-index on a niche one tells you where they are distinctively reachable.
- **At least 3 unexpected candidates, every time.** Obvious segments crowd out non-obvious ones by default.
- **Always name an anti-audience** — and frame it in resource terms, never as a judgement about people.
- **Every recommendation names a trade-off.** "No trade-off" is a rejected answer.
- **Never answer "can this be free?" with encouragement.** Answer with channel, required asset, time-to-signal, and the condition under which it becomes no.
- **Name the regime before recommending.** Narrowing is right for a challenger and wrong for an established mass-market brand.
- **A tie is a tie.** Two segments within ~0.3 are not distinguishable by analysis — resolve with an experiment, not more argument.
- **Match the user's language.** Formulate natively in Russian or English. Use each market's canonical framework names (Хант / Schwartz, ABCDX / ICP).
- **Something in the report must be unwelcome.** A report that flatters every prior belief has agreed, not researched.

---

## When to hand off

This skill chooses **who** to sell to and **where** they are. It is upstream of, not a substitute for:

| Task | Use instead |
|---|---|
| Sharpening the positioning statement, category choice, differentiation | `positioning-master` — this skill produces the audience input it needs |
| Designing the offer, pricing, guarantees, value stack | `strong-offer-creator` |
| Building the funnel, sequences, landing pages, checkout | `sales-funnel-architect` |
| Channel execution, lead magnets, outbound systems, lead scoring | `leadgen-architect` |
| Partner and affiliate channel design | `affiliate-partner-marketing-master` |

**Order of operations:** audience → positioning → offer → funnel → channels. Skipping to funnel work with an unresolved audience is the most expensive mistake in the chain, because everything downstream inherits the error.
