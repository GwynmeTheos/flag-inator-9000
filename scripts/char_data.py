# Useful dictionaries script.


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
        limbCount = 0
        for limb in character['character']['cyberwares']['cyberware']:
            limbAGI = 0

            if limb['category'] == 'Cyberlimb':
                try:
                    if limb['limbslot'] == 'arm' or limb['limbslot'] == 'leg':
                        limbCount += 1
                    for mods in limb['children']['cyberware']:
                        # Normal Limbs
                        if mods['name'] == 'Customized Agility' or mods['name'] == "Enhanced Agility":
                            limbAGI += int(mods['rating'])
                        # Centaur Liminal Body
                        elif mods['category'] == 'Cyberlimb':
                            try:
                                for limBodyMods in mods['children']['cyberware']:
                                    if limBodyMods['name'] == 'Customized Agility' or limBodyMods['name'] == "Enhanced Agility":
                                        limbAGI += int(limBodyMods['rating'])
                            except TypeError:
                                pass
                except TypeError:
                    pass
            if limbAGI > highestLimbAGI:
                highestLimbAGI = limbAGI
        attributesDict['highestLimbAGI'] = highestLimbAGI
        if 2 <= limbCount <= 3:
            attributesDict['highestLimbAGI'] += 1
        elif limbCount >= 4:
            attributesDict['highestLimbAGI'] += 2
    except TypeError:
        attributesDict['highestLimbAGI'] = 0

    # Find and add the highest limb's STR rating.
    highestLimbSTR = 0
    try:
        limbCount = 0
        for limb in character['character']['cyberwares']['cyberware']:
            limbSTR = 0

            if limb['category'] == 'Cyberlimb':
                try:
                    if limb['limbslot'] == 'arm' or limb['limbslot'] == 'leg':
                        limbCount += 1
                    for mods in limb['children']['cyberware']:
                        # Normal Limbs
                        if mods['name'] == 'Customized Strength' or mods['name'] == "Enhanced Strength":
                            limbSTR += int(mods['rating'])
                        # Centaur Liminal Body
                        elif mods['category'] == 'Cyberlimb':
                            try:
                                for limBodyMods in mods['children']['cyberware']:
                                    if limBodyMods['name'] == 'Customized Strength' or limBodyMods['name'] == "Enhanced Strength":
                                        limbSTR += int(limBodyMods['rating'])
                            except TypeError:
                                pass
                except TypeError:
                    pass
            if limbSTR > highestLimbSTR:
                highestLimbSTR = limbSTR
        attributesDict['highestLimbSTR'] = highestLimbSTR
        if 2 <= limbCount <= 3:
            attributesDict['highestLimbSTR'] += 1
        elif limbCount >= 4:
            attributesDict['highestLimbSTR'] += 2
    except TypeError:
        attributesDict['highestLimbSTR'] = 0

    # Find and add the highest arm's AGI rating.
    highestArmAGI = 0
    try:
        limbCount = 0
        for limb in character['character']['cyberwares']['cyberware']:
            armAGI = 0
            if limb['limbslot'] == 'arm' or limb['limbslot'] == 'leg':
                limbCount += 1
            if limb['limbslot'] == 'arm':
                try:
                    for mods in limb['children']['cyberware']:
                        # Normal Limbs
                        if mods['name'] == 'Customized Agility' or mods['name'] == 'Enhanced Agility':
                            armAGI += int(mods['rating'])
                        # Centaur Liminal body
                        elif mods['category'] == 'Cyberlimbs':
                            try:
                                for limBodyMods in mods['children']['cyberware']:
                                    if limBodyMods['name'] == 'Customized Agility' or limBodyMods['name'] == "Enhanced Agility":
                                        armAGI += int(limBodyMods['rating'])
                            except TypeError:
                                pass

                except TypeError:
                    pass

                if armAGI > highestArmAGI:
                    highestArmAGI = armAGI
        attributesDict['highestArmAGI'] = highestArmAGI
        if 2 <= limbCount <= 3:
            attributesDict['highestArmAGI'] += 1
        elif limbCount >= 4:
            attributesDict['highestArmAGI'] += 2
    except TypeError:
        attributesDict['highestArmAGI'] = 0

    # Find and add the highest arm's AGI rating.
    highestArmSTR = 0
    try:
        limbCount = 0
        for limb in character['character']['cyberwares']['cyberware']:
            armSTR = 0
            if limb['limbslot'] == 'arm' or limb['limbslot'] == 'leg':
                limbCount += 1
            if limb['limbslot'] == 'arm':
                try:
                    for mods in limb['children']['cyberware']:
                        # Normal Limbs
                        if mods['name'] == 'Customized Strength' or mods['name'] == 'Enhanced Strength':
                            armSTR += int(mods['rating'])
                        # Centaur Liminal body
                        elif mods['category'] == 'Cyberlimbs':
                            try:
                                for limBodyMods in mods['children']['cyberware']:
                                    if limBodyMods['name'] == 'Customized Strength' or limBodyMods['name'] == "Enhanced Strength":
                                        armSTR += int(limBodyMods['rating'])
                            except TypeError:
                                pass

                except TypeError:
                    pass

                if armSTR > highestArmSTR:
                    highestArmSTR = armSTR
        attributesDict['highestArmSTR'] = highestArmSTR
        if 2 <= limbCount <= 3:
            attributesDict['highestArmSTR'] += 1
        elif limbCount >= 4:
            attributesDict['highestArmSTR'] += 2
    except TypeError:
        attributesDict['highestArmSTR'] = 0

    return attributesDict


# def createImprovementDict(character):
#    skillImprovementsDict = dict()
#
#    for skill in character['character']['improvements']['improvement']:
#        if skill['customid'] == 'skilllevel':
#            skillImprovementsDict[skill['improvedname']] = int(skill['val'])
#
#    return skillImprovementsDict
