# Building an Audience Avatar From Comments

**What this is.** A complete method for constructing a sourced, defensible customer avatar out of the comments people leave around a product, a service, a category, or a competitor.

**Why it has its own file.** The skill already has review mining (`interview-and-survey-kits.md` Kit 7). **Comments are a different instrument with a different sampling frame, and treating them as "reviews with worse formatting" wastes most of their value.**

*Written English-primary to match the rest of the skill, with RU platform recipes inline. For a Russian engagement, pair this with `ru-market-playbook.md`.*

---

## §1 — Why comments are not reviews

| | **Reviews** | **Comments** |
|---|---|---|
| Who writes them | **Buyers only** | Buyers, near-buyers, refusers, lurkers, competitors, the merely curious |
| When | Retrospectively, after outcome is known | **In the moment, mid-decision** |
| Prompted by | A form asking "what did you think?" | A stimulus they chose to react to |
| Structured by | A rating scale and a text box | Nothing |
| Subject | The product | **The commenter** |
| Reveals | Satisfaction, feature gaps, switching reasons | **Identity, circumstance, objections, vocabulary, and the objections that never reach a sales call** |
| Stimulus | Unknown / generic | **Known and timestamped** |

**The load-bearing difference:** a review is written *about the product*. A comment is written *about the commenter* — because nothing asked them anything, so what they chose to say is a statement of what is on their mind.

**The second load-bearing difference:** reviews contain only people who bought. **Comments contain the people who didn't.** That is where Blue Ocean Tier-1 and Tier-2 noncustomers live, and it is the single hardest audience to reach by any other free method. [E — noncustomer tiers, `../research/frameworks.md` A3]

**The third:** because the stimulus is known, a comment is a **stimulus-response pair**, not a free-floating opinion. You know exactly what they were reacting to. That turns comment data from an anecdote pile into something closer to an experiment.

RU practice arrives at the same conclusion from the other direction: comments and community discussion are where you hear people's real words **«без маркетингового фильтра»** — without the marketing filter. [E — RU practitioner sources, `../research/source-map.md` §8.4/§8.5]

---

## §2 — What comments can and cannot tell you

**Be ruthless about this.** Half of the credibility of a comment-derived avatar comes from stating its limits before anyone else does.

### Comments are strong evidence for

- **Vocabulary** — the exact words, in the wild, unprompted. The best copy source that exists.
- **Objections** — pre-sale, unfiltered, and *ranked by how many people agree*.
- **Current alternatives** — people volunteer what they use instead, constantly.
- **Awareness distribution** — see §6, the awareness tell.
- **Identity claims** — "as a freelance designer…", "we're a 12-person agency and…"
- **Emotional register** — how much the problem actually costs them, in tone.
- **Who the segment trusts** — whose answers get thanked.

### Comments are weak or invalid evidence for

- **Prevalence.** Commenters are a vocal, self-selected minority. **You can never say "40% of our audience thinks X"** from comment data. You can say "X was raised by 23 distinct people across 5 stimuli, and never contradicted."
- **The indifferent majority.** Comments over-represent the emotionally activated — delighted or angry. The people who quietly bought and are quietly satisfied write nothing.
- **Purchase intent.** A comment costs nothing. It is interest, not intent. Never score a segment on comment volume. [See the interest≠intent rule in `../SKILL.md`]
- **Demographics.** Unless self-declared, do not infer them. Guessing age or gender from a name or a photo is both unreliable and, in a client deliverable, indefensible.
- **Anything about people who did not comment** — including most of your buyers.

### Four biases to correct for, by name

| Bias | Mechanism | Correction |
|---|---|---|
| **Stimulus selection** | A post about price attracts price-sensitive people. The stimulus recruits the commenter. | **§3 — use a portfolio of stimuli.** This is the whole method. |
| **Top-comment selection** | Platforms sort by engagement, which selects for entertainment, not representativeness. | **Always also read sorted by "new."** The middle of the distribution is where ordinary buyers are. |
| **Performance** | Public professional platforms make people perform competence; anonymous ones make people perform outrage. | Weight anonymous venues for pain, named venues for identity claims. Cross-check across both. |
| **Contamination** | Bots, competitors, paid comments, brigading. | Check account history. A commenter with no history and a strong opinion is not evidence. |

