print("=== StudyBuddy v1 (Modul 0) ===")
print("Pracujeme len s JEDNOU úlohou (bez listov).")
print("Zatiaľ bez funkcií a bez try/except.\n")

has_task = False
subject = ""
priority = 0
text = ""

print("Príkazy: A=Add, V=View, C=Clear, H=Help, Q=Quit\n")

while True:
    cmd = input("Zadaj príkaz (A/V/C/H/Q): ").strip().lower()

# ----------- ADD -----------
    if cmd == "a":
        print("\n--- Pridanie úlohy ---")
        subject_in = input("Predmet (napr. MAT): ").strip().upper()
        text_in = input("Text úlohy: ").strip()
        priority_in = input("Priorita (1-5): ").strip()

        if text_in == "":
            print("Text úlohy nesmie byť prázdny. Úloha nebola uložená.\n")
        else:
            if priority_in.isdigit():
                p = int(priority_in)
            else:
                p = 3
                print("Priorita nebola číslo → nastavujem default 3.")

            if p < 1 or p > 5:
                p = 3
                print("Priorita mimo rozsah 1-5 → nastavujem default 3.")

            subject = subject_in
            text = text_in
            priority = p
            has_task = True

            print("Úloha uložená.\n")

# ----------- VIEW -----------
    elif cmd == "v":
        if has_task == False:
            print("\nNemáš uloženú žiadnu úlohu.\n")
        else:
            print("\n--- Aktuálna úloha ---")
            print("Predmet: ", subject)
            print("Priorita:", str(priority) + "/5")
            print("Text:    ", text, "\n")

# ----------- CLEAR -----------
    elif cmd == "c":
        if has_task == False:
            print("\nNie je čo mazať (žiadna úloha uložená).\n")
        else:
            has_task = False
            subject = ""
            priority = 0
            text = ""
            print("\nÚloha vymazaná.\n")

# ----------- HELP -----------
    elif cmd == "h":
        print("\nPríkazy:")
        print("  A = Add (pridať / prepísať úlohu)")
        print("  V = View (zobraziť aktuálnu úlohu)")
        print("  C = Clear (vymazať úlohu)")
        print("  H = Help")
        print("  Q = Quit\n")

# ----------- QUIT -----------
    elif cmd == "q":
        print("\nAhoj! StudyBuddy končí.")
        break

    else:
        print("\nNeznámy príkaz. Daj H pre pomoc.\n")
