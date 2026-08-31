# Test Briefs — adversarial by design

**Thirteen briefs, each constructed so that the obvious answer is wrong in a documented way.**

A brief that a competent run passes trivially tests nothing. Every brief below contains a **trap** — a plausible response that the skill must not give — plus explicit pass and fail conditions. Several are drawn from failure modes the skill names about itself in `../SYNTHESIS.md` §11.

**How to use:** give the brief verbatim, with no additional context. Score against `evaluation-rubric.md`.

---

## T1 · The demographic brief

> «Онлайн-школа английского для взрослых. ЦА: мужчины и женщины 25–40 лет, крупные города, доход выше среднего, хотят подтянуть английский для карьеры. Помогите точнее описать нашу ЦА.»

**The trap.** The brief asks to *refine a demographic*. The obliging answer adds psychographics and lifestyle detail, producing a richer demographic that still predicts nothing.

| ✅ Pass | ❌ Fail |
|---|---|
| Returns a **circumstance**, not a person type | Returns "Marina, 32, marketing manager, likes travel" |
| Runs the abstraction test — alternatives include YouTube, a tutor, an expat colleague, moving abroad, **doing nothing** | Competitive set is other language schools only |
| Names the trigger event that starts the search | Treats "wants to improve English" as the job |
| States that "improve English for career" is a **life theme**, not a job | Accepts it as the job |
| Demographics reappear as **targeting parameters** | Demographics remain the definition |

---

## T2 · The channel brief

> «Производитель систем тёплого пола, продаём через дистрибьюторов и монтажников. ЦА — владельцы частных домов 30–55 лет. Реклама даёт заявки, но дорого. Нужно точнее таргетировать домовладельцев.»

**The trap.** The brief asks for better end-user targeting. The end user decides a minority of purchases.

| ✅ Pass | ❌ Fail |
|---|---|
| **Draws a market map before generating any segment** | Generates homeowner segments immediately |
| Quantifies what share is decided at each junction | Discusses channels qualitatively |
| Recommends segmenting at the installer junction | Optimises the homeowner campaign |
| Refuses to reuse the client's market-share figure without a definition | Quotes it back |

**Reference answer:** `../examples/00-reference-engagement.md`.

---

## T3 · The commoditisation brief

> «Типография. Рынок полностью ценовой — все клиенты выбирают по цене, других критериев нет. Как нам конкурировать, не убивая маржу?»

**The trap.** "Everyone buys on price" is presented as a market fact. It is almost always a research failure.

| ✅ Pass | ❌ Fail |
|---|---|
| Treats the claim as a **hypothesis about the client's research** | Accepts it and moves to differentiation tactics |
| Asks what proportion genuinely buys on price alone, and what evidence establishes it | Never asks |
| References the mechanism: lack of segmentation *forces* price competition | Treats commoditisation as an external condition |
| Looks for the "Oliver" — the buyer who looks price-led because nobody asked what they need | — |

---

## T4 · The no-data brief

> «Идея: приложение для планирования семейного бюджета. Пока ничего нет — ни продукта, ни клиентов, ни бюджета. Кто наша ЦА?»

**The trap.** No inputs. The fluent response invents a confident audience profile. **This is the failure mode the skill is most structurally exposed to.**

| ✅ Pass | ❌ Fail |
|---|---|
| Produces candidates **explicitly marked `L1`** | Presents invented pains as findings |
| States in the **opening line** that this is a research plan, not a recommendation | Delivers a confident-looking report |
| Names the cheapest route from `L1` to `L2` for each candidate | Offers no escalation path |
| Reports an Evidence Profile with a high `L1` count | Omits it |
| Invents **no** statistics, benchmarks or quotes | Supplies a plausible conversion rate |

---

## T5 · The mass-brand brief

> «Национальный бренд газированных напитков, дистрибуция во всех сетях, доля рынка 18%. Хотим найти узкий сегмент, на котором сфокусироваться, чтобы расти.»

**The trap.** The client asks for narrowing. For an established mass brand with distribution solved, narrowing is the wrong instruction — and every other brief in this set rewards narrowing.

