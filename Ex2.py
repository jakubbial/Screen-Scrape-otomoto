# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

Number = int(input("Podaj jakiś numer\n"))
Modulo_2 = Number % 2
Modulo_4 = Number % 4

if Modulo_4 == 0:
    print("Liczba podzielna przez 4")
elif Modulo_2 == 0:
    print("Liczba parzysta")
elif Modulo_2 >= 1:
    print("Liczba nieparzysta")

Dzielona = int(input("Podaj liczbe do podzielenia\n"))
Dzielna = int(input("Podaj liczbę dzieląca\n"))

Modulo_dowolne = Dzielona % Dzielna

if Modulo_dowolne == 0:
    print("Twoja liczba jest podzielna przez ta drugą")
elif Modulo_dowolne >= 1:
    print("Twoja liczba nie jest podzielna")
else:
    print("nie wiem", Modulo_dowolne)
