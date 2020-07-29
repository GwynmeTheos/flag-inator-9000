# Armor flag checker.


def armorFlagCheck(character):
    accruedFlags = 0

    for gear in character['character']['armors']['armor']:
        if 