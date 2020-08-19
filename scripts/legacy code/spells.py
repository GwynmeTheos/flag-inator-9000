# Spell count flag checker.

import math


def spellFlagCheck(character, skillsDict):
    spellCount = 0
    spellcastingRating = 0
    try:
        for i in character['character']['spells']['spell']:
            spellCount += 1
        try:
            for qual in character['character']['qualities']['quality']:
                if qual['name'] == "Dedicated Spellslinger":
                    spellcastingRating = skillsDict['MAGSkills']['Spellcasting']
        except TypeError:
            pass
    except TypeError:
        pass

    spellCount -= 10 + spellcastingRating

    if spellCount <= 0:
        return 0
    else:
        accruedFlags = int(spellCount / 3)
        print("    [" + str(spellCount) + " spells at 1 per 3 spells after first 10] = +" + str(accruedFlags) + " Flag")

        return accruedFlags
