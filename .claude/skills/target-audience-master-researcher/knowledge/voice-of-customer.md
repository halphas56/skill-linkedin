# Voice of Customer

**A separate module, not a step inside another one.** VOC is the discipline of capturing what buyers actually say, in the words they actually use, and refusing to translate it into marketing language.

**Why it needs its own file.** Paraphrasing is the default behaviour of every analyst and every language model, it feels like doing the work, and it destroys the asset. The value of a customer quote lives in the exact words. Rewrite them and you have replaced evidence with your own assumptions — which is the one failure mode Russian practitioner sources name explicitly: **подмена настоящих слов клиента своими предположениями.** `[E]`

---

## §1 — The paraphrase decay chain

Watch a real research artefact die by degrees. Each step feels like a small tidy-up. Each step deletes something specific and unrecoverable.

| Step | The text | What was deleted |
|---|---|---|
| **0 · Raw** | «Я заебался каждый вечер переносить заявки из Telegram в CRM» | — nothing yet |
| 1 · "Cleaned up" | «Устал каждый вечер переносить заявки из Telegram в CRM» | **Intensity.** "Заебался" ≠ "устал". One is a person at their limit; the other is mildly inconvenienced. Urgency just dropped by half |
| 2 · Third person | «Тратит время на ручной перенос заявок» | **First person, the frequency ("каждый вечер"), the time of day, both named systems.** The trigger and the integration spec vanish together |
| 3 · Professionalised | «Неэффективный процесс обработки лидов» | **The human being.** Now it is a category, not a person. No ad can be written from this |
| 4 · Strategic | «Клиенты хотят автоматизировать бизнес» | **Everything.** This sentence fits any company on earth, describes nobody, and predicts nothing |

Step 4 is where most audience research is delivered.

**What step 0 hands you that step 4 does not:**
- **Every evening** → the frequency, and therefore the urgency and the pricing logic
- **Telegram → CRM** → the exact integration, the exact competitor ("doing it by hand"), the exact demo to build
- **Заебался** → the emotional register the ad copy must match
- **"Я"** → a real person you can go and find more of

**The rule: verbatim or nothing.** Store the raw string. Do all analysis on the raw string. Decide about client-facing presentation separately and last — and when profanity or rawness must be softened for a deck, keep the original in the research file and note that it was softened.

---

## §2 — The reasoning chain

