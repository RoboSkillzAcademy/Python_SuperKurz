print("=== Bufetovy poradca ===")
print("Vyberie ti jedlo podla casu, rozpoctu a chuti.\n")

minutes_str = input("Kolko minut mas do hodiny? (napr. 12): ").strip()
budget_str = input("Kolko € mas? (napr. 3): ").strip()
mood_raw = input("Chut? (SLADKE/SLANE): ")

"""
TODO 1
Normalizuj mood: 
- odstran okrajove medzery
- zmen na velke pismena

mood = ...
"""

mood = "TODO"

minutes = 10
budget = 2

"""
TODO 2:
Bezpecny casting:
- if minutes_str je cislo → minutes = minutes_str typu Integer
- if budget_str je cislo → budget = budget_str typu Integer
(inak nechaj defaulty)

if ...:
    ...
if ...:
    ...
"""

print("\nDEBUG:", "minutes =", minutes, "| budget =", budget, "| mood =", mood)

"""
TODO 3:
Rozhodovanie (nastav premennu recommendation):
- if minutes <= 5 → "banan alebo tycinka"
- elif budget <= 2 → "rozok + sunka"
- else:
    - if mood == "SLADKE" → "kolac + caj"
    - elif mood == "SLANE" → "sendvic"
    - else → "voda"
"""

recommendation = "TODO"

print("\nOdporucanie:", recommendation)

"""
Bonus: 
if budget >= 5 vypis "Možes si dat aj nieco extra"

if ...:
    ...
"""