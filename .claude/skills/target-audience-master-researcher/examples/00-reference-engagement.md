# Reference Engagement — a channel business, end to end

**This is the reference implementation.** It runs the current instrument set in order, on a business where the obvious audience is the wrong one. Every other example in this folder predates research passes 3–6 and should be read as a partial demonstration; this one is the standard.

**Why a channel business:** it exercises the instruments the others never touch — market definition by need, the market map with quantified leverage, buyer ≠ user, the four forces, evidence levels, TAS with sources per cell, the anti-ICP, and circle-before-square validation.

**The finding, up front:** the client's assumed audience controls roughly a quarter of the purchase decisions in their own market. The other three quarters are decided by someone they have never marketed to.

---

## The brief as received

> «Производитель систем тёплого пола. Продаём через дистрибьюторов и монтажников. ЦА — владельцы частных домов и квартир 30–55 лет, средний доход и выше, делают ремонт. Реклама в Яндексе и на маркетплейсах даёт заявки, но дорого и мало кто доходит до покупки. Нужно понять, как точнее таргетировать домовладельцев.»

*(Underfloor heating manufacturer. Sells through distributors and installers. Stated audience: homeowners aged 30–55, mid-income and above, renovating. Search and marketplace ads generate leads but expensively, with poor conversion. Wants better homeowner targeting.)*

**What the client asked for:** better targeting of homeowners.
**What the brief actually contains:** a demographic, a channel complaint, and an unexamined assumption about who decides.

---

## Step 0 — Size the pass, and ask the two intake questions

**Pass size:** one week. The client has an ad budget currently being spent badly, so the cost of a wrong answer is ongoing.

**Question 1 — the earliest broken link.** *Market boundary → where decisions happen → whose struggle → profile → words → offer → message.* The client has jumped to **message**. Nothing upstream has been established. **Start at the boundary.**

**Question 2 — will they act?** *"If this says your best audience is one you don't currently serve, will you change the product, the pricing, the sales script and the channel?"*

> Client: *«Продукт менять сложно, каталог уже свёрстан. Но скрипты, обучение и условия для партнёров — да, можем.»*

**Recorded as a scoping fact, not a footnote.** Product change is off the table; commercial terms and enablement are on it. This eliminates any recommendation whose only route to value is a product variant, and it is why §9 recommends what it does.

---

## Step 1 — Market definition by need

**The substitution test.** Not "the underfloor heating market" — that is a product category. What would this customer do instead?

| Alternative | Category |
|---|---|
| Radiators / conventional wet system | Heating |
| Underfloor heating from a competitor | Same category |
| Electric mats vs. water circuits | Adjacent technology |
| Better insulation and windows instead | **Construction, not heating** |
| Heat pump with a different distribution | **Different system entirely** |
| **Do nothing — put down a rug and wear slippers** | **Nothing** |

**Candidates come from several different categories → the boundary is at the right altitude.** `[E — abstraction test, corroborated by McDonald's market-definition rule and Osterwalder's "forget what you sell"]`

**Market defined as:** *"making a floor comfortable to stand on barefoot in a heated space, at a running cost the owner considers acceptable."*

**What that immediately changes:** insulation contractors and heat-pump installers are competitors. Neither appears anywhere in the client's competitive analysis.

**The market-share consequence.** The client quotes "около 6% рынка". Six per cent of *what*? Of electric underfloor heating in three regions — a number computed on a boundary that excludes half the real substitutes. `[L2 — client-reported, definition unverified]` **Not reused anywhere in this analysis.**

---

## Step 2 — The market map

Built from distributor sell-through data the client already had, plus twelve calls. Volumes are annual units, RU market, client's three core regions.

```
JUNCTION              VOLUME    DECIDED HERE           REMAINING
──────────────────────────────────────────────────────────────────
End customers          48,000   25%  = 12,000          75% still open
  (homeowners)

Installers             31,000   52%  = 25,000          23% still open
  (bригады, частные мастера)

Designers / architects  9,000   14%  =  6,800           9% still open

Distributors / wholesale 6,000   9%  =  4,200           0%
                                ─────────────────
                                48,000 total decided
```

**The finding, and it reframes the whole engagement:**

> **75% of purchases in this market are decided somewhere other than the end customer.** The single largest decision-making junction is the **installer**, at 52%.

`[L4 — triangulated: distributor sell-through data (behavioural) · 12 installer calls (stated) · 30 marketplace Q&A threads where buyers explicitly defer to their installer (behavioural, independent population)]`

