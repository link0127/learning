
"""
def hello(name):
    return "Hello " + name + "!"

def osszead(a, b):
    return a+b

print(hello("Bálint"))
print(osszead(10, 3)+7)
print(len(bulk))

class Balint:
    name = ""
    weight = 14

    def setName(self, name):
        self.name = name

    def getNameLength(self):
        return len(self.name)

    def feed(self):
        self.weight += 1

    def getWeight(self):
        return self.weight

osztaly = Balint()
print(type(osztaly))
print(type(""))

osztaly.setName("Bálint")
print(osztaly.getNameLength())

print("kiskutyqvagyok".upper())

print(osztaly.getWeight())
osztaly.feed()
print(osztaly.getWeight())

masodikosztaly = Balint()
print(masodikosztaly.getWeight())


"""


#-------------------------------------------------------------


"""
for i in [10, 8, 6, 4, 2, 4, 6, 8, 10]:
    draw = ""
    for j in range(1,i):
        draw +="*"
    print(draw.center(30))

"""
"""
input_width = 10 #input("Kérem a szélességet\n")

draw = str()
for i in range(1,input_width):
    draw = "*" * input_width
    print(draw.center(input_width))
"""
"""
draw = str()
for i in [10, 8, 6, 4, 2, 4, 6, 8, 10]:
    draw = "*" * i
    print(draw.center(input_width))
"""


#-------------------------------------------------------------


"""
input_width = int (input("Kérem a szélességet\n"))

draw = str()
i = input_width
input_width_csokkeno = input_width


for i in range(1,input_width):
    if input_width_csokkeno>0:
        draw = "*" * input_width_csokkeno
        print(draw.center(input_width))
        input_width_csokkeno -= 2

input_width_novekvo = 0
for y in range (1,input_width):
    input_width_novekvo += 2
    if input_width_novekvo<=input_width:
        draw = "*" * input_width_novekvo
        print(draw.center(input_width))

"""

#with def; where everything is stored on a variable


def homokora(input_width):

    draw = str()
    i = input_width
    input_width_csokkeno = input_width
    all = str()

    for i in range(input_width):
        if input_width_csokkeno>0:
            draw = "*" * input_width_csokkeno
            all += draw.center(input_width) + "\n"
            input_width_csokkeno -= 2


    input_width_novekvo = 0
    for y in range (input_width):
        input_width_novekvo += 2
        if input_width_novekvo<=input_width:
            draw = "*" * input_width_novekvo
            all += draw.center(input_width) + "\n"

    return all

input_width = int (input("Kérem a szélességet\n"))
print(homokora(input_width))




"""
def homokora(size):
    returnVal = ""
    for j in list(range(size, 1, -2)) + list(range(2, size+1, 2)):
        returnVal += ("*" * j).center(size) + "\n"
    return returnVal

while True:
    szam = (int)(input("Kérem a méretet:\n"))
    if szam%2 == 0:
        break
    else:
        print("Páros számot adj meg")

print(homokora(szam))

"""


