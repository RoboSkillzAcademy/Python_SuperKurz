print("=== StudyBuddy v1 (Modul 0) ===")

has_task = False
subject = ""
priority = 0
text = ""

print("Prikazy: A=Add, V=View, C=Clear, H=Help, Q=Quit\n")

while True:
    cmd = input("Zadaj prikaz (A/V/C/H/Q): ").strip().lower()

# ----------- ADD -----------
    if cmd == "a":
        print("\n--- Pridanie ulohy ---")
        subject_in = input("Predmet (napr. MAT): ").strip().upper()
        text_in = input("Text ulohy: ").strip()
        priority_in = input("Priorita (1-5): ").strip()

        if text_in == "":
            print("Text ulohy nesmie byt prazdny. Uloha nebola ulozena.\n")
        else:
            if priority_in.isdigit():
                p = int(priority_in)
            else:
                p = 3
                print("Priorita nebola cislo → nastavujem default 3.")

            if p < 1 or p > 5:
                p = 3
                print("Priorita mimo rozsah 1-5 → nastavujem default 3.")

            subject = subject_in
            text = text_in
            priority = p
            has_task = True

            print("Uloha ulozena.\n")

# ----------- VIEW -----------
    elif cmd == "v":
        if has_task == False:
            print("\nNemas ulozenu ziadnu ulohu.\n")
        else:
            print("\n--- Aktualna uloha ---")
            print("Predmet: ", subject)
            print("Priorita:", str(priority) + "/5")
            print("Text:    ", text, "\n")

# ----------- CLEAR -----------
    elif cmd == "c":
        if has_task == False:
            print("\nNie je co mazat (ziadna uloha ulozena).\n")
        else:
            has_task = False
            subject = ""
            priority = 0
            text = ""
            print("\nUloha vymazana.\n")

# ----------- HELP -----------
    elif cmd == "h":
        print("\nPrikazy:")
        print("  A = Add (pridat / prepisat ulohu)")
        print("  V = View (zobrazit aktualnu ulohu)")
        print("  C = Clear (vymazat ulohu)")
        print("  H = Help")
        print("  Q = Quit\n")

# ----------- QUIT -----------
    elif cmd == "q":
        print("\nAhoj! StudyBuddy konci.")
        break

    else:
        print("\nNeznamy prikaz. Daj H pre pomoc.\n")
