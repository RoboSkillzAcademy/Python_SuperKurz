"""
library_tracker_todo.py
Modul 2 Triedna kniznica
bez funkcii bez try/except
Temy: list tuple set for filtre prehlady append
"""

print("=== Triedna kniznica ===")
print("Evidencia knih filtrovanie a prehlady")
print()

"""
Predpripravene data
Format tuplu: (titul zanr pocet_stran dostupna)
dostupna = True alebo False
"""
books = [
    ("Maly princ",           "roman",   96,  True),
    ("1984",                 "sci-fi",  328, False),
    ("Harry Potter 1",       "fantasy", 223, True),
    ("Duna",                 "sci-fi",  412, False),
    ("Hobit",                "fantasy", 310, True),
    ("Zaklinac 1",           "fantasy", 288, True),
    ("Sapiens",              "fakty",   443, False),
    ("Kratka historia casu", "fakty",   212, True),
    ("Neuromancer",          "sci-fi",  271, False),
    ("Pan prstenov 1",       "fantasy", 423, True),
]


"""
-------------------------------------------------------
CAST 1  Zakladny vypis vsetkych knih
Temy: for cyklus  indexovanie tuplu  vlastny counter
-------------------------------------------------------
"""
print("--- Vsetky knihy ---")

"""
TODO 1  (4-6 riadkov)

Prechadzaj cez books pomocou for
Pre kazdu knihu vypis riadok vo formate:
    1  Maly princ  roman  96 str  dostupna
    2  1984  sci-fi  328 str  nedostupna

Indexovanie tuplu:
    book[0] = titul
    book[1] = zanr
    book[2] = pocet stran
    book[3] = True/False

Dostupnost:
    if book[3] >> stav = "dostupna"
    else        >> stav = "nedostupna"

Poradove cislo: vlastny counter zacinajuci na 1

    counter = 1
    for book in books:
        titul  = book[0]
        zanr   = ...
        strany = ...
        if book[3]:
            stav = "dostupna"
        else:
            stav = ...
        print(str(counter) + "  " + titul + ...)
        counter = counter + 1
"""
pass  # zmaz ked dopisetes TO-DO 1

print()


"""
-------------------------------------------------------
CAST 2  Filter len dostupne knihy
Temy: for s podmienkou  pocitadlo
-------------------------------------------------------
"""
print("--- Dostupne knihy ---")

"""
TODO 2  (4-5 riadkov)

Prechadzaj cez books pomocou for
Vypis len tie kde book[3] == True
Pocitaj do premennej available_count (zacina na 0)
Na konci vypis celkovy pocet

    available_count = 0
    for book in books:
        if ...:
            print(...)
            available_count = available_count + 1
    print("Dostupnych knih " + str(available_count))
"""
pass  # zmaz ked dopisetes TO-DO 2

print()


"""
-------------------------------------------------------
CAST 3  Unikatne zanre pomocou set
Temy: set()  add()  sorted()
-------------------------------------------------------
"""
print("--- Zanre v kniznici ---")

"""
TODO 3  (4-5 riadkov)

Vytvor prazdny set:  genres = set()
Prechadzaj cez books a pridavaj book[1] do setu cez add()
Vypis zoradene zanre cez sorted()  kazdy na novy riadok
Na konci vypis celkovy pocet unikatnych zanrov

    genres = set()
    for book in books:
        genres.add(...)
    for g in sorted(genres):
        print(" - " + g)
    print("Pocet zanrov " + str(len(genres)))
"""
pass  # zmaz ked dopisetes TO-DO 3

print()


"""
-------------------------------------------------------
CAST 4  Filter podla zanru  vstup od pouzivatela
Temy: for podmienka  found flag
-------------------------------------------------------
"""
print("--- Filter podla zanru ---")

zanr_query = input("Zadaj zanr (napr fantasy): ").strip().lower()

"""
TODO 4  (5-6 riadkov)

Prechadzaj cez books
Vypis len tie kde book[1] == zanr_query
Pouzi found flag: nastav False pred cyklom
Ak po cykle found == False vypis "Ziadna kniha v tomto zanri"

    found = False
    for book in books:
        if ...:
            print(" - " + book[0] + "  " + str(book[2]) + " str")
            found = True
    if not found:
        print("Ziadna kniha v tomto zanri")
"""
pass  # zmaz ked dopisetes TO-DO 4

print()


"""
-------------------------------------------------------
CAST 5  Pridanie novej knihy
Temy: tuple vytvorenie  append  isdigit casting
-------------------------------------------------------
"""
print("--- Pridaj novu knihu ---")

titul_in   = input("Titul: ").strip()
zanr_in    = input("Zanr: ").strip().lower()
strany_str = input("Pocet stran: ").strip()

"""
TODO 5  (5-6 riadkov)

Bezpecny casting strany_str:
    ak isdigit >> pocet_stran = int(strany_str)
    inak       >> pocet_stran = 0  + vypis upozornenia

Vytvor novy tuple: (titul_in  zanr_in  pocet_stran  True)
Pridaj do books cez append
Vypis: "Kniha <titul> pridana  Celkom knih <len(books)>"

    if strany_str.isdigit():
        pocet_stran = int(strany_str)
    else:
        pocet_stran = 0
        print("Pocet stran nebol cislo nastavujem 0")
    new_book = (...)
    books.append(new_book)
    print("Kniha " + titul_in + " pridana  Celkom knih " + str(len(books)))
"""
pass  # zmaz ked dopisetes TO-DO 5

print()
print("Hotovo")