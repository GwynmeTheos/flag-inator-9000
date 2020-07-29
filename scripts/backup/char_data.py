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
