# -*- coding: utf-8 -*-
import random
stars = "*"  * 10
print("Witaj w symulatorze rzutu kostka")

while 5>2:

    print(stars)
    print("MENU")
    print("1.Losuj")
    print("2.Wyjscie")
    print(stars)

    wybor = int(input("Co chcesz zrobic? : "))

    if wybor == 1:
        print("Symulator rzutu kostka")

        print("Losowanie...")

        oczka = random.randint(1, 6)

        print("Wylosowano: ", oczka)

        border = "X" * 9

        if oczka == 1:
            row1 = "X" + "       " + "X"
            row2 = "X" + "   O   " + "X"
            row3 = "X" + "       " + "X"

        elif oczka == 2:
            row1 = "X" + " O     " + "X"
            row2 = "X" + "       " + "X"
            row3 = "X" + "     O " + "X"

        elif oczka == 3:
            row1 = "X" + " O     " + "X"
            row2 = "X" + "   O   " + "X"
            row3 = "X" + "     O " + "X"

        elif oczka == 4:
            row1 = "X" + " O   O " + "X"
            row2 = "X" + "       " + "X"
            row3 = "X" + " O   O " + "X"

        elif oczka == 5:
            row1 = "X" + " O   O " + "X"
            row2 = "X" + "   O   " + "X"
            row3 = "X" + " O   O " + "X"

        else:
            row1 = "X" + " O   O " + "X"
            row2 = "X" + " O   O " + "X"
            row3 = "X" + " O   O " + "X"

        print(border)
        print(row1)
        print(row2)
        print(row3)
        print(border)
    elif wybor == 2:
        break
    else:
        print("Podales zla liczbe!!!.Sprobuj jeszcze raz")