Borrowed from conversion-research practice (CXL's ResearchXL model), and binding here: `[E]`

```
DATA  →  OBSERVATION  →  INSIGHT  →  HYPOTHESIS
```

| Stage | What it is | Example |
|---|---|---|
| **Data** | The raw artefact, unedited | «Я заебался каждый вечер переносить заявки из Telegram в CRM» |
| **Observation** | A neutral, countable statement about the data | 14 of 60 comments describe manual transfer between two named systems; 9 specify a daily cadence |
| **Insight** | What that means, stated as a claim with a level | The struggling moment is a *daily repeated* manual task, not a one-off setup problem `[L3]` |
| **Hypothesis** | A falsifiable prediction with a test | A message built on "stop the evening copy-paste" will outperform "automate your business" on cost-per-booked-call. Test: two landing pages, equal traffic, 2 weeks |

**The failure mode this prevents:**

```
DATA  →  CONFIDENT ASSUMPTION
```

An LLM will jump straight from a handful of comments to a fluent paragraph describing "the modern entrepreneur's desire for efficiency." That paragraph is `L0` (`evidence-ladder.md`) and must never be presented as a finding.

**Enforcement: never skip a stage in writing.** Each stage gets its own column in the swipe file. If you cannot write the observation, you do not have the insight.

---

## §3 — The seven language types

Harvest each separately. They power different assets, and mixing them into one "quotes" pile makes all of them unusable.

---

### 1. Pain language
**What it is.** How they describe the problem when nobody is selling to them.

**Harvest from.** Forum posts, comments, support tickets, 3–4 star reviews, sales-call transcripts, anonymous venting.

**Powers.** Ad hooks, headlines, the opening line of cold outreach, content titles.

**Look for.** First person · a time marker · a named system or person · a physical or emotional consequence.

**Example.** «каждый вечер по часу свожу два экселя» · "I spend Sunday nights reconciling two exports"

**Anti-pattern.** Category nouns: "inefficiency", "lack of automation", "неоптимальные процессы". Nobody has ever said these words about their own life.

---

### 2. Desired-outcome language
**What it is.** How they describe the after-state — in *their* metric, not yours.

**Harvest from.** "I just want to…" statements, success criteria in interviews (Ring 2), positive reviews describing relief.

**Powers.** Value propositions, promise lines, case-study titles, onboarding goals.

**Look for.** The metric they are personally measured on. Wynter's buyer-intelligence practice puts this directly: **"What metric is your ICP measured on?"** `[E]`

**How to actually get it — never accept an adjective.** `[E — Osterwalder]` If they say *"waiting is a waste of time,"* ask **after how many minutes** it starts feeling wasted → the pain becomes *"losing more than X minutes."* If they say *"improve performance,"* ask what exactly they expect → the gain becomes *"raise X above Y."* If they say *"a pay rise,"* ask **to what amount.** Every "too slow", "too expensive", "not reliable enough" has a number behind it, and that number is the specification for the promise, the proof, the price and the guarantee. Full technique: `customer-profile.md` §5.

**Example.** «чтобы в понедельник цифры уже сходились» · "so the report goes out before the client asks for it"

**Anti-pattern.** Your metric substituted for theirs. "Increase efficiency by 30%" is a vendor sentence.

---

### 3. Objection language
**What it is.** The exact form of the doubt — Anxiety and Habit made verbal (`jtbd-engine.md` §4).

**Harvest from.** Comment replies, "but what about…", questions asked last on a call, churn interviews, competitor review complaints, marketplace pre-purchase questions.

**Powers.** FAQ, risk reversal, guarantees, sales objection handling, the "who this isn't for" section.

**Look for.** Conditionals: "if only…", "as long as…", "but what if…", «а если…», «а вдруг…».

**Example.** «а если нам потом всё это переносить обратно?» · "what happens to my data if we cancel?"

**Rule.** Rank objections by **agreement count**, not by how difficult they feel to answer. Comments hand you a pre-ranked list for free.

---

### 4. Comparison language
**What it is.** The dimensions on which they actually compare options — Ring 5.

**Harvest from.** "X vs Y" threads, "what do you use for…" discussions, review comparison sections, switching stories.

**Powers.** Comparison pages, positioning contrast, sales battlecards, feature prioritisation.

**Look for.** The dimension named, and the tiebreaker. The tiebreaker is rarely the headline feature.

**Example.** "Both do the job, but theirs has a Russian-language interface and support in our timezone."

**Note.** Comparison language reveals the **real** competitive set, which routinely differs from the client's list. See `jtbd-engine.md` §7.

---

### 5. Trigger language
**What it is.** How they describe the moment things changed.

**Harvest from.** Switch interviews (the backwards timeline), "we recently…", "after we…", job postings, funding announcements.

**Powers.** Timing, ad targeting, outbound hooks, seasonal campaigns.

**Look for.** Time markers and events: "после того как…", "когда у нас ушёл…", "since we moved to…", "right after the audit".

**Example.** «после того как ушёл маркетолог, всё встало» · "since the new CFO arrived, everything needs a business case"

**Why this is the highest-value type.** It converts a static list into a **queue** — you know not just who, but *when*.

---

### 6. Emotion language
**What it is.** The register. Intensity, frustration, embarrassment, relief, fear.

**Harvest from.** Anonymous venting, late-night posts, one-star reviews, unedited voice notes, the moment in an interview when they stop being professional.

**Powers.** Tone of voice, creative direction, the emotional match of the hook.

**Look for.** Profanity, hyperbole, ALL CAPS, repeated punctuation, self-deprecation, "I'm the only one who…".

**Example.** «я уже ненавижу этот отчёт» · "I dread Mondays because of this"

**The intensity rule.** **Emotional intensity is a proxy for urgency and therefore for willingness to pay.** Strip it out and you systematically underestimate how much a segment will pay. This is the most commonly destroyed signal in the entire discipline.

---

### 7. Decision-criteria language
**What it is.** The explicit and implicit rules by which they will choose.

**Harvest from.** Interviews (Ring 5), RFPs, tender requirements, "we needed something that…", procurement questionnaires.

**Powers.** Sales narrative, proof requirements, qualification questions, what to build next.

**Look for.** Hard constraints (must-haves, dealbreakers) separated from preferences.

**Example.** "It had to work without IT involvement — we don't have IT."

**Rule.** Separate **stated** criteria from **revealed** criteria. What they say matters is Ring 5; what they actually bought is `L6`. When these conflict, the transaction wins.

---

## §4 — Competitor quote-mining: free customer interviews

Competitor reviews and comments contain interviews someone else already conducted and published. Four sentence patterns extract almost everything worth having.

| Pattern | What it yields | Feeds |
|---|---|---|
| **"I bought X because…"** · «Я купил X потому что…» | The buying trigger + the winning criterion | Trigger language · Ring 1 · Ring 5 |
| **"I switched from X to Y because…"** · «Я перешёл с X на Y потому что…» | The switching trigger + the failure that caused it | The single most valuable pattern — it is a completed Four Forces case |
| **"I like X, but…"** · «Мне нравится X, но…» | The unmet need inside a satisfied customer | Differentiation opportunity · underserved outcome |
| **"I would use X if…"** · «Я бы пользовался X, если бы…» | The exact barrier blocking a willing buyer | Anxiety · a refuser (Blue Ocean Tier 2) defining itself |

### Search technique

Search these strings literally, in both languages, on G2, Capterra, Trustpilot, Reddit, marketplace reviews, app stores and Yandex Maps. Add the competitor's name. Sort by newest.

The third and fourth patterns are the most under-exploited: **"I like X, but…" and "I would use X if…" are people telling you, unprompted and in public, exactly what to build and what to say.**

### Where to look, by what you need

| You need | Source |
|---|---|
| Switching reasons, B2B software | G2, Capterra, TrustRadius |
| Consumer pain and use context | Amazon, Wildberries, Ozon reviews |
| Local service expectations | Yandex Maps, 2GIS, Google reviews |
| Mobile churn triggers | App Store, Google Play — 1★ for churn, 3★ for unmet needs |
| Unfiltered professional talk | Reddit, Telegram chats, industry forums, vc.ru comments |
| Pre-purchase objections from **non-buyers** | Marketplace "questions about the product" · comment threads |

---

## §5 — The pains-and-gains probe

For direct research, Wynter's buyer-intelligence framing produces usable answers fast: `[E]`

1. What are the top 3 **pains** of this ICP regarding [problem area]?
2. What are the top 3 **outcomes** they are trying to get?
3. **What metric is this person measured on?**
4. What are their current **priorities** — what is already on their list this quarter?

Question 3 is the highest-yield question in B2B audience research. **A person's measured metric predicts their behaviour better than their job title, their company size, or their stated preferences.** It tells you what they can defend internally, which is what actually determines whether a deal closes.

Question 4 matters because relevance is temporal: messaging lands when it maps to a priority already on the list, and bounces when it asks them to add one.

---

## §6 — The swipe file

One file per engagement. This is the deliverable that outlives the report.

```
| # | Verbatim (exact) | Type | Source | Date | Agreement | Observation | Level |
```

**Rules:**
- `Verbatim` is the raw string. Never edited. Never translated in this column.
- `Type` is one of the seven (§3).
- `Agreement` is likes, upvotes, "+1" replies, or repeat count — this is what carries a quote from `L2` to `L3`.
- `Observation` is the neutral countable statement (§2), never the interpretation.
- One row per quote. A rich quote appears in multiple rows with different types.

### Volume floor

~20–30 reviews and comments + ~10 call recordings + ~10 search queries as a first pass. `[E — RU practice]` Stop when 20 consecutive artefacts produce no new language.

**Target:** at least **5 verbatim quotes per language type per segment**. Fewer than 3 means that type is `L2` and cannot support a message decision.

---

## §7 — Cross-language handling

For RU/UA/EN engagements, this is where credibility is won or lost.

- **Never translate the swipe file.** Store every quote in its original language. Translation destroys register, idiom and intensity — precisely the signal you collected it for.
- **Formulate natively.** Copy is written in the target language from that language's quotes. A message translated from English reads as foreign and undermines the trust it was built to create.
- **Harvest per language separately.** RU and EN audiences for the same product describe the same problem in structurally different ways, and often care about different dimensions.
- **Keep RU/UA framework names local.** Хант, 5W, ABCDX with RU clients; Schwartz, JTBD, ICP with EN clients. Same mechanics, different canonical vocabulary.
- **When a quote must appear in a translated deck:** show the original, put the translation underneath in smaller type, and never the reverse.

---

## §8 — Quality gate

- [ ] Every quote stored **verbatim**, unedited, untranslated
- [ ] Every quote tagged with one of the **seven types**
- [ ] Every quote carries source, date and agreement count
- [ ] `DATA → OBSERVATION → INSIGHT → HYPOTHESIS` written out in full — **no stage skipped**
- [ ] ≥5 quotes per language type per segment (or the type is marked thin)
- [ ] All four competitor patterns searched (§4)
- [ ] Emotional intensity **preserved**, not sanitised
- [ ] Every insight carries an evidence level (`evidence-ladder.md`)
- [ ] No category nouns presented as customer language
- [ ] Client-facing copy uses **their** words, not the industry's

### The final test

Read your headline aloud to someone in the segment. **If they would not recognise it as something a person like them would say, you paraphrased.** Go back to the raw column.
