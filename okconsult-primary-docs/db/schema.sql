-- =====================================================================
--  Первинка — схема БД (PostgreSQL 15+ / Supabase)
--  Виконувати зверху вниз у SQL Editor. Ідемпотентна: create if not exists.
--
--  Мультитенантність — по клієнту на обслуговуванні (clients), а не по
--  співробітнику: ОК Консалтинг веде облік кільком юрособам одночасно.
-- =====================================================================

create extension if not exists pg_trgm;      -- нечіткий пошук номенклатури й контрагентів
create extension if not exists pgcrypto;     -- gen_random_uuid()

-- ---------------------------------------------------------------- клієнти
create table if not exists clients (
  id              text primary key,                 -- 'lina', 'budal'
  name            text not null,
  edrpou          text not null,
  vat_payer       boolean not null default true,
  accounting_sys  text not null default 'bas',      -- bas | 1c83
  odata_base_url  text,                             -- https://host/lina/odata/standard.odata
  odata_user      text,                             -- логін; пароль — тільки в credentials n8n
  vchasno_account text,
  active          boolean not null default true,
  created_at      timestamptz not null default now()
);
comment on table clients is 'Юрособи на бухобслуговуванні. Одна база 1С/BAS = один рядок.';

create table if not exists users (
  id         uuid primary key default gen_random_uuid(),
  full_name  text not null,
  email      text unique not null,
  role       text not null default 'operator',      -- operator | chief | admin
  client_ids text[] not null default '{}',          -- порожній масив у chief/admin = всі клієнти
  active     boolean not null default true
);

-- ------------------------------------------------------------ контрагенти
create table if not exists counterparties (
  id           bigint generated always as identity primary key,
  client_id    text not null references clients(id),
  edrpou       text,                                -- ЄДРПОУ (8) або ІПН ФОП (10)
  name         text not null,
  name_norm    text not null,                       -- lower, без «ТОВ/ПрАТ/ФОП», без лапок і пробілів
  is_supplier  boolean not null default true,
  is_customer  boolean not null default false,
  email_docs   text,                                -- куди слати запити оригіналів і акти звірок
  vchasno_id   text,
  one_c_ref    text,                                -- GUID довідника «Контрагенти» в базі клієнта
  created_at   timestamptz not null default now(),
  created_by   text not null default 'system'       -- system | <email оператора>
);
-- Природний ключ: у межах бази клієнта ЄДРПОУ унікальний.
create unique index if not exists ux_cp_client_edrpou on counterparties (client_id, edrpou) where edrpou is not null;
create index if not exists ix_cp_name_trgm on counterparties using gin (name_norm gin_trgm_ops);

-- ------------------------------------------------------------ номенклатура
create table if not exists nomenclature (
  id          bigint generated always as identity primary key,
  client_id   text not null references clients(id),
  code_1c     text,                                 -- артикул/код у базі клієнта
  name        text not null,
  name_norm   text not null,
  unit        text,                                 -- шт, кг, меш, посл
  kind        text not null default 'goods',        -- goods | service
  vat_rate    numeric(5,2) not null default 20.00,
  acct_debit  text,                                 -- рахунок за замовчуванням: 281, 209, 92…
  one_c_ref   text,
  active      boolean not null default true
);
create unique index if not exists ux_nom_client_code on nomenclature (client_id, code_1c) where code_1c is not null;
create index if not exists ix_nom_name_trgm on nomenclature using gin (name_norm gin_trgm_ops);

-- Таблиця навчання: підтверджене людиною зіставлення «як пише постачальник» → позиція клієнта.
-- Саме вона робить систему дешевшою з кожним місяцем: наступного разу LLM не викликається.
create table if not exists nomenclature_aliases (
  id              bigint generated always as identity primary key,
  client_id       text not null references clients(id),
  counterparty_id bigint references counterparties(id),   -- null = діє для всіх постачальників
  alias_norm      text not null,
  nomenclature_id bigint not null references nomenclature(id),
  source          text not null default 'confirmed',      -- confirmed | imported
  confirmed_by    text,
  confirmed_at    timestamptz not null default now(),
  hits            int not null default 0
);
create unique index if not exists ux_alias on nomenclature_aliases (client_id, coalesce(counterparty_id, 0), alias_norm);
create index if not exists ix_alias_trgm on nomenclature_aliases using gin (alias_norm gin_trgm_ops);

-- ----------------------------------------------- правила рахунків обліку
-- Рахунок обліку — це РІШЕННЯ, тому воно живе в правилах, а не в моделі.
-- Перемога за найбільшим priority серед тих, чиї непорожні умови збіглися.
create table if not exists account_rules (
  id               bigint generated always as identity primary key,
  client_id        text not null references clients(id),
  priority         int not null default 100,
  match_doc_type   text,                            -- 'ВН' | 'Акт' | 'ПН' | null = будь-який
  match_cp_id      bigint references counterparties(id),
  match_nom_kind   text,                            -- goods | service
  match_nom_id     bigint references nomenclature(id),
  match_name_like  text,                            -- ILIKE-шаблон по найменуванню рядка
  debit_account    text not null,
  credit_account   text not null default '631',
  vat_account      text default '6442',
  cost_center      text,
  comment          text,
  active           boolean not null default true
);
create index if not exists ix_rules_client on account_rules (client_id, active, priority desc);

