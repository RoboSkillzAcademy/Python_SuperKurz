"""
Tema: rozklad problemu na funkcie  parametre  navratove hodnoty
Pribeh: kalkulacka priemernej znamky a odporucania pre studienta
"""

print("=== Kalkulacka znamok ===")
print("Prikazy: A=Add V=View AVG=Priemer R=Report C=Clear H=Help Q=Quit")
print()


"""
Predpripravene data   znamky ako list   kazda polozka je tuple (predmet znamka)
"""
grades = [
    ("MAT", 2),
    ("BIO", 3),
    ("ENG", 1),
    ("FYZ", 4),
    ("SLO", 2),
]

"""
-------------------------------------------------------
TODO 1

Napiste funkciu get_subject_and_grade()
Funkcia nema parametre
Funkcia sa opyta pouzivatela na predmet a znamku
Vracia tuple (subject  grade) kde:
    subject = string UPPER  nesmie byt prazdny
    grade   = int 1-5  validovany cez while + isdigit

Navratova hodnota: (subject  grade)

    def get_subject_and_grade():
        while True:
            subject_in = input("Predmet: ").strip().upper()
            if subject_in != "":
                break
            print("Predmet nesmie byt prazdny")

        p = 0
        while True:
            ...

        return (subject_in  p)
-------------------------------------------------------
"""
def get_subject_and_grade():
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 2

Napiste funkciu calculate_average(grades)
Funkcia dostane list tuplov (predmet  znamka)
Spocita priemer vsetkych znamok
Vracia float   priemer

Ak je grades prazdny   vracia 0.0

Navratova hodnota: float

    def calculate_average(grades):
        if len(grades) == 0:
            return 0.0
        total = 0
        for g in grades:
            total = total + g[1]
        return total / len(grades)
-------------------------------------------------------
"""
def calculate_average(grades):
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 3

Napiste funkciu get_recommendation(average)
Funkcia dostane float   priemer znamok
Vracia string s odporucenim podla tabulky:
    priemer <= 1.5   "Vyborne  drz tak"
    priemer <= 2.5   "Dobry vysledok"
    priemer <= 3.5   "Ujde  ale da sa lepsie"
    inak             "Treba zapracovat"

Navratova hodnota: string

    def get_recommendation(average):
        if average <= 1.5:
            return ...
        elif ...
-------------------------------------------------------
"""
def get_recommendation(average):
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 4

Napiste funkciu print_grades(grades)
Funkcia dostane list tuplov (predmet  znamka)
Vypise vsetky znamky ocislovane
Format:  1  MAT  2
Ak je zoznam prazdny vypise "Ziadne znamky"

Navratova hodnota: None   len vypis

    def print_grades(grades):
        if len(grades) == 0:
            print("Ziadne znamky")
            return
        counter = 1
        for g in grades:
            ...
-------------------------------------------------------
"""
def print_grades(grades):
    pass  # zmaz a implementuj


"""
=======================================================
HLAVNE MENU   funkcie su uz volane   doplnte TO-DO 5
=======================================================
"""

while True:
    cmd = input("Prikaz (A/V/AVG/R/C/H/Q): ").strip().lower()


    if cmd == "h":
        print()
        print("A   = pridaj znamku")
        print("V   = zobraz vsetky znamky")
        print("AVG = vypocitaj priemer")
        print("R   = report  priemer + odporucanie")
        print("C   = vymazat vsetky znamky")
        print("Q   = koniec")
        print()


    elif cmd == "a":
        """
        TODO 5a   (1-2 riadky)

        Zavolaj get_subject_and_grade()
        Uloz navratovu hodnotu do premennej new_grade
        Pridaj new_grade do grades cez append
        Vypis: "Ulozene  <predmet>  znamka <cislo>"

            new_grade = get_subject_and_grade()
            grades.append(new_grade)
            print("Ulozene  " + new_grade[0] + "  znamka " + str(new_grade[1]))
        """
        pass  # zmaz a implementuj


    elif cmd == "v":
        print()
        print_grades(grades)
        print()


    elif cmd == "avg":
        """
        TODO 5b   (2-3 riadky)

        Zavolaj calculate_average(grades)
        Uloz vysledok do avg
        Vypis priemer zaokruhleny na 2 desatinne miesta
        Ak je grades prazdny vypis upozornenie

            if len(grades) == 0:
                print("Ziadne znamky")
            else:
                avg = calculate_average(grades)
                print("Priemer: " + str(round(avg  2)))
        """
        pass  # zmaz a implementuj


    elif cmd == "r":
        """
        TODO 5c   (3-4 riadky)

        Zavolaj calculate_average(grades)
        Zavolaj get_recommendation(avg)
        Vypis report:
            priemer
            pocet znamok
            odporucanie

            avg = calculate_average(grades)
            rec = get_recommendation(avg)
            print("Priemer: " + str(round(avg  2)))
            print("Pocet znamok: " + str(len(grades)))
            print("Odporucanie: " + rec)
        """
        pass  # zmaz a implementuj


    elif cmd == "c":
        grades = []
        print()
        print("Vsetky znamky vymazane")
        print()


    elif cmd == "q":
        print()
        print("Ahoj  Drzim palce")
        break


    else:
        print()
        print("Neznamy prikaz  Daj H pre pomoc")
        print()
