# Beginner python - Lesson 5 - homework 2
# ICAO talking
# level: medium
# Hint: use file operation to read the input files.
#############################################################
# This will only work on windows!                           #
# !!!!! You will need to install these under pycharm: !!!!! #
# pip install pyttsx3 pypiwin32                             #
#############################################################
import pyttsx3

# One time initialization
engine = pyttsx3.init()
# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
#engine.say("You've got mail!")
#engine.say("You can queue up multiple items")

# your code comes here :) (I left the above as an example)

f = open("morse.txt")
TextTomb = f.readlines()
f.close()

InputFile = open("testfile.txt")
InputText = InputFile.readlines()
InputFile.close()

Sor = ()
Dictonary = {}

for sorok in TextTomb:
    Sor = sorok.split("\t")
    ICAOResult = Sor[1]
    ICAOLetter = Sor[0]
    Dictonary[ICAOLetter] = ICAOResult

for lines in InputText:
    for InputBetuk in lines:
        for DictonaryBetuk in Dictonary:
            if InputBetuk == DictonaryBetuk:
                engine.say(Dictonary[DictonaryBetuk])


# Flush the say() queue and play the audio
engine.runAndWait()