-- ---------------------------------------------------------------- документи
create table if not exists documents (
  id              bigint generated always as identity primary key,
  client_id       text not null references clients(id),
  source          text not null,                    -- vchasno | email | medoc | upload | manual
  source_ref      text,                             -- id документа у Вчасно / Message-ID листа
  natural_key     text not null,                    -- client|edrpou|type|number|date — ключ ідемпотентності
  direction       text not null default 'in',       -- in (від постачальника) | out
  doc_type        text not null,                    -- ВН | Акт | Рахунок | ПН | ТТН
  doc_number      text not null,
  doc_date        date not null,
  counterparty_id bigint references counterparties(id),
  currency        text not null default 'UAH',
  amount_base     numeric(14,2),                    -- без ПДВ
  amount_vat      numeric(14,2),
  amount_total    numeric(14,2),
  status          text not null default 'new',
  -- new → extracted → review → verified → posting → posted
  --                       ↘ error   ↘ snoozed   ↘ rejected
  review_reason   text,                             -- людською мовою: чому документ у черзі
  confidence      text,                             -- high | medium | low | n/a (дані з XML)
  extracted       jsonb not null default '{}',      -- сирий вихід екстрактора, для розбору інцидентів
  file_url        text,
  owner_email     text,                             -- у помилки завжди є власник
  sla_due_at      timestamptz,
  verified_by     text,
  verified_at     timestamptz,
  posted_at       timestamptz,
  one_c_ref       text,                             -- GUID створеного документа в базі клієнта
  last_error      text,
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);
create unique index if not exists ux_doc_natural on documents (natural_key);
create index if not exists ix_doc_status on documents (client_id, status, sla_due_at);
create index if not exists ix_doc_number on documents (doc_number);
create index if not exists ix_doc_date on documents (client_id, doc_date desc);

create table if not exists document_lines (
  id              bigint generated always as identity primary key,
  document_id     bigint not null references documents(id) on delete cascade,
  line_no         int not null,
  raw_name        text not null,                    -- як написано в документі постачальника
  raw_unit        text,
  qty             numeric(14,3),
  price           numeric(14,4),
  amount          numeric(14,2),
  vat_amount      numeric(14,2),
  nomenclature_id bigint references nomenclature(id),
  match_method    text,                             -- code | alias | trgm | llm | manual
  match_conf      text,                             -- exact | high | medium | low
  debit_account   text,
  credit_account  text,
  needs_review    boolean not null default false,
  candidates      jsonb,                            -- топ-3 варіанти для екрана перевірки
  unique (document_id, line_no)
);

-- ---------------------------------------------------- контроль оригіналів
create table if not exists originals (
  document_id   bigint primary key references documents(id) on delete cascade,
  required      boolean not null default true,      -- false, якщо підписано в ЕДО
  stage         text not null default 'awaiting',   -- not_required | awaiting | chased | received | filed
  due_days      int not null default 14,
  received_at   timestamptz,
  chase_count   int not null default 0,
  last_chase_at timestamptz,
  folder_ref    text,                               -- «08/2026, папка 3»
  updated_at    timestamptz not null default now()
);
create index if not exists ix_orig_stage on originals (stage, last_chase_at);

-- ------------------------------------------------------------------- банк
create table if not exists bank_transactions (
  id             bigint generated always as identity primary key,
  client_id      text not null references clients(id),
  account_iban   text not null,
  ext_id         text not null,                     -- ID транзакції з API банку — ключ дедупу
  op_date        date not null,
  op_time        time,
  amount         numeric(14,2) not null,
  direction      text not null,                     -- in | out
  cp_edrpou      text,
  cp_name        text,
  purpose        text not null,                     -- призначення платежу, сире
  parsed         jsonb,                             -- {doc_numbers:[], contract:null, vat:1240.00}
  match_document_id bigint references documents(id),
  match_method   text,                              -- rule | llm | manual
  match_conf     text,
  split          jsonb,                             -- часткова оплата за кількома документами
  status         text not null default 'new',       -- new | matched | review | unknown | posted
  one_c_ref      text,
  created_at     timestamptz not null default now()
);
create unique index if not exists ux_btx_ext on bank_transactions (client_id, ext_id);
create index if not exists ix_btx_status on bank_transactions (client_id, status, op_date desc);

