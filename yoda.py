import re

def english2yoda(inputText: str) -> str:
    yoda = ""
    pattern = r"(.*\.|.*\?|.*!)"
    lines = re.findall(pattern, inputText)

    for text in lines:
        splitted = text.strip()[0:-1].split(" ")

        if text[-1] == '.':
            splitted.append(splitted.pop(0))
            splitted.append(splitted.pop(0) + ".")

        elif text[-1] == "?":
            splitted.append(splitted.pop(0))
            splitted.append(splitted.pop(0))
            splitted.append(splitted.pop(0) + "?")
        elif text[-1] == "!":
            splitted.append(splitted.pop(0) + "!")
            splitted.append('Hmmm.')

        splitted[0] = " " + splitted[0].capitalize()
        yoda += " ".join(splitted)
    return yoda.strip()

text = "I am a good Python programmer. Could you do it alone? Be confident!"
# expected result: A good python programmer I am. It alone could you do? Confident be! Hmmmm.

print(english2yoda(text))

#text = "I am a good Python programmer. Could you do it alone? Be confident!"