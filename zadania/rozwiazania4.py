
# Przekazywanie rozpakowanych argumentów w wywołaniu funkcji (* oraz **)

# Zadanie 1
# Rozpakuj listę argumentów i wywołaj funkcję z poprzedniego zadania.


def foo3(*args, **kwargs):
    res = 1
    for value in kwargs.values():
        res = res * value
    return res, sum(args)


l = [1, 2, 3]


foo3(*l)


# Zadanie 2
# Rozpakuj słownik argumentów nazwanych i wywołaj funkcję z poprzedniego zadania.