-- ------------------------------------------------------------ акти звірок
create table if not exists reconciliation_acts (
  id              bigint generated always as identity primary key,
  client_id       text not null references clients(id),
  counterparty_id bigint not null references counterparties(id),
  period_from     date not null,
  period_to       date not null,
  our_balance     numeric(14,2) not null,
  their_balance   numeric(14,2),
  discrepancies   jsonb not null default '[]',      -- [{side:'us'|'them', doc, amount, note}]
  status          text not null default 'draft',    -- draft | sent | signed | disputed
  vchasno_doc_id  text,
  sent_at         timestamptz,
  signed_at       timestamptz,
  created_at      timestamptz not null default now(),
  unique (client_id, counterparty_id, period_from, period_to)
);

-- --------------------------------------------- автоматизації й спостережність
create table if not exists automations (
  key         text primary key,                     -- vchasno | email | post | bank | orig | acts
  name        text not null,
  description text not null,
  autonomy    int not null default 1,               -- 1 радить | 2 з підтвердженням | 3 сама
  enabled     boolean not null default true,
  limits      jsonb not null default '{}',
  updated_by  text,
  updated_at  timestamptz not null default now()
);

create table if not exists automation_runs (
  id            bigint generated always as identity primary key,
  automation_key text not null references automations(key),
  client_id     text references clients(id),
  trigger_mode  text not null default 'schedule',   -- schedule | webhook | manual | retry
  entity_type   text,                               -- document | bank_tx | act
  entity_id     bigint,
  entity_label  text,                               -- «РН-0004821 · ТОВ «Лінія Смаку»» — пошук ведеться по ньому
  status        text not null default 'running',    -- running | ok | fail | waiting_human | skipped_duplicate
  steps         jsonb not null default '[]',        -- [{n, title, status, io}]
  error_human   text,                               -- що впало, чому, що зробити
  error_raw     text,
  retry_of      bigint references automation_runs(id),
  idempotency_key text,
  started_at    timestamptz not null default now(),
  finished_at   timestamptz
);
create index if not exists ix_runs_label on automation_runs using gin (entity_label gin_trgm_ops);
create index if not exists ix_runs_status on automation_runs (automation_key, status, started_at desc);

-- Дії людей і автоматики в одній стрічці — інакше автоматика «як би не працює».
create table if not exists activity (
  id          bigint generated always as identity primary key,
  client_id   text references clients(id),
  entity_type text not null,
  entity_id   bigint not null,
  actor_type  text not null,                        -- human | automation
  actor_name  text not null,
  action      text not null,                        -- «створила чернетку заказу»
  basis       jsonb,                                -- {source:'email', ref:'<msgid>'}
  result      text,
  approved_by text,
  created_at  timestamptz not null default now()
);
create index if not exists ix_activity_entity on activity (entity_type, entity_id, created_at desc);

-- ---------------------------------------------------- ідемпотентність і DLQ
-- Єдина точка дедупу для всіх транспортів. Перший крок будь-якого прийому:
-- insert ... on conflict do nothing; 0 рядків = вже бачили, виходимо.
create table if not exists processed_sources (
  source      text not null,                        -- vchasno | email | medoc | bank
  external_id text not null,                        -- doc id / Message-ID / tx id
  client_id   text,
  received_at timestamptz not null default now(),
  primary key (source, external_id)
);

create table if not exists failed_events (
  id              bigint generated always as identity primary key,
  source          text not null,
  external_id     text,
  payload         jsonb not null,                   -- достатньо для повторного програвання
  error           text not null,
  attempts        int not null default 0,
  status          text not null default 'failed',   -- failed | replaying | resolved | discarded
  first_failed_at timestamptz not null default now(),
  last_attempt_at timestamptz
);
create index if not exists ix_dlq_status on failed_events (status, first_failed_at);

-- ------------------------------------------------------------- тригер updated_at
create or replace function touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;

drop trigger if exists trg_documents_touch on documents;
create trigger trg_documents_touch before update on documents
  for each row execute function touch_updated_at();

-- ------------------------------------------------------------- стартові дані
insert into automations (key, name, description, autonomy, enabled, limits) values
  ('vchasno','Приймання документів з Вчасно','Кожні 5 хв забирає нові документи, зіставляє контрагента за ЄДРПОУ й номенклатуру за кодом.',3,true,'{"max_docs_per_hour":500}'),
  ('email','Розпізнавання документів з пошти','Читає docs@, чистить цитати й підписи, витягує поля з PDF і сканів.',2,true,'{"max_attachment_mb":20}'),
  ('post','Проведення в BAS / 1С','Створює «Надходження товарів та послуг» у базі клієнта.',2,true,'{"no_posting_above":100000}'),
  ('bank','Рознесення банківської виписки','Забирає виписку, розбирає призначення платежу, зіставляє з документами.',2,true,'{}'),
  ('orig','Нагадування про оригінали','Готує лист постачальнику, якщо оригінал не надійшов у строк.',1,true,'{"max_letters_per_cp_per_week":1}'),
  ('acts','Акти звірок','Тягне обороти з бази клієнта, формує акт, показує розбіжності.',1,false,'{}')
on conflict (key) do nothing;
