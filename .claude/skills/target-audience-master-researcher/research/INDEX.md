# `research/` — index

**Tier 5. Consult, never read through.** Four files, ~77 000 tokens between them.
Loading one whole is almost always the wrong move: `target-audience-research-report.md`
alone is roughly 39 000 tokens and will not fit alongside an engagement.

**This file exists so you can find a section without opening a file to look for it.**

> **Already know which framework you want?** Don't come here — go straight to
> [`frameworks.md`](frameworks.md) and use its own **Quick routing table** (§ *Quick
> routing table*, at the end), which maps ~40 questions onto framework cards A1–G.
> This index routes between *files*; that table routes *inside* the framework library.

---

## Which file

| You need | File | Size | Open it when |
|---|---|---|---|
| **A framework, by name or by the question it answers** | [`frameworks.md`](frameworks.md) | ~17 600 tok | Default entry point. 48 cards, each self-contained — read the card, not the file |
| **Whether a claim is sourced, and how well** | [`source-map.md`](source-map.md) | ~20 400 tok | Before asserting anything the client could challenge, and whenever a number needs attribution |
| **A worked case, a weak→strong rewrite, or a named failure pattern** | [`examples.md`](examples.md) | ~6 300 tok | When output looks generic and you need a concrete before/after |
| **The full argument, with the reasoning that produced the method** | [`target-audience-research-report.md`](target-audience-research-report.md) | ~39 200 tok | **Rarely.** Only when the method itself is being questioned or extended. Read one `§` by heading, never the file |

**If you are running an engagement, none of these four is on the critical path.**
The knowledge layer (`../knowledge/`) is the execution layer; `research/` is why it
says what it says.

---

## `frameworks.md` — 48 cards in 7 groups

| Group | Cards | Covers |
|---|---|---|
| **A. Choosing the market** | A1–A9 | Beachhead · market types · noncustomer tiers · four criteria · attractiveness matrix · TAM/SAM/SOM · market definition + market map · micro-segments & KDF/CPI · the commoditisation diagnostic |
| **B. Understanding demand** | B1–B13 | JTBD statement · Big/Little Hire · three fallacies · ODI · four forces · Mom Test · lead users · awareness stages · Hunt's ladder (RU) · five rings · How Brands Grow (the counterweight) · CEP 7W+3C · Customer Profile · buying roles · test the circle first |
| **C. Measuring fit** | C1–C6 | PMF engine · ABCDX (RU) · four fits · B2B buying group · Van Westendorp · EVE + price segmentation |
| **D. Finding and reaching them** | D1–D6 | Bullseye + 19 channels · watering holes · trigger events · community taxonomy · ad-library archaeology · do things that don't scale |
| **E. Making the message land** | E1–E12 | Positioning · message testing · smoke tests · review mining · search intent · comment mining · VOC seven types · laddering · **EPPM (the ethics of pain messaging)** · frequency ≠ importance · two pain scores + behavioural rung · concentration/threshold/evolution |
| **F. RU-canonical** | F1–F5 | 5W Шеррингтона · Khramatrix · карта эмпатии · the RU zero-budget research stack · RU habitats |
| **G. The Evidence Ladder** | G | The protocol under everything else |

Cards are numbered, not ordered by importance. **E8–E12 were added in a later pass and
sit after F** in the file — search by card ID rather than scrolling.

---

## `source-map.md` — 13 clusters + the honest parts

| Cluster | Subject |
|---|---|
| 1 | Market & segment selection |
| 2 | JTBD & demand-side research |
| 3 | Positioning from the audience |
| 4 | PMF measurement & segmentation-by-fit |
| 5 | Channels, habitats & acquisition |
| 6 | Research methods & evidence gathering |
| 7 | Pricing, ability & willingness to pay |
| 8 | Russian-language market practice |
| 9 | JTBD depth, the buying decision, VOC, CEP, pricing |
| 10 | Systematic segmentation & market mapping (McDonald & Dunbar) |
| 11 | The Customer Profile (Osterwalder et al.) |
| 12 | Pain: root-cause discovery + the ethics of pain messaging |
| 13 | Pain economics: prioritisation, evidence grading, discovery craft |

Two sections matter more than the clusters when you are about to make a claim:

- **`## Blocked / unreachable sources`** — what could not be retrieved. If your claim
  rests on one of these, say so.
- **`## Coverage self-assessment`** — where the corpus is thin. Read before promising
  depth on a topic.

Every entry carries a reliability score (1–5) **and depth of review** (read in full /
search extract only / retrieval blocked). *Reliability is not depth* — a 5-rated source
reviewed only at search-extract level does not license a confident claim.

---

## `examples.md` — four banks

| § | Contents | Use for |
|---|---|---|
| **1.1–1.5** | Superhuman · the milkshake · Buffer & Tesla · segment pivots · lead users. Marked **[DOCUMENTED]** | The only real cases in the corpus. Safe to cite |
| **2.1–2.15** | 15 weak→strong rewrites across every business model, incl. two RU. Marked **[CONSTRUCTED]** | Fixing vague output. **2.15 is the universal repair** |
| **3.1–3.5** | Where unexpected segments hide — the unmarketed vertical, your own data, refusers, the unaddressed buying-group seat, the adjacent market | Step 6 when candidates look obvious |
| **4.1–4.9** | Failure anatomies — "everyone with this problem" · the engaged non-buyer · the unreachable perfect segment · the audience that cannot pay · persona theatre · the Product Hunt false positive · copying the competitor · research that never terminates · **narrow targeting in the wrong regime** | Self-review before delivery |

**`[DOCUMENTED]` vs `[CONSTRUCTED]` is load-bearing.** Only §1 may be presented to a
client as precedent. Everything else is an illustration, and saying otherwise is the
fastest way to lose an engagement.

---

## `target-audience-research-report.md` — read one `§` at a time

| § | Subject | Worth opening when |
|---|---|---|
| §0 | **Four laws that generate most of the rest** | The best 2 000 tokens in the file. Start here if you open it at all |
| §1 | What makes an audience "good" — 23 factors | Building or defending scoring weights |
| §2 | Types of audiences — 20 lenses | Segment generation feels stuck |
| §3 | Finding unexpected audiences — 16 generators (**3.4 disqualifies fast**) | Step 6 needs its 3 non-obvious candidates |
| §4 | Research methods — 26 | Choosing an instrument |
| §5 | The habitat atlas — 34 surfaces | Step 12 |
| §6 | Free vs paid acquisition — 19 methods | Step 13 |
| §7 | The audience scoring matrix | Where TAS comes from |
| §8 | Positioning around the audience | Step 14 |
| §9 | **Rules: how to do it, and how not to** | Second-best section. Pre-delivery review |
| §10 | The master framework | Understanding why the workflow is ordered as it is |
| Appendix | RU / EN terminology bridge | Any RU engagement |

Also `## Scope and method` at the top: what the report is and is not, and the retrieval
failures behind it. Read it before quoting the report as authority.
