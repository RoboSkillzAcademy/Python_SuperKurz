def scitaj(a, b):
    """
    Vráti súčet dvoch čísel.
    Príklad: scitaj(3, 4) → 7

    TODO 1
    Doplň telo funkcie.
    Jeden riadok: return ...
    """
    pass


def odcitaj(a, b):
    """
    Vráti rozdiel dvoch čísel (a - b).
    Príklad: odcitaj(10, 3) → 7

    TODO 2
    Doplň telo funkcie.
    """
    pass


def nasob(a, b):
    """
    Vráti súčin dvoch čísel.
    Príklad: nasob(4, 5) → 20

    TODO 3
    Doplň telo funkcie.
    """
    pass


def vydel(a, b):
    """
    Vráti podiel dvoch čísel (a / b).
    Ak je b == 0, nevyhadzuje výnimku -- vráti chybovú správu ako string.
    Príklad: vydel(10, 2) → 5.0
    Príklad: vydel(5, 0)  → 'Chyba: delenie nulou'

    TODO 4
    Doplň telo funkcie.
    Nezabudni ošetriť prípad b == 0.
    """
    pass


def ziskaj_cislo(vyzva):
    """
    Vypýta od používateľa číslo.
    Opakuje sa dovtedy, kým nezadá platné číslo (float).
    Vráti float.

    Príklad použitia:
        cislo = ziskaj_cislo('Zadaj prvé číslo: ')

    TODO 5
    Použi while True s break.
    Skús skonvertovať vstup na float.
    Ak sa to nepodarí (nie je to číslo), vypíš upozornenie a opakuj.
    Bez try/except: použi pomocnú funkciu alebo replace + isdigit.

    Tip -- jednoduchá kontrola bez try/except:
        vstup = input(vyzva).strip().replace('.', '', 1).replace('-', '', 1)
        if vstup.isdigit():
            return float(...)
        else:
            print('Prosím zadaj číslo.')
    """
    pass


def vypocitaj(a, b, operacia):
    """
    Podľa operácie (+, -, *, /) zavolá správnu matematickú funkciu
    a vráti výsledok.
    Ak je operácia neznáma, vráti chybovú správu ako string.

    Príklad: vypocitaj(10, 5, '+') → 15
    Príklad: vypocitaj(10, 5, '%') → 'Neznáma operácia: %'

    TO-DO 6
    Použi if/elif/else.
    Každá vetva zavolá jednu z matematických funkcií (scitaj, odcitaj...).
    Funkcia NEVOLÁ print() -- len vracia hodnotu.
    """
    pass


# ── HLAVNÝ PROGRAM ────────────────────────────────────────────────────


if __name__ == "__main__":
    """
    TO-DO 7
    Spoj všetko dohromady.

    Program má:
        1. Vypísať hlavičku  '=== Kalkulačka ==='
        2. Opýtať sa na prvé číslo cez ziskaj_cislo()
        3. Opýtať sa na druhé číslo cez ziskaj_cislo()
        4. Opýtať sa na operáciu: input('Operácia (+, -, *, /): ')
        5. Zavolať vypocitaj(a, b, operacia)
        6. Vypísať výsledok

    Príklad výstupu:
        === Kalkulačka ===
        Zadaj prvé číslo: 10
        Zadaj druhé číslo: 3
        Operácia (+, -, *, /): *
        Výsledok: 10.0 * 3.0 = 30.0
    """
    pass


# ── ROZŠÍRENIE (voliteľné -- pre rýchle účastníčky) ──────────────────


def mocnina(zaklad, exponent=2):
    """
    Vráti zaklad umocnený na exponent.
    Default exponent je 2 (druhá mocnina).
    Príklad: mocnina(3)    → 9
    Príklad: mocnina(2, 8) → 256

    BONUS TO-DO A
    Doplň telo funkcie. Jeden riadok.
    """
    pass


def koren(x):
    """
    Vráti druhú odmocninu z x.
    Ak je x záporné, vráti chybovú správu ako string.
    Príklad: koren(9)  → 3.0
    Príklad: koren(-1) → 'Chyba: odmocnina zo záporného čísla'

    Tip: odmocnina = x ** 0.5

    BONUS TO-DO B
    Doplň telo funkcie vrátane validácie.
    """
    pass
