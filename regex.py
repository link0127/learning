
import re

inputtext="""Types of fruit
Fruit is the sweet, fleshy, edible part of a plant. It generally contains seeds. Fruits are usually eaten raw, although some varieties can be cooked. They come in a wide variety of colours, shapes and flavours. Common types of fruits that are readily available include:
Apples and pears
Citrus – oranges, grapefruits, mandarins and limes
Stone fruit – nectarines, apricots, peaches and plums
Tropical and exotic – bananas and mangoes
Berries – strawberries, raspberries, blueberries, kiwifruit and passionfruit
Melons – watermelons, rockmelons and honeydew melons
Tomatoes and avocados.

Types of vegetables
Vegetables are available in many varieties and can be classified into biological groups or ‘families’, including:
Leafy green – lettuce, spinach and silverbeet
Cruciferous – cabbage, cauliflower, Brussels sprouts and broccoli
Marrow – pumpkin, cucumber and zucchini
Root – potato, sweet potato and yam
Edible plant stem – celery and asparagus
Allium – onion, garlic and shallot."""




fruits  = r"[Aa]pple|[Pp]ear|[Oo]range|[Gg]rapefruit|[Mm]andarin|[Ll]ime|[Nn]ectarine|[Aa]pricot|[Pp]eache|[Pp]lum|[Bb]anana|[Mm]angoe|[Ss]trawberrie|[Rr]aspberrie|[Bb]lueberrie|[Kk]iwifruit|[Pp]assionfruit|[Ww]atermelon|[Rr]ockmelon|[Hh]oneydew. melon|[Tt]omatoe|[Aa]vocado"
veggies = r"[Ll]ettuce|[Ss]pinach|[Ss]ilverbeet|[Cc]abbage|[Cc]auliflower|[Bb]russel. sprouts|[Bb]roccoli|[Pp]umpkin|[Cc]ucumber|[Zz]ucchini|[Pp]otato|[Ss]weet potato|[Yy]am|[Cc]elery|[Aa]sparagus|[Oo]nion|[Gg]arlic|[Ss]hallot"

print("Fruits:")
for i in re.findall(fruits, inputtext):
    print(i)

print("\n" + "*" * 40 + "\n")


print("Veggies:")
for i in re.findall(veggies, inputtext):
    print(i)

# Lesson10 - homework 2
# BGP neighbor parser
# level: medium
# Hint: use my last example. No splitting needed. Only match full lines! Still do it with one regex call!
#
# Desired output:
# out = {'10.253.226.154': {'AS': 21302, 'uptime': '2w6d', 'state': '1'}, ...}
# watch out as we can have other time format by UpDown! (hour:mm:ss)
# also State can be different like Active...

import re


inputtext = """Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.253.226.154  4        21302  629191  124768      441    0    0 2w6d            1
150.127.7.253   4        64768 1659177 1659244      441    0    0 38w3d          OpenConfirm
150.127.6.254   4        64768  622538  622617      441    0    0 14w2d          70
150.127.9.254   4        64768  622538  622617      441    0    0 14y2w          Idle
150.127.10.254   4        64768  622538  622617      441    0    0 14h2m          Established
150.127.11.254   4        64768  622538  622617      441    0    0 14h2m          Active
10.253.226.154  4        21302  629191  124768      441    0    0 2w6d            1
150.127.12.253   4        64768 1659177 1659244      441    0    0 38w3d          70
150.127.13.254   4        64768  622538  622617      441    0    0 14w2d          70"""

out = dict()

# Desired output:
# out = {'10.253.226.154': {'AS': 21302, 'uptime': '2w6d', 'state': '1'}, ...}
# watch out as we can have other time format by UpDown! (hour:mm:ss)
# also State can be different like Active...

# your code comes here
#Regex for the output;
#(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) *\d *(\d{1,5}) *\d* *\d* *\d* *\d* *\d* *(\d{1,2}(w|y|h)\d{1,2}(w|m|d)) *((\d{1,6}|\w{1,13}))
pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*\d\s*(\d{1,5})\s*\d*\s*\d*\s*\d*\s*\d*\s*\d*\s(\d{1,2}[a-z]\d{1,2}[a-z])\s*(.*)"
entries = re.findall(pattern, inputtext)
for entry in entries:
    #print(entry)
    out[entry[0]] = {
        'AS': entry[1],
        'uptime': entry[2],
        'state': entry[3]
    }

print(out)

"""
    prop = {
        'AS': entry[1],
        'uptime': entry[2],
        'state': entry[3]
    }
    
    out[entry[0]] = prop
    
    az összes ua a megoldás
    
    properties = dict()
    properties['AS'] = entry[1]
    properties['uptime'] = entry[2]
    properties['state'] = entry[3]
    out[entry[0]] = properties
"""











