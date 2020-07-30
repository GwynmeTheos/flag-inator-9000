# Attribute flag checker.


def attributeFlagCheck(character, attributesDict):
    accruedFlags = 0

    # Base attributes:
    for currentAtt in character['character']['attributes']['attribute']:

        if (currentAtt['name'] == 'MAG') or (currentAtt['name'] == 'RES') or (currentAtt['name'] == 'DEP'):
            if int(currentAtt['totalvalue']) > 6:
                if int(currentAtt['totalvalue']) == 7:
                    accruedFlags += 2
                    print("    [" + currentAtt['name'] + " at " + currentAtt['totalvalue'] + "] = +2 Flag")
                elif int(currentAtt['totalvalue']) == 8:
                    accruedFlags += 5
                    print("    [" + currentAtt['name'] + " at " + currentAtt['totalvalue'] + "] = +5 Flag")
                elif int(currentAtt['totalvalue']) == 9:
                    accruedFlags += 9
                    print("    [" + currentAtt['name'] + " at " + currentAtt['totalvalue'] + "] = +9 Flag")
                elif int(currentAtt['totalvalue']) >= 10:
                    accruedFlags += 14
                    print("    [" + currentAtt['name'] + " at " + currentAtt['totalvalue'] + "] = +14 Flag")

        elif currentAtt['name'] == 'ESS' or currentAtt['name'] == 'EDG' or currentAtt['name'] == 'MAGAdept':
            continue

        elif currentAtt['name'] == 'STR' or currentAtt['name'] == 'AGI':
            if attributesDict[currentAtt['name']] == 1:
                accruedFlags += 2
                print("    [" + currentAtt['name'] + " at 1] = +2 Flag")

            if attributesDict[str('highestLimb' + currentAtt['name'])] >= 9 and attributesDict[str('highestLimb' + currentAtt['name'])] > int(currentAtt['metatypemax']):
                accruedFlags += 2
                print("    [Highest Limb " + currentAtt['name'] + " at " + str(attributesDict[str('highestLimb' + currentAtt['name'])]) + ", over Metatype limit] = +2 Flag")

        else:
            if attributesDict[currentAtt['name']] == 1:
                accruedFlags += 2
                print("    [" + currentAtt['name'] + " at 1] = +2 Flag")

            if attributesDict[str('average' + currentAtt['name'])] >= 9 and attributesDict[str('average' + currentAtt['name'])] > int(currentAtt['metatypemax']):
                accruedFlags += 2
                print("    [" + currentAtt['name'] + " at " + str(attributesDict[str('average' + currentAtt['name'])]) + ", over Metatype limit] = +2 Flag")

    return accruedFlags
