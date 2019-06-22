# Zadania przypominające

## Zadanie 1
Napisz funkcję która działa w następujący sposób:
```
>> zad1()
Dzisiaj jest sobota
>> zad1('niedziela')
Jutro jest niedziela
>> zad1('poniedzialek')
Poniedziałek jest za 2 dni
>> zad1('wtorek')
Wtorek jest za 3 dni
```
Dla ambitnych: Spraw, aby funkcja brała pod uwagę datę (dzień tygodnia) np. jutro wynik wywołania tej funkcji będzie inny.


## Zadanie 2
Napisz funkcję która zwraca sumę długości argumentów nazwanych oraz ich sumę długości ich wartości.
```
>> zad2(foo='1', bar='test')
(6, 5)
```

Dla ambitnych: Spraw, aby funkcja przyjmowała tylko argumenty nazwane.

## Zadanie 3
Rozpakuj rezultat wywołania funkcji z poprzedniego zadania do osobnych zmiennych.


## Zadanie 4
Zaanotuj napisane funkcje odpowiednimi typami, tak aby `mypy` nie zwracał błędów.