---

## §3 — The Stimulus Map (the core of the method)

**Every comment is a response to something.** Choose what you sample *by choosing what you read comments under.* Sampling a single stimulus type produces a confidently wrong avatar.

Build a portfolio. Aim for **at least four types, ideally eight**, across at least two platforms.

| # | Stimulus type | Who it pulls | What it uniquely reveals |
|---|---|---|---|
| S1 | **Your own product post / launch** | Existing customers + the already-interested | Value language, feature gaps, who self-identifies as a user |
| S2 | **A competitor's post or launch** | Their customers and their doubters | Comparative criteria, switching triggers, what they're tolerating |
| S3 | **A price, cost, or "is it worth it" post** | Price-sensitive + actual budget-holders (they argue with each other) | WTP boundaries, budget objections, **and often two distinct avatars in one thread** |
| S4 | **A "how do I do X" question thread** | Problem-aware, pre-category | **Vocabulary before the category name exists for them** |
| S5 | **A contrarian or opinionated take on the category** | The strongly-identified core | Identity, values, in-group vocabulary, sacred cows |
| S6 | **A long-running ad (60+ days) and its comments** | Who the algorithm decided to target — plus who objects to being targeted | Validated angle *and* the objection the advertiser has not answered |
| S7 | **A complaint, churn, or "I quit X" post** | Churned users and refusers | **Anxiety and Habit forces**, in their own words |
| S8 | **"What do you use for X?" thread** | Solution-aware, in-market now | The real competitive set, including "nothing" and "a spreadsheet" |
| S9 | **An explainer / educational post** | Unaware and problem-aware | Where the education gap is; the confusion points |
| S10 | **A success story or case study** | Aspirational + the sceptics | Desired identity, and the disbelief triggers that block the sale |
| S11 | **Marketplace pre-purchase questions** («вопросы о товаре» on WB/Ozon, Amazon "Customer questions") | People who have **not** bought and are deciding right now | Raw pre-purchase objections, timestamped `[S — reasoned; no dedicated source found for this surface in the corpus]` |
| S12 | **A job posting's comments / reposts** (B2B) | Peers recognising the same problem | Trigger confirmation from adjacent companies |

### The rule

**No avatar claim may rest on a single stimulus type.** A trait that appears only under S3 (a price post) is a trait of *people who comment on price posts*, not of your audience. A trait that appears under S1, S4, S7 and S8 is probably real.

This single rule is what separates this method from "we read some comments."

---

## §4 — Extraction schema

Read every comment once and tag it. Do not summarise while reading — **tag first, cluster later.** Summarising while reading is how you end up finding what you expected.

### Tag codes

| Code | Signal | Example shape |
|---|---|---|
| `ID` | Identity claim (self-declared role, situation, business type) | "as a solo bookkeeper…", "мы небольшое производство…" |
| `CIRC` | Circumstance / trigger — **the *when*** | "since our finance guy left…", "after the audit…" |
| `ALT` | Current alternative | "I just use a spreadsheet", "мы это в блокноте ведём" |
| `PAIN` | Struggle statement | "it takes me a whole evening every week" |
| `DES` | Desired outcome | "I just want to stop thinking about it" |
| `OBJ` | Objection / anxiety about the new | "but what if it doesn't sync?" |
| `HAB` | Habit / switching cost | "we've done it this way for years" |
| `$` | Money signal | "for that price I'd rather…", "мы платим 40к за это" |
| `VOCAB` | A phrase worth stealing verbatim | any |
| `AWARE` | Awareness-stage tell (§6) | "а что, так можно было?" |
| `+1` | Agreement / me-too / "same here" | **counts as frequency evidence** |
| `AUTH` | This person is being treated as an authority | others thanking or deferring to them |
| `NEG` | Explicitly not the audience | "this isn't for people like me because…" |