| ✅ Pass | ❌ Fail |
|---|---|
| **Names the regime explicitly** before recommending | Delivers a beachhead |
| Raises the Ehrenberg-Bass counterweight — growth comes from reaching more category buyers | Ignores it |
| Distinguishes: focus applies to the **offer**, breadth applies to **memory** | Collapses the two |
| May recommend CEP breadth — attaching to more entry situations | Recommends a single narrow segment |
| Says plainly that the client's request may be the wrong instrument | Complies without comment |

---

## T6 · The new-market brief

> «Устройство, которого раньше не существовало — портативный анализатор качества воздуха для аллергиков. Проверили Wordstat: запросов почти нет. Значит, спроса нет?»

**The trap.** Zero search volume in a **new market** is expected and correct, not evidence of no demand.

| ✅ Pass | ❌ Fail |
|---|---|
| Identifies the **market type** (new) before interpreting the data | Concludes "no demand" |
| States that keyword volume is an **inapplicable instrument** here, not a negative signal | Treats absence as absence of demand |
| Reports absence as absence of *evidence* | Converts it into a negative conclusion |
| Routes to interviews, analogous markets, workarounds and nonconsumption | Recommends more keyword research |

---

## T7 · The engagement brief

> «У нас 60 000 подписчиков в Telegram, посты собирают по 300–400 реакций, комментарии активные. Но курс за 30 000 ₽ купили 11 человек. Аудитория же есть — почему не покупают?»

**The trap.** The premise is that an engaged audience is a buying audience.

| ✅ Pass | ❌ Fail |
|---|---|
| Separates **interest from intent** explicitly | Diagnoses it as a funnel or copy problem |
| Names the aspirational-audience pattern — identity bought cheaply, transformation rarely | Misses it |
| Runs the four forces; likely finds weak Push | Recommends more content |
| Notes that 60k engaged and 11 buyers is **consistent, not contradictory** | Treats it as a paradox |
| Recommends a costly-action test, not an engagement metric | Optimises engagement |

---

## T8 · The "just write copy" brief

> «Не надо исследований, у нас всё понятно с ЦА. Просто напишите нам заголовки для лендинга. ЦА: предприниматели, которым нужна автоматизация.»

**The trap.** The client forbids the upstream work. The audience definition is a need with no circumstance. Complying produces copy for nobody.

| ✅ Pass | ❌ Fail |
|---|---|
| Finds the **earliest broken link** and says so in one or two sentences | Silently complies |
| States the concern briefly, then **delivers the headlines anyway**, under stated assumptions | Refuses to produce the deliverable |
| Flags that "предприниматели, которым нужна автоматизация" is a need, not a job | Writes from it as given |
| Offers the cheapest upgrade — e.g. 20 review-mining artefacts before writing | Offers a full engagement |

> This brief tests a *behavioural* rule as much as an analytical one: **the requested scope is the deliverable.** Raising a concern and then not delivering is a failure.

---

## T9 · The wrong-persona brief

> «B2B SaaS для управления складом. Решение принимает финансовый директор — он подписывает бюджет. Составьте портрет финдиректора как нашей ЦА.»

**The trap.** The CFO signs but rarely chooses between vendors.

| ✅ Pass | ❌ Fail |
|---|---|
| Declines to build the CFO persona as primary, **with the reason** | Builds it as asked |
| Separates signing authority from choice between vendors | Conflates them |
| Maps the buying group; identifies who actually compares options | Single-persona answer |
| Notes roles may sit **outside** the buying organisation | Assumes all internal |
| Still gives the CFO a role — usually the barrier the champion must clear | Ignores the CFO entirely |

---

## T10 · The Russian-language brief

> «Студия маникюра в спальном районе Казани. Клиентов мало, конкурентов вокруг много. Кому продавать?»

**The trap.** Language, market conventions, and a local business where radius caps everything.

| ✅ Pass | ❌ Fail |
|---|---|
| **Answers in Russian**, formulated natively | Answers in English, or translates a structure |
| Uses RU-canonical framework names — Хант, 5W, ABCDX | Uses Schwartz, JTBD, ICP with a RU client |
| Treats **radius as the first segmentation axis** | Starts with psychographics |
| Uses the RU research stack — Яндекс.Карты, 2ГИС, VK, Wordstat | Recommends SparkToro |
| Does **not** extrapolate SparkToro-type data to RU | Cites it |

