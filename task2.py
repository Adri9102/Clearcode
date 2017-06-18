import sys

spells = \
    {
        'fe': 1,
        'jee': 3,
        'je': 2,
        'ne': 2,
        'ai': 2,
        'ain': 3,
        'dai': 5
    }


def damage(spell):
    dam = 0
    if not isinstance(spell, str):
        print("Invalid input format, excepted string")
        sys.exit(1)
    if (spell.find("fe") > spell.rfind("ai") or spell.find("fe") == -1 or spell.count("fe") != 1):
        # print("Fail",spell)
        return dam
    else:
        spell = spell[spell.find("fe"):]
        spell = spell[:spell.rfind("ai") + 2]
        while spell[0] != "":
            temp = spell[0]
            exist1 = False
            breaked = False
            for sp1 in spells:
                if (sp1.find(temp) == 0):
                    exist1 = True
                    temp += spell[1]
                    exist2 = False
                    for sp2 in spells:
                        if (sp2.find(temp) == 0):
                            exist2 = True
                            if (len(spell) < 3):
                                dam += spells[temp]
                                if dam < 0:
                                    dam = 0
                                return dam
                                pass
                            temp += spell[2]
                            exist3 = False
                            for sp3 in spells:
                                if (sp3.find(temp) == 0):
                                    exist3 = True
                                    if (temp == "ain"):
                                        if (spell[3] == "e"):
                                            temp = ""
                                            dam += spells["ai"] + spells["ne"]
                                            spell = spell[4:]
                                            breaked = True
                                        else:
                                            dam += spells[temp]
                                            temp = spell[3]
                                            spell = spell[3:]
                                            breaked = True
                                    else:
                                        dam += spells[temp]
                                        temp = ""
                                        spell = spell[3:]
                                        breaked = True
                                        break
                                if breaked:
                                    break
                            if (not exist3):
                                temp2 = temp[-1:]
                                temp = temp[:2]
                                dam += spells[temp]
                                spell = spell[2:]
                                temp = temp2
                                del temp2
                                breaked = True
                                break
                        if breaked:
                            break
                    if (not exist2):
                        temp = temp[1:]
                        dam -= 1
                        spell = spell[1:]
                        breaked = True
                        break
                if breaked:
                    break
            if (not exist1):
                temp = ""
                dam -= 1
                spell = spell[1:]
                # print("Correct",spell)


print(damage('feai'))
