# Adept Power flag checker.

def adeptPowerFlagCheck(character):
    accruedFlags = 0

    try:
        for power in character['character']['powers']['power']:
            if power['name'] == 'Heightened Concentration':
                accruedFlags += 1
                print("    [Heightened Concentration] = +1 Flag")
            elif power['name'] == 'Mystic Aptitude':
                accruedFlags += 2
                print("    [Mystic Aptitude] = +2 Flag")
    except TypeError:
        pass

    return accruedFlags
