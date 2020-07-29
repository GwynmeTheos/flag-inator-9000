# Ware flag checker.


def wareFlagCheck(character):
    accruedFlags = 0

    # Specific 'ware
    try:
        for ware in character['character']['cyberwares']['cyberware']:
            # Adapsin
            if ware['name'] == 'Adapsin':
                accruedFlags += 1
                print("    [Adapsin] = +1 Flag")
            # Pain Editor
            elif ware['name'] == 'Pain Editor':
                accruedFlags += 2
                print("    [Pain Editor] = +1 Flag")
            # MBW
            elif ware['name'] == 'Move-by-Wire' and (ware['rating'] == '2' or ware['rating'] == '3'):
                accruedFlags += 1
                print("    [MBW Rating 2 or 3] = +1 Flag")
            # Genetic Optmization
            elif ware['name'] == 'Genetic Optimization (Body)':
                accruedFlags += 1
                print("    [Genetic Optimization (Body)] = +1 Flag")
            elif ware['name'] == 'Genetic Optimization (Agility)':
                accruedFlags += 1
                print("    [Genetic Optimization (Agility)] = +1 Flag")
            elif ware['name'] == 'Genetic Optimization (Strength)':
                accruedFlags += 1
                print("    [Genetic Optimization (Strength)] = +1 Flag")
            elif ware['name'] == 'Genetic Optimization (Charisma)':
                accruedFlags += 1
                print("    [Genetic Optimization (Charisma)] = +1 Flag")
            elif ware['name'] == 'Genetic Optimization (Intuition)':
                accruedFlags += 1
                print("    [Genetic Optimization (Intuition)] = +1 Flag")
            elif ware['name'] == 'Genetic Optimization (Logic)':
                accruedFlags += 1
                print("    [Genetic Optimization (Logic)] = +1 Flag")
            elif ware['name'] == 'Genetic Optimization (Willpower)':
                accruedFlags += 1
                print("    [Genetic Optimization (Willpower)] = +1 Flag")
            # Narco
            elif ware['name'] == 'Narco':
                accruedFlags += 1
                print("    [Narco] = +1 Flag")
            else:
                continue
    except TypeError:
        pass

    # Betaware
    try:
        for ware in character['character']['cyberwares']['cyberware']:
            if ware['grade'] == 'Betaware' or ware['grade'] == 'Betaware (Adapsin)':
                accruedFlags += 1
                print("    [Betaware: " + ware['name'] + "] = +1 Flag")
    except TypeError:
        pass

    return accruedFlags
