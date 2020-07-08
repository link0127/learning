import terito

#Létrehozzuk a terítőnket
terito = terito.Terito()
# Így generáljuk le mindig ugyan azt a terítőt, hogy loadStaticTerito(), ez amíg próbálkozol hasznos
terito.loadStaticTerito()
# Ha szeretnéd látni a terítőt, akkor írtam egy draw metódust, ha ezt kiszeded, akkor nem látod kirajzolva
print(terito.drawTerito())
# Csak hogy lásd minek kell kijönnie majd Neked is:
#x, y = terito.getSolution()
#print("A helyes megoldás: \nSor: " + (str)(x) + " és az oszlop: " + (str)(y))

# És akkor ide jöhet a kódod. A terítő listát betöltöttem Neked, a terito_data válltozóba, ezzel dolgozz:

terito_data = terito.get()

sor_counter = 0
sorFinal = int()
oszlopFinal = int()

for sor in terito_data:
    oszlop_counter = 0
    for sorElemek in sor:
        if sorElemek == 1:
            sorFinal = sor_counter
        if sorElemek == 1:
            oszlopFinal = oszlop_counter
            break
        oszlop_counter += 1
    sor_counter += 1

print("Az elrejtett karakter a " + str(sorFinal) + ". sorban és a " + str(oszlopFinal) + ". oszlopban van.")

"""
# Ha már ezzel a "statikus" terítővel megy a kódod, akkor így is próbáljuk ki, mert ez minden futtatáskor máshova rakja az X-et
terito = Terito()
terito.setSize(30)
terito.generate()
print(terito.drawTerito())
x, y = terito.getSolution()
print("A helyes megoldás: \nSor: " + (str)(x) + " és az oszlop: " + (str)(y))
"""
"""
tomb =[
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"],
    ["X","@","@","@"],
    ["@","@","@","@"],
    ["@","@","@","@"]
    ]
sor_counter = 0
sorFinal = int()
oszlopFinal = int()

for sor in terito:
    sor_counter += 1
    for sorElemek in sor:
        if sorElemek == 1:
            sorFinal = sor_counter
            break

for oszlop in terito:
    oszlop_counter = 0
    for oszlopElemek in oszlop:
        oszlop_counter +=1
        if oszlopElemek == 1:
            oszlopFinal = oszlop_counter


print("Az elrejtett karakter a " + str(sorFinal) + ". sorban és a " + str(oszlopFinal) + ". oszlopban van.")
"""