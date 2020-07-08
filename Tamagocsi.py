from os import system
import random

class Tamagocsi:
    Name = ""
    Weight = 50
    Food = 2
    Drink = 1
    Age = 1
    Sick = False

    def __init__(self, name):
        self.Name = name

    def getName(self):
        return self.Name

    def getSick(self):
        return self.Sick

    def setSick(self, status):
        self.Sick = status

    def randomSick(self):
        self.setSick((bool) (random.randint(0, 1)))

    def live(self):
        self.randomSick()
        self.Age += 1
        self.Weight -= 1

    def feeding(self):
        if(self.getSick()):
            self.Weight -= 3
        else:
            self.Weight = self.Weight + self.Food

    def drinking(self):
        if (self.getSick()):
            self.Weight -= 2
        else:
            self.Weight = self.Weight + self.Drink

    def getWeight(self):
        return self.Weight

class IlledelmesTamagocsi(Tamagocsi):

    def feeding(self):
        super().feeding()
        print('Köszönöm, hogy megetettél! A súlyom most: ', self.getWeight())

    def drinking(self):
        super().drinking()
        print('Köszönöm, hogy megitattál! A súlyom most: ', self.getWeight())


jozsi = IlledelmesTamagocsi("Józsi")
lofasz = IlledelmesTamagocsi("Lófasz")

Welcome = "Válassz\n(1) Kilépés\n(2) Képernyő tisztítás\n(3) Etetés\n(4) Itatás\n(5) józsi kiválasztása\n(6) lófasz kiválasztása"
selectedTamagocsi = jozsi
print("Udv! Létrehoztam józsi és lofasz nevű állatodat. A navigációhoz ezt használhatod:")
print(Welcome)

while True:
    #print(jozsi.Welcome)
    Option = (int) (input())

    if Option >= 1 and Option <= 6:

        selectedTamagocsi.live()
        print(selectedTamagocsi.getWeight())

        if Option == 1:
            exit(0)
        elif Option == 2:
            system('cls')
        elif Option == 3:
            selectedTamagocsi.feeding()
        elif Option == 4:
            selectedTamagocsi.drinking()
        elif Option == 5 or Option == 6:
            selectedTamagocsi = jozsi if Option == 5 else lofasz
            print("Mostantól " + selectedTamagocsi.getName() + " tamagocsit használod.")
            print("Neki a súlya most: ", selectedTamagocsi.getWeight())

    else:
        print(Welcome)