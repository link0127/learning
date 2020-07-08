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


allatok = []

navigacio = []
navigacio.append("1. Tamagocsi letrehozasa")
navigacio.append("2. ")

while True:
