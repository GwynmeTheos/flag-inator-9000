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
                print("    [Pain Editor] = +2 Flag")
            # MBW
            elif ware['name'] == 'Move-by-Wire' and (ware['rating'] == '2' or ware['rating'] == '3'):
                accruedFlags += 1
                print("    [MBW Rating 2 or 3] = +1 Flag")
            # Genetic Optmization
            elif ware['name'] == 'Genetic Optimization (Body)'\
                    or ware['name'] == 'Genetic Optimization (Agility)'\
                    or ware['name'] == 'Genetic Optimization (Strength)'\
                    or ware['name'] == 'Genetic Optimization (Reaction)'\
                    or ware['name'] == 'Genetic Optimization (Charisma)'\
                    or ware['name'] == 'Genetic Optimization (Intuition)'\
                    or ware['name'] == 'Genetic Optimization (Logic)'\
                    or ware['name'] == 'Genetic Optimization (Willpower)':
                accruedFlags += 1
                print("    [" + ware['name'] + "] = +1 Flag")

            # Narco
            elif ware['name'] == 'Narco':
                accruedFlags += 1
                print("    [Narco] = +1 Flag")
            else:
                continue
    except TypeError:
        pass

    # Betaware and Deltaware Base Ess Cost
    try:
        betaCostSum = 0
        deltaCostSum = 0
        for ware in character['character']['cyberwares']['cyberware']:
            # Betaware
            if ware['grade'] == "Betaware" or ware['grade'] == "Betaware (Adapsin)":
                betaCostSum += float(ware['ess'])
            # Deltaware
            elif ware['grade'] == "Deltaware" or ware['grade'] == "Deltaware (Adapsin)":
                deltaCostSum += float(ware['ess']) * 2
        accruedFlags += int(betaCostSum) + int(deltaCostSum)
        if int(betaCostSum) != 0:
            print("    [Sum of base cost of Betaware] = +" + str(int(betaCostSum)) + " Flag")
        if int(deltaCostSum) != 0:
            print("    [Sum of base cost of Deltaware] = +" + str(int(deltaCostSum)) + " Flag")
    except TypeError:
        pass

    return accruedFlags