### What the evidence actually looked like

From marketplace pre-purchase questions — people who had **not yet bought**, asking in public:

> «Мастер сказал брать [конкурент], но тут дешевле. Есть разница?»
> «Какой кабель посоветуете? Плиточник сказал что любой подойдёт»
> «Купил по совету монтажника, он с этим брендом работает»

**Three of thirty threads contained an explicit statement that the installer chose the brand.** That is `L3` on its own — one source type. It reached `L4` when the distributor data showed 52% of volume moving through installer-specified orders and the calls independently confirmed it.

### The client's reaction, recorded

> «Мы это знали. Просто никогда не считали.»

**This is the most common shape of a market-map finding.** The fact was available inside the company; nobody had quantified it, so nobody had acted on it. Passive data does not broadcast itself. `[E — Christensen, active vs passive data]`

---

## Step 3 — Where to segment

**Rule: segment at every leverage junction, not only at the end user.** `[E — McDonald]`

| Junction | Share decided | Segment here? |
|---|---|---|
| **Installers** | **52%** | **Yes — primary.** Largest, currently unaddressed |
| End customers | 25% | Yes — secondary. Already addressed, badly |
| Designers | 14% | Yes — but small and slow; deferred with a stated condition |
| Distributors | 9% | No. Price-driven, no brand preference to build |

**The client's entire marketing budget was pointed at the 25% junction.**

---

## Step 4 — JTBD on the primary junction

### The six-link chain — installers

```
When       I'm quoting a bathroom or kitchen renovation and the client
           asks about a warm floor,
and then   they ask me which brand and expect me to just know,
I struggle to  recommend confidently without risking a callback I'll have to
           service for free two winters from now,
so I want to  name one brand I've never been burned by and move the
           conversation on,
because right now  I default to whatever the wholesaler had in stock last time,
and I'll choose based on  whether it has failed on me before, whether the
           wholesaler stocks it locally, and how fast I can get a replacement
           if it does fail.
```

`[L4 — 12 installer calls · marketplace threads · a 340-message installer Telegram chat, three independent source types]`

**Note what the functional job is not.** It is not "install heating." It is **"make a recommendation I won't regret."** The client's entire product marketing addresses heating performance; the installer's job is about *reputational risk over a two-year horizon*.

### Three dimensions

| Dimension | The job |
|---|---|
| **Functional** | Specify a system that works and can be serviced locally |
| **Emotional** | Not be the person who has to come back for free in January |
| **Social** | Look competent in front of a client who is spending a lot of money and does not understand what they are buying |

The **social** dimension is doing most of the work here, and none of the client's materials address it. `[E — Osterwalder: social/emotional jobs frequently outweigh functional]`

### Four forces

```
Push    ▓▓▓▓░░░░░░  4/10   Current default works "well enough"          L3
Pull    ▓▓▓░░░░░░░  3/10   No brand has given them a reason to switch    L4
Anxiety ▓▓▓▓▓▓▓▓░░  8/10   "What if this one fails and I eat the cost?"  L4
Habit   ▓▓▓▓▓▓▓░░░  7/10   Buys what the local wholesaler stocks         L4

        Push+Pull = 7   vs   Anxiety+Habit = 15   →  NO SWITCH
        Binding constraint: ANXIETY
```

**This is the central diagnostic of the engagement.**

The client's entire budget funds **Pull** — features, performance, marketplace ads. The binding constraint is **Anxiety**, and secondarily **Habit**. Adding benefits to a message losing to fear is spending on the wrong side of an inequality. `[E — Moesta / Christensen]`

**What Anxiety-binding prescribes:** risk reversal, not more benefits. Warranty terms the installer can quote to *their* client. A replacement guarantee with a stated turnaround. Named references from installers in the same city. A failure-rate figure they can repeat.

**What Habit-binding prescribes:** local stock depth. If the wholesaler two streets away does not have it, none of the above matters.

### Supporting jobs — the transferrer role

*"What happens when you're done with it?"*

> «Если через год потечёт — кто едет? Я. Бесплатно.»

**The end-of-life job is the anxiety.** For an installer, the product's failure mode *is* their unpaid Saturday. This surfaced only because the transferrer role was asked about explicitly. `[E — Osterwalder]`

---

## Step 5 — Segment generation

12 candidates generated. Four shown; the negative-jobs and nonconsumption generators produced the two most interesting.

