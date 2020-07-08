"""
In the first task, please create a base class Animal with class attribute 'species', instance attribute 'name', 'age' and method 'speak'. Constructor should set initial values of these attributes.
Then please create some animal classes with overrides class attributes and inherits behaviour from Animal class. Some ideas: Dog, Cat, GuineaPig, Fish, etc... Don't forget to override speak :) Dog for example speaks: 'Bark bark!'

Bonus if child classes have extra attributes or methods!

"""

# Beginner python - Lesson 8 - homework 1
# Animal inheritance
# level: easy
"""
class Animal:

    species = "None"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Please override the speak method in your class!")
        exit(1)

    def play(self):
        print("Please override the play method in your class!")
        exit(1)


class Dog(Animal):

    species = "Dog"

    def speak(self):
        return "VAU, VAU"

class Cat(Animal):

    species = "Cat"

    def speak(self):
        return "Miauu, miauu"

    def play(self):
        return "RUN RUN"


import random

zoo = list()
for i in range(0, 10):
    kutya_v_macska = random.randint(0, 1)
    if kutya_v_macska == 0:
        animal = Cat("Pihe", random.randint(1, 100))
    elif kutya_v_macska == 1:
        animal = Dog("Negró", random.randint(1, 100))

    zoo.append(animal)

print(zoo)
print(len(zoo))

for animal in zoo:
    print(animal.age)
    print(animal.speak())
    print(animal.play())

"""


"""
Zoo2
"""

"""
In the first task, please create a base class Animal with class attribute 'species', instance attribute 'name', 'age' and method 'speak'. Constructor should set initial values of these attributes.
Then please create some animal classes with overrides class attributes and inherits behaviour from Animal class. Some ideas: Dog, Cat, GuineaPig, Fish, etc... Don't forget to override speak :) Dog for example speaks: 'Bark bark!'

Bonus if child classes have extra attributes or methods!

"""


# Beginner python - Lesson 8 - homework 1
# Animal inheritance
# level: easy

class Animal:

    species = "General animal"

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def speak(self):
        return "Please override the speak method in your class!"
        exit(1)



class Beez(Animal):

    species = "Beez"

    def speak(self):
        return "Buzz, buzz"

    def type(self):
        return "Stingy"

class Bats(Animal):

    species = "Bats"

    def speak(self):
        return "Screech, screech"

    def type(self):
        return "Scary"

test = Animal("Allatka", 20)
print(test.species)
print(test.speak())


allat = Beez("Mehecske", 2)
print(allat.species)
print(allat.speak())
print(allat.type())


allat = Bats("Denever", 5)
print(allat.species)
print(allat.speak())
print(allat.type())