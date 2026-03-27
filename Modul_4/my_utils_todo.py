def normalizuj_mena(*mena):
    """
    Normalizuje jedno alebo viac mien (strip + capitalize).
    Používa *args a list comprehension.

    Args:
        *mena -- ľubovoľný počet reťazcov

    Returns:
        list normalizovaných mien

    Príklad:
        normalizuj_mena(' JANA ', 'mia') → ['Jana', 'Mia']

    Táto funkcia je HOTOVÁ -- ukážka správneho štýlu.
    Použi ju ako vzor pre ostatné funkcie.
    """
    return [m.strip().capitalize() for m in mena]


def posli_email(adresat, predmet, sprava, cc=None, priorita='normal'):
    """
    Simuluje odoslanie emailu -- vypíše formátovaný výstup do konzoly.
    Používa default a keyword argumenty.

    Args:
        adresat  -- emailová adresa príjemcu (str)
        predmet  -- predmet emailu (str)
        sprava   -- telo emailu (str)
        cc       -- kópia (str alebo None, default None)
        priorita -- 'low', 'normal' alebo 'high' (default 'normal')

    Returns:
        None (vedľajší efekt: vypíše email)

    Príklad:
        posli_email('jana@email.sk', 'Ahoj', 'Ako sa mas?')
        posli_email('mia@sk', 'SOS', 'Pomoc!', priorita='high')

    TO-DO 1
    Vypíš formátovaný blok napr.:
        --- Email ---
        Komu:     jana@email.sk
        Predmet:  Ahoj
        Priorita: normal
        CC:       (žiadna)
        Správa:   Ako sa mas?
    Ak cc je None, vypíš '(žiadna)'.
    """
    pass


def analyzuj_text(text):
    """
    Analyzuje zadaný text a vráti štatistický slovník.
    Používa dict comprehension, set comprehension a list comprehension.

    Args:
        text -- ľubovoľný reťazec

    Returns:
        dict s kľúčmi:
            'dlzky_slov'     -- set unikátnych dĺžok slov
            'pocty_znakov'   -- dict {znak: počet} len pre písmená (isalpha)
            'najdlhsie_slova' -- list slov s maximálnou dĺžkou

    Príklad:
        analyzuj_text('mam rada python')
        → {
            'dlzky_slov':      {3, 4, 6},
            'pocty_znakov':    {'m': 2, 'a': 3, 'r': 1, ...},
            'najdlhsie_slova': ['python']
          }

    TO-DO 2
    Všetko len pomocou comprehensions -- žiadne for-cykly s append.
    Postup:
        slova = text.split()
        dlzky_slov     = set comprehension cez slova
        pocty_znakov   = dict comprehension cez set(text) s podmienkou isalpha
        max_dlzka      = max(len(s) for s in slova) -- ak slova nie je prázdne
        najdlhsie_slova = list comprehension cez slova s podmienkou
    """
    pass


def cezar_sifra(text, posun=3):
    """
    Zašifruje alebo dešifruje text Caesarovou šifrou.
    Používa default argument a list comprehension / map.

    Args:
        text  -- vstupný reťazec
        posun -- posun abecedy (default 3, záporné číslo = dešifrovanie)

    Returns:
        str -- zašifrovaný/dešifrovaný text

    Príklad:
        cezar_sifra('Ahoj')    → 'Dkrm'
        cezar_sifra('Dkrm', -3) → 'Ahoj'

    TO-DO 3 (BONUS -- náročnejšia)
    Pravidlá:
        Veľké písmená posúvaj v rozsahu A-Z (ord 65-90).
        Malé písmená posúvaj v rozsahu a-z (ord 97-122).
        Ostatné znaky (medzery, čísla) nechaj bez zmeny.
    Tip: chr(((ord(c) - 65 + posun) % 26) + 65) pre veľké písmená.
    """
    pass


# ── Matematika ────────────────────────────────────────────────────────


def faktorial(n):
    """
    Rekurzívne vypočíta n! (faktoriál).
    Táto funkcia je HOTOVÁ -- ukážka rekurzie.

    Args:
        n -- nezáporné celé číslo

    Returns:
        int

    Príklad:
        faktorial(5) → 120
        faktorial(0) → 1
    """
    if n <= 1:
        return 1
    return n * faktorial(n - 1)


def rozsah_statistiky(*cisla):
    """
    Vráti základné štatistiky ľubovoľného počtu čísel.
    Používa *args a zabudované funkcie (min, max, sum, sorted).

    Args:
        *cisla -- ľubovoľný počet čísel

    Returns:
        dict s kľúčmi: 'min', 'max', 'priemer', 'median'
        Ak nie sú zadané žiadne čísla, vráti prázdny dict {}.

    Príklad:
        rozsah_statistiky(3, 1, 4, 1, 5, 9)
        → {'min': 1, 'max': 9, 'priemer': 3.83, 'median': 3.5}

    TO-DO 4
    Mediána pre párny počet prvkov = priemer dvoch stredných hodnôt.
    Priemer zaokrúhli na 2 desatinné miesta (round).
    """
    pass


