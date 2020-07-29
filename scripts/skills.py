# Skill flag checker.


def skillFlagCheck(character, skillsDict, attributesDict, skillImprovements):
    accruedFlags = 0

    for currentSkill in character['character']['newskills']['skills']['skill']:

        # Body skills:
        try:
            accruedFlags += BODSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Combat skills:
        try:
            accruedFlags += CombatSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Unarmed Combat skill:
        try:
            accruedFlags += UnarmedCombatSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Agility skills:
        try:
            accruedFlags += AGISkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Reaction skills:
        try:
            accruedFlags += REASkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Strength skills:
        try:
            accruedFlags += STRSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Charisma skills:
        try:
            accruedFlags += CHASkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Intuition skills:
        try:
            accruedFlags += INTSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Logic skills:
        try:
            accruedFlags += LOGSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Willpower skills:
        try:
            accruedFlags += WILSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Magic skills:
        try:
            accruedFlags += MAGSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

        # Resonance skills:
        try:
            accruedFlags += RESSkills(currentSkill, attributesDict, skillImprovements)
        except TypeError:
            pass

    return accruedFlags


def BODSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['BODSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageBOD']
            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def CombatSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['CombatSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

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

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) +
                      " dicepool] = +" + str(dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def UnarmedCombatSkills(currentSkill, attributesDict, skillImprovements):
    if 'Unarmed Combat' == currentSkill['name']:

        ratingFlags = 0
        dicepoolFlags = 0

        # Rating check:
        try:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[
                'Unarmed Combat']
        except KeyError:
            skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
        if skillRating > 7:

            if skillRating >= 8:
                ratingFlags += 1
            if skillRating >= 9:
                ratingFlags += 1
            if skillRating >= 10:
                ratingFlags += 2
            if skillRating >= 11:
                ratingFlags += 2
            if skillRating >= 12:
                ratingFlags += 4
            if skillRating >= 13:
                ratingFlags += 4

            print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                ratingFlags) + " Flag")

        # Dicepool check:
        if attributesDict['averageLOG'] > attributesDict['averageAGI']:
            dicepool = skillRating + attributesDict['averageLOG']
            higherRating = "Logic"
        else:
            if attributesDict['averageAGI'] > attributesDict['highestLimbAGI']:
                dicepool = skillRating + attributesDict['averageAGI']
            else:
                dicepool = skillRating + attributesDict['highestLimbAGI']
            higherRating = "Agility"

        if not (dicepool - 1 < 12):

            if dicepool >= 13:
                dicepoolFlags += 1
            if dicepool >= 14:
                dicepoolFlags += 1
            if dicepool >= 15:
                dicepoolFlags += 1
            if dicepool >= 16:
                dicepoolFlags += 2
            if dicepool >= 17:
                dicepoolFlags += 2
            if dicepool >= 18:
                dicepoolFlags += 2
            if dicepool >= 19:
                for ratingOver19 in range(19, dicepool + 1, 1):
                    dicepoolFlags += 5

            print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) +
                  " dicepool] = +" + str(dicepoolFlags) + " Flag")

        return ratingFlags + dicepoolFlags


def AGISkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['AGISkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            if currentSkill['name'] == 'Sneaking':
                if attributesDict['averageINT'] > attributesDict['averageAGI']:
                    dicepool = skillRating + attributesDict['averageINT']
                    higherRating = "Intuition"
                else:
                    dicepool = skillRating + attributesDict['AGI']
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

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(
                    dicepool) + " dicepool] = +"
                      + str(dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def REASkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['CombatSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +" + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            if attributesDict['averageINT'] > attributesDict['averageREA']:
                dicepool = skillRating + attributesDict['averageINT']
                higherRating = "Intuition"
            else:
                dicepool = skillRating + attributesDict['averageREA']
                higherRating = "Reaction"
            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) +
                      " dicepool] = +" + str(dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def STRSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['STRSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageSTR']
            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Strength at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def CHASkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['CHASkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageCHA']
            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Charisma at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def INTSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['INTSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageINT']

            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, (dicepool + 1), 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Intuition at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def LOGSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['LOGSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

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

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(
                    dicepool) + " dicepool] = +"
                      + str(dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def WILSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['BODSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageWIL']
            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Willpower at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def MAGSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['MAGSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageMAG']
            if not (dicepool - 1 < 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Magic at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags


def RESSkills(currentSkill, skillsDict, attributesDict, skillImprovements):
    for skill in skillsDict['RESSkills']:
        if skill == currentSkill['name']:

            ratingFlags = 0
            dicepoolFlags = 0

            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating > 7:

                if skillRating >= 8:
                    ratingFlags += 1
                if skillRating >= 9:
                    ratingFlags += 1
                if skillRating >= 10:
                    ratingFlags += 2
                if skillRating >= 11:
                    ratingFlags += 2
                if skillRating >= 12:
                    ratingFlags += 4
                if skillRating >= 13:
                    ratingFlags += 4

                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    ratingFlags) + " Flag")

            # Dicepool check:
            dicepool = skillRating + attributesDict['averageRES']
            if not (dicepool - 1 <= 12):

                if dicepool >= 13:
                    dicepoolFlags += 1
                if dicepool >= 14:
                    dicepoolFlags += 1
                if dicepool >= 15:
                    dicepoolFlags += 1
                if dicepool >= 16:
                    dicepoolFlags += 2
                if dicepool >= 17:
                    dicepoolFlags += 2
                if dicepool >= 18:
                    dicepoolFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        dicepoolFlags += 5

                print("    [" + currentSkill['name'] + " + Resonance at " + str(dicepool) + " dicepool] = +" + str(
                    dicepoolFlags) + " Flag")

            return ratingFlags + dicepoolFlags
