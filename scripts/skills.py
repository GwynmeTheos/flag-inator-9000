# Skill flag checker.


def skillFlagCheck(character, skillsDict, attributesDict):
    accruedFlags = 0

    for currentSkill in character['character']['newskills']['skills']['skill']:

        # Body skills:
        try:
            accruedFlags += BODSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Combat skills:
        try:
            accruedFlags += CombatSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Unarmed Combat skill:
        try:
            accruedFlags += UnarmedCombatSkills(currentSkill, attributesDict)
        except TypeError:
            pass

        # Agility skills:
        try:
            accruedFlags += AGISkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Reaction skills:
        try:
            accruedFlags += REASkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Strength skills:
        try:
            accruedFlags += STRSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Charisma skills:
        try:
            accruedFlags += CHASkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Intuition skills:
        try:
            accruedFlags += INTSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Logic skills:
        try:
            accruedFlags += LOGSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Willpower skills:
        try:
            accruedFlags += WILSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Magic skills:
        try:
            accruedFlags += MAGSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

        # Resonance skills:
        try:
            accruedFlags += RESSkills(currentSkill, skillsDict, attributesDict)
        except TypeError:
            pass

    return accruedFlags


def BODSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['BODSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageBOD']
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def CombatSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['CombatSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            if attributesDict['averageLOG'] > attributesDict['averageAGI']:
                dicepool = skillRating + attributesDict['averageLOG']
                higherRating = "Logic"
            else:
                if attributesDict['averageAGI'] > attributesDict['highestArmAGI']:
                    dicepool = skillRating + attributesDict['averageAGI']
                else:
                    dicepool = skillRating + attributesDict['highestArmAGI']
                higherRating = "Agility"
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def UnarmedCombatSkills(currentSkill, attributesDict):
    if 'Unarmed Combat' == currentSkill['name']:
        accruedFlags = 0

        # Rating check:
        skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
        if skillRating > 7:
            if skillRating == 8 or skillRating == 9:
                accruedFlags += 1
                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
            elif skillRating == 10 or skillRating == 11:
                accruedFlags += 2
                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
            elif skillRating == 12 or skillRating == 13:
                accruedFlags += 4
                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

        # Dicepool check:

        if attributesDict['averageLOG'] > attributesDict['averageAGI']:
            dicepool = skillRating + attributesDict['averageLOG']
            higherRating = "Logic"
        else:
            if attributesDict['averageAGI'] > attributesDict['highestLimbAGI']:
                print(attributesDict['averageAGI'] + ">" + attributesDict['highestLimbAGI'])
                dicepool = skillRating + attributesDict['averageAGI']
            else:
                dicepool = skillRating + attributesDict['highestLimbAGI']
            higherRating = "Agility"

        if not (dicepool - 1 < 12):
            if dicepool == 13 or dicepool == 14 or dicepool == 15:
                accruedFlags += 1
                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
            elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                accruedFlags += 2
                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +2 Flag")
            if dicepool >= 19:
                accruedFlags += 5
                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")

        return accruedFlags


def AGISkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['AGISkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            if currentSkill['name'] == 'Sneaking':
                if attributesDict['averageINT'] > attributesDict['averageAGI']:
                    dicepool = skillRating + attributesDict['averageINT']
                    higherRating = "Intuition"
                else:
                    dicepool = skillRating + attributesDict['averageAGI']
                    higherRating = "Agility"
            elif currentSkill['name'] == 'Escape Artist' or currentSkill['name'] == 'Locksmith':
                if attributesDict['averageLOG'] > attributesDict['averageAGI']:
                    dicepool = skillRating + attributesDict['averageLOG']
                    higherRating = "Logic"
                else:
                    dicepool = skillRating + attributesDict['averageAGI']
                    higherRating = "Agility"
            else:
                dicepool = skillRating + attributesDict['averageAGI']
                higherRating = "Agility"
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def REASkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['REASkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            if attributesDict['averageINT'] > attributesDict['averageREA']:
                dicepool = skillRating + attributesDict['averageINT']
                higherRating = "Intuition"
            else:
                dicepool = skillRating + attributesDict['averageREA']
                higherRating = "Reaction"
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def STRSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['STRSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageSTR']
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Strength at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Strength at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Strength at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def CHASkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['CHASkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageCHA']
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Charisma at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Charisma at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Charisma at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def INTSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['INTSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageINT']

            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Intuition at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Intuition at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Intuition at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def LOGSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['LOGSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            if currentSkill['name'] == 'Computer' or currentSkill['name'] == 'Electronic Warfare':
                if attributesDict['averageINT'] < attributesDict['averageLOG']:
                    dicepool = skillRating + attributesDict['averageLOG']
                    higherRating = "Logic"
                else:
                    dicepool = skillRating + attributesDict['averageINT']
                    higherRating = "Intuition"
            elif currentSkill['name'] == 'Software':
                if attributesDict['averageRES'] > attributesDict['averageLOG']:
                    dicepool = skillRating + attributesDict['averageRES']
                    higherRating = "Resonance"
                else:
                    dicepool = skillRating + attributesDict['averageLOG']
                    higherRating = "Logic"
            else:
                dicepool = skillRating + attributesDict['averageLOG']
                higherRating = "Logic"

            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def WILSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['BODSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageWIL']
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def MAGSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['MAGSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageMAG']
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags


def RESSkills(currentSkill, skillsDict, attributesDict):
    for skill in skillsDict['RESSkills']:
        if skill == currentSkill['name']:
            accruedFlags = 0

            # Rating check:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:
                if skillRating == 8 or skillRating == 9:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +1 Flag")
                elif skillRating == 10 or skillRating == 11:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +2 Flag")
                elif skillRating == 12 or skillRating == 13:
                    accruedFlags += 4
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +4 Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageRES']
            if not (dicepool - 1 < 12):
                if dicepool == 13 or dicepool == 14 or dicepool == 15:
                    accruedFlags += 1
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +1 Flag")
                elif dicepool == 16 or dicepool == 17 or dicepool == 18:
                    accruedFlags += 2
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +2 Flag")
                if dicepool >= 19:
                    accruedFlags += 5
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +5 Flag")

            return accruedFlags
