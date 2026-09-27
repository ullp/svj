# Právní případy SVJ – statická webová aplikace

Tento repozitář obsahuje samostatnou statickou HTML aplikaci pro přehled právních případů, důkazů, stavů, komentářů a pracovních poznámek.

## Spuštění lokálně

Otevřete soubor:

```text
0-data/pravni-pripady/index.html
```

nebo spusťte jednoduchý statický server z kořene repozitáře:

```bash
python3 -m http.server 8080
```

a otevřete:

```text
http://localhost:8080/0-data/pravni-pripady/
```

## Publikace na GitHub Pages

1. Inicializujte Git repozitář a nahrajte ho na GitHub.
2. V GitHubu otevřete **Settings → Pages**.
3. Zvolte deployment z větve, např. `main`, složku `/ (root)`.
4. Aplikace bude dostupná na adrese podobné:

```text
https://UZIVATEL.github.io/REPO/0-data/pravni-pripady/
```

Všechny odkazy jsou relativní, aplikace proto funguje i v podadresáři GitHub Pages.

## Profily a aktualizace od uživatelů

Aplikace je bez backendu. Na GitHub Pages tedy sama nemůže zapisovat změny do repozitáře. Změny se ukládají lokálně v prohlížeči (`localStorage`) a mezi uživateli se předávají přes JSON:

1. Uživatel vyplní **Synchronizace profilů → Jméno profilu**.
2. Provede změny v komentářích, stavech, checklistech nebo editacích.
3. Klikne na **Export celého stavu** a pošle soubor `pravni-pripady-stav.json` správci.
4. Správce nebo jiný uživatel použije **Import JSON**. Import změny slučuje:
   - komentáře podle ID,
   - stavy/checklisty/editace podle importovaného souboru,
   - historii zachová jako součást importu.

Pokud je soubor `pravni-pripady-stav.json` umístěn vedle `index.html` a aplikace běží přes HTTP(S), načte se při prvním otevření jako výchozí stav.

## Přihlášení

`login.html` poskytuje pouze lokální UI ochranu rolí v prohlížeči. Nejde o serverovou autentizaci. Veřejný GitHub repozitář ani GitHub Pages proto nepoužívejte pro citlivá neveřejná data bez dodatečné ochrany.
