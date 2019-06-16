
# Zadanie 1
# Napisz funkcję, która zwraca napis "Hello World".


def hello_world():
    print('Hello world!')

# Zadanie 2
# Zmodyfikuj funkcję w taki sposób, aby zamiast "World" zwracała napis przekazany przez argument.


def hello_world2(word):
    print(f'Hello {word}!')

# Zadanie 3
# Dodaj swoje imię jako domyślną wartość argumentu.


def hello_world3(word='Bartek'):
    print(f'Hello {word}!')

# Zadanie 4


''' Napisz drugą funkcję, która będzie przyjmować obowiązkowo imię oraz opcjonalnie znak interpunkcyjny, 
który powinien znaleźć się na końcu zwracanego napisu. '''


def hello_world4(name, punctuation=''):
    print(f'Hello {name}{punctuation}')

# Zadanie 5
# Zamień argumenty (imię i znak interpunkcyjny) miejscami i uruchom funkcję.

def hello_world5(punctuation='', name):
    print(f'Hello {name}{punctuation}')



