# StudyBuddy v2

## Príkazy programu

| Príkaz | Popis |
|--------|-------|
| A | Pridaj úlohu (Add) |
| V | Zobraz aktuálnu úlohu (View) |
| C | Vymaž úlohu (Clear) |
| SP | Hľadaj podľa predmetu (Search Predmet) |
| ST | Hľadaj podľa slova v texte (Search Text) |
| H | Pomoc (Help) |
| Q | Koniec (Quit) |

---

## Model — premenné programu

Rovnaké štyri premenné ako vo v1:

```python
has_task = False
subject  = ""
priority = 0
text     = ""
```

`has_task` je prepínač — hovorí programu, či už nejaká úloha existuje.

---

## Úlohy — čo treba doplniť

### TO-DO 1 — while validácia priority

Nachádza sa vo vetve `cmd == "a"`, po načítaní predmetu a textu.

Cieľ: opýtaj sa na prioritu opakovane, kým používateľ nezadá platné číslo od 1 do 5.

Pravidlá:
- Použi `while True` s `break` pri správnom vstupe.
- Vstup skontroluj cez `isdigit()` — overí, či je to vôbec číslo.
- Potom skontroluj rozsah: `p >= 1 and p <= 5`.
- Ak vstup nie je platný, vypíš upozornenie a opakuj.
- Nepoužívaj `try/except`.

Postup:
1. Nastav `p = 0` pred cyklom.
2. V cykle načítaj vstup, normalizuj cez `.strip()`.
3. Ak `isdigit()` a rozsah OK — ulož do `p` a volaj `break`.
4. Inak vypíš správu a pokračuj v cykle.

---

### TO-DO 2 — while vyhľadávanie podľa predmetu

Nachádza sa vo vetve `cmd == "sp"`.

Cieľ: opakuj sa, kým používateľ nezadá "stop". Pre každý vstup porovnaj s uloženým predmetom.

Pravidlá:
- Normalizuj vstup cez `.strip().upper()` — predmet je vždy uložený ako veľké písmená.
- Porovnaj `query == subject`.
- Ak zhoda — vypíš úlohu.
- Ak nie — vypíš, že predmet sa nezhoduje.
- Ukonči cyklus keď `query == "STOP"`.

Postup:
1. Spusti `while True`.
2. Načítaj vstup, normalizuj na `UPPER`.
3. Ak je vstup `"STOP"` — `break`.
4. Inak porovnaj a vypíš výsledok.

---

### TO-DO 3 — while vyhľadávanie podľa slova v texte

Nachádza sa vo vetve `cmd == "st"`.

Cieľ: opakuj sa, kým používateľ nezadá "stop". Pre každý vstup hľadaj slovo v texte úlohy.

Pravidlá:
- Normalizuj keyword cez `.strip().lower()`.
- Hľadaj pomocou operátora `in`: `keyword in text.lower()`.
- Ak nájdeš — vypíš text úlohy.
- Ak nie — vypíš, že slovo sa nenašlo.
- Ukonči cyklus keď `keyword == "stop"`.

Postup:
1. Spusti `while True`.
2. Načítaj vstup, normalizuj na `lower`.
3. Ak je vstup `"stop"` — `break`.
4. Inak použi `in` a vypíš výsledok.

---

## Testovací scenár

Spusti program a vyskúšaj tieto kroky v poradí:

1. Zadaj `A` — predmet `mat`, text `opakovanie integralov`, priorita `abc` — program sa má opýtať znova.
2. Zadaj prioritu `0` — program sa má opýtať znova.
3. Zadaj prioritu `3` — úloha sa uloží.
4. Zadaj `V` — úloha sa zobrazí s predmetom `MAT` a prioritou `3/5`.
5. Zadaj `SP` — hľadaj `mat` — má nájsť. Hľadaj `bio` — nemá nájsť. Zadaj `stop`.
6. Zadaj `ST` — hľadaj `integra` — má nájsť (čiastočná zhoda cez `in`). Zadaj `stop`.
7. Zadaj `C` — úloha sa vymaže.
8. Zadaj `SP` — program oznámi, že nie je čo hľadať.
9. Zadaj `Q` — program skončí.

---

## Čo je nové oproti v1

| Funkcia | v1 | v2 |
|---------|----|----|
| Pridanie úlohy | áno | áno |
| Validácia priority | len default 3 | while cyklus, opakuje sa |
| Zobrazenie úlohy | áno | áno |
| Vymazanie úlohy | áno | áno |
| Hľadanie podľa predmetu | nie | áno, while + upper |
| Hľadanie podľa textu | nie | áno, while + in + lower |