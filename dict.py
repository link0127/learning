dict_en = {'igen': 'yes',
           'nem': 'no',
           'van': 'is'
           }
dict_no = {'igen': 'ja',
           'nem': 'nei',
           'van': 'er'
           }
dict_cn = {'igen': '对',   # dui
           'nem': '没有',  # méi you
           'van': '是'     # shi
           }
dict_de = {'igen': 'ja',
           'nem': 'nein',
           'van': 'ist'
           }

hundict = {'no': dict_no, 'en': dict_en, 'cn': dict_cn, 'de': dict_de}

def translator(original_dict, source_lang, dest_lang):
    return_dict = {}
    source_dict = {}
    dest_dict = {}
    for source_items in original_dict:
        if source_lang == source_items:
            source_dict = original_dict[source_lang]
    for dest_items in original_dict:
        if dest_items == dest_lang:
            dest_dict = original_dict[dest_lang]

    for key in source_dict:
        return_dict[ source_dict[key] ] = dest_dict[key]

    return return_dict




def translatorVSZ(original_dict, source_lang, dest_lang):
    outputDict = {}
    if source_lang in original_dict and dest_lang in original_dict:
        for hu, foreignWord in original_dict[source_lang].items():
            if hu in original_dict[dest_lang]:
                outputDict[foreignWord] = original_dict[dest_lang][hu]

    return outputDict


print(translatorVSZ(hundict, 'en', 'de'))


print(translator(hundict, 'en', 'de'))

"""


proba = {
    'igen': {
        'en': 'yes',
        'no': 'ja',
        'cn': '对',
        'de': 'ja'
    }
}


veglegesDict = {}
dicts = {
    'en': dict_en,
    'de': dict_de,
    'cn': dict_cn,
    'no': dict_no
}

print(dicts)


for key, value in dicts.items():
    #if key not in veglegesDict:
    #    veglegesDict[key] = {}
    for hu, trans in value.items():
        if hu not in veglegesDict:
            veglegesDict[hu] = {}
        veglegesDict[hu][key] = trans
        
        
print(veglegesDict)

"""
