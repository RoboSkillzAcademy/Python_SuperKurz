# StudyBuddy v1 (Modul 0)

Tvoj cieľ je naprogramovať **konzolovú mini-appku StudyBuddy**, ktorá vie pracovať iba s **jednou úlohou**.  
Budeš používať iba: **premenné, input/output, casting (isdigit + int), if/elif/else, while, string úpravy (strip/lower/upper)**.

---

## Čo má aplikácia vedieť (funkcie programu)
Aplikácia má mať jednoduché menu s príkazmi:

- **A** = Add (pridať / prepísať úlohu)
- **V** = View (zobraziť aktuálnu úlohu)
- **C** = Clear (vymazať úlohu)
- **H** = Help (vypísať príkazy)
- **Q** = Quit (ukončiť program)

Aplikácia pracuje len s **jednou** úlohou uloženou v premenných:
- `subject` (predmet)
- `text` (text úlohy)
- `priority` (priorita 1–5 ako číslo)
- `has_task` (True/False — či už je uložená úloha)

---

## Obmedzenia (dôležité!)
- ❌ Nepoužívaj **listy**, sety, slovníky, tuple…
- ❌ Nepoužívaj **funkcie** (`def`)
- ❌ Nepoužívaj **try/except**
- ✅ Casting priority rieš cez `isdigit()` + `int()`

---

## Krok za krokom (úlohy)

### 1) Vytvor základný súbor
1. Vytvor súbor `studybuddy_v1.py`
2. Na začiatok vypíš:
   - názov programu
   - krátku informáciu, že pracujeme s 1 úlohou
   - zoznam príkazov (A/V/C/H/Q)

---

### 2) Priprav premenné (model)
Vytvor 4 premenné s počiatočnými hodnotami:

- `has_task (boolean)`
- `subject (string)`
- `priority (integer)`
- `text (string)`

> Tip: `has_task` bude “prepínač”, či už nejaká úloha existuje.

---

### 3) Vytvor hlavný cyklus programu (menu)
Použi nekonečný cyklus:

- `while True:`
  - načítaj príkaz od používateľa
  - urob normalizáciu:
    - `strip()` (odstráni medzery)
    - `lower()` (zmení na malé písmená)

Príklad:
- používateľ zadá `"A"` → ty z toho spravíš `"a"`

---

### 4) Spracuj príkaz **A** (Add)
Keď je príkaz `"a"`:

1. Opýtaj sa na:
   - predmet (`subject_in`)
   - text úlohy (`text_in`)
   - prioritu (`priority_in`)

2. Spracovanie vstupov:
   - predmet: `strip()` + `upper()`
   - text: `strip()`
   - priorita: `strip()`

3. Validácia textu:
   - ak `text_in` je prázdny (`""`), vypíš chybu:
     - „Text úlohy nesmie byť prázdny. Úloha nebola uložená.“
   - a **neukladaj** úlohu

4. Validácia priority (bez try/except):
   - ak `priority_in.isdigit()` je True → `p = int(priority_in)`
   - inak nastav `p = 3` a vypíš:
     - „Priorita nebola číslo → nastavujem default 3.“

5. Kontrola rozsahu priority:
   - ak `p < 1` alebo `p > 5` → nastav `p = 3` a vypíš:
     - „Priorita mimo rozsah 1-5 → nastavujem default 3.“

6. Uloženie úlohy:
   - `subject = subject_in`
   - `text = text_in`
   - `priority = p`
   - `has_task = True`
   - vypíš: „Úloha uložená.“

---

### 5) Spracuj príkaz **V** (View)
Keď je príkaz `"v"`:

- ak `has_task == False`:
  - vypíš: „Nemáš uloženú žiadnu úlohu.“
- inak vypíš úlohu v peknom formáte, napr.:
```
--- Aktuálna úloha ---
Predmet: MAT
Priorita: 4/5
Text: opakovanie integrály
```

---

### 6) Spracuj príkaz **C** (Clear)
Keď je príkaz `"c"`:

- ak `has_task == False`:
  - vypíš: „Nie je čo mazať.“
- inak:
  - nastav späť “prázdny stav”:
    - `has_task = False`
    - `subject = ""`
    - `priority = 0`
    - `text = ""`
  - vypíš: „Úloha vymazaná.“

---

### 7) Spracuj príkaz **H** (Help)
Keď je príkaz `"h"`:

- vypíš zoznam príkazov (A/V/C/H/Q)

---

### 8) Spracuj príkaz **Q** (Quit)
Keď je príkaz `"q"`:

- vypíš rozlúčkovú správu a ukonči cyklus pomocou `break`

---

### 9) Spracuj neznáme príkazy
Ak príkaz nie je ani `"a"`, `"v"`, `"c"`, `"h"`, `"q"`:

- vypíš: „Neznámy príkaz. Daj H pre pomoc.“

---

## Testovací scenár (musí fungovať)
Skús tieto kroky:

1. Spusť program → zadaj `V` → má vypísať, že nemáš úlohu
2. Zadaj `A` → zadaj:
   - predmet: `mat`
   - text: `  integrály  `
   - priorita: `5`
3. Zadaj `V` → má zobraziť:
   - predmet ako `MAT` (uppercase)
   - text bez medzier na okrajoch
4. Zadaj `C` → vymaže úlohu
5. Zadaj `V` → znova hláška, že nemáš úlohu
6. Zadaj `A` a daj prioritu `abc` → musí nastaviť default 3 a upozorniť
7. Zadaj `Q` → program skončí

---

## Bonus (dobrovoľné, ak stíhaš)
- Pridaj “status” správu po každom príkaze (napr. čo sa stalo)
- Pridaj jednoduchý “DEBUG” print (zakomentovaný), ktorý ukáže typ priority_in

---

Hotovo = máš StudyBuddy v1 pripravený na ďalší modul, kde bude validácia cez cykly.