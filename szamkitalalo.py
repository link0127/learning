import random

print("Számkitaláló 1.0")
print("A játék lényege, hogy a program gondol egy számra 1 és 10 között, Neked meg ki kell találnod.")

while True:
    command = input("Kezdhetjük [i/n]: ")
    if command == "i" or command == "n":
        if(command == "n"):
            print("Sajnálom, hogy kilépsz. Viszlát!")
            exit(0)
        print("\n\nAkkor kezdjük a játékot. Ha bármikor azt adod válasznak, hogy exit, akkor vége a játéknak.")
        print("Amennyiben azt adod válasznak, hogy give up akkor megmutatom mi a helyes válasz.\n\n")
        break
    else:
        print("Kérjük, csak a megadott válaszokból válaszolj (i = igen, n = nem).")

while True:
    print("Gondoltam egy számra 1 és 10 között. Kitalálod?")
    number = random.randint(1, 10)
    while True:
        answer = input("Válaszod (egy szám, exit vagy give up): ")
        if answer == "exit":
            print("Viszlát!")
            exit(0)
        elif answer == "give up":
            print("A szám amire gondoltam:" , number)
            break
        elif answer.isnumeric():
            toint = int(answer)
            if toint == number:
                print("\n\nGratulálok eltaláltad!")
                break
            print("Nem talált! Próbálkozz újra!")
        else:
            print("Kérlek, csak számot vagy a két bűvös parancsot add meg és ne mást.")

    again = input("\n\nSzeretnél egy újat játszani? [i/n]: ")
    if again == "n":
        print("Viszlát!")
        exit(0)
    elif again == "i":
        continue
    else:
        print("Kérjük csak i vagy n választ adj meg.")