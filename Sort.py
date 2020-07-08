"""
You have a database. Please sort the devices by name in the sites! At the end write out the db with the pprint.

In [ ]:
# Beginner python - Lesson 4 - homework 2
# Sort inventory
# level: medium
# Hint: use dict and list functions and loop
from pprint import pprint
"""


from pprint import pprint

db={
    "HU": {
        "BDP": ["HUBDP-LANCUA001", "HUBDP-LANCUA006", "HUBDP-LANCCO001", "HUBDP-WANRTC001"]
    },
    "GB": {
        "FAW": ["GBFAW-LANCUA002", "GBFAW-LANCUA001"],
        "AVO": ["GBAVO-LANCUA002", "GBAVO-LANCUA001"],
        "BIT": ["GBBIT-WANRTC001"]
    },
    "FR": {
        "NDG": ["FRNDG-LANCUA092", "FRNDG-LANCUA001"]
    },
    "US": {
        "DAL": ["USDAL-WANRTC001", "USDAL-LANCUA001", "USDAL-WANRTV001"],
        "HHL": ["USHHL-LANCCO002", "USHHL-LANCCO001"]
    }
}

# your code comes here
#print(db["HU"]["BDP"][0])

"""
for Country in db:
    SiteAndDeviceList = db[Country]

    for SiteCode in SiteAndDeviceList:
        OrderedDeviceList = SiteAndDeviceList[SiteCode]
        OrderedDeviceList.sort()

print("------------------------------------")
pprint(db)
"""


for Country in db:
    for SiteCode in db[Country]:
        db[Country][SiteCode].sort()
pprint(db)

"""
class bemutatom:

    szam = 0

    def szamBeallit(self, szamocska):
        self.szam = szamocska

    def getSzam(self):
        return self.szam

proba = bemutatom()
print(proba)
print(proba.getSzam())
kutyuska = proba
print(kutyuska)

kutyuska.szamBeallit(10)

print(proba.getSzam())

"""



db2 = {
    "HU": {
      "BDP": ["HUBDP-LANCUA001", "HUBDP-LANCUA006", "HUBDP-LANCCO001", "HUBDP-WANRTC001"],
      "AVO": ["HUAVO-LANCUA002", "HUAVO-LANCUA001"]
    },
    "US": {
        "DAL": ["USDAL-WANRTC001", "USDAL-LANCUA001", "USDAL-WANRTV001"],
        "HHL": ["USHHL-LANCCO002", "USHHL-LANCCO001"]
    }
}
print("-------------------------------------")
kulcs1 = "HU"
b = '7000'

db = {}
db[kulcs1] = {}
db[kulcs1]["BDP"] = list()

db["EGYEDI"] = {}
db["EGYEDI"]["MON"] = ['159', '500']

db["kulcs3"] = {}
db["kulcs3"]["KAR"] = list()

print(db)
print(db["EGYEDI"]["MON"])
print(type(db["EGYEDI"]["MON"]))

db["EGYEDI"]["MON"].append(500)
print(db["EGYEDI"]["MON"])

a = 5 # type: int



"""
# sort example

def important_numbers_ahead(number):
    # important numbers:
    if number in [13, 40, 42, 69, 79, 255]:
        return float("-inf")
    else:
        return number

numbers = [1, 5, -2, 67, 69, 42, 79, 102, 33]
numbers.sort(key=important_numbers_ahead)
print(numbers)

"""