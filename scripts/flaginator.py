# Flag-inator 9000

import os
import xmltodict
import math
import time


def createSkillDict():
    # Every skill in Shadowrun:
    skillsDict = dict()

    skillsDict['BODSkills'] = ['Diving', 'Free-Fall']
    skillsDict['CombatSkills'] = ['Archery', 'Automatics', 'Blades', 'Clubs', 'Gunnery', 'Heavy Weapons', 'Longarms',
                                  'Palming', 'Pistols', 'Throwing Weapons']
    skillsDict['AGISkills'] = ['Escape Artist', 'Flight', 'Gymnastics', 'Locksmith', 'Sneaking']
    skillsDict['REASkills'] = ['Pilot Aerospace', 'Pilot Aircraft', 'Pilot Ground Craft', 'Pilot Walker',
                               'Pilot Watercraft']
    skillsDict['STRSkills'] = ['Running', 'Swimming']
    skillsDict['CHASkills'] = ['Animal Handling', 'Con', 'Etiquette', 'Impersonation', 'Instruction', 'Intimidation',
                               'Leadership', 'Negotiation', 'Performance']
    skillsDict['INTSkills'] = ['Artisan', 'Assensing', 'Disguise', 'Navigation', 'Perception', 'Tracking']
    skillsDict['LOGSkills'] = ['Aeronautics Mechanic', 'Arcana', 'Armorer', 'Automotive Mechanic', 'Biotechnology',
                               'Chemistry', 'Computer', 'Cybercombat', 'Cybertechnology', 'Demolitions',
                               'Electronic Warfare', 'First Aid', 'Forgery', 'Hacking', 'Hardware',
                               'Industrial Mechanic', 'Medicine', 'Nautical Mechanic', 'Software']
    skillsDict['WILSkills'] = ['Astral Combat', 'Survival']
    skillsDict['MAGSkills'] = ['Alchemy', 'Artificing', 'Banishing', 'Binding', 'Counterspelling', 'Disenchanting',
                               'Ritual Spellcasting', 'Spellcasting', 'Summoning']
    skillsDict['RESSkills'] = ['Compiling', 'Decompiling', 'Registering']

    return skillsDict


def createAttributeDict(character):
    # The character's innate attributes:
    attributesDict = dict()

    for att in character['character']['attributes']['attribute']:
        attRating = int(att['base']) + int(att['karma']) + int(att['metatypemin'])
        attributesDict[att['name']] = attRating
        attributesDict[str('average' + att['name'])] = int(att['totalvalue'])

    # Find and add the highest limb's AGI rating.
    highestLimbAGI = 0
    try:
        for limb in character['character']['cyberwares']['cyberware']:
            limbAGI = 0
            if limb['category'] == 'Cyberlimb':
                if limb['children']['cyberware']['name'] == "Customized Agility":
                    limbAGI = int(limb['children']['cyberware']['rating'])
                elif limb['children']['cyberware']['name'] == "Enhanced Agility":
                    limbAGI += int(limb['children']['cyberware']['rating'])
                if limbAGI > highestLimbAGI:
                    highestLimbAGI = limbAGI
        attributesDict['highestLimbAGI'] = highestLimbAGI
    except TypeError:
        attributesDict['highestLimbAGI'] = 0

    # Find and add the highest arm's AGI rating.
    highestArmAGI = 0
    try:
        for limb in character['character']['cyberwares']['cyberware']:
            if limb['limbslot'] == 'arm':
                armAGI = 0
                if limb['children']['cyberware']['name'] == "Customized Agility":
                    armAGI = int(limb['children']['cyberware']['rating'])
                elif limb['children']['cyberware']['name'] == "Enhanced Agility":
                    armAGI += int(limb['children']['cyberware']['rating'])
                if armAGI > highestArmAGI:
                    highestArmAGI = armAGI
        attributesDict['highestArmAGI'] = highestArmAGI
    except TypeError:
        attributesDict['highestArmAGI'] = 0

    return attributesDict


def createImprovementDict(character):
    skillImprovementsDict = dict()

    for skill in character['character']['improvements']['improvement']:
        if skill['customid'] == 'skilllevel':
            skillImprovementsDict[skill['improvedname']] = int(skill['val'])

    return skillImprovementsDict


