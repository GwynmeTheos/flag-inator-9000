# Useful dictionaries script.


def createSkillDict(character):
    # We will pre-count all of the important skill dicepools.
    skillsDict = dict()

    # First, name every single skill in the game.
    skillsDict['BODSkills'] = {'Diving': 0,
                               'Free-Fall': 0}
    skillsDict['CombatSkills'] = {'Archery': 0,
                                  'Automatics': 0,
                                  'Blades': 0,
                                  'Clubs': 0,
                                  'Gunnery': 0,
                                  'Heavy Weapons': 0,
                                  'Longarms': 0,
                                  'Palming': 0,
                                  'Pistols': 0,
                                  'Throwing Weapons': 0,
                                  'Unarmed Combat': 0}
    skillsDict['AGISkills'] = {'Escape Artist': 0,
                               'Flight': 0,
                               'Gymnastics': 0,
                               'Locksmith': 0,
                               'Sneaking': 0}
    skillsDict['REASkills'] = {'Pilot Aerospace': 0,
                               'Pilot Aircraft': 0,
                               'Pilot Ground Craft': 0,
                               'Pilot Walker': 0,
                               'Pilot Watercraft': 0}
    skillsDict['STRSkills'] = {'Running': 0,
                               'Swimming': 0}
    skillsDict['CHASkills'] = {'Animal Handling': 0,
                               'Con': 0,
                               'Etiquette': 0,
                               'Impersonation': 0,
                               'Instruction': 0,
                               'Intimidation': 0,
                               'Leadership': 0,
                               'Negotiation': 0,
                               'Performance': 0}
    skillsDict['INTSkills'] = {'Artisan': 0,
                               'Assensing': 0,
                               'Disguise': 0,
                               'Navigation': 0,
                               'Perception': 0,
                               'Tracking': 0}
    skillsDict['LOGSkills'] = {'Aeronautics Mechanic': 0,
                               'Arcana': 0,
                               'Armorer': 0,
                               'Automotive Mechanic': 0,
                               'Biotechnology': 0,
                               'Chemistry': 0,
                               'Computer': 0,
                               'Cybercombat': 0,
                               'Cybertechnology': 0,
                               'Demolitions': 0,
                               'Electronic Warfare': 0,
                               'First Aid': 0,
                               'Forgery': 0,
                               'Hacking': 0,
                               'Hardware': 0,
                               'Industrial Mechanic': 0,
                               'Medicine': 0,
                               'Nautical Mechanic': 0,
                               'Software': 0}
    skillsDict['WILSkills'] = {'Astral Combat': 0,
                               'Survival': 0}
    skillsDict['MAGSkills'] = {'Alchemy': 0,
                               'Artificing': 0,
                               'Banishing': 0,
                               'Binding': 0,
                               'Counterspelling': 0,
                               'Disenchanting': 0,
                               'Ritual Spellcasting': 0,
                               'Spellcasting': 0,
                               'Summoning': 0}
    skillsDict['RESSkills'] = {'Compiling': 0,
                               'Decompiling': 0,
                               'Registering': 0}
    skillsDict['EXOSkills'] = list()

    # Loop through every single skill and add the skill rating to the dicepool.
    for skill in character['character']['newskills']['skills']['skill']:
        try:
            for skillList in skillsDict.keys():
                try:
                    for skillName in skillsDict[skillList].keys():
                        if skillName == skill['name']:
                            skillsDict[skillList][skillName] += int(skill['karma']) + int(skill['base'])
                except AttributeError:
                    # Getting to EXOSkills breaks it, so this is here to just pass.
                    pass
        except KeyError:
            # It is an exotic skill.
            skillsDict['EXOSkills'].append({'Name': "Exotic: " + skill['specific'],
                                            'Rating': int(skill['karma']) + int(skill['base']),
                                            'Category': skill['skillcategory']})

    # Loop through the skill groups and add the skill group rating.
    for skillGroup in character['character']['newskills']['groups']['group']:
        if skillGroup['name'] == "Tasking":
            skillsDict['RESSkills']['Compiling'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['RESSkills']['Decompiling'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['RESSkills']['Registering'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Stealth":
            skillsDict['INTSkills']['Disguise'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CombatSkills']['Palming'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['AGISkills']['Sneaking'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Sorcery":
            skillsDict['MAGSkills']['Counterspelling'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['MAGSkills']['Ritual Spellcasting'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['MAGSkills']['Spellcasting'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Outdoors":
            skillsDict['INTSkills']['Navigation'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['WILSkills']['Survival'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['INTSkills']['Tracking'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Engineering":
            skillsDict['LOGSkills']['Aeronautics Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Automotive Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Industrial Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Nautical Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Influence":
            skillsDict['CHASkills']['Etiquette'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CHASkills']['Leadership'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CHASkills']['Negotiation'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Firearms":
            skillsDict['CombatSkills']['Automatics'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CombatSkills']['Longarms'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CombatSkills']['Pistols'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Enchanting":
            skillsDict['MAGSkills']['Alchemy'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['MAGSkills']['Artificing'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['MAGSkills']['Disenchanting'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Electronics":
            skillsDict['LOGSkills']['Computer'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Hardware'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Software'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Cracking":
            skillsDict['LOGSkills']['Cybercombat'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Electronic Warfare'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Hacking'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Conjuring":
            skillsDict['MAGSkills']['Banishing'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['MAGSkills']['Binding'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['MAGSkills']['Summoning'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Close Combat":
            skillsDict['CombatSkills']['Blades'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CombatSkills']['Clubs'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CombatSkills']['Unarmed Combat'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Biotech":
            skillsDict['LOGSkills']['Biotechnology'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Cybertechnology'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['First Aid'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['LOGSkills']['Medicine'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Athletics":
            skillsDict['AGISkills']['Flight'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['AGISkills']['Gymnastics'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['STRSkills']['Running'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['STRSkills']['Swimming'] += int(skillGroup['karma']) + int(skillGroup['base'])

        elif skillGroup['name'] == "Acting":
            skillsDict['CHASkills']['Con'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CHASkills']['Impersonation'] += int(skillGroup['karma']) + int(skillGroup['base'])
            skillsDict['CHASkills']['Performance'] += int(skillGroup['karma']) + int(skillGroup['base'])

    return skillsDict


def createAttributeDict(character):
    # The character's innate attributes:
    attributesDict = dict()



    return attributesDict


def findTalent(character):
    talent = 'Mundane'
    try:
        for charTalent in character['character']['qualities']['quality']:
            if charTalent['name'] == "Adept" \
                    or charTalent['name'] == "Apprentice" \
                    or charTalent['name'] == "Aspected Magician" \
                    or charTalent['name'] == "Magician" \
                    or charTalent['name'] == "Mystic Adept" \
                    or charTalent['name'] == "Enchanter" \
                    or charTalent['name'] == "Explorer" \
                    or charTalent['name'] == "Aware"\
                    or charTalent['name'] == "Technomancer":
                talent = charTalent['name']
    except TypeError:
        pass

    return talent

# def createImprovementDict(character):
#    skillImprovementsDict = dict()
#
#    for skill in character['character']['improvements']['improvement']:
#        if skill['customid'] == 'skilllevel':
#            skillImprovementsDict[skill['improvedname']] = int(skill['val'])
#
#    return skillImprovementsDict
