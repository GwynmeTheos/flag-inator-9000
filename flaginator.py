# Flag-inator 9000

import os
import xmltodict
import math
import time

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

    # The file has been read, time to check for Flags. Initialize the Flag counter and let's start.

    currentFlag = 0
    start_time = time.time()

    # Awakened or Emerged?
    print("\n-> Priority Talent:\n\n", end="")

    if character['character']['prioritytalent'] == "Technomancer":
        currentFlag += 3
        print("    [Technomancer] = +3 Flag")

    elif character['character']['prioritytalent'] == "Aspected Magician":
        currentFlag += 1
        print("    [Aspected Magician] = +1 Flag")

    elif character['character']['prioritytalent'] == "Adept":
        currentFlag += 2
        print("    [Adept] = +2 Flag")

    elif character['character']['prioritytalent'] == "Magician":
        currentFlag += 3
        print("    [Magician] = +3 Flag")

    elif character['character']['prioritytalent'] == "Mystic Adept":
        currentFlag += 7
        print("    [Mystic Adept] = +7 Flag")

    # Initiation Grade
    print("\n-> Initiation Grade:\n\n", end="")

    if character['character']['magenabled'] == "True" and character['character']['initiategrade'] != "0":
        initiationGrade = int(character['character']['initiategrade'])
        for grade in range(1, initiationGrade + 1, 1):
            if 1 <= grade < 4:
                currentFlag += 1
                print("    [Initiatiate Grade " + str(grade) + "] = +1 Flag")
            elif 4 <= grade < 7:
                currentFlag += 2
                print("    [Initiatiate Grade " + str(grade) + "] = +2 Flag")
            elif 7 <= grade:
                currentFlag += math.ceil(grade / 2)
                print("    [Initiatiate Grade " + str(grade) + "] = +" + str(math.ceil(grade / 2)) + " Flag")

        for art in character['character']['arts']['art']:
            if art['name'] == "Blood Magic":
                currentFlag += 5
                print("\n    [Blood Magic] = +5 Flag")

    # Cyber/Bio/Gene/Nano'ware
    print("\n-> 'Ware:\n\n", end="")

    if character['character']['totaless'] != "6.0":
        for cyberware in character['character']['cyberwares']['cyberware']:
            if cyberware['name'] == "Adapsin":
                currentFlag += 1
                print("    [Adapsin] = +1 Flag")

            elif cyberware['name'] == "Pain Editor":
                currentFlag += 2
                print("    [Pain Editor] = +2 Flag")

            elif cyberware['name'].find("Move-by-Wire") != -1 and (
                    cyberware['rating'] == "2" or cyberware['rating'] == "3"):
                currentFlag += 1
                print("    [Move-By-Wire System Rating 2-3] = +1 Flag")

            elif cyberware['name'].find("Genetic Optimization") != -1:
                currentFlag += 1
                print("    [" + cyberware['name'] + "] = +1 Flag")

            elif cyberware['name'] == "Narco":
                currentFlag += 1
                print("    [Narco] = +1 Flag")

    # Skill Ratings and Total Dicepool
    print("\n-> Skills:\n\n", end="")

    # Forgive me, lord, for what I am going to do.

    # Every skill in Shadowrun:
    BODSkills = ['Diving', 'Free-Fall']
    CombatSkills = ['Archery', 'Automatics', 'Blades', 'Clubs', 'Gunnery', 'Heavy Weapons', 'Longarms', 'Palming',
                    'Pistols', 'Throwing Weapons']
    AGISkills = ['Escape Artist', 'Flight', 'Gymnastics', 'Locksmith', 'Sneaking']
    REASkills = ['Pilot Aerospace', 'Pilot Aircraft', 'Pilot Ground Craft', 'Pilot Walker', 'Pilot Watercraft']
    STRSkills = ['Running', 'Swimming']
    CHASkills = ['Animal Handling', 'Con', 'Etiquette', 'Impersonation', 'Instruction', 'Intimidation', 'Leadership',
                 'Negotiation', 'Performance']
    INTSkills = ['Artisan', 'Assensing', 'Disguise', 'Navigation', 'Perception', 'Tracking']
    LOGSkills = ['Aeronautics Mechanic', 'Arcana', 'Armorer', 'Automotive Mechanic', 'Biotechnology', 'Chemistry',
                 'Computer', 'Cybercombat', 'Cybertechnology', 'Demolitions', 'Electronic Warfare', 'First Aid',
                 'Forgery', 'Hacking', 'Hardware', 'Industrial Mechanic', 'Medicine', 'Nautical Mechanic', 'Software']
    WILSkills = ['Astral Combat', 'Survival']
    MAGSkills = ['Alchemy', 'Artificing', 'Banishing', 'Binding', 'Counterspelling', 'Disenchanting',
                 'Ritual Spellcasting', 'Spellcasting', 'Summoning']
    RESSkills = ['Compiling', 'Decompiling', 'Registering']

    # The character's attributes:
    attributes = dict()
    for att in character['character']['attributes']['attribute']:
        attRating = int(att['base']) + int(att['karma']) + int(att['metatypemin'])
        attributes[att['name']] = attRating

    # Find and add the highest limb's AGI rating.
    highestLimbAGI = 0
    try:
        for limb in character['character']['cyberwares']['cyberware']:
            if limb['category'] == 'Cyberlimb':
                if limb['children']['cyberware']['name'] == "Customized Agility":
                    if int(limb['children']['cyberware']['rating']) > highestLimbAGI:
                        highestLimbAGI = int(limb['children']['cyberware']['rating'])
        attributes['highestLimbAGI'] = highestLimbAGI
    except TypeError:
        attributes['highestLimbAGI'] = 0

    # Find and add the highest arm's AGI rating.
    highestArmAGI = 0
    try:
        for limb in character['character']['cyberwares']['cyberware']:
            if limb['limbslot'] == 'arm':
                if limb['children']['cyberware']['name'] == "Customized Agility":
                    if int(limb['children']['cyberware']['rating']) > highestLimbAGI:
                        highestLimbAGI = int(limb['children']['cyberware']['rating'])
        attributes['highestArmAGI'] = highestArmAGI
    except TypeError:
        attributes['highestArmAGI'] = 0

    # If they have any Improvements that increase their skill rating, we need to find those.
    skillImprovements = dict()
    for skill in character['character']['improvements']['improvement']:
        if skill['customid'] == 'skilllevel':
            skillImprovements[skill['improvedname']] = int(skill['val'])

    for currentSkill in character['character']['newskills']['skills']['skill']:

        # Body skills:
        for skill in BODSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['BOD']
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Body at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                break

        # Combat skills:
        for skill in CombatSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                if attributes['LOG'] > attributes['AGI']:
                    dicepool = skillRating + attributes['LOG']
                    higherRating = "Logic"
                else:
                    if attributes['AGI'] > attributes['highestArmAGI']:
                        dicepool = skillRating + attributes['AGI']
                    else:
                        dicepool = skillRating + attributes['highestArmAGI']
                    higherRating = "Agility"
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) +
                          " dicepool] = +" + str(accruedFlags) + " Flag")
                break

        # Unarmed Combat skill:
        if 'Unarmed Combat' == currentSkill['name']:
            # Rating check:
            try:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements['Unarmed Combat']
            except KeyError:
                skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
            if skillRating >= 7:
                accruedFlags = 0
                if skillRating >= 8:
                    accruedFlags += 1
                if skillRating >= 9:
                    accruedFlags += 1
                if skillRating >= 10:
                    accruedFlags += 2
                if skillRating >= 11:
                    accruedFlags += 2
                if skillRating >= 12:
                    accruedFlags += 4
                if skillRating >= 13:
                    accruedFlags += 4
                currentFlag += accruedFlags
                print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                    accruedFlags) + " Flag")

            # Dicepool check:
            if attributes['LOG'] > attributes['AGI']:
                dicepool = skillRating + attributes['LOG']
                higherRating = "Logic"
            else:
                if attributes['AGI'] > attributes['highestLimbAGI']:
                    dicepool = skillRating + attributes['AGI']
                else:
                    dicepool = skillRating + attributes['highestLimbAGI']
                higherRating = "Agility"
            if not (dicepool - 1 <= 12):
                accruedFlags = 0
                if dicepool >= 13:
                    accruedFlags += 1
                if dicepool >= 14:
                    accruedFlags += 1
                if dicepool >= 15:
                    accruedFlags += 1
                if dicepool >= 16:
                    accruedFlags += 2
                if dicepool >= 17:
                    accruedFlags += 2
                if dicepool >= 18:
                    accruedFlags += 2
                if dicepool >= 19:
                    for ratingOver19 in range(19, dicepool + 1, 1):
                        accruedFlags += 5
                currentFlag += accruedFlags
                print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) +
                      " dicepool] = +" + str(accruedFlags) + " Flag")
            break

        # Agility skills:
        for skill in AGISkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                if currentSkill['name'] == 'Sneaking':
                    if attributes['INT'] > attributes['AGI']:
                        dicepool = skillRating + attributes['INT']
                        higherRating = "Intuition"
                    else:
                        dicepool = skillRating + attributes['AGI']
                        higherRating = "Agility"
                elif currentSkill['name'] == 'Escape Artist' or currentSkill['name'] == 'Locksmith':
                    if attributes['LOG'] > attributes['AGI']:
                        dicepool = skillRating + attributes['INT']
                        higherRating = "Logic"
                    else:
                        dicepool = skillRating + attributes['AGI']
                        higherRating = "Agility"
                else:
                    dicepool = skillRating + attributes['AGI']
                    higherRating = "Agility"
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +"
                          + str(accruedFlags) + " Flag")
                break

        # Reaction skills:
        for skill in CombatSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = +" + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                if attributes['INT'] > attributes['REA']:
                    dicepool = skillRating + attributes['INT']
                    higherRating = "Intuition"
                else:
                    dicepool = skillRating + attributes['REA']
                    higherRating = "Reaction"
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) +
                          " dicepool] = +" + str(accruedFlags) + " Flag")
                break

        # Strength skills:
        for skill in STRSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['STR']
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Strength at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                break

        # Charisma skills:
        for skill in CHASkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['CHA']
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Charisma at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                break

        # Intuition skills:
        for skill in INTSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['INT']

                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, (dicepool + 1), 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Intuition at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                break

        # Logic skills:
        for skill in LOGSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                if currentSkill['name'] == 'Computer' or currentSkill['name'] == 'Electronic Warfare':
                    if attributes['INT'] > attributes['LOG']:
                        dicepool = skillRating + attributes['LOG']
                        higherRating = "Logic"
                    else:
                        dicepool = skillRating + attributes['INT']
                        higherRating = "Intuition"
                elif currentSkill['name'] == 'Software':
                    if attributes['RES'] > attributes['LOG']:
                        dicepool = skillRating + attributes['RES']
                        higherRating = "Resonance"
                    else:
                        dicepool = skillRating + attributes['LOG']
                        higherRating = "Logic"
                else:
                    dicepool = skillRating + attributes['LOG']
                    higherRating = "Logic"

                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + " + higherRating + " at " + str(dicepool) + " dicepool] = +"
                          + str(accruedFlags) + " Flag")
                break

        # Willpower skills:
        for skill in BODSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['BOD']
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Willpower at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                break

        # Magic skills:
        for skill in MAGSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['MAG']
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Magic at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                break

        # Resonance skills:
        for skill in RESSkills:
            if skill == currentSkill['name']:
                # Rating check:
                try:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base']) + skillImprovements[skill]
                except KeyError:
                    skillRating = int(currentSkill['karma']) + int(currentSkill['base'])
                if skillRating >= 7:
                    accruedFlags = 0
                    if skillRating >= 8:
                        accruedFlags += 1
                    if skillRating >= 9:
                        accruedFlags += 1
                    if skillRating >= 10:
                        accruedFlags += 2
                    if skillRating >= 11:
                        accruedFlags += 2
                    if skillRating >= 12:
                        accruedFlags += 4
                    if skillRating >= 13:
                        accruedFlags += 4
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " at Rating " + str(skillRating) + "] = + " + str(
                        accruedFlags) + " Flag")

                # Dicepool check:
                dicepool = skillRating + attributes['RES']
                if not (dicepool - 1 <= 12):
                    accruedFlags = 0
                    if dicepool >= 13:
                        accruedFlags += 1
                    if dicepool >= 14:
                        accruedFlags += 1
                    if dicepool >= 15:
                        accruedFlags += 1
                    if dicepool >= 16:
                        accruedFlags += 2
                    if dicepool >= 17:
                        accruedFlags += 2
                    if dicepool >= 18:
                        accruedFlags += 2
                    if dicepool >= 19:
                        for ratingOver19 in range(19, dicepool+1, 1):
                            accruedFlags += 5
                    currentFlag += accruedFlags
                    print("    [" + currentSkill['name'] + " + Resonance at " + str(dicepool) + " dicepool] = +" + str(
                        accruedFlags) + " Flag")
                continue

    # Skill Ratings and Total Dicepool
    print("\n-> Attributes:\n\n", end="")

    

    print("\nTotal Flag Points: " + str(currentFlag))

    print("--- Finished in %s seconds ---" % (time.time() - start_time))
    input("\nPress enter to continue...")
