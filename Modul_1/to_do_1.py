# to_do_1.py
# Modul 1 — Kontrolór rozvrhu (bez listov, bez funkcií, bez try/except)
# Témy: while (validácia vstupu), for (prehľad), in + .lower() (vyhľadávanie)

print("=== Kontrolór rozvrhu ===")
print("Zadaj predmety dnešného dňa a program ich skontroluje.\n")

# Predpripravené dáta — rozvrh v jednom stringu (oddelené čiarkou)
# Toto je zámerné: budete prechádzať cez ne cez for
schedule_raw = "matematika,biologia,anglictina,fyzika,slovenčina"
schedule_str = schedule_raw.lower()   # normalizácia raz pre všetky

print("Dnešný rozvrh (interný záznam):", schedule_raw)
print()

# -------------------------------------------------------
# ČASŤ 1: Validovaný vstup — počet hodín dnes (1–10)
# -------------------------------------------------------

lessons_count = 0

# TO-DO 1 (3–5 riadkov):
# Opýtaj sa používateľa na počet hodín dnes.
# Použi while cyklus, ktorý sa opakuje, kým nie je vstup platný:
# - musí byť číslo (isdigit)
# - musí byť v rozsahu 1 až 10
# Keď je vstup OK, ukonči cyklus.
# (Použi break alebo podmienku priamo v while)
#
# while ...:
#     raw = input("Koľko hodín máš dnes? (1–10): ").strip()
#     if ...:
#         lessons_count = int(raw)
#         if ...:
#             ...
#             break
#     print("Neplatný vstup. Skús znova.")
pass  # toto zmaž keď dopíšeš TO-DO 1

print(f"\nDnes máš {lessons_count} hodín.\n")

# -------------------------------------------------------
# ČASŤ 2: Vyhľadávanie predmetu (while + in + .lower())
# -------------------------------------------------------

print("--- Hľadanie v rozvrhu ---")

# TO-DO 2 (4–6 riadkov):
# Opýtaj sa používateľa na predmet, ktorý chce nájsť.
# Cyklus nech beží, kým používateľ nezadá "stop".
# Pre každý zadaný predmet:
# - normalizuj vstup: strip + lower
# - ak sa predmet nachádza v schedule_str (použi: in) → vypíš "<predmet> je v rozvrhu"
# - inak → vypíš "<predmet> NIE je v rozvrhu"
#
# while True:
#     query_raw = input("Hľadaj predmet (alebo 'stop'): ")
#     query = ...
#     if query == "stop":
#         break
#     if ... in ...:
#         print(...)
#     else:
#         print(...)
pass  # toto zmaž keď dopíšeš TO-DO 2

# -------------------------------------------------------
# ČASŤ 3: Prehľad — vypíš všetky predmety (for cyklus)
# -------------------------------------------------------

print("\n--- Predmety v dnešnom rozvrhu ---")

# Predpripravená pomôcka: rozdelenie stringu na časti
subjects_list_raw = schedule_str.split(",")   # toto je len technická pomôcka, nie "náš list dát"

# TO-DO 3 (3–4 riadky):
# Prechádzaj cez subjects_list_raw pomocou for cyklu.
# Pre každý predmet vypíš riadok vo formáte:
#   "  - Matematika"  (prvé písmeno veľké — použi .capitalize())
# Nakoniec vypíš celkový počet predmetov (použi premennú counter, ktorú
# zvyšuješ v cykle — BEZ len())
#
# counter = 0
# for subj in subjects_list_raw:
#     print(...)
#     counter = counter + 1
# print("Celkom predmetov:", ...)
pass  # toto zmaž keď dopíšeš TO-DO 3

print("\nHotovo!")