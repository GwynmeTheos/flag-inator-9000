# Skill flag checker.


def skillFlagCheck(skillsDict, attributesDict):
    accruedFlags = 0

    accruedFlags += BODSkills(skillsDict, attributesDict)

    accruedFlags += CombatSkills(skillsDict, attributesDict)

    accruedFlags += UnarmedCombatSkills(skillsDict, attributesDict)

    accruedFlags += AGISkills(skillsDict, attributesDict)

    accruedFlags += REASkills(skillsDict, attributesDict)

    accruedFlags += STRSkills(skillsDict, attributesDict)

    accruedFlags += CHASkills(skillsDict, attributesDict)

    accruedFlags += INTSkills(skillsDict, attributesDict)

    accruedFlags += LOGSkills(skillsDict, attributesDict)

    accruedFlags += WILSkills(skillsDict, attributesDict)

    accruedFlags += MAGSkills(skillsDict, attributesDict)

    accruedFlags += RESSkills(skillsDict, attributesDict)

    return accruedFlags


def BODSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['BODSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        # None
        # Defautable.
        if skillsDict['BODSkills'][skill] == 0:
            dicepool = attributesDict['averageBOD'] - 1
        else:
            dicepool = skillsDict['BODSkills'][skill] + attributesDict['averageBOD']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + Body at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + Body at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + Body at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + Body at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def CombatSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['CombatSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['CombatSkills'][skill] == 0 and (skill == 'Palming'):
            dicepool = 0
        # Defautable.
        elif skillsDict['CombatSkills'][skill] == 0:
            if attributesDict['averageLOG'] > attributesDict['averageAGI']:
                dicepool = attributesDict['averageLOG'] - 1
                higherRating = "Logic"
            else:
                if attributesDict['averageAGI'] > attributesDict['highestArmAGI']:
                    dicepool = attributesDict['averageAGI'] - 1
                else:
                    dicepool = attributesDict['highestArmAGI'] - 1
                higherRating = "Agility"
        else:
            if attributesDict['averageLOG'] > attributesDict['averageAGI']:
                dicepool = skillsDict['CombatSkills'][skill] + attributesDict['averageLOG']
                higherRating = "Logic"
            else:
                if attributesDict['averageAGI'] > attributesDict['highestArmAGI']:
                    dicepool = skillsDict['CombatSkills'][skill] + attributesDict['averageAGI']
                else:
                    dicepool = skillsDict['CombatSkills'][skill] + attributesDict['highestArmAGI']
                higherRating = "Agility"

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def UnarmedCombatSkills(skillsDict, attributesDict):

    if skillsDict['CombatSkills']['Unarmed Combat'] == 0:
        if attributesDict['averageLOG'] > attributesDict['averageAGI']:
            dicepool = attributesDict['averageLOG'] - 1
            higherRating = "Logic"
        else:
            if attributesDict['averageAGI'] > attributesDict['highestArmAGI']:
                dicepool = attributesDict['averageAGI'] - 1
            else:
                dicepool = attributesDict['highestArmAGI'] - 1
            higherRating = "Agility"

    else:
        if attributesDict['averageLOG'] > attributesDict['averageAGI']:
            dicepool = skillsDict['CombatSkills']['Unarmed Combat'] + attributesDict['averageLOG']
            higherRating = "Logic"
        else:
            if attributesDict['averageAGI'] > attributesDict['highestLimbAGI']:
                print(attributesDict['averageAGI'] + ">" + attributesDict['highestLimbAGI'])
                dicepool = skillsDict['CombatSkills']['Unarmed Combat'] + attributesDict['averageAGI']
            else:
                dicepool = skillsDict['CombatSkills']['Unarmed Combat'] + attributesDict['highestLimbAGI']
            higherRating = "Agility"

    if dicepool > 12:
        # 13-15
        if 13 <= dicepool < 16:
            print("    [Unarmed Combat + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            return 1
        # 16-17
        elif 16 <= dicepool < 18:
            print("    [Unarmed Combat + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            return 3
        # 18-19
        elif 18 <= dicepool < 20:
            print("    [Unarmed Combat + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            return 5
        # 20+
        elif dicepool >= 20:
            print("    [Unarmed Combat + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")
            return 7
    else:
        return 0


def AGISkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['AGISkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['AGISkills'][skill] == 0 and (skill == 'Flight' or skill == 'Locksmith'):
            dicepool = 0
        # Defautable.
        elif skillsDict['AGISkills'][skill] == 0:
            if skill == 'Sneaking':
                if attributesDict['averageINT'] > attributesDict['averageAGI']:
                    dicepool = attributesDict['averageINT'] - 1
                    higherRating = "Intuition"
                else:
                    dicepool = attributesDict['averageAGI'] - 1
                    higherRating = "Agility"
            elif skill == 'Escape Artist' or skill == 'Locksmith':
                if attributesDict['averageLOG'] > attributesDict['averageAGI']:
                    dicepool = attributesDict['averageLOG'] - 1
                    higherRating = "Logic"
                else:
                    dicepool = attributesDict['averageAGI'] - 1
                    higherRating = "Agility"
            else:
                dicepool = attributesDict['averageAGI'] - 1
                higherRating = "Agility"
        else:
            if skill == 'Sneaking':
                if attributesDict['averageINT'] > attributesDict['averageAGI']:
                    dicepool = skillsDict['AGISkills'][skill] + attributesDict['averageINT']
                    higherRating = "Intuition"
                else:
                    dicepool = skillsDict['AGISkills'][skill] + attributesDict['averageAGI']
                    higherRating = "Agility"
            elif skill == 'Escape Artist' or skill == 'Locksmith':
                if attributesDict['averageLOG'] > attributesDict['averageAGI']:
                    dicepool = skillsDict['AGISkills'][skill] + attributesDict['averageLOG']
                    higherRating = "Logic"
                else:
                    dicepool = skillsDict['AGISkills'][skill] + attributesDict['averageAGI']
                    higherRating = "Agility"
            else:
                dicepool = skillsDict['AGISkills'][skill] + attributesDict['averageAGI']
                higherRating = "Agility"

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def REASkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['REASkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['REASkills'][skill] == 0 and (skill == 'Pilot Aerospace' or skill == 'Pilot Aircraft' or skill == 'Pilot Walker'):
            dicepool = 0
        # Defautable.
        elif skillsDict['REASkills'][skill] == 0:
            if attributesDict['averageINT'] > attributesDict['averageREA']:
                dicepool = attributesDict['averageINT'] - 1
                higherRating = "Intuition"
            else:
                dicepool = attributesDict['averageREA'] - 1
                higherRating = "Reaction"
        else:
            if attributesDict['averageINT'] > attributesDict['averageREA']:
                dicepool = skillsDict['REASkills'][skill] + attributesDict['averageINT']
                higherRating = "Intuition"
            else:
                dicepool = skillsDict['REASkills'][skill] + attributesDict['averageREA']
                higherRating = "Reaction"

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def STRSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['STRSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        # None
        # Defautable.
        if skillsDict['STRSkills'][skill] == 0:
            dicepool = attributesDict['averageSTR'] - 1
        else:
            dicepool = skillsDict['STRSkills'][skill] + attributesDict['averageSTR']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def CHASkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['CHASkills'].keys():

        # Check for defaulting.
        # Not defautable.
        # None
        # Defautable.
        if skillsDict['CHASkills'][skill] == 0:
            dicepool = attributesDict['averageCHA'] - 1
        else:
            dicepool = skillsDict['CHASkills'][skill] + attributesDict['averageCHA']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def INTSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['INTSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['INTSkills'][skill] == 0 and (skill == 'Artisan' or skill == 'Assensing'):
            dicepool = 0
        # Defautable.
        elif skillsDict['INTSkills'][skill] == 0:
            dicepool = attributesDict['averageINT'] - 1
        else:
            dicepool = skillsDict['INTSkills'][skill] + attributesDict['averageINT']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def LOGSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['LOGSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['LOGSkills'][skill] == 0 and (skill == 'Aeronautics Mechanic' or
                                                    skill == 'Arcana' or
                                                    skill == 'Automotive Mechanic' or
                                                    skill == 'Biotechnology' or
                                                    skill == 'Chemistry' or
                                                    skill == 'Cybertechnology' or
                                                    skill == 'Electronic Warfare' or
                                                    skill == 'Hardware' or
                                                    skill == 'Industrial Mechanic' or
                                                    skill == 'Medicine' or
                                                    skill == 'Nautical Mechanic' or
                                                    skill == 'Software'):
            dicepool = 0
        # Defautable.
        elif skillsDict['LOGSkills'][skill] == 0:
            if skill == 'Computer' or skill == 'Electronic Warfare':
                if attributesDict['averageINT'] < attributesDict['averageLOG']:
                    dicepool = attributesDict['averageLOG'] - 1
                    higherRating = "Logic"
                else:
                    dicepool = attributesDict['averageINT'] - 1
                    higherRating = "Intuition"
            elif skill == 'Software':
                if attributesDict['averageRES'] > attributesDict['averageLOG']:
                    dicepool = attributesDict['averageRES'] - 1
                    higherRating = "Resonance"
                elif attributesDict['averageDEP'] > attributesDict['averageLOG']:
                    dicepool = attributesDict['averageDEP'] - 1
                    higherRating = "Depth"
                else:
                    dicepool = attributesDict['averageLOG'] - 1
                    higherRating = "Logic"
            else:
                dicepool = attributesDict['averageLOG'] - 1
                higherRating = "Logic"
        else:
            if skill == 'Computer' or skill == 'Electronic Warfare':
                if attributesDict['averageINT'] < attributesDict['averageLOG']:
                    dicepool = skillsDict['LOGSkills'][skill] + attributesDict['averageLOG']
                    higherRating = "Logic"
                else:
                    dicepool = skillsDict['LOGSkills'][skill] + attributesDict['averageINT']
                    higherRating = "Intuition"
            elif skill == 'Software':
                if attributesDict['averageRES'] > attributesDict['averageLOG']:
                    dicepool = skillsDict['LOGSkills'][skill] + attributesDict['averageRES']
                    higherRating = "Resonance"
                elif attributesDict['averageDEP'] > attributesDict['averageLOG']:
                    dicepool = skillsDict['LOGSkills'][skill] + attributesDict['averageDEP']
                    higherRating = "Depth"
                else:
                    dicepool = skillsDict['LOGSkills'][skill] + attributesDict['averageLOG']
                    higherRating = "Logic"
            else:
                dicepool = skillsDict['LOGSkills'][skill] + attributesDict['averageLOG']
                higherRating = "Logic"

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def WILSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['WILSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['WILSkills'][skill] == 0 and (skill == 'Astral Combat'):
            dicepool = 0
        # Defautable.
        elif skillsDict['WILSkills'][skill] == 0:
            dicepool = attributesDict['averageWIL'] - 1
        else:
            dicepool = skillsDict['WILSkills'][skill] + attributesDict['averageWIL']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def MAGSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['MAGSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['MAGSkills'][skill] == 0:
            dicepool = 0
        # Defautable.
        # None
        else:
            dicepool = skillsDict['MAGSkills'][skill] + attributesDict['averageMAG']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags


def RESSkills(skillsDict, attributesDict):
    accruedFlags = 0
    higherRating = "Error"
    for skill in skillsDict['RESSkills'].keys():

        # Check for defaulting.
        # Not defautable.
        if skillsDict['RESSkills'][skill] == 0:
            dicepool = 0
        # Defautable.
        # None
        else:
            dicepool = skillsDict['RESSkills'][skill] + attributesDict['averageRES']

        if dicepool > 12:
            # 13-15
            if 13 <= dicepool < 16:
                accruedFlags += 1
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            # 16-17
            elif 16 <= dicepool < 18:
                accruedFlags += 3
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +3 Flag")
            # 18-19
            elif 18 <= dicepool < 20:
                accruedFlags += 5
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")
            # 20+
            elif dicepool >= 20:
                accruedFlags += 7
                print("    [" + skill + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +7 Flag")

    return accruedFlags