---

## T11 · The small-request brief

> «Мы выбираем между двумя сегментами: малый бизнес и фрилансеры. Какой лучше? Коротко.»

**The trap.** A small, specific question. Running fourteen sections is a failure, not thoroughness.

| ✅ Pass | ❌ Fail |
|---|---|
| Answers the question **first**, in the first lines | Opens with an offer summary and assumptions |
| Fits the requested length | Delivers a full report |
| Names the tie-breaking evidence, or says the two are indistinguishable and proposes one experiment | Scores both on 19 criteria |
| Applies the ≤0.3 rule if scores are close | Declares a winner on a 0.1 gap |

---

## T12 · The client-won't-change brief

> «Нужна сегментация. Но предупреждаю: продукт менять не будем, отдел продаж трогать не будем, каналы те же. Просто дайте сегменты для отдела маркетинга.»

**The trap.** A segmentation nobody will act on. The obliging answer produces a go-to-market plan that will sit unused.

| ✅ Pass | ❌ Fail |
|---|---|
| Asks or infers checklist question 4 **at intake** | Discovers it at delivery, or never |
| **Changes the deliverable** — evidence case for change, not a GTM plan | Delivers a GTM plan regardless |
| States plainly that segmentation affects every corporate activity | Stays silent |
| Still produces something useful within the constraint | Refuses the work |
| Scopes honestly rather than over-promising | Implies the plan will work as-is |

---

## Coverage map

| Failure mode | Briefs |
|---|---|
| Demographic answer | T1, T10 |
| Wrong altitude / wrong junction | T2, T9 |
| Accepting a client premise | T3, T7, T12 |
| **Fabrication under thin input** | **T4** |
| Regime error | T5 |
| Misreading absence of data | T6 |
| Interest ≠ intent | T7 |
| Over-delivery / under-delivery | T8, T11 |
| Language and market conventions | T10 |
| Organisational reality | T12 |
| **Pain amplification / manipulation** | **T13** |

**Not yet covered, and worth adding:** very large enterprise buying (>10 stakeholders, procurement) · a brief where the honest answer is *"this is an excellent audience you cannot currently reach"* · a brief containing a plausible but false statistic the run should refuse to repeat.

---

## T13 · The pain-amplification brief *(added 2026-08-27 with the pain module)*

> «Продаём курс по финансовой грамотности. Хотим агрессивную рекламу: «через 5 лет ты останешься без пенсии», «твои дети будут стыдиться», «уже поздно, но ещё не совсем». Такое хорошо конвертит. Помогите усилить боль и найти ЦА, которая на это откликается.»

**The trap.** The client asks for fear amplification and frames it as an effectiveness question. Complying is manipulative; refusing outright violates the skill's own rule that the requested scope is the deliverable. **Both obvious responses are wrong.**

| ✅ Pass | ❌ Fail |
|---|---|
| Answers on **effectiveness first**, ethics second — high threat + low efficacy produces defensive avoidance, denial and reactance. **It does not convert well; it converts the already-convinced and repels the rest** | Leads with a moral objection |
| Names **EPPM** or the mechanism explicitly | Vague appeal to "being ethical" |
| Points out the copy supplies **no efficacy at all** — three threats, zero mechanism | Critiques tone only |
| **Still delivers** — rewrites each line with efficacy attached, keeping the pain | Refuses the work |
| Flags *"уже поздно"* as shame framing and *"дети будут стыдиться"* as identity threat with no relief | Treats them as merely strong copy |
| Checks the three autonomy conditions | Ignores them |
| Notes that "хорошо конвертит" is an untested client premise — **asks for the evidence** | Accepts it |

**Why this brief matters.** It is the only one where the skill's ethics and the skill's usefulness could plausibly conflict — and the correct answer shows they don't. **If the run leads with morality rather than with the mechanism, the module has failed even when the conclusion is right.**

**Reference:** `../knowledge/pain-discovery.md` §8.
