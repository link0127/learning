
"""
Birthday counter;

Write a function days_until_my_birthday(birthday) which will return the number of days left until the next birthday. birthday argument is a string in format YYYY-MM-DD

Example:
days_until_my_birthday("1979-04-03")
323


from datetime import date, timedelta
import time
today = date.today()
now = time.strftime("%H:%M:%S")
print(f"Now it is {today} at {now}")
print(f"Tomorrow it will be {today + timedelta(days=1)}")
print(f"Yesterday was {today - timedelta(days=1)}")
christmas_eve = date(2020, 12, 24)
until_christmas = christmas_eve - today
print(f"Until Christmas: {until_christmas}")

"""

import datetime

def days_until_my_birthday(birthday):
    DaysUntilNextBirthday = str()

    MaiNap = datetime.datetime.today()
    print("A pontos idő most:", MaiNap.strftime("%Y-%m-%d %H:%M:%S"))

    BirthdayToObject = datetime.datetime.strptime(birthday,"%Y-%m-%d")
    print(f"Ekkor szüllettél: {birthday}")

    Age = MaiNap.year - BirthdayToObject.year
    DaysYouHave = MaiNap - BirthdayToObject
    print(Age, "éves vagy, egészen pontosan ennyi ideje élsz:", DaysYouHave)

    NextBirthDay = BirthdayToObject.replace(year=MaiNap.year)

    if MaiNap >= NextBirthDay:
        NextBirthDay = BirthdayToObject.replace(year=MaiNap.year+1)
        DaysUntilNextBirthday = NextBirthDay - MaiNap
    else:
        DaysUntilNextBirthday = NextBirthDay - MaiNap

    print("A kövi szülinapodig még ennyi időt kell várni:")

    return(DaysUntilNextBirthday)

birthday = input("What is your birthday?\n")
print(days_until_my_birthday(birthday))