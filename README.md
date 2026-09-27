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

## Profily a automatická databázová synchronizace

Aplikace zůstává statická a funguje na GitHub Pages bez vlastního serveru. Sdílená „databáze“ je JSON soubor `0-data/pravni-pripady/pravni-pripady-stav.json` uložený přímo v GitHub repozitáři. Web ho čte a zapisuje přes GitHub Contents API, takže po dokončení editace se změny automaticky sloučí a uloží pro ostatní profily.

Postup nastavení v prohlížeči každého uživatele, který má zapisovat:

1. V GitHubu vytvořte **fine-grained personal access token** pro tento repozitář s oprávněním **Contents: Read and write**.
2. Přihlaste se do aplikace a otevřete **Databáze → Nastavit GitHub DB**.
3. Vyplňte vlastníka repozitáře, název repozitáře, větev (`main`), cestu `0-data/pravni-pripady/pravni-pripady-stav.json` a token.
4. Od této chvíle aplikace při otevření načítá sdílený stav a při uložení komentářů, stavů, checklistů, editací a historie spouští automatickou synchronizaci. Ruční export/import už není potřeba.

Synchronizace před zápisem vždy načte aktuální soubor z GitHubu, sloučí ho s lokálními změnami a při konfliktu zápisu (`409 Conflict`) provede nové načtení a opakuje zápis až třikrát. V horní liště se zobrazuje stav: lokální režim, čekající změna, synchronizace, úspěch nebo chyba.

Token se ukládá pouze lokálně do `localStorage` daného prohlížeče. Pokud GitHub databáze není nastavena, aplikace dál funguje lokálně a při prvním otevření přes HTTP(S) načte výchozí soubor `pravni-pripady-stav.json`.

## Přihlášení

`login.html` poskytuje pouze lokální UI ochranu rolí v prohlížeči. Nejde o serverovou autentizaci. Veřejný GitHub repozitář ani GitHub Pages proto nepoužívejte pro citlivá neveřejná data bez dodatečné ochrany.