### The row format

One row per *signal*, not per comment. A rich comment yields four rows.

```
| ID# | Stimulus | Platform | Date | Tag | Verbatim (exact) | Agreement (likes/replies) | Commenter note |
```

**`Verbatim` must be exact.** No cleaning, no translating, no paraphrasing. The moment you paraphrase, you have substituted your words for theirs — which is the single documented failure mode of the whole RU comment-analysis practice: подмена настоящих слов клиента своими предположениями. [E — `../research/source-map.md` §8.4]

---

## §5 — Meta-signals: reading what isn't written

Most of the value is not in the comment text.

| Meta-signal | What it means | How to use it |
|---|---|---|
| **Likes / upvotes on a comment** | How many people held that view without writing it | **The cheapest frequency multiplier available.** A comment with 200 likes is 200 data points, not one. |
| **Reply threads** | The objection being argued out in public | Read the *whole* thread — the rebuttals are your objection-handling copy |
| **"+1", "same", "это про меня"** | Self-identification with a pain | Count them. This is the closest comments get to quantitative. |
| **Who answers questions and gets thanked** | The segment's trusted nodes | Habitat map input; also potential partners (see `../research/target-audience-research-report.md` §5.30) |
| **What gets ignored** | **Negative evidence.** A stimulus with high views and no comments = nobody cares. | A feature or angle nobody comments on is an angle to drop. Silence is data. |
| **Controversial sort** (Reddit) / heavily-replied comments | Where the audience splits | **Splits = segmentation signal.** See §7. |
| **Comment-to-view ratio** | Emotional activation of the topic | Compare across stimuli to find which problem actually burns |
| **Deleted/edited comments** | Often the most honest ones | If visible in quote-replies, they're worth reading |

---

## §6 — The awareness tell

You can read an audience's **awareness distribution directly from the phrasing of its comments** — no survey required. This maps straight onto Hunt's ladder for RU clients and Schwartz's stages for EN. [E — `../research/frameworks.md` B6/B7]

| Comment shape | Stage | What they need |
|---|---|---|
| "wait, that's a thing?" · «а что, так можно было?» | **Unaware → Problem-aware** | To be shown the problem has a name |
| "how do you even deal with this?" · «как вы вообще с этим справляетесь?» | **Problem-aware** | To learn solutions exist |
| "what do you use for this?" · «а чем вы это делаете?» | **Problem → Solution-aware** | Category education |
| "how is this different from [X]?" · «а чем лучше, чем [X]?» | **Solution-aware** | Differentiation |
| "does it do [specific thing]?" · «а [конкретная функция] есть?» | **Product-aware** | Specification and reassurance |
| "is there a discount / trial?" · «скидка будет?» | **Most aware** | A reason to act now |
| "tried it, didn't work for us because…" | **Refuser** — most valuable of all | To be interviewed, not marketed to |

**Do this as a count.** The *ratio* between these shapes tells you where the market sits, which decides channel and message before anything else does:

```
AWARENESS MIX (n = ___ comments, ___ stimuli)
Unaware/problem-aware   ___ %   → education cost is yours; free content works, paid burns
Solution-aware          ___ %   → the sweet spot; comparison content
Product-aware+          ___ %   → harvest; offer and proof
Refusers                ___ %   → interview these people (§8)
```

If the mix is dominated by the first row, **free acquisition in under a year is unrealistic** and the correct move is to narrow to a problem-aware sub-segment. [E — `../checklists/free-acquisition-checklist.md`]

---

## §7 — From tags to avatar

### Step 1 — Cluster by circumstance, not by demographic

Group `CIRC` and `ID` rows. You are looking for **recurring situations**, not recurring people-types. "Freelancers" is not a cluster. "People whose one clever spreadsheet just broke and who built it themselves" is.

### Step 2 — Detect multiple avatars via contradiction

**This is the step everyone skips, and it is where the method earns its keep.**

Scan for comment pairs that directly contradict each other under the *same* stimulus:

