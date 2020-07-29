# Spell count flag checker.

import math


def spellFlagCheck(character):
    accruedFlags = 0
    spellCount = 0

    for spell in character['character']['spells']['spell']:
        spellCount += 1

    if spellCount == 0:
        return 0
    else:
        accruedFlags = math.floor(spellCount / 5) * 1
        print("    [" + str(spellCount) + " spells at 1 per 5 spells] = +" + str(accruedFlags) + " Flag")
        return accruedFlags
