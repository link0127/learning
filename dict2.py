# task1: define a new language
# task2: define hundict to contain all languages
# task3: define a function which converts hundict to other direction (nodict for example)

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


def reverse_dict(orig_dict: dict, orig_lang: str = 'hu', new_lang: str = 'en') -> dict:
    newdict = {}
    # iterate on original dict and build new language -> orig lang dict
    for olang, odict in orig_dict.items():
        # no   {'igen': 'ja',....}
        # skip language if that's the new language
        if olang == new_lang:
            continue
        newdict[olang] = {}
        for key, value in odict.items():
            newdict[olang].update({orig_dict[new_lang][key]: value})

    # transpose new language to use it's value as key for other dics
    # {'ja': 'igen', ...}
    trans = {value: key for key, value in orig_dict[new_lang].items()}
    newdict.update({orig_lang: trans})
    return newdict

def main():
    hundict = {'no': dict_no, 'en': dict_en, 'cn': dict_cn, 'de': dict_de}

    print("Hun->Nor igen:", hundict['no']['igen'])

    nodict = reverse_dict(hundict, 'hu', 'no')
    print("Nor->Eng ja:", nodict['en']['ja'])

if __name__ == "__main__":
    main()