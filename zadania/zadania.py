
# Mutable vs immutable na przykładzie struktur danych

## Zadanie 1
# Napisz funkcję, która zwraca krotkę z liczbami od 0 do `n`, gdzie `n` jest parametrem funkcji.


 def ranger(n):
     return tuple(range(n))

# Zadanie 2
# Stwórz krotkę ze swoim wzrostem i przypisz do zmiennej.


bk = (181,)

# Zadanie 3
# Stwórz krotkę z imionami kolegów i przypisz do zmiennej.

friends = ('Michal', 'Grzgorz', 'Adrian')

# Zadanie 4
# Wykorzystująć pętlę `for` utwórz napis zawierający ciąg imion kolegów z grupy.

names = ''

for name in friends:
    names = names + name

# Zadanie 5
# Przed konkatenacją string wykonaj funkcję `id` na zmiennej zawierającej dodane do tej pory imiona.

names = ''

for name in friends:
    print(id(names))
    names = names + name

## Zadanie 6
# Napisz funkcję, która:
'''
>> zad6('1234')
"12_SDA_34"
>> zad6('12345')
"12_SDA_45"
>> zad6('ALA')
A_SDA_A"
'''

def zad6(word='1234'):
    sda = '_SDA_'
    if len(word) % 2:
        n_cut = len(word)//2
    return word[:n_cut]+sda+word[n_cut:]
    else:
        n_cut = len(word)

