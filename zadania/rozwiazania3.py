
import numpy as np

# Argumenty wielokrotne *args, **kwargs

# Zadanie 1
# Napisz funkcję która przyjmuję dowolną liczbę argumentów pozycyjnych i zwraca krotkę, która je zawiera.


def foo(*args):
    return args


# Zadanie 2
# Zmodyfikuj funkcję tak aby przyjmowała również argumenty nazwane i
# zwracała krotkę zawierającą argumenty pozycyjne i nazwane.


def foo2(*args, **kwargs):
    return args, kwargs

# Zadanie 3
# Zmodyfikuj funkcję tak aby zwracała sumę argumentów pozycyjnych oraz iloczyn argumentów nazwanych.


def foo3(*args, **kwargs):
    res = 1
    for value in kwargs.values():
        res = res * value
    return res, sum(args)


# Zadanie 4
# Napisz funkcję, która zwróci nazwy wszystkich argumentów nazwanych.


def foo4(**kwargs):
    return list((kwargs.keys()))
