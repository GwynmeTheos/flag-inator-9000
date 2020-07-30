# Spell count flag checker.

import math


def spellFlagCheck(character):
    spellCount = 0

    try:
        for i in character['character']['spells']['spell']:
            spellCount += 1
    except TypeError:
        pass

    if spellCount == 0:
        return 0
    else:
        accruedFlags = math.floor(spellCount / 5) * 1
        print("    [" + str(spellCount) + " spells at 1 per 5 spells] = +" + str(accruedFlags) + " Flag")

        return accruedFlags
