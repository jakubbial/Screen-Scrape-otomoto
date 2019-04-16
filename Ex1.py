# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

Name = input("Wpisz swoje imię\n")
Wiek = input("Wpisz swój wiek\n")

Lata_do_setki = 100 - int(Wiek)

print(Name, " do setki pozostało ci ", Lata_do_setki, " lat")

Wypisz_jeszcze_raz = input("Ile razy mam to jeszcze napisać?\n")

for i in range(0, int(Wypisz_jeszcze_raz)):
    print(Name, " do setki pozostało ci ", Lata_do_setki, " lat")