- "way too expensive for what it is" ←→ "honestly cheap for the time it saves"
- "too complicated" ←→ "finally something that doesn't oversimplify"
- "wish it did more" ←→ "wish it did less"

**A contradiction is not noise to be averaged. It is the segmentation boundary showing itself.** Averaging them produces a fictional person who wants a moderately-priced, moderately-complex product that nobody asked for.

When you find a contradiction pair, split and re-cluster. Then ask what *else* differs between the two groups — that difference is your segmenting variable, and you found it for free.

> This is the same failure as Christensen's milkshake: two real audiences averaged into one fictional one. [E — `../research/frameworks.md` B1]

### Step 3 — Fill the avatar card, with citations

Use `../templates/avatar-card-template.md`.

**The governing rule: no field may be filled without at least one cited comment.**

Empty fields stay empty and become research tasks. An avatar with six sourced fields and eight blanks is a better deliverable than one with fourteen fields of confident invention — and it tells the client exactly what to research next.

### Step 4 — Score the confidence of every claim

| Claim confidence | Requirements |
|---|---|
| **High** | ≥5 distinct commenters · across ≥3 different stimulus types · with agreement signals (likes/+1) |
| **Medium** | ≥3 distinct commenters · across ≥2 stimulus types |
| **Low** | 1–2 commenters, or all from one stimulus type → **label as hypothesis** |
| **Reject** | Single comment, no agreement, no corroboration → do not put it in the avatar |

Mark each field `[E-high]` / `[E-med]` / `[A]`. The skill's evidence markers apply here unchanged.

### Step 5 — Build the anti-avatar

Collect every `NEG` tag. "This isn't for me because…" is a gift: it is the anti-audience defining itself, in public, for free, without being asked. [E — anti-audience, `../research/frameworks.md` C2]

---

## §8 — Turning commenters into interviewees

**Comments are a recruiting pool, not just a data source — and this is their most under-used property.**

The people with the most useful comments are pre-qualified: they have the problem, they can articulate it, and they have already demonstrated willingness to talk about it in public.

**Priority order for outreach:**
1. **Refusers** (`NEG`, "tried it, didn't work for us because…") — the least-interviewed group in commerce
2. **Workaround builders** (`ALT` describing something they built) — lead-user signal
3. **High-agreement pain commenters** (`PAIN` with many likes) — they speak for a crowd
4. **Authorities** (`AUTH`) — market structure, and possible partners

**The approach message:**

> "You commented on [specific post] that [their exact words]. I'm researching how people handle [problem] — not selling anything. Would you be up for 15 minutes? Happy to share what I've found from the other conversations."

Then run **Kit 2 (Problem Interview)** from `interview-and-survey-kits.md`. Their comment is the specific observable fact that makes the outreach non-generic — which is exactly what makes manual outreach work at all. [E — `../research/frameworks.md` D6]

---

## §9 — Seeded stimulus: generating the comments you need

If existing stimuli don't cover a segment, **publish one that does.** This turns comment mining from passive to active, and the signal arrives in days.

| Seed | Pulls | Format |
|---|---|---|
| A genuine question about the problem | Problem-aware + workaround builders | "How are you all handling [X] right now? Currently doing [Y] and it's painful." |
| An honest contrarian opinion you actually hold | The identified core, plus the opposition | "I think [common category belief] is wrong, because…" |
| A public teardown of a category artefact | Practitioners with standards | See `../research/target-audience-research-report.md` §6.2 M8 |
| Your own workaround, shared freely | People with the same problem, who reveal themselves by asking for it | "Built this spreadsheet to handle [X], happy to share" |
| A "what would you want?" spec post | Solution-aware; surfaces the real requirement list | — |

### The ethical line, and it is not optional

- **The post must be genuine.** A real question you actually have, or an opinion you actually hold. Manufactured rage-bait to farm comments is deceptive, it damages the credibility you are trying to build, and communities detect it.
- **Do not misrepresent who you are.** Posting as a "regular user" while researching for a vendor is a fabrication.
- **Follow the venue's rules.** Many communities prohibit research recruitment; some require disclosure.
- **If you will use the responses, say so** when asked — and always when the venue requires it.

