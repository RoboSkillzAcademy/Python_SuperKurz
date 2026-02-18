print("=== Study Timer Coach ===")
print("Prikazy: S=Setup, C=Check, R=Reset, H=Help, Q=Quit\n")

has_plan = False
subject = ""
minutes_goal = 0
mode = ""   # "light" alebo "hard"

while True:
    cmd = input("Zadaj prikaz (S/C/R/H/Q): ").strip().lower()

    if cmd == "h":
        print("\nS = nastav plan ucenia")
        print("C = skontroluj, ci si splnil plan")
        print("R = vymaz plan")
        print("Q = koniec\n")

    elif cmd == "s":
        subject_in = input("Predmet (napr. MAT): ").strip().upper()
        minutes_str = input("Kolko minut chces dnes ucit? (napr. 25): ").strip()
        mode_raw = input("Rezim (LIGHT/HARD): ")

        """
        TODO 1:
        Normalizuj mode na male pismena a bez okrajovych medzier
        mode_in = ...
        """
        mode_in = "TODO"

        m = 20 # default, ked nie je cislo

        """
        TODO 2:
        if minutes_str je cislo → m = minutes_str typu Integer
        (inak nechaj default 20)
        
        if ...:
            ...
        """

        if m < 10:
            print("Prilis malo — nastavujem minimum 10 min.")
            m = 10

        has_plan = True
        subject = subject_in
        minutes_goal = m
        mode = mode_in

        if mode == "hard":
            print("OK! Skus 25 min focus + 5 min pauza.")
        else:
            print("OK! Skus 15 min focus + 3 min pauza.")

        print(f"Plan: {subject} na {minutes_goal} min.\n")

    elif cmd == "c":
        if has_plan == False:
            print("\nNajprv nastav plan cez S.\n")
        else:
            real_str = input("Kolko minut si sa realne ucil? ").strip()

            """
            # TODO 3:
            # Bezpecne pretypuj real_str:
            # - if je cislo → real = real_str typu Integer
            # - inak real = 0
            """
            real = -1  # TODO

            if real >= minutes_goal:
                print("\nSplnene! Dobry vykon.\n")
            else:
                missing = minutes_goal - real
                print(f"\nEšte chyba {missing} min. Skus to dorazit!\n")

    elif cmd == "r":
        has_plan = False
        subject = ""
        minutes_goal = 0
        mode = ""
        print("\nPlan vymazany.\n")

    elif cmd == "q":
        print("\nDrzim palce pri uceni!")
        break

    else:
        print("\nNeznamy prikaz. Daj H pre pomoc.\n")