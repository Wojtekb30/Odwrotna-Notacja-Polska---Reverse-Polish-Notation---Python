# Odwortna Notacja Polska

Moja implementacja liczenia działań w Odwrotej Notacji Polskiej w Python.

Jak działa:

Wpisane działanie zostaje przekonwertowane na tabelę. 

Program skanuje ją od lewej do prawej aż znajdzie znak wskazujący na obliczenie (+, -, *, /). Wykonuje je, zapisuje liczbę wynikową, czyści resztę wykonanego działania i przesuwa wszystkie elementy tabeli do lewej. Jest to zapętlane aż w tabeli zostanie tylko jedna liczba będąca wynikiem.

# Reverse Polish Notation

My implementation of calculating Reverse Polish Notation in Python.

How it works:

The typed calculation is converted into a table. 

The program scans it from left to right until it finds a character indicating a operation (+, -, *, /). It performs it, stores the resulting number, clears the other elements of the just done calculation and moves all the elements of the table to the left. This is looped until there is only one number (which is the result) left in the table.