| # | Segment | Generator | Entry level |
|---|---|---|---|
| 1 | Installers who fear the callback | JTBD + four forces | `L4` |
| 2 | Installers who avoid quoting warm floors at all | **Negative jobs** | `L3` |
| 3 | Renovation-project managers specifying for others | Different-X (T1, T12) | `L2` |
| 4 | Homeowners already burned by a failed system | Trigger event | `L2` |

### The negative-jobs candidate — the one nobody looks for

*"What does this customer wish they did not have to do at all?"* `[E — Christensen: "negative jobs are often the best innovation opportunities"]`

> «Я вообще не берусь за тёплый пол. Слишком много мороки, а если что — виноват я.»

**Installers who decline the work entirely.** They are invisible in every dataset — no sales, no leads, no support tickets — because *nonconsumption generates no data*. `[E]`

The nonconsumption diagnostic applies directly: the client described the market as saturated. **A market looks saturated when the job has been defined poorly.** `[E — Christensen]` Sizing the *struggle* population against the *buying* population showed a gap the client had never counted.

`[L3 — 4 of 12 calls mentioned avoiding the category; corroborated in the Telegram chat; NOT yet triangulated with a behavioural source. Flagged as the primary research task.]`

---

## Step 6 — Scoring

Four columns, always together. Never a bare score.

| Segment | TAS | Gates | Evidence | Assumptions |
|---|---|---|---|---|
| **1 · Installers who fear the callback** | **4.31** | PASS | **L4** | 5/45 |
| 2 · Installers who avoid the category | 3.94 | PASS | L3 | 14/45 |
| 4 · Burned homeowners | 3.72 | PASS | L2 | 21/45 |
| 3 · Project managers | 3.55 | **FAIL — Reachability = 1** | L2 | 26/45 |

### Segment 1, worked

```
P 4 [L4: reputational + unpaid-labour cost, 12/12 calls]        0.15 × 4 = 0.60
U 3 [L3: chronic, not acute — no deadline]                      0.12 × 3 = 0.36
W 4 [L5: already pay a premium for stocked brands]              0.12 × 4 = 0.48
A 5 [L6: they buy this category weekly, professionally]         0.10 × 5 = 0.50
R 5 [L4: wholesaler counters, 3 TG chats, trade events]         0.10 × 5 = 0.50
F 4 [L3: warranty terms are ours to set — and in scope]         0.08 × 4 = 0.32
G 3 [L2: category flat; no strong signal either way]            0.08 × 3 = 0.24
L 5 [L5: specifies repeatedly, ~40+ jobs/year]                  0.07 × 5 = 0.35
C 4 [L4: competitors market to homeowners too]                  0.06 × 4 = 0.24
D 5 [L5: 52% of decisions, measured]                            0.06 × 5 = 0.30
E 4 [mean level across load-bearing claims = L4]                0.06 × 4 = 0.24
                                                                ─────────────
                                                          TAS =        4.13
```

*(Reported as 4.31 after re-scoring R and F following the second call round — the TAS moved because evidence moved, which is what it is for.)*

**Read the table correctly:**
- **Segment 3 is out despite a passing-range score** — no way to reach project managers affordably. A gate failure is a disqualification, not a deduction.
- **Segment 1 beats Segment 2 on 0.37 points but on evidence by a full level.** The gap that matters is `L4` vs `L3` and 5 assumptions vs 14.
- **Segment 4 scores respectably and is 21/45 assumptions.** That is a research plan wearing a recommendation's clothing.

---

## Step 7 — The anti-ICP

| Who to refuse | Pattern | Currently |
|---|---|---|
| **Price-led distributors buying on spot deals** | AI-1 + AI-5 — no loyalty, no LTV, trains the market to discount | ~9% of volume, ~2% of margin, sets the reference price everyone else negotiates against |

**Framed in resource terms, never as a judgement.** And with a referral: send them to the economy sub-brand rather than discounting the main line.

> The strongest argument for the anti-ICP here is not margin. It is that a system specified on price alone by a distributor, installed by whoever is cheapest, **produces the failure that creates the installer's anxiety in Segment 1.** Refusing this segment is how you protect the primary one. `[E — Christensen: signal "this is not for you" or they'll say it's a crummy product]`

---

## Step 8 — Validation plan, circle before square

**The sequencing is not optional.** If you test an offer and it fails, you cannot tell whether the offer was wrong or the audience was wrong. `[E — Osterwalder]`

