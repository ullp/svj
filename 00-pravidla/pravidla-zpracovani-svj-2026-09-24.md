# Pravidla dalšího zpracování a přidávání materiálů pro schůzi SVJ U Beránky – 24. 9. 2026

Autor: Petr Ullmann
Datum: 22. 9. 2026
Verze: 1.0

---

## 1. Účel a rozsah

Tento dokument stanoví **pravidla práce s podklady** pro schůzi SVJ U Beránky (24. 9. 2026):

- jak ověřovat a zařazovat nové materiály,
- jak je doplňovat do checklistu (`checklist-porada-svj.md` / `checklist-porada-svj.html`),
- jak postupovat před, během a po schůzi,
- jak komunikovat přes datovou schránku (DS) a s advokátním zastoupením.

Cílem je, aby každý bod checklistu byl **doložený, ověřitelný a právně podložený** a aby žádný materiál nepřišel o vazbu na zdroj (důkaz).

## 2. Struktura repozitáře a pojmenování

- Struktura repozitáře (detail v `README.md`): `00-pravidla/` – pravidla a checklist, `01-zapisy/` – zápisy a nahrávky, `02-dokumenty/` – oficiální dokumenty (vč. `stanovy/`, plných mocí, oznámení a výzev), `03-podklady-dukazy/` – důkazy pro advokáta (vč. `vyuctovani-2024/`, `vyuctovani-2025/`, `datove-schranky/`, `attachments/`, `fotky/`), `04-stiznosti/` – stížnosti, `x-duplicates/` – starší verze a přesné kopie (archiv, nevstupuje do postupu), `tools/` – nástroje.
- **Originální dokumenty se nikdy nepřepisují.** Pracovní poznámky se ukládají do samostatných `.md` souborů.
- Nové soubory pojmenovávat ve tvaru `YYYY-MM-DD-popis.obsah` (např. `2026-09-23 vyuctovani-teplo-kalkulace.pdf`). Existující soubory si ponechávají původní jména (dokumentovaná výjimka, dokud nedojde k jednorázovému přejmenování).
- Každý nový soubor uvést v Changelogu tohoto dokumentu (datum, název, zdroj, čím byl doložen).
- Odezílat podklady přes `tools/extract_pdf.py`, `tools/extract_pages.py` – extrakci vždy označit jako „pracovní opis, ověřit proti originálu“.

## 3. Povinné náležitosti nového bodu checklistu

Každý nový bod musí obsahovat všech pět částí (jinak bod není zařazen):

1. **Faktický popis** – co se stalo, s částkami, daty, ID zpráv DS, jmény.
2. **Podklady (důkazy)** – přesná cesta k souboru od rootu repozitáře (např. `01-zapisy/…pdf`, strana/případně ID zprávy DS).
3. **Právní rámec** – konkrétní ustanovení (§ … OZ) se stavem ověření: `ověřeno (kdy/kým)` nebo `ke ověření – Mgr. Panuška`.
4. **Požadavek / návrh usnesení** – formulace, kterou lze na schůzi předložit (splnitelná, s lhůtou).
5. **Priorita**: 🔴 vysoká / nosný bod, 🟠 střední, 🟡 doprovodné.

Šablona zápisu do MD:

```markdown
- [ ] **<Stručný název / požadavek>:** <popis vč. částek, dat, ID zpráv>.
  - **Podklady:** `03-podklady-dukazy/…` (datum, strana / ID zprávy DS)
  - **Právní rámec:** § … OZ (ověřeno dne … / ke ověření)
  - **Požadavek:** <formulace usnesení + lhůta>
  - **Priorita:** 🔴
```

Odpovídající zápis do HTML (`00-pravidla/checklist-porada-svj.html`, pole `items` příslušné sekce v `SECTIONS`):

```js
// sekce s id "A" …
items:[
  {t:"…existující položky…"},
  {t:"<b>Titulek / požadavek:</b> popis … <em>(Podklady: 03-podklady-dukazy/…; Právní rámec: § … OZ)</em>"}
]
```

## 4. Ověřovací workflow (5 kroků)

1. **Zařazení** – přidávat pouze materiály s doloženým zdrojem (originál, oficiální kopie, potvrzení o doručení DS). Nepotvrzená tvrzení označit jako „nezjištěno“ a nezařazovat jako fakt.
2. **Kontrola čísel** – částky z vyúčtování (bod D: SLUŽBY obj. 4, GARÁŽ obj. 704) vždy přepočítat proti PDF a uvést zdroj; počítat s přeplatky 58 548 Kč a zadrženými 27 000 Kč.
3. **Právní kontrola** – právní odkazy před jednáním konzultovat s advokátem (Mgr. Martin Panuška, CAK 13030; plná moc `02-dokumenty/PlnaMoc.pdf` z 18. 5. 2026, jednotky 2140/9 a 2140/12). Další kontakty: Lucie Pražáková / bytovadruzstva.cz dle `03-podklady-dukazy/Kata info.md`.
4. **Zapracování** – nový bod přidat **souběžně do MD i HTML** (oba soubory musí zůstat obsahově totožné) a zapsat Changelog (níže).
5. **Předání** – alespoň 1 den před schůzí (do 23. 9. 2026) vygenerovat export pro advokáta (HTML/PDF) a vytisknout pracovní kopii.

## 5. Časový režim kolem schůze 24. 9. 2026

