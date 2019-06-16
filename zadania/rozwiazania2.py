
# Argumenty pozycyjne i nazwane funkcji

# Zadanie 1
# Napisz funkcję,która przyjmuję numer telefonu oraz opcjonalnie numer kierunkowy(+48) i flagę czy wyświetlić kierunkowy
# a następnie wyświetla numer w formacie: `+48 123456789` lub `123456789`.


def show_telnumber(number, prefix=False):
    if prefix:
        print(f'+48 {number}')
    else:
        print(number)


# Zadanie 2
# Uruchom funkcję z różną liczbą argumentów pozycyjnych (tylko numer, numer i kierunkowy, numer i kierunkowy oraz flaga)

# Zadanie 3
# Uruchom funkcję podając różną liczbę argumenty nazwanych.

# Zadanie 4
# Uruchom funkcję używając argumentów nazwanych i pozycyjnych.