| # | Tests | Hypothesis | Method | Success | Falsifies if | Cost |
|---|---|---|---|---|---|---|
| **1** | **The circle** | Anxiety, not Pull, is the binding constraint for installers | 15 structured calls: rank warranty / stock depth / price / performance by 100-point allocation | Warranty + stock > 55 of 100 combined | Price alone > 40 | Low |
| **2** | **The circle** | Segment 2 exists at scale | Count category-avoidance mentions across 3 chats + ask wholesalers what share of installers never order it | ≥15% of installers avoid the category | <5% | Low |
| 3 | The square | Risk reversal outperforms performance messaging | Two versions of the same wholesaler counter-card, split by branch | 2× enquiry rate | No difference | Low |
| 4 | The square | Installers will trade loyalty for guaranteed replacement | Offer 48-hour replacement to 20 installers, unadvertised | ≥8 specify it on the next job | ≤2 | Medium |

**Experiments 1 and 2 run first and gate the rest.** If experiment 1 comes back showing price dominance, the entire four-forces diagnosis is wrong and Step 4 must be redone before any money is spent on experiment 3.

**Declared in advance:** a result of "price > 40" reverses the primary recommendation.

---

## Step 9 — Recommendation

**Primary audience: installers who fear the callback.** `L4`, gates passed, 5 assumptions.

- **Why attractive:** 52% of decisions, measured; buys weekly; specifies 40+ times a year; reachable at wholesaler counters and in three named chats
- **Why they can pay:** they already pay a premium for locally stocked brands — `L5`, behavioural
- **Why loyal:** switching costs them reputational risk, which cuts both ways once you are the default
- **Why positioning can be strong:** every competitor markets to homeowners. **The largest decision-making junction in this market is uncontested**
- **What must be validated first:** experiment 1. The whole recommendation rests on Anxiety being the binding constraint

**Backup:** Segment 2, conditional on experiment 2 clearing 15%.

**Refuse:** price-led spot distributors.

**First experiment:** #1. **First message angle:** the replacement guarantee, phrased for the installer to repeat to *their* client. **First channel:** wholesaler counters in the three regions, because Habit is the second constraint and stock proximity is where Habit is fought.

### The trade-off, named

**Reaching installers means partially abandoning the homeowner campaign that currently produces the client's only visible leads.** Those leads are expensive and convert badly, but they are visible, and visible activity is politically easier to defend than a counter-card programme with no dashboard. **This recommendation will look like doing less for the first quarter.**

That is the actual risk in this engagement, and it is organisational, not analytical.

---

## Step 10 — Honest limitations

- **Segment 2 is `L3`, not `L4`.** It rests on stated sources only. Experiment 2 exists to fix that; until it returns, it is a hypothesis with a number attached.
- **The 25/52/14/9 split derives partly from distributor sell-through**, which reflects *ordering* behaviour, not *specification* behaviour. The two were corroborated by calls but not measured independently. Recorded as the load-bearing assumption.
- **Designers (14%) were deferred, not dismissed.** The condition for promotion is stated: if the client enters the new-build segment, designers become primary because specification there happens at design stage.
- **Product change was out of scope from intake.** Some of the strongest available moves — a genuinely different failure rate, a serviceable connector — were therefore never considered. The client should know that the recommendation is constrained by their own scoping decision, not by the market.
- **No end-customer research was done at depth.** The 25% junction was scoped out after the market map. If the channel strategy works, that decision should be revisited within a year.

---

## What this example demonstrates

| Instrument | Where |
|---|---|
| Intake question 4 — will they act? | Step 0 — and it constrained the final recommendation |
| Market definition by need, substitution test | Step 1 |
| Refusing a client's market-share figure | Step 1 |
| **Market map with quantified leverage** | Step 2 — the finding of the engagement |
| Segmenting at every junction | Step 3 |
| Six-link chain, three dimensions | Step 4 |
| **Four forces + binding constraint** | Step 4 — the diagnostic that redirects the budget |
| Transferrer role | Step 4 |
| Negative jobs + nonconsumption | Step 5 |
| Evidence levels on every claim | Throughout |
| TAS with sources per cell, four columns | Step 6 |
| Gate override on a passing score | Step 6 |
| Anti-ICP framed in resource terms | Step 7 |
| **Circle before square** | Step 8 |
| Declared falsification condition | Step 8 |
| Trade-off named | Step 9 |
| Load-bearing assumption stated | Step 10 |

**The shape to imitate:** the client asked for better targeting of the audience they assumed. The answer was that their assumed audience decides a quarter of their market. **Nothing in the brief was wrong; the brief was aimed one link too far down the chain.**
