"""
event_planner_todo.py
Modul 3   Funkcie a parametre
bez tried  bez try/except

Tema: rozklad problemu na funkcie  parametre  navratove hodnoty
Pribeh: planovac skolskych udalosti  pridat  filtrovat  zhrnutie
"""

print("=== Planovac udalosti ===")
print("Prikazy: A=Add V=View F=Filter S=Summary H=Help Q=Quit")
print()


"""
Predpripravene data
Format tuplu: (nazov  typ  kapacita)
typ = "sportova"  "kulturna"  "akademicka"
"""
events = [
    ("Skolsky ples",         "kulturna",   120),
    ("Olympiada z MAT",      "akademicka",  30),
    ("Futbalovy turnaj",     "sportova",    50),
    ("Debatna sutaz",        "akademicka",  25),
    ("Divadelne predstavenie","kulturna",   80),
    ("Atleticky den",        "sportova",   200),
]

"""
-------------------------------------------------------
TODO 1

Napiste funkciu format_event(event  index)
Funkcia dostane jeden tuple event a int index
Vracia naformatovany string vo formate:
    "1  Skolsky ples  kulturna  120 miest"

Navratova hodnota: string

    def format_event(event  index):
        return (str(index) + "  " + event[0] + "  "
                + event[1] + "  " + str(event[2]) + " miest")
-------------------------------------------------------
"""
def format_event(event, index):
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 2

Napiste funkciu print_events(events)
Funkcia dostane list tuplov
Vypise vsetky udalosti pomocou format_event()
Ak je zoznam prazdny vypise "Ziadne udalosti"
Navratova hodnota: None

Poznamka: tato funkcia vola format_event   jedna funkcia vola druhu

    def print_events(events):
        if len(events) == 0:
            print("Ziadne udalosti")
            return
        counter = 1
        for event in events:
            print(format_event(event  counter))
            counter = counter + 1
-------------------------------------------------------
"""
def print_events(events):
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 3

Napiste funkciu filter_by_type(events  event_type)
Funkcia dostane list tuplov a string event_type
Vracia novy list   len udalosti kde event[1] == event_type
Ak nenajde zianu vracia prazdny list

Navratova hodnota: list

    def filter_by_type(events  event_type):
        result = []
        for event in events:
            if event[1] == event_type:
                result.append(event)
        return result
-------------------------------------------------------
"""
def filter_by_type(events, event_type):
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 4

Napiste funkciu get_total_capacity(events)
Funkcia dostane list tuplov
Spocita celkovu kapacitu   sucet vsetkych event[2]
Vracia int

Navratova hodnota: int

    def get_total_capacity(events):
        total = 0
        for event in events:
            total = total + event[2]
        return total
-------------------------------------------------------
"""
def get_total_capacity(events):
    pass  # zmaz a implementuj


"""
-------------------------------------------------------
TODO 5

Napiste funkciu get_input_event()
Funkcia nema parametre
Opyta sa pouzivatela na nazov  typ a kapacitu
Vracia tuple (nazov  typ  kapacita)

Validacie:
    nazov nesmie byt prazdny   while loop
    typ musi byt sportova / kulturna / akademicka   while loop
    kapacita cez isdigit   inak default 50

Navratova hodnota: tuple

    def get_input_event():
        while True:
            nazov = input("Nazov udalosti: ").strip()
            if nazov != "":
                break
            print("Nazov nesmie byt prazdny")

        platne_typy = ["sportova"  "kulturna"  "akademicka"]
        while True:
            typ = input("Typ (sportova/kulturna/akademicka): ").strip().lower()
            if typ in platne_typy:
                break
            print("Neplatny typ  zadaj sportova  kulturna alebo akademicka")

        kap_str = input("Kapacita: ").strip()
        if kap_str.isdigit():
            kapacita = int(kap_str)
        else:
            kapacita = 50
            print("Neplatna kapacita  nastavujem 50")

        return (nazov  typ  kapacita)
-------------------------------------------------------
"""
def get_input_event():
    pass  # zmaz a implementuj


"""
=======================================================
HLAVNE MENU
=======================================================
"""

while True:
    cmd = input("Prikaz (A/V/F/S/H/Q): ").strip().lower()


    if cmd == "h":
        print()
        print("A = pridaj udalost")
        print("V = zobraz vsetky udalosti")
        print("F = filter podla typu")
        print("S = zhrnutie")
        print("Q = koniec")
        print()


    elif cmd == "a":
        """
        TODO 6a   (2-3 riadky)

        Zavolaj get_input_event()
        Uloz navratovu hodnotu do new_event
        Pridaj do events cez append
        Vypis potvrdenie

            new_event = get_input_event()
            events.append(new_event)
            print("Pridane:  " + new_event[0])
        """
        pass  # zmaz a implementuj


    elif cmd == "v":
        print()
        print_events(events)
        print()


    elif cmd == "f":
        typ_query = input("Typ (sportova/kulturna/akademicka): ").strip().lower()
        """
        TODO 6b   (3-4 riadky)

        Zavolaj filter_by_type(events  typ_query)
        Uloz vysledok do filtered
        Vypis nadpis a zavolaj print_events(filtered)

            filtered = filter_by_type(events  typ_query)
            print()
            print("--- " + typ_query + " ---")
            print_events(filtered)
        """
        pass  # zmaz a implementuj
        print()


    elif cmd == "s":
        """
        TODO 6c   (4-5 riadkov)

        Vypis zhrnutie vsetkych typov udalosti
        Pre kazdy typ zavolaj filter_by_type a get_total_capacity
        Vypis:
            Celkom udalosti: <pocet>
            sportova: <pocet>  kapacita <celkova>
            kulturna: <pocet>  kapacita <celkova>
            akademicka: <pocet>  kapacita <celkova>
            Celkova kapacita: <sucet>

            print("Celkom udalosti: " + str(len(events)))
            for typ in ["sportova"  "kulturna"  "akademicka"]:
                skupina = filter_by_type(events  typ)
                kap     = get_total_capacity(skupina)
                print(typ + ": " + str(len(skupina)) + "  kapacita " + str(kap))
            print("Celkova kapacita: " + str(get_total_capacity(events)))
        """
        print()
        pass  # zmaz a implementuj
        print()


    elif cmd == "q":
        print()
        print("Ahoj  Drzim palce")
        break


    else:
        print()
        print("Neznamy prikaz  Daj H pre pomoc")
        print()