---

## §10 — Platform recipes

| Platform | Where the comments are | Sort / read strategy | Notes |
|---|---|---|---|
| **YouTube** | Under videos; also community-tab posts | **Sort by "Newest" as well as "Top."** Read replies — the argument is in the replies | Top-voted comments are ranked objections, pre-sorted for you. A pinned comment reshapes the whole thread — account for it |
| **TikTok** | Under videos; **Ads Manager → Comment Insights** for your own ads | Comment Insights provides sentiment ratio, word cloud, comment-audience and trend modules [E — TikTok Ads Manager docs] | Short comments; use saves/shares as intent proxy. Search your problem phrase as a *query* — younger users search here |
| **Instagram** | Post comments; question stickers | Comments are short and social | Weak for depth, useful for identity and local signals. Note the platform's legal status in RU when planning channels |
| **Telegram** | **Channel post comments ≠ chat messages.** Both matter | Read the last ~200 messages of relevant chats; check **reactions** as the agreement signal | **RU primary surface.** A large channel with dead comments is a broadcast, not a community. Find via TGStat |
| **VK** | Group posts, wall comments | Group comments skew regional | Good for local and mass-consumer RU segments |
| **vc.ru / Habr** | Article comments | **Read what people argue with, not what they applaud** | Comments are frequently more informative than the article. Arguing competently = engaged, often a buyer |
| **Reddit** | Post comments | Use **"Controversial"** sort to find splits (§7); "New" for unfiltered | Isolate the four conversation types: Pain Points · Solution Requests · Money Talk · Hot Discussions [E — `../research/frameworks.md` D4] |
| **LinkedIn** | Post comments | **Check commenters' job titles.** Are these buyers or peers? | The peer-applause trap lives here. Content adored by competitors and invisible to buyers looks identical to success |
| **Marketplaces (WB / Ozon / Amazon)** | «Вопросы о товаре» / Customer questions | Read questions, not answers | **Pre-purchase objections from people who have not bought.** `[S — reasoned; no dedicated source in the corpus]` |
| **App stores** | Review replies and developer responses | 1-star for churn triggers, 3-star for unmet needs | Vendor replies reveal what they consider acceptable |
| **Ad comments (live, not in the library)** | Under running ads on-platform | Cross-reference with the Ad Library to find 60+ day runners, then read *those* ads' comments | **The angle is validated; the comments contain the objection the advertiser has not answered.** Highest-value stimulus in the whole map |

---

## §11 — Sample sizes and stopping rule

| Depth | Comments | Stimuli | Platforms |
|---|---|---|---|
| **Minimum defensible** | 100 | ≥4 types | ≥2 |
| Comfortable | 300 | ≥8 types | ≥3 |
| Diminishing returns | ~600 | — | — |

Consistent with RU practice, which puts a first-pass floor at roughly 20–30 reviews plus a set of forum and social comments. [E — `../research/source-map.md` §8.5]

**Stopping rule:** stop when 20 consecutive comments produce **no new tag content** — only repeats of clusters you already have. That is saturation, and reading further is procrastination with a spreadsheet open.

---

## §12 — Using an LLM to process comments at scale

Legitimate and fast, with three hard constraints. Comment volumes exceed manual reading quickly, and an LLM is genuinely good at tagging — and genuinely dangerous at summarising.

**The three rules:**

1. **Quote or nothing.** Every output row must contain an exact verbatim substring of an input comment. If the model cannot quote it, it invented it.
2. **Cluster, don't characterise.** Ask it to group comments and label groups. **Never** ask it to "describe the typical customer" — that produces fluent, confident persona theatre from thin data. You do the avatar synthesis; the model does the sorting.
3. **Count, don't estimate.** Counts come from the spreadsheet, not from the model's impression. A model asked "what percentage feel X" will produce a number, and the number will be fiction.