def talentFlagCheck(character):
    accruedFlags = 0

    if character['character']['prioritytalent'] == "Technomancer":
        accruedFlags += 3
        print("    [Technomancer] = +3 Flag")

    elif character['character']['prioritytalent'] == "Aspected Magician":
        accruedFlags += 1
        print("    [Aspected Magician] = +1 Flag")

    elif character['character']['prioritytalent'] == "Adept":
        accruedFlags += 2
        print("    [Adept] = +2 Flag")

    elif character['character']['prioritytalent'] == "Magician":
        accruedFlags += 3
        print("    [Magician] = +3 Flag")

    elif character['character']['prioritytalent'] == "Mystic Adept":
        accruedFlags += 7
        print("    [Mystic Adept] = +7 Flag")

    return accruedFlags


def initiateFlagCheck(character):
    accruedFlags = 0

    if character['character']['magenabled'] == "True" and character['character']['initiategrade'] != "0":
        initiationGrade = int(character['character']['initiategrade'])
        for grade in range(1, initiationGrade + 1, 1):
            if 1 <= grade < 4:
                accruedFlags += 1
                print("    [Initiatiate Grade " + str(grade) + "] = +1 Flag")
            elif 4 <= grade < 7:
                accruedFlags += 2
                print("    [Initiatiate Grade " + str(grade) + "] = +2 Flag")
            elif 7 <= grade:
                accruedFlags += math.ceil(grade / 2)
                print("    [Initiatiate Grade " + str(grade) + "] = +" + str(math.ceil(grade / 2)) + " Flag")

        for art in character['character']['arts']['art']:
            if art['name'] == "Blood Magic":
                accruedFlags += 5
                print("\n    [Blood Magic] = +5 Flag")

    return accruedFlags


def wareFlagCheck(character):
    accruedFlags = 0

    for ware in character['character']['cyberwares']['cyberware']:
        if ware['name'] == 'Adapsin':
            accruedFlags += 1
            print("\n    [Adapsin] = +1 Flag")
        elif ware['name'] == 'Pain Editor':
            accruedFlags += 2
            print("\n    [Pain Editor] = +1 Flag")
        elif ware['name'] == 'Move-by-Wire' and (ware['rating'] == '2' or ware['rating'] == '3'):
            accruedFlags += 1
            print("\n    [MBW Rating 2 or 3] = +1 Flag")
        elif ware['name'].find('Genetic Optmization'):
            accruedFlags += 1
            print("\n    [" + ware['name'] + "] = +1 Flag")
        elif ware['name'] == 'Narco':
            accruedFlags += 1
            print("\n    [Narco] = +1 Flag")

    return accruedFlags


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


def attributeFlagCheck(character, attributesDict):
    accruedFlags = 0

    # Attributes at 1:


while True:
    os.system("CLS")
    print("""------------> WELCOME TO THE FLAG-INATOR 9000 <------------\n
Please type the full name of the file that you'd like to calculate the flag points of.
Exclude the \".chum5\" portion. Make sure the file is in the same directory as this script.
\n""", end="")

    filename = input("File name: ")

    print("\n-----------------------------------------------------------")

    # Attempt to read and parse the Chummer file, if it doesn't work, send out an error message.
    try:
        with open(str(filename + ".chum5"), mode="r", encoding="utf-8") as file:
            character = xmltodict.parse(file.read())
    except FileNotFoundError:
        print("""\nThis filename specified is wrong or the file is missing.\n
1) Make sure that the filename does NOT include the file extension: \".chum5\";
2) That the name is spelt correctly (case sensitive);
3) That the file is in the same directory as this script.

If this issue persists, call Arisu-sensei.
\n""", end="")

        input("Press enter to continue...")
        continue

    # The file has been read.

    # Initialize the flag counter.
    currentFlag = 0

    # Create the dictionaries for the skills and the character's attributes.
    skillsDict = createSkillDict()
    attributesDict = createAttributeDict(character)
    # If they have any Improvements that increase their skill rating, we need to find those.
    skillImprovements = createImprovementDict(character)

    # For performance checking.
    start_time = time.time()

    # Awakened or Emerged?
    print("\n-> Priority Talent:\n\n", end="")
    currentFlag += talentFlagCheck(character)

    # Initiation Grade
    print("\n-> Initiation Grade:\n\n", end="")
    currentFlag += initiateFlagCheck(character)

    # Cyber/Bio/Gene/Nano'ware
    print("\n-> 'Ware:\n\n", end="")
    currentFlag += wareFlagCheck(character)

    # Skill Ratings and Total Dicepool
    print("\n-> Skills:\n\n", end="")
    currentFlag += skillFlagCheck(character, skillsDict, attributesDict, skillImprovements)

    # Attributes
    print("\n-> Attributes:\n\n", end="")
    # currentFlag += attributeFlagCheck(character, attributesDict)

    print("\nTotal Flag Points: " + str(currentFlag))

    print("--- Finished in %s seconds ---" % (time.time() - start_time))
    input("\nPress enter to continue...")
