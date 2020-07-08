

akarmi = input("adj meg valamit")

file = open("ip.txt", "w")
file.write(akarmi + "\n")
file.close()

file = open("ip.txt", "r")
print(file.read())