**A working prompt shape:**

> "Here are N comments. For each, output rows only where a signal is present, using these tags: ID, CIRC, ALT, PAIN, DES, OBJ, HAB, $, VOCAB, AWARE, +1, AUTH, NEG. Each row: comment number · tag · **exact verbatim substring** · nothing else. Do not paraphrase. Do not infer demographics. Do not summarise. If no signal is present, skip the comment."

Then cluster the tagged rows yourself, or in a second pass that only sees the verbatim column.

---

## §13 — Ethics and legal

- **Public ≠ consent to be profiled.** A public comment can be read and analysed in aggregate. Compiling a named dossier on an individual commenter is a different act. Don't.
- **Anonymise in deliverables.** Quote verbatim, attribute to a platform and a date, not to a person. A client deck naming commenters is a reputational hazard for everyone in it — including your client.
- **Do not infer sensitive characteristics** — health, beliefs, orientation, financial distress — from comments, and never build targeting on such inference. If a segment is genuinely defined by a sensitive circumstance, it must rest on **self-identification**, the product must genuinely suit them, and the language must be respectful. [E — `../OPERATING-MANUAL.md` §10]
- **Respect platform ToS on scraping.** Manual reading is always permitted; automated collection often is not.
- **Do not fabricate comments** — not as illustrations, not as "representative examples," not in a mock-up. If you need an example, mark it clearly as constructed.
- **Do not bait.** See §9.
- **RU note:** public comments still fall under personal-data rules (152-ФЗ) when tied to an identifiable person. Aggregate and anonymise.

---

## §14 — Quality gate

Do not deliver a comment-derived avatar until every line passes.

- [ ] **≥4 stimulus types** sampled, listed by name in the deliverable
- [ ] **≥2 platforms**
- [ ] **≥100 comments** tagged
- [ ] Comments read sorted by **new**, not only by top
- [ ] Every avatar field carries **≥1 verbatim citation**, or is left blank
- [ ] Blank fields listed explicitly as research tasks
- [ ] Every claim marked `[E-high]` / `[E-med]` / `[A]`
- [ ] **Contradiction scan run** — and if contradictions were found, the avatar was split rather than averaged
- [ ] **Awareness mix counted**, not estimated
- [ ] **Anti-avatar built** from `NEG` tags
- [ ] Verbatims are exact — **no paraphrasing, no cleanup, no translation**
- [ ] No demographic inferred that was not self-declared
- [ ] No prevalence claim ("X% of our audience…") made from comment data
- [ ] Vocal-minority limitation stated **in the deliverable**, not just known
- [ ] ≥3 commenters identified as interview candidates (§8)
- [ ] Commenter accounts spot-checked for bots and competitors

**The final honesty check:** an avatar built from comments describes *people who comment*. Say so in the deliverable, in one sentence, before the client works it out themselves. It costs nothing and it is the difference between a research asset and a confident-sounding document.

---

## §15 — Where this fits in the workflow

Slots into **Step 5 (collect evidence)** of the main workflow.

**Use it as the primary method when:**
- there is no access to buyers, and no customer list
- the client is pre-launch and needs vocabulary and objections fast
- the budget is zero and the timeline is days
- you need **noncustomers** — refusers and near-buyers — that reviews structurally cannot give you
- an existing avatar smells invented and needs to be replaced with something sourced

**Do not use it alone when:**
- prevalence matters → add a survey
- the segment is B2B enterprise → most of that decision happens in private, and the comment layer is thin
- the category has almost no public conversation → the absence is itself a finding (low community density → free acquisition is unlikely)

**Then hand off:**
- Avatar → `../templates/avatar-card-template.md`
- Vocabulary and objections → `../templates/positioning-template.md` (§8 language, §9 objections)
- Commenters → interviews via `interview-and-survey-kits.md` Kit 2
- Habitats discovered → `habitat-research-playbook.md`
- Segments discovered → score them in `../templates/scoring-matrix-template.md` **like any other candidate.** A segment found in comments gets no scoring discount for being interesting.
