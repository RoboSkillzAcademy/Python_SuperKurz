"""
studybuddy_v2_todo.py
Modul 1  StudyBuddy v2
bez listov  bez funkcii  bez try/except

Novinky oproti v1:
    while validacia priority (1-5)  nie len default
    while vyhladavanie v texte a predmete
    normalizacia vstupu strip lower upper
"""

print("=== StudyBuddy v2 ===")
print("Prikazy: A=Add V=View C=Clear SP=Search-Predmet ST=Search-Text H=Help Q=Quit")
print()

"""
Model  jedna uloha v premennych  rovnako ako v1
"""
has_task    = False
subject     = ""
priority    = 0
text        = ""


while True:
    cmd = input("Prikaz: ").strip().lower()


    """
    -------------------------------------------------------
    H  Help
    -------------------------------------------------------
    """
    if cmd == "h":
        print()
        print("A  = pridaj ulohu")
        print("V  = zobraz ulohu")
        print("C  = vymazat ulohu")
        print("SP = hladaj podla predmetu")
        print("ST = hladaj podla slova v texte")
        print("H  = pomoc")
        print("Q  = koniec")
        print()


    """
    -------------------------------------------------------
    A  Add  pridanie ulohy
    Novinka v2: while validacia priority  nie len default
    -------------------------------------------------------
    """
    elif cmd == "a":
        subject_in = input("Predmet (napr MAT): ").strip().upper()
        text_in    = input("Text ulohy: ").strip()

        if text_in == "":
            print("Text nesmie byt prazdny  uloha nebola ulozena")
            print()
        elif subject_in == "":
            print("Predmet nesmie byt prazdny  uloha nebola ulozena")
            print()
        else:
            """
            TO-DO 1  (4-6 riadkov)

            Pouzi while cyklus na validaciu priority
            Opytaj sa opakovane  kym pouzivatel nezada cislo 1 az 5
            Bez try/except  pouzi isdigit() a kontrolu rozsahu

                p = 0
                while True:
                    priority_in = input("Priorita (1-5): ").strip()
                    if priority_in.isdigit():
                        p = int(priority_in)
                        if p >= 1 and p <= 5:
                            break
                    print("Neplatna priorita  zadaj cislo 1 az 5")
            """
            p = 0
            pass  # zmaz ked dopisetes TO-DO 1

            subject  = subject_in
            text     = text_in
            priority = p
            has_task = True
            print("Uloha ulozena")
            print()


    """
    -------------------------------------------------------
    V  View  vypis aktualnej ulohy
    -------------------------------------------------------
    """
    elif cmd == "v":
        if has_task == False:
            print()
            print("Nemas ulozenu ziadu ulohu")
            print()
        else:
            print()
            print("--- Aktualna uloha ---")
            print("Predmet:  " + subject)
            print("Priorita: " + str(priority) + "/5")
            print("Text:     " + text)
            print()


    """
    -------------------------------------------------------
    C  Clear  vymazanie ulohy
    -------------------------------------------------------
    """
    elif cmd == "c":
        if has_task == False:
            print()
            print("Nie je co mazat")
            print()
        else:
            has_task = False
            subject  = ""
            priority = 0
            text     = ""
            print()
            print("Uloha vymazana")
            print()


    """
    -------------------------------------------------------
    SP  Search by Predmet
    Novinka v2: while vyhladavacia slucka  in  upper
    -------------------------------------------------------
    """
    elif cmd == "sp":
        if has_task == False:
            print()
            print("Nemas ziadu ulohu  najprv pridaj cez A")
            print()
        else:
            """
            TO-DO 2  (6-8 riadkov)

            Pouzi while cyklus ktory sa opakuje kym pouzivatel nezada "stop"
            Pre kazdy vstup:
                normalizuj na UPPER
                porovnaj so subject (subject je uz UPPER)
                ak sa zhoduje vypis ulohu
                ak nie vypis "Predmet sa nezhoduje"

                query = ""
                while query != "stop":
                    query = input("Hladaj predmet (alebo stop): ").strip().upper()
                    if query == "STOP":
                        break
                    if query == subject:
                        print("Najdene:  " + subject + "  " + str(priority) + "/5  " + text)
                    else:
                        print("Predmet " + query + " sa nezhoduje s " + subject)
            """
            pass  # zmaz ked dopisetes TO-DO 2

            print()


    """
    -------------------------------------------------------
    ST  Search by Text
    Novinka v2: in operator  lower normalizacia
    -------------------------------------------------------
    """
    elif cmd == "st":
        if has_task == False:
            print()
            print("Nemas ziadu ulohu  najprv pridaj cez A")
            print()
        else:
            """
            TO-DO 3  (6-8 riadkov)

            Pouzi while cyklus ktory sa opakuje kym pouzivatel nezada "stop"
            Pre kazdy vstup:
                normalizuj keyword na lower
                hladaj keyword v text.lower() pomocou operatora in
                ak najdes vypis "Najdene: <text>"
                ak nie vypis "Slovo <keyword> sa nenaslo v texte"

                while True:
                    keyword = input("Hladaj slovo v texte (alebo stop): ").strip().lower()
                    if keyword == "stop":
                        break
                    if keyword in text.lower():
                        print("Najdene:  " + text)
                    else:
                        print("Slovo " + keyword + " sa nenaslo v texte")
            """
            pass  # zmaz ked dopisetes TO-DO 3

            print()


    """
    -------------------------------------------------------
    Q  Quit
    -------------------------------------------------------
    """
    elif cmd == "q":
        print()
        print("Ahoj  StudyBuddy konci")
        break


    else:
        print()
        print("Neznamy prikaz  Daj H pre pomoc")
        print()