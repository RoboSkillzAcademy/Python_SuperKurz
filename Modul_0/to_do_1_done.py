print("=== Bufetový poradca ===")
print("Vyberie ti jedlo podľa času, rozpočtu a chuti.\n")

minutes_str = input("Kolko minut mas do hodiny? (napr. 12): ").strip()
budget_str = input("Kolko € mas? (napr. 3): ").strip()
mood_raw = input("Chut? (SLADKE/SLANE): ")

# TO-DO 1 (DONE): normalizacia mood
mood = mood_raw.strip().upper()

minutes = 10
budget = 2

# TO-DO 2 (DONE): bezpecny casting
if minutes_str.isdigit():
    minutes = int(minutes_str)

if budget_str.isdigit():
    budget = int(budget_str)

print("\nDEBUG:", "minutes =", minutes, "| budget =", budget, "| mood =", mood)

# TO-DO 3 (DONE): rozhodovanie
if minutes <= 5:
    recommendation = "banan alebo tycinka"
elif budget <= 2:
    recommendation = "rozok + sunka"
else:
    if mood == "SLADKE":
        recommendation = "kolac + caj"
    elif mood == "SLANE":
        recommendation = "sendvic"
    else:
        recommendation = "voda"

print("\nOdporucanie:", recommendation)

# Bonus (DONE)
if budget >= 5:
    print("Možes si dat aj nieco extra")
