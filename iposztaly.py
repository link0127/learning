import random

class IPOsztalyom:
    r = 0
    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0

    def __init__(self):
        self.r = random.randint(1, 10)

    def setFirstOctet(self, szam):
        self.o1 = szam * self.r

    def setSecondOctet(self, szam):
        self.o2 = szam * self.r

    def setThirdOctet(self, szam):
        self.o3 = szam * self.r

    def setFourthOctet(self, szam):
        self.o4 = szam * self.r

    def increaseSecondOctetWith(self, szam):
        self.o2 += szam

    def getFirstOctet(self):
        return self.o1 / self.r

    def __str__(self):
        return "The IP address is: " + (str)((int)(self.o1/self.r)) + "." + (str)((int)(self.o2/self.r)) + "." + (str)((int)(self.o3/self.r)) + "." + (str)((int)(self.o4/self.r))

alma = IPOsztalyom()
alma.setFirstOctet(10)
print(alma.o1)
print(alma.getFirstOctet())