def splosnit(zoznam):
    """
    Rekurzívne splošťuje vnorený zoznam ľubovoľnej hĺbky.

    Args:
        zoznam -- list ktorý môže obsahovať ďalšie listy

    Returns:
        flat list

    Príklad:
        splosnit([1, [2, [3, 4]], 5]) → [1, 2, 3, 4, 5]
        splosnit([1, 2, 3])           → [1, 2, 3]

    TO-DO 5
    Rekurzívny postup:
        výsledok = []
        pre každý prvok v zozname:
            ak je prvok list → rekurzívne zavolaj splosnit(prvok) a rozsir vysledok
            inak → pridaj prvok do výsledku
        vráť výsledok
    """
    pass


def prvocisla_do(n):
    """
    Vráti list všetkých prvočísel do n (vrátane) pomocou Eratosthenovho sita.

    Args:
        n -- horná hranica (int)

    Returns:
        list prvočísel

    Príklad:
        prvocisla_do(20) → [2, 3, 5, 7, 11, 13, 17, 19]

    TO-DO 6 (BONUS)
    Eratostenovo sito:
        1. Vytvor zoznam True pre každé číslo od 0 do n.
        2. Pre každé p od 2 dokiaľ p*p <= n:
               ak je sito[p] True, označ všetky násobky p ako False.
        3. Vráť [i for i, je_prvocislo in enumerate(sito) if je_prvocislo and i >= 2]
    """
    pass


# ── Práca s kolekciami ────────────────────────────────────────────────


def priemer(*cisla):
    """
    Vypočíta priemer ľubovoľného počtu čísel.
    Ak nie sú zadané žiadne čísla, vráti 0.
    Používa *args.

    Args:
        *cisla -- ľubovoľný počet čísel

    Returns:
        float

    Príklad:
        priemer(10, 20, 30) → 20.0
        priemer(5)          → 5.0
        priemer()           → 0

    TO-DO 7
    Dva riadky: kontrola prázdnosti + výpočet.
    """
    pass


def filtruj(data, **kriteria):
    """
    Vyfiltruje zoznam slovníkov podľa keyword kritérií.
    Každé kľúčové slovo musí sedieť s kľúčom v slovníku.
    Podporuje špeciálny suffix _max pre porovnanie <=.
    Používa **kwargs a list comprehension / filter.

    Args:
        data      -- list slovníkov
        **kriteria -- filtrovacie podmienky

    Returns:
        list slovníkov ktoré spĺňajú všetky podmienky

    Príklad:
        produkty = [
            {'nazov': 'Laptop',  'kategoria': 'tech', 'cena': 800},
            {'nazov': 'Telefon', 'kategoria': 'tech', 'cena': 400},
            {'nazov': 'Kniha',   'kategoria': 'edu',  'cena': 20},
        ]
        filtruj(data=produkty, kategoria='tech', cena_max=500)
        → [{'nazov': 'Telefon', 'kategoria': 'tech', 'cena': 400}]

    TO-DO 8 (BONUS -- najnáročnejšia)
    Pre každú podmienku v kriteria:
        ak kľúč končí na '_max' → porovnaj item[kľúč_bez_max] <= hodnota
        inak → porovnaj item[kľúč] == hodnota
    """
    pass


def zip_do_slovnika(kluce, hodnoty):
    """
    Spoji dva zoznamy do slovníka pomocou zip() a dict comprehension.

    Args:
        kluce   -- list kľúčov
        hodnoty -- list hodnôt

    Returns:
        dict

    Príklad:
        zip_do_slovnika(['a', 'b', 'c'], [1, 2, 3]) → {'a': 1, 'b': 2, 'c': 3}

    TO-DO 9
    Jeden riadok s dict comprehension a zip().
    """
    pass


# ── Rýchly self-test (spustí sa len pri python my_utils.py) ──────────


if __name__ == "__main__":
    print("=== Self-test my_utils.py ===")
    print()

    # normalizuj_mena -- hotová
    print("normalizuj_mena:")
    print(normalizuj_mena(' JANA ', 'mia', '  ZUZKA'))
    print()

    # faktorial -- hotový
    print("faktorial:")
    print(faktorial(5))
    print(faktorial(0))
    print()

    """
    TO-DO 10
    Sem pridaj testy pre všetky funkcie ktoré si implementovala.
    Použi print() alebo assert.

    Príklad:
        assert priemer(10, 20, 30) == 20.0,  'priemer: chyba'
        assert priemer() == 0,               'priemer prazdny: chyba'
        print('priemer: OK')

    Minimum: aspoň 1 test na každú funkciu ktorú si doplnila.
    """
    pass
