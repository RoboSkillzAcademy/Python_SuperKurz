print("=== Study Timer Coach ===")
print("Príkazy: S=Setup, C=Check, R=Reset, H=Help, Q=Quit\n")

has_plan = False
subject = ""
minutes_goal = 0
mode = ""   # "light" alebo "hard"

while True:
    cmd = input("Zadaj príkaz (S/C/R/H/Q): ").strip().lower()

    if cmd == "h":
        print("\nS = nastav plán učenia")
        print("C = skontroluj, či si splnil plán")
        print("R = vymaž plán")
        print("Q = koniec\n")

    elif cmd == "s":
        subject_in = input("Predmet (napr. MAT): ").strip().upper()
        minutes_str = input("Koľko minút chceš dnes učiť? (napr. 25): ").strip()
        mode_raw = input("Režim (LIGHT/HARD): ")

        """
        TODO 1:
        Normalizuj mode na malé písmená a bez okrajových medzier
        mode_in = ...
        """
        mode_in = "TODO"

        m = 20

        """
        TODO 2:
        if minutes_str je číslo → m = int(minutes_str)
        (inak nechaj default 20)
        
        if ...:
            ...
        """

        if m < 10:
            print("Príliš málo — nastavujem minimum 10 min.")
            m = 10

        has_plan = True
        subject = subject_in
        minutes_goal = m
        mode = mode_in

        if mode == "hard":
            print("OK! Skús 25 min focus + 5 min pauza.")
        else:
            print("OK! Skús 15 min focus + 3 min pauza.")

        print(f"Plán: {subject} na {minutes_goal} min.\n")

    elif cmd == "c":
        if has_plan == False:
            print("\nNajprv nastav plán cez S.\n")
        else:
            real_str = input("Koľko minút si sa reálne učil? ").strip()

            """
            # TODO 3:
            # Bezpečne pretypuj real_str:
            # - if je číslo → real = int(real_str)
            # - inak real = 0
            """
            real = -1  # TODO

            if real >= minutes_goal:
                print("\nSplnené! Dobrý výkon.\n")
            else:
                missing = minutes_goal - real
                print(f"\nEšte chýba {missing} min. Skús to doraziť!\n")

    elif cmd == "r":
        has_plan = False
        subject = ""
        minutes_goal = 0
        mode = ""
        print("\nPlán vymazaný.\n")

    elif cmd == "q":
        print("\nDržím palce pri učení!")
        break

    else:
        print("\nNeznámy príkaz. Daj H pre pomoc.\n")
