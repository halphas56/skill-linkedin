# skill-linkedin

Рабочий репозиторий: Claude-скиллы и стратегические документы.

## Что здесь

| Путь | Что это |
|---|---|
| [`.claude/skills/`](.claude/skills/) | Скиллы. Claude Code подхватывает их автоматически в сессиях этого репозитория |
| [`strategy/`](strategy/) | Стратегические разборы (аутбаунд, каналы лидогенерации), `.md` + собранные `.pdf` |
| [`scripts/`](scripts/) | Утилиты репозитория |

## Скиллы

### [`target-audience-master-researcher`](.claude/skills/target-audience-master-researcher/)

Поиск целевой аудитории, которая действительно платит — включая неочевидные
сегменты. 14 knowledge-модулей, 53 карточки фреймворков, 13 тестовых брифов
под одним `SKILL.md`.

- [`SKILL.md`](.claude/skills/target-audience-master-researcher/SKILL.md) — точка входа
- [`README.md`](.claude/skills/target-audience-master-researcher/README.md) — что скилл делает и как он собирался
- [`ANALYSIS.md`](.claude/skills/target-audience-master-researcher/ANALYSIS.md) — аудит упаковки и что осталось доделать

## Проверка скиллов

После любой правки скилла:

```bash
python3 scripts/validate-skills.py
```

Проверяет то, что ломается молча: лимит `description` в 1024 символа (за ним
хвост обрезается вместе с триггерами), валидность фронтматтера, битые
относительные ссылки, вернувшиеся CRLF — и **числа, которыми скилл описывает
сам себя**. Последнее не паранойя: три таких числа уже разошлись с
действительностью, пока скилл дорастал проходами. Ненулевой код возврата = есть
ошибки; предупреждения прогон не валят.

Новое счётное утверждение в скилле → строка в `COUNT_CHECKS` внутри скрипта.

## Утилиты

| Скрипт | Назначение |
|---|---|
| [`scripts/validate-skills.py`](scripts/validate-skills.py) | Валидация скиллов (выше) |
| [`scripts/strategy-md2pdf.py`](scripts/strategy-md2pdf.py) | `strategy/*.md` → PDF (WeasyPrint) |

Внутри скилла есть свой, другой конвертер —
[`tools/md2pdf.py`](.claude/skills/target-audience-master-researcher/tools/md2pdf.py)
(headless Chrome, обложка, оглавление, нумерация страниц). Это не дубль:
у них разные движки и разное назначение.