### Před schůzí (22.–23. 9. 2026)
- Doplnit chybějící podklady (kalkulace záloh, vyúčtování, zápis 27. 5. 2026, potvrzení PDZ z 29. 5. 2026).
- Projít checklist v HTML, zaškrtnout, co je připraveno, ke každému bodu doplnit komentář „co přednést“.
- Vyexportovat pro advokáta a vytisknout 2 kopie (jedna pro vedení schůze, jedna pro zapisovatele).

### Během schůze (24. 9. 2026)
- Checklist používat jako živý záznam: zaškrtávat projednané body a **do komentářů zaznamenávat**: kdo bod přednesl, reakci výboru, výsledek hlasování (počet PRO/PROTI/ZDRŽEL) a domluvené lhůty.
- Ověřit vždy: program a jeho schválení, usnášeníschopnost, kdo schůzi vede (funkce předsedy – viz bod B/D), zda jsou k bodům předloženy podklady, složení komise pro sčítání hlasů.
- Trvat na zařazení bodů A–I z checklistu; nesouhlas či námitku zaznamenat jmenně do komentáře a požadat zápis do zápisu.

### Po schůzi (do 8. 10. 2026)
- Do 3 dnů: doplnit checklist, vygenerovat TXT export pro DS a HTML/PDF pro advokáta, archivovat zálohu JSON.
- Připomínky k zápisu uplatnit písemně ve lhůtě (14 dnů dle checklistu), nápravy vymáhat s lhůtami z návrhů usnesení (15 / 30 / 60 dnů).
- Zkontrolovat, zda výbor odpověděl na podání přes DS do 30 dnů (§ 1208, § 1209 OZ); při prodlení připravit výzvu.

## 6. Pravidla komunikace přes datovou schránku

- Každé podání zaevidovat: **věc, datum odeslání, ID zprávy, potvrzení o doručení (PDZ)** – ukládat do `03-podklady-dukazy/datove-schranky/` (viz vzor `03-podklady-dukazy/datove-schranky/Datové schránky.pdf`).
- Text zprávy připravit exportem **„Export pro datovou schránku (.txt)“** z HTML checklistu (vložit do těla zprávy, případně přiložit i jako přílohu); právní podání vždy jako **PDF z tisku** („Tisk / uložit jako PDF“).
- Ponechávat kopii každé odeslané zprávy a lhůtu na odpověď si poznamenat do komentáře příslušného bodu.
- Na nezodpovězená podání (6 ks dle checklistu) upozornit výbor i advokáta; po 30 dnech eskalovat.

## 7. Pravidla právní jistoty

- Nic nepodepisovat ani neuznávat bez projednání s advokátem; návrhy usnesení předem přeposlat k revizi.
- Právní vady stanov (§ 1169 OZ, náhradní shromáždění, per rollam, hlasování mimo program) vždy uvádět jako **právní námitku do zápisu**, ne jen jako diskusní připomínku.
- Tvrzení z `.pages` a extrahovaných opisů označovat jako neověřená do doby, než je potvrdí originál nebo druhá strana.

## 8. Verzování a Changelog

- MD i HTML držet obsahově totožné; změnu zapsat do Changelogu níže (datum, autor, co se změnilo, zdroj).
- HTML checklist obsahuje stavové ukládání v prohlížeči – průběžně používat „Záloha JSON“ (soubor přejmenovat na `checklist-stav-YYYY-MM-DD.json`).
- Při přidání bodu aktualizovat číslování sekcí jen na konci (A–I jsou stabilní), nové sekce označovat od **J** výše.

## 9. Role a kontakty

| Role | Kontakt / poznámka |
|---|---|
| Správce repozitáře a checklistu | Petr Ullmann |
| Advokátní zastoupení | Mgr. Martin Panuška, CAK 13030 – `02-dokumenty/PlnaMoc.pdf` (18. 5. 2026) |
| Konzultace problematiky SVJ | Lucie Pražáková, bytovadruzstva.cz (dle `03-podklady-dukazy/Kata info.md`) |
| Polic ČR (konzultace vydírání) | `orp1.mop.vokovice.podatelna@pcr.cz` (dle `04-stiznosti/policie.md`) |

## 10. Minimální checklist ověření během schůze

1. Program schůze a zařazení bodů A–I.
2. Usnášeníschopnost a ověření, kdo schůzi řídí (platnost funkce předsedy).
3. Předložení podkladů k hlasovaným bodům (smlouvy, kalkulace, ceníky).
4. Průběh hlasování – výsledek zapsat do komentářů.
5. Námitky k neplatnosti schůze 27. 5. 2026 a anulaci hlasování.
6. Lhůty a povinnosti výboru (DS 30 dnů, dokumenty 15 dnů, oprava zápisu).
7. Zda byl pořízen zápis a kdo jej vyhotoví.

---

## Changelog

| Datum | Autor | Změna | Zdroj |
|---|---|---|---|
| 22. 9. 2026 | P. Ullmann | Vznik dokumentu (verze 1.0) | `checklist-porada-svj.md`, `info.md` |
| 22. 9. 2026 | P. Ullmann | Reorganizace repozitáře: `docs/` → `00-pravidla/`–`04-stiznosti/`, aktualizace všech cest; `info.md` → `03-podklady-dukazy/analyza-stanov.md` (detail v `README.md`) | `README.md` |
| 22. 9. 2026 | P. Ullmann | Dohledání podkladů z `xx/`: 60 souborů zařazeno do `01-…`–`04-…`, 41 duplicit (shodný SHA1 / starší verze dle data) → `x-duplicates/xx/`, smazán jen IDE odpad `.idea/`; ověřeno SHA1 a existencí cest | import `xx/` |
