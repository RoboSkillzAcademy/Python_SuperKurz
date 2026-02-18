print("=== Bufetový poradca ===")
print("Vyberie ti jedlo podľa času, rozpočtu a chuti.\n")

minutes_str = input("Koľko minút máš do hodiny? (napr. 12): ").strip()
budget_str = input("Koľko € máš? (napr. 3): ").strip()
mood_raw = input("Chuť? (SLADKE/SLANE): ")

"""
TODO 1
Normalizuj mood: 
- odstráň okrajové medzery
- zmeň na veľké písmená

mood = ...
"""

mood = "TODO"

minutes = 10
budget = 2

"""
TODO 2:
Bezpečný casting:
- if minutes_str je číslo → minutes = minutes_str typu Integer
- if budget_str je číslo → budget = budget_str typu Integer
(inak nechaj defaulty)

if ...:
    ...
if ...:
    ...
"""

print("\nDEBUG:", "minutes =", minutes, "| budget =", budget, "| mood =", mood)

"""
TODO 3:
Rozhodovanie (nastav premennú recommendation):
- if minutes <= 5 → "banán alebo tyčinka"
- elif budget <= 2 → "rožok + šunka"
- else:
    - if mood == "SLADKE" → "koláč + čaj"
    - elif mood == "SLANE" → "sendvič"
    - else → "voda"
"""

recommendation = "TODO"

print("\nOdporúčanie:", recommendation)

"""
Bonus: 
if budget >= 5 vypíš "Môžeš si dať aj niečo extra"

if ...:
    ...
"""