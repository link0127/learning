
f = open("morse.txt")
TextTomb = f.readlines()
f.close()

InputFile = open("testfile.txt")
InputText = InputFile.readlines()
InputFile.close()

"""VSZ
"""

szotar = dict()
for sor in TextTomb:
    items = sor.split('\t')
    szotar[items[0]] = items[-1].replace('\n', '')

result = []
for lines in InputText:
    for InputBetuk in lines:
        result.append(szotar[InputBetuk.upper()])


print(" ".join(result))

#END VSZ

"""
Sor = ()
Dictonary = {}
Result = str()

for sorok in TextTomb:
    Sor = sorok.split("\t")
    SorTorles = Sor[3]
    SorToroltMorse = SorTorles[:-1]
    Dictonary[Sor[0]]= SorToroltMorse

for lines in InputText:
    for InputBetuk in lines:
        for DictonaryBetuk in Dictonary:
            if InputBetuk == DictonaryBetuk:
                Result += Dictonary[DictonaryBetuk]
                Result += " "

print(Result)

"""

"""
counter = 0
for i in Dictonary:
    if i == "D":
        print("The morse code of", test, "is ", Dictonary[test])
        break
    counter +=1
    print(counter)

"""