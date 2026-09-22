# SVJ U Beránky – podklady ke schůzi a právnímu zastoupení

Tento repozitář shromažďuje vše kolem jednání SVJ (schůze **24. 9. 2026**), včetně důkazů pro advokáta.
Pravidla pro přidávání a ověřování nových materiálů: [`00-pravidla/pravidla-zpracovani-svj-2026-09-24.md`](00-pravidla/pravidla-zpracovani-svj-2026-09-24.md) (§ 2 popisuje strukturu níže).

## Kde co najdu

| Složka | Obsah |
|---|---|
| [`00-pravidla/`](00-pravidla/) | **Checklist schůze** – `checklist-porada-svj.html` (otevřít v prohlížeči: checkboxy, komentáře, uložení, exporty pro datovou schránku / advokáta), jeho zdrojová MD verze a **pravidla zpracování** repozitáře |
| [`01-zapisy/`](01-zapisy/) | Zápisy ze schůzek (PDF / Google Docs), svolání shromáždění s návrhy usnesení (`.md` + zdroj `.docx`), výzva k vyhotovení zápisu, návrh bodu programu, **audio/videozáznamy schůze 27. 5. 2026** (`27. 5.*.mp3` ≈ 322 MB, `SchuzeSVJ-2026-05-27.mp3`, `ZaznamSchuzeSVJ.mp3/.mov/.aup3`), rozpracovaný zápis `SVJ meet.md`, `schuze vybaervene.pages` (zdroj k PDF) |
| [`02-dokumenty/`](02-dokumenty/) | Oficiální dokumenty: **stanovy** (`stanovy/` – vč. `SVJ stanovy 2026.pdf` a verze s připomínkami advokáta), plné moci, oznámení o neplatnosti schůze (zdroj + kopie pro odeslání), **výzvy** (`Výzva k nápravě`, `svj_vyzva_k_naprave`, `Vyzva k vraceni preplatku`), žádosti, smlouva s BD, nástěnky (PDF + text), pravidla a předávací protokol, odstoupení/zrušení členství, základní info (bankovní účet, DS, zateplení) |
| [`03-podklady-dukyzy/`](03-podklady-dukyzy/) | **Důkazy a podklady pro advokáta**: vyúčtování (`vyuctovani-2024/`, `vyuctovani-2025/` – `Scan.pdf`), potvrzení zpráv DS (`datove-schranky/`), **fotky** (`fotky/` – vč. `plany-klicek/` a `svj-fotky-2026/`), přílohy – textové zprávy (`attachments/`), analýza a návrhy ke stanovám, právní stanoviska, ceny energií, kotel, fond oprav, přepisy konverzací a poznámky |
| [`04-stiznosti/`](04-stiznosti/) | **Stížnosti**: `Stížnost na činnost Václava Hodka v rámci SVJ.pdf`, `Stiznost na SVJ pro vlastniky.pages`, `SVJ oficialni stiznost na chuzi.pages`, `Zdarzovani preplatku 2025-2026.pages`, `Zaloba - Hodek.pages`, `Hodek 10 bodu.pages`, `Sniznost a navrh na kontrolni mechanismus SVJ.pages`, `znepristupneni prostor domu.pages`, `prestupky-SVJ.txt`, `fond-oprav-stiznost.md`, kontakt PČR |
| [`x-duplicates/`](x-duplicates/) | **Starší verze a přesné kopie** (původní cesty ze smazaného `xx/`) – jen archiv, do pracovního postupu nevstupuje; nic se nemaže, jen přesouvá |
| [`tools/`](tools/) | Skripty na extrakci textu z PDF / `.pages` (`extract_pdf.py`, `extract_pages.py`, `extract_iwa.py`) |

## Rychlý start

1. **Checklist na schůzi:** otevři `00-pravidla/checklist-porada-svj.html` v prohlížeči (funguje offline). Stav (zaškrtnutí, komentáře) se ukládá do prohlížeče – průběžně používej „Zálohu JSON“.
2. **Nový materiál:** postupuj podle `00-pravidla/pravidla-zpracovani-svj-2026-09-24.md` – zařadit do správné složky, doložit zdroj, doplnit současně do MD i HTML checklistu a zapsat Changelog.
3. **Pro advokáta / datovou schránku:** z checklistu exportuj „HTML pro advokáta“ / „Tisk–PDF“, resp. `.txt` pro tělo zprávy DS.

## Poznámky

- Originální soubory se nepřepisují; pracovní poznámky patří do vlastních `.md` souborů.
- `*.gdoc` jsou odkazy na Google Docs – offline se neotevřou.
- Reorganizace 22. 9. 2026: složku `docs/` nahradila soustava `01-…`–`04-…`; dřívější `info.md` z rootu je nyní `03-podklady-dukyzy/analyza-stanov.md`.
- Reorganizace 22. 9. 2026 (2): obsah dočasného `xx/` rozřazen do `01-…`–`04-…` (60 souborů), duplicity (shodný SHA1 či starší verze téhož dokumentu dle data) přesunuty do `x-duplicates/xx/` (41 ks), smazán jen IDE odpad `stanovy/2026/.idea/`.
