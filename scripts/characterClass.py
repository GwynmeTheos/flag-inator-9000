# Character class

import os, math


class Character:
    accrued_flags = int()
    # Character talent and metatype/variancy
    talent = str()
    meta = dict()
    # Stuff everyone has.
    attributes = dict()
    skills = dict()
    attributePeaks = dict()
    qualities = dict()
    # Gear
    armor = int()
    foci = list()
    # 'Ware
    ware = dict()
    essence = dict()
    # Awakened
    initiateGrade = int()
    bloodMage = bool()
    toxicMage = bool()
    spells = int()
    adeptPowers = dict()
    # Verbosity
    verbose = bool()

    def __init__(self, save_file, settings):
        # Verbosity check
        if settings['verbose'] == 'True':
            self.verbose = True
        elif settings['verbose'] == 'False':
            self.verbose = False
        else:
            self.verbose = True
        # "save_file" is a dict parsed from the xml .chum5 file.
        self.GenerateTalentQualities(save_file)
        self.GenerateMetatype(save_file)
        self.GenerateAttributes(save_file)
        self.GenerateSkills(save_file)
        self.GenerateArmor(save_file)
        self.GenerateWareEssence(save_file)
        self.GenerateFociSpellsPowers(save_file)
        self.GenerateInitiateTradition(save_file)

    def GenerateTalentQualities(self, save_file):
        # Talents and qualities.
        self.talent = 'Mundane'
        try:
            inDebtCount = 0
            shivaArmsCount = 0
            for quality in save_file['character']['qualities']['quality']:
                # Talents
                if quality['name'] == "Adept" \
                        or quality['name'] == "Apprentice" \
                        or quality['name'] == "Aspected Magician" \
                        or quality['name'] == "Magician" \
                        or quality['name'] == "Mystic Adept" \
                        or quality['name'] == "Enchanter" \
                        or quality['name'] == "Explorer" \
                        or quality['name'] == "Aware" \
                        or quality['name'] == "Technomancer":
                    self.talent = quality['name']
                # Qualities
                # All qualities aside from the specified below:
                self.qualities[quality['name']] = True
                # In Debt
                if quality['name'] == "In Debt":
                    inDebtCount = + 1
                # Fame and Day Job
                if quality['name'].find('Fame:') != -1:
                    fameQual = quality['name'].replace("Fame: ", "")
                    try:
                        if fameQual == 'Local' and not (self.qualities['Fame'] > 4):
                            self.qualities['Fame'] = 3
                        elif fameQual == 'National' and not (self.qualities['Fame'] > 8):
                            self.qualities['Fame'] = 7
                        elif fameQual == 'Megacorporate' and not (self.qualities['Fame'] > 11):
                            self.qualities['Fame'] = 10
                        elif fameQual == 'Global':
                            self.qualities['Fame'] = 12
                    except KeyError:
                        if fameQual == 'Local':
                            self.qualities['Fame'] = 3
                        elif fameQual == 'National':
                            self.qualities['Fame'] = 7
                        elif fameQual == 'Megacorporate':
                            self.qualities['Fame'] = 10
                        elif fameQual == 'Global':
                            self.qualities['Fame'] = 12
                        else:
                            pass

                if quality['name'].find('Day Job') != -1:
                    dayJobQual = quality['name'].replace("Day Job ", "").replace("(", "").replace(")", "")
                    try:
                        if dayJobQual == '10 hrs' and not (self.qualities['Day Job'] > 1):
                            self.qualities['Day Job'] = 0
                        elif dayJobQual == '20 hrs' and not (self.qualities['Day Job'] > 3):
                            self.qualities['Day Job'] = 2
                        elif dayJobQual == '40 hrs':
                            self.qualities['Day Job'] = 5
                    except KeyError:
                        if dayJobQual == '10 hrs':
                            self.qualities['Day Job'] = 0
                        elif dayJobQual == '20 hrs':
                            self.qualities['Day Job'] = 2
                        elif dayJobQual == '40 hrs':
                            self.qualities['Day Job'] = 5

            # In Debt
            self.qualities['In Debt'] = inDebtCount
            # Shiva Arms
            self.qualities['Shiva Arms'] = shivaArmsCount

        except TypeError:
            pass

    def GenerateMetatype(self, save_file):
        try:
            self.meta['type'] = save_file['character']['metatype']
        except TypeError:
            self.meta['type'] = "None"
        try:
            self.meta['variant'] = save_file['character']['metavariant']
        except TypeError:
            self.meta['variant'] = "None"
        try:
            self.meta['category'] = save_file['character']['metatypecategory']
        except TypeError:
            self.meta['category'] = "None"

    def GenerateAttributes(self, save_file):
        for att in save_file['character']['attributes']['attribute']:
            attRating = int(att['base']) + int(att['karma']) + int(att['metatypemin'])
            self.attributes[att['name']] = attRating
            self.attributes[str('average' + att['name'])] = int(att['totalvalue'])

        # Find and add the highest limb's AGI rating.
        # We also use this to count the amount of limbs, for Redliner.
        # It makes no difference if we just add the redliner bonus at the end of the code, 'cause it is applied to all
        # limbs, and as such, the highest without Redliner is also the highest with Redliner.
        highestLimbAGI = 0
        limbCount = 0
        try:
            for ware in save_file['character']['cyberwares']['cyberware']:
                limbAGI = 0
                # If Liminal Centaur Body
                if ware['name'] == "Liminal Body, Centaur":
                    try:
                        for limBodyLimbs in ware['children']['cyberware']:
                            limbAGI = 0
                            if limBodyLimbs['category'] == "Cyberlimb" and (
                                    limBodyLimbs['limbslot'] == "leg" or limBodyLimbs['limbslot'] == "arm"):
                                limbCount += 1
                                try:
                                    for limBodyMods in limBodyLimbs['children']['cyberware']:
                                        if limBodyMods['name'] == 'Customized Agility' or limBodyMods['name'] == "Enhanced Agility":
                                            limbAGI += int(limBodyMods['rating'])
                                    if limbAGI > highestLimbAGI:
                                        highestLimbAGI = limbAGI
                                except TypeError:
                                    continue
                    except TypeError:
                        continue
                # If Normal Limb
                elif ware['category'] == "Cyberlimb" and (ware['limbslot'] == "leg" or ware['limbslot'] == "arm"):
                    limbCount += 1
                    try:
                        for mods in ware['children']['cyberware']:
                            if mods['name'] == "Customized Agility" or mods['name'] == "Enhanced Agility":
                                limbAGI += int(mods['rating'])
                        if limbAGI > highestLimbAGI:
                            highestLimbAGI = limbAGI
                    except TypeError:
                        continue
                # Else, it's just another 'ware.
                else:
                    continue
            self.attributes['highestLimbAGI'] = highestLimbAGI
            # Add Redliner bonuses.
            if 2 <= limbCount <= 3:
                self.attributes['highestLimbAGI'] += 1
            elif limbCount >= 4:
                self.attributes['highestLimbAGI'] += 2
        except TypeError:
            self.attributes['highestLimbAGI'] = 0

        # Find and add the highest limb's STR rating.
        highestLimbSTR = 0
        try:
            for ware in save_file['character']['cyberwares']['cyberware']:
                limbSTR = 0
                # If Liminal Centaur Body
                if ware['name'] == "Liminal Body, Centaur":
                    try:
                        for limBodyLimbs in ware['children']['cyberware']:
                            limbSTR = 0
                            if limBodyLimbs['category'] == "Cyberlimb" and (
                                    limBodyLimbs['limbslot'] == "leg" or limBodyLimbs['limbslot'] == "arm"):
                                try:
                                    for limBodyMods in limBodyLimbs['children']['cyberware']:
                                        if limBodyMods['name'] == 'Customized Strength' or limBodyMods['name'] == "Enhanced Strength":
                                            limbSTR += int(limBodyMods['rating'])
                                    if limbSTR > highestLimbSTR:
                                        highestLimbSTR = limbSTR
                                except TypeError:
                                    continue
                    except TypeError:
                        continue
                # If Normal Limb
                elif ware['category'] == "Cyberlimb" and (ware['limbslot'] == "leg" or ware['limbslot'] == "arm"):
                    try:
                        for mods in ware['children']['cyberware']:
                            if mods['name'] == "Customized Strength" or mods['name'] == "Enhanced Strength":
                                limbSTR += int(mods['rating'])
                        if limbSTR > highestLimbSTR:
                            highestLimbSTR = limbSTR
                    except TypeError:
                        continue
                # Else, it's just another 'ware.
                else:
                    continue
            self.attributes['highestLimbSTR'] = highestLimbSTR
            # Add Redliner bonuses.
            if 2 <= limbCount <= 3:
                self.attributes['highestLimbSTR'] += 1
            elif limbCount >= 4:
                self.attributes['highestLimbSTR'] += 2
        except TypeError:
            self.attributes['highestLimbSTR'] = 0

        # Find and add the highest arm's AGI rating.
        highestArmAGI = 0
        try:
            for ware in save_file['character']['cyberwares']['cyberware']:
                armAGI = 0
                # If Liminal Centaur Body
                if ware['name'] == "Liminal Body, Centaur":
                    try:
                        for limBodyLimbs in ware['children']['cyberware']:
                            armAGI = 0
                            if limBodyLimbs['category'] == "Cyberlimb" and limBodyLimbs['limbslot'] == "arm":
                                try:
                                    for limBodyMods in limBodyLimbs['children']['cyberware']:
                                        if limBodyMods['name'] == 'Customized Agility' or limBodyMods['name'] == "Enhanced Agility":
                                            armAGI += int(limBodyMods['rating'])
                                    if armAGI > highestArmAGI:
                                        highestArmAGI = armAGI
                                except TypeError:
                                    continue
                    except TypeError:
                        continue
                # If Normal Limb
                elif ware['category'] == "Cyberlimb" and ware['limbslot'] == "arm":
                    try:
                        for mods in ware['children']['cyberware']:
                            if mods['name'] == "Customized Agility" or mods['name'] == "Enhanced Agility":
                                armAGI += int(mods['rating'])
                        if armAGI > highestArmAGI:
                            highestArmAGI = armAGI
                    except TypeError:
                        continue
                # Else, it's just another 'ware.
                else:
                    continue
            self.attributes['highestArmAGI'] = highestArmAGI
            # Add Redliner bonuses.
            if 2 <= limbCount <= 3:
                self.attributes['highestArmAGI'] += 1
            elif limbCount >= 4:
                self.attributes['highestArmAGI'] += 2
        except TypeError:
            self.attributes['highestArmAGI'] = 0

        # Find and add the highest arm's STR rating.
        highestArmSTR = 0
        try:
            for ware in save_file['character']['cyberwares']['cyberware']:
                armSTR = 0
                # If Liminal Centaur Body
                if ware['name'] == "Liminal Body, Centaur":
                    try:
                        for limBodyLimbs in ware['children']['cyberware']:
                            armSTR = 0
                            if limBodyLimbs['category'] == "Cyberlimb" and limBodyLimbs['limbslot'] == "arm":
                                try:
                                    for limBodyMods in limBodyLimbs['children']['cyberware']:
                                        if limBodyMods['name'] == 'Customized Strength' or limBodyMods['name'] == "Enhanced Strength":
                                            armSTR += int(limBodyMods['rating'])
                                    if armSTR > highestArmSTR:
                                        highestArmSTR = armSTR
                                except TypeError:
                                    continue
                    except TypeError:
                        continue
                # If Normal Limb
                elif ware['category'] == "Cyberlimb" and ware['limbslot'] == "arm":
                    try:
                        for mods in ware['children']['cyberware']:
                            if mods['name'] == "Customized Agility" or mods['name'] == "Enhanced Agility":
                                armSTR += int(mods['rating'])
                        if armSTR > highestArmSTR:
                            highestArmSTR = armSTR
                    except TypeError:
                        continue
                # Else, it's just another 'ware.
                else:
                    continue
            self.attributes['highestArmSTR'] = highestArmSTR
            # Add Redliner bonuses.
            if 2 <= limbCount <= 3:
                self.attributes['highestArmSTR'] += 1
            elif limbCount >= 4:
                self.attributes['highestArmSTR'] += 2
        except TypeError:
            self.attributes['highestArmSTR'] = 0

    def GenerateSkills(self, save_file):
        # First, name every single skill in the game.
        self.skills['BODSkills'] = {'Diving': 0,                 # Default
                                    'Free-Fall': 0}              # Default
        self.skills['CombatSkills'] = {'Archery': 0,             # Default
                                       'Automatics': 0,          # Default
                                       'Blades': 0,              # Default
                                       'Clubs': 0,               # Default
                                       'Heavy Weapons': 0,       # Default
                                       'Longarms': 0,            # Default
                                       'Palming': 0,
                                       'Pistols': 0,             # Default
                                       'Throwing Weapons': 0,    # Default
                                       'Unarmed Combat': 0}      # Default
        self.skills['AGISkills'] = {'Escape Artist': 0,          # Default
                                    'Flight': 0,
                                    'Gunnery': 0,                # Default
                                    'Gymnastics': 0,             # Default
                                    'Locksmith': 0,
                                    'Sneaking': 0}               # Default
        self.skills['REASkills'] = {'Pilot Aerospace': 0,
                                    'Pilot Aircraft': 0,
                                    'Pilot Ground Craft': 0,     # Default
                                    'Pilot Walker': 0,
                                    'Pilot Watercraft': 0}       # Default
        self.skills['STRSkills'] = {'Running': 0,                # Default
                                    'Swimming': 0}               # Default
        self.skills['CHASkills'] = {'Animal Handling': 0,        # Default
                                    'Con': 0,                    # Default
                                    'Etiquette': 0,              # Default
                                    'Impersonation': 0,          # Default
                                    'Instruction': 0,            # Default
                                    'Intimidation': 0,           # Default
                                    'Leadership': 0,             # Default
                                    'Negotiation': 0,            # Default
                                    'Performance': 0}            # Default
        self.skills['INTSkills'] = {'Artisan': 0,
                                    'Assensing': 0,
                                    'Disguise': 0,               # Default
                                    'Navigation': 0,             # Default
                                    'Perception': 0,             # Default
                                    'Tracking': 0}               # Default
        self.skills['LOGSkills'] = {'Aeronautics Mechanic': 0,
                                    'Arcana': 0,
                                    'Armorer': 0,                # Default
                                    'Automotive Mechanic': 0,
                                    'Biotechnology': 0,
                                    'Chemistry': 0,
                                    'Cybertechnology': 0,
                                    'Demolitions': 0,            # Default
                                    'First Aid': 0,              # Default
                                    'Forgery': 0,                # Default
                                    'Industrial Mechanic': 0,
                                    'Medicine': 0,
                                    'Nautical Mechanic': 0}
        self.skills['HackSkills'] = {'Computer': 0,              # Default
                                     'Cybercombat': 0,           # Default
                                     'Electronic Warfare': 0,
                                     'Hacking': 0,               # Default
                                     'Hardware': 0,
                                     'Software': 0}
        self.skills['WILSkills'] = {'Astral Combat': 0,
                                    'Survival': 0}
        self.skills['MAGSkills'] = {'Alchemy': 0,
                                    'Artificing': 0,
                                    'Banishing': 0,
                                    'Binding': 0,
                                    'Counterspelling': 0,
                                    'Disenchanting': 0,
                                    'Ritual Spellcasting': 0,
                                    'Spellcasting': 0,
                                    'Summoning': 0}
        self.skills['RESSkills'] = {'Compiling': 0,
                                    'Decompiling': 0,
                                    'Registering': 0}
        self.skills['EXOSkills'] = list()

        # Loop through every single skill and add the skill rating to the dicepool.
        for skill in save_file['character']['newskills']['skills']['skill']:
            try:
                for skillList in self.skills.keys():
                    try:
                        for skillName in self.skills[skillList].keys():
                            if skillName == skill['name']:
                                self.skills[skillList][skillName] += int(skill['karma']) + int(skill['base'])
                    except AttributeError:
                        # Getting to EXOSkills breaks it, so this is here to just pass.
                        pass
            except KeyError:
                # It is an exotic skill.
                self.skills['EXOSkills'].append({'Name': "Exotic: " + skill['specific'],
                                                 'Rating': int(skill['karma']) + int(skill['base']),
                                                 'Category': skill['skillcategory']})

        # Loop through the skill groups and add the skill group rating.
        for skillGroup in save_file['character']['newskills']['groups']['group']:
            if skillGroup['name'] == "Tasking":
                self.skills['RESSkills']['Compiling'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['RESSkills']['Decompiling'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['RESSkills']['Registering'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Stealth":
                self.skills['INTSkills']['Disguise'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CombatSkills']['Palming'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['AGISkills']['Sneaking'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Sorcery":
                self.skills['MAGSkills']['Counterspelling'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['MAGSkills']['Ritual Spellcasting'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['MAGSkills']['Spellcasting'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Outdoors":
                self.skills['INTSkills']['Navigation'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['WILSkills']['Survival'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['INTSkills']['Tracking'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Engineering":
                self.skills['LOGSkills']['Aeronautics Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['LOGSkills']['Automotive Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['LOGSkills']['Industrial Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['LOGSkills']['Nautical Mechanic'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Influence":
                self.skills['CHASkills']['Etiquette'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CHASkills']['Leadership'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CHASkills']['Negotiation'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Firearms":
                self.skills['CombatSkills']['Automatics'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CombatSkills']['Longarms'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CombatSkills']['Pistols'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Enchanting":
                self.skills['MAGSkills']['Alchemy'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['MAGSkills']['Artificing'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['MAGSkills']['Disenchanting'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Electronics":
                self.skills['HackSkills']['Computer'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['HackSkills']['Hardware'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['HackSkills']['Software'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Cracking":
                self.skills['HackSkills']['Cybercombat'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['HackSkills']['Electronic Warfare'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['HackSkills']['Hacking'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Conjuring":
                self.skills['MAGSkills']['Banishing'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['MAGSkills']['Binding'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['MAGSkills']['Summoning'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Close Combat":
                self.skills['CombatSkills']['Blades'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CombatSkills']['Clubs'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CombatSkills']['Unarmed Combat'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Biotech":
                self.skills['LOGSkills']['Biotechnology'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['LOGSkills']['Cybertechnology'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['LOGSkills']['First Aid'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['LOGSkills']['Medicine'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Athletics":
                self.skills['AGISkills']['Flight'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['AGISkills']['Gymnastics'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['STRSkills']['Running'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['STRSkills']['Swimming'] += int(skillGroup['karma']) + int(skillGroup['base'])

            elif skillGroup['name'] == "Acting":
                self.skills['CHASkills']['Con'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CHASkills']['Impersonation'] += int(skillGroup['karma']) + int(skillGroup['base'])
                self.skills['CHASkills']['Performance'] += int(skillGroup['karma']) + int(skillGroup['base'])

        # Attribute + Skill Rank flags are calculated based on attribute,
        # which means we really only care for the highest skill rating tied to a specific attribute.

        self.attributePeaks = {'BOD': [0, False], 'AGI': [0, False], 'REA': [0, False], 'STR': [0, False],
                               'CHA': [0, False], 'INT': [0, False], 'LOG': [0, False], 'WIL': [0, False],
                               'MAG': [0, False], 'RES': [0, False], 'DEP': [0, False]}

    def GenerateArmor(self, save_file):
        armorDict = {'defaultArmor': 0}
        extraArmor = 0
        # First thing to do is to find the armors that person own.
        try:
            for armor in save_file['character']['armors']['armor']:
                # If the first character in the string is "+", just continue, those are extra armor.
                if armor['armor'][0] == '+':
                    continue
                # If the armor value is 0, it's not necessary to check it.
                elif armor['armor'] == '0':
                    continue
                # Only actual armor is left. Time to process those.
                else:
                    totalArmorValue = int(armor['armor'])
                    # Loop through the mods in that piece of armor.
                    for mods in armor['armormods']['armormod']:
                        if mods['name'] == 'Full Body Armor: Helmet':
                            continue
                        else:
                            totalArmorValue += int(mods['armor'])

                    armorDict[armor['name']] = totalArmorValue
        except TypeError:
            pass
        # Now that we have the armor in a dict. We need to figure out if they have 'ware that gives armor.
        try:
            for ware in save_file['character']['cyberwares']['cyberware']:
                # Skin mods
                if ware['name'] == 'Orthoskin':
                    extraArmor += int(ware['rating'])
                elif ware['name'] == 'Dermal Plating':
                    extraArmor += int(ware['rating'])
                elif ware['name'] == 'Smartskin':
                    extraArmor += int(ware['rating'])
                # Bone mods
                elif ware['name'] == 'Bone Lacing (Plastic)':
                    extraArmor += 1
                elif ware['name'] == 'Bone Lacing (Aluminum)':
                    extraArmor += 2
                elif ware['name'] == 'Bone Lacing (Titanium)':
                    extraArmor += 3
                # Limbs and liminal bodies
                elif ware['category'] == 'Cyberlimb':
                    for mods in ware['children']['cyberware']:
                        # Normal limbs and liminal bodies without extra limbs
                        if mods['name'] == 'Armor':
                            extraArmor += int(mods['rating'])
                        # Liminal bodies with extra limbs
                        elif mods['category'] == 'Cyberlimb':
                            for limbMods in mods['children']['cyberware']:
                                if limbMods['name'] == 'Armor':
                                    extraArmor += int(mods['rating'])
        except TypeError:
            pass
        # Now that we have every single bit of cyberware that is capable of adding armor, time to check a few qualities.
        try:
            for quality in save_file['character']['qualities']['quality']:
                if quality['name'] == 'Crystal Limb (Arm)' or quality['name'] == 'Crystal Limb (Leg)':
                    extraArmor += 1
                elif quality['name'] == 'Dermal Deposits':
                    extraArmor += 1
                elif quality['name'] == 'Dermal Alteration (Bark Skin)':
                    extraArmor += 2
                elif quality['name'] == 'Dermal Alteration (Granite Shell)':
                    # extraArmor += 4
                    pass
                elif quality['name'] == 'Dermal Alteration (Rhino Hide)':
                    extraArmor += 3
                # Infected Armor
                elif quality['name'] == 'Infected Optional Power: Armor':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Dzoo-Noo-Qua':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Fomoraig':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Ghoul (Human)':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Ghoul (Dwarf)':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Ghoul (Elf)':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Ghoul (Ork)':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Ghoul (Sasquatch)':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Ghoul (Troll)':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Gnawer':
                    extraArmor += 1
                elif quality['name'] == 'Infected: Harvester':
                    extraArmor += 2
                elif quality['name'] == 'Infected: Loup-Garou':
                    extraArmor += 2
                elif quality['name'] == 'Infected: Mutaqua':
                    extraArmor += 1
        except TypeError:
            pass
        # Finally, check for Mystic Armor.
        try:
            for power in save_file['character']['powers']['power']:
                if power['name'] == 'Mystic Armor':
                    extraArmor += int(power['rating'])
        except TypeError:
            pass
        # With all of the extra armor modifiers, we will check the worn armor dictionary for the highest armor, and then
        # apply the extra armor on top of it.
        highestArmorValue = armorDict['defaultArmor']
        for armor in armorDict:
            if (extraArmor + armorDict[armor]) > highestArmorValue:
                highestArmorValue = extraArmor + armorDict[armor]
            else:
                continue

        # Finally, write that to the class.
        self.armor = highestArmorValue

    def GenerateWareEssence(self, save_file):
        # Get a dict of every single ware in the character.
        try:
            for ware in save_file['character']['cyberwares']['cyberware']:
                # Special formatting: FixedValues(x,y,z)
                if ware['ess'].find('FixedValues') != -1:
                    essence = ware['ess'].replace('FixedValues', '').replace(')', '').replace('(', '')
                    essence = essence.split(',')
                    essence = essence[int(ware['rating']) - 1]
                    self.ware[ware['name']] = {'Essence': float(essence), 'Grade': ware['grade'],
                                               'Rating': int(ware['rating'])}
                # Special Formating: Rating * x.y
                elif ware['ess'].find('Rating * ') != -1:
                    essence = ware['ess'].replace('Rating * ', '').replace(')', '').replace('(', '')
                    essence = float(eval(essence)) * int(ware['rating'])
                    self.ware[ware['name']] = {'Essence': float(essence), 'Grade': ware['grade'],
                                               'Rating': int(ware['rating'])}
                else:
                    self.ware[ware['name']] = {'Essence': float(ware['ess']), 'Grade': ware['grade'],
                                               'Rating': int(ware['rating'])}
        except TypeError:
            self.ware = None

        # Check total essence, deltaware and betaware.
        # Total
        self.essence['Total'] = float(save_file['character']['totaless'])
        if self.ware is None:
            pass
        else:
            # Beta
            betaCount = float()
            for ware in self.ware.keys():
                if self.ware[ware]['Grade'] == 'Betaware' or self.ware[ware]['Grade'] == 'Betaware (Adapsin)':
                    betaCount += self.ware[ware]['Essence']
            self.essence['Betaware'] = betaCount
            # Delta
            deltaCount = float()
            for ware in self.ware.keys():
                if self.ware[ware]['Grade'] == 'Deltaware' or self.ware[ware]['Grade'] == 'Deltaware (Adapsin)':
                    deltaCount += self.ware[ware]['Essence']
            self.essence['Deltaware'] = deltaCount

    def GenerateFociSpellsPowers(self, save_file):
        # Foci
        try:
            for gear in save_file['character']['gears']['gear']:
                if gear['category'] == 'Foci':
                    self.foci.append([gear['name'], int(gear['rating'])])
        except TypeError:
            self.foci = None
        # Spells
        try:
            for i in save_file['character']['spells']['spell']:
                self.spells += 1
        except TypeError:
            self.spells = None
        # Adept powers
        try:
            for power in save_file['character']['powers']['power']:
                self.adeptPowers[power['name']] = int(power['rating'])
        except TypeError:
            self.adeptPowers = None

    def GenerateInitiateTradition(self, save_file):
        # Initiate Grade
        try:
            self.initiateGrade = int(save_file['character']['initiategrade'])
        except TypeError:
            self.initiateGrade = None
        # Blood Mage
        try:
            for art in save_file['character']['arts']['art']:
                if art['name'] == "Blood Magic":
                    self.bloodMage = True
        except TypeError:
            self.bloodMage = False
        # Toxic Mage
        try:
            if save_file['character']['tradition']['name'] == 'Toxic':
                self.toxicMage = True
        except KeyError:
            self.toxicMage = False

    def CheckFlags(self):
        os.system("CLS")
        self.CheckMetatype()
        self.CheckTalents()
        self.CheckQualities()
        self.CheckAttributes()
        self.CheckSkills()
        self.CheckArmor()
        self.CheckWareEssence()
        self.CheckFociSpellsPowers()
        self.CheckInitiateTradition()

        print("\n-----> Total Flag = " + str(self.accrued_flags))

    def CheckMetatype(self):
        flags = int()
        output = "<Metatype>\n"

        # Category
        if self.meta['category'] == 'Metahuman':
            # Type
            if self.meta['type'] == 'Human':
                # Variant
                if self.meta['variant'] == 'Nartaki':
                    output += "    [" + self.meta['type'] + "] +3 Flag points\n"
                    flags += 3

            elif self.meta['type'] == 'Elf':
                if self.meta['variant'] == 'Dryad':
                    output += "    [" + self.meta['type'] + "] +5 Flag points\n"
                    flags += 5
                elif self.meta['variant'] == 'Nocturna':
                    output += "    [" + self.meta['type'] + "] +6 Flag points\n"
                    flags += 6
                else:
                    output += "    [" + self.meta['type'] + "] +2 Flag points\n"
                    flags += 2

            elif self.meta['type'] == 'Dwarf':
                if self.meta['variant'] == 'Gnome':
                    output += "    [" + self.meta['type'] + "] +5 Flag points\n"
                    flags += 5

            elif self.meta['type'] == 'Ork':
                if self.meta['variant'] == 'Oni':
                    output += "    [" + self.meta['type'] + "] +1 Flag points\n"
                    flags += 1

        elif self.meta['category'] == 'Metasapient':
            # Type
            if self.meta['type'] == 'A.I.':
                output += "    [" + self.meta['type'] + "] +6 Flag points\n"
                flags += 6
            elif self.meta['type'] == 'Naga.':
                output += "    [" + self.meta['type'] + "] +14 Flag points\n"
                flags += 14
            elif self.meta['type'] == 'Sasquatch':
                output += "    [" + self.meta['type'] + "] +10 Flag points\n"
                flags += 10
            elif self.meta['type'] == 'Centaur':
                output += "    [" + self.meta['type'] + "] +12 Flag points\n"
                flags += 12

        elif self.meta['category'] == 'Shapeshifter':
            output += "    [" + self.meta['type'] + "] +7 Flag points\n"
            flags += 7

        if flags > 0:
            if self.verbose:
                print(output)
            self.accrued_flags += flags

    def CheckTalents(self):
        flags = int()
        output = "<Talent>\n"
        if self.talent == 'Technomancer':
            output += "    [" + self.talent + "] +3 Flag points\n"
            flags += 3
        elif self.talent == 'Adept':
            output += "    [" + self.talent + "] +2 Flag points\n"
            flags += 2
        elif self.talent == 'Magician':
            output += "    [" + self.talent + "] +2 Flag points\n"
            flags += 2
        elif self.talent == 'Mystic Adept':
            output += "    [" + self.talent + "] +7 Flag points\n"
            flags += 7
        elif self.talent == 'Aspected Magician' \
                or self.talent == 'Enchanter' \
                or self.talent == 'Explorer' \
                or self.talent == 'Aware' \
                or self.talent == 'Apprentice':
            output += "    [" + self.talent + "] +1 Flag points\n"
            flags += 1

        if flags > 0:
            if self.verbose:
                print(output)
            self.accrued_flags += flags

    def CheckQualities(self):
        flags = int()
        output = "<Qualities>\n"

        for quality in self.qualities.keys():
            # Misc
            if quality == 'Archivist':
                output += "    [Archivist] +2 Flag points\n"
                flags += 2
            elif quality == 'Groveler':
                output += "    [Groveler] +2 Flag points\n"
                flags += 2
            elif quality == 'Prototype Transhuman':
                output += "    [Prototype Transhuman] +3 Flag points\n"
                flags += 3
            elif quality == 'Resonant Discordance':
                output += "    [Resonant Discordance] +2 Flag points\n"
                flags += 2
            elif quality == 'Exceptional Attribute':
                output += "    [Exceptional Attribute] +2 Flag points\n"
                flags += 2
            # Drake
            elif quality.find('Dracoform') != -1:
                try:
                    if quality['Latent Dracomorphosis']:
                        output += "    [" + quality + "] +9 Flag points\n"
                        flags += 4
                except KeyError:
                    output += "    [" + quality + "] +9 Flag points\n"
                    flags += 9
            elif quality == 'Latent Dracomorphosis':
                output += "    [Latent Dracomorphosis] +5 Flag points\n"
                flags += 5
            # Metagenic
            elif quality == 'Astral Hazing' and self.talent == 'Mundane':
                output += "    [Mundane Astral Hazing] +4 Flag points\n"
                flags += 4
            elif quality == 'Symbiosis':
                output += "    [Symbiosis] +1 Flag points\n"
                flags += 1
            elif quality.find('Impaired Attribute') != -1:
                output += "    [" + quality + "] +2 Flag points\n"
                flags += 2
            elif quality.find('Metagenic Improvement') != -1:
                output += "    [Metagenic Improvement] +4 Flag points\n"
                flags += 4
            # HMHVV
            elif quality.find('Carrier') != -1:
                output += "    [HMHVV Carrier] +5 Flag points\n"
                flags += 5
            elif quality == 'Infected: Banshee' or \
                 quality == 'Infected: Dzoo-Noo-Qua' or \
                 quality == 'Infected: Goblin' or \
                 quality == 'Infected: Mutaqua' or \
                 quality == 'Infected: Nosferatu' or \
                 quality == 'Infected: Sukuyan (Human)' or \
                 quality == 'Infected: Sukuyan (Non-Human)' or \
                 quality == 'Infected: Vampire (Human)' or \
                 quality == 'Infected: Vampire (Non-Human)' or \
                 quality == 'Infected: Wendigo':
                output += "    [Strain I & Ia Infected] +16 Flag points\n"
                flags += 16
            elif quality == 'Infected: Fomoraig' or \
                 quality == 'Infected: Bandersnatch' or \
                 quality == 'Infected: Gnawer' or \
                 quality == 'Infected: Grendel' or \
                 quality == 'Infected: Harvester' or \
                 quality == 'Infected: Loup-Garou':
                output += "    [Strain II] +14 Flag points\n"
                flags += 14
            elif quality == 'Infected: Ghoul (Human)' or \
                 quality == 'Infected: Ghoul (Dwarf)' or \
                 quality == 'Infected: Ghoul (Elf)' or \
                 quality == 'Infected: Ghoul (Ork)' or \
                 quality == 'Infected: Ghoul (Sasquatch)' or \
                 quality == 'Infected: Ghoul (Troll)':
                output += "    [Strain III] +12 Flag points\n"
                flags += 12
        # Day Job and Fame
        try:
            if self.qualities['Fame'] and self.qualities['Day Job']:
                flags += self.qualities['Fame'] + self.qualities['Day Job']
                output += "    [Fame + Day Job] +" + str(self.qualities['Fame'] + self.qualities['Day Job']) + " Flag points\n"
        except KeyError:
            pass
        # Shiva Arms
        try:
            if self.qualities['Shiva Arms'] > 0:
                flags += self.qualities['Shiva Arms']
                output += "    [Shiva Arms] +" + str(self.qualities['Shiva Arms']) + " Flag points\n"
        except KeyError:
            pass
        # In Debt
        try:
            if 3 <= self.qualities['In Debt'] <= 5:
                flags += 2
                output += "    [In Debt 3 - 5] +2 Flag points\n"
            elif 6 <= self.qualities['In Debt'] <= 8:
                flags += 4
                output += "    [In Debt 6 - 8] +4 Flag points\n"
            elif 9 <= self.qualities['In Debt'] <= 11:
                flags += 6
                output += "    [In Debt 9 - 11] +6 Flag points\n"
            elif 12 <= self.qualities['In Debt'] <= 14:
                flags += 8
                output += "    [In Debt 12 - 14] +8 Flag points\n"
            elif self.qualities['In Debt'] >= 15:
                flags += 10
                output += "    [In Debt 15] +10 Flag points\n"
        except KeyError:
            pass

        if flags > 0:
            if self.verbose:
                print(output)
            self.accrued_flags += flags

    def CheckAttributes(self):
        flags = int()
        output = "<Attributes>\n"

        # Att at 1
        if self.attributes['BOD'] == 1:
            output += "    [BOD at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['AGI'] == 1:
            output += "    [AGI at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['REA'] == 1:
            output += "    [REA at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['STR'] == 1:
            output += "    [STR at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['CHA'] == 1:
            output += "    [CHA at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['INT'] == 1:
            output += "    [INT at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['LOG'] == 1:
            output += "    [LOG at 1] +2 Flag points\n"
            flags += 2
        if self.attributes['WIL'] == 1:
            output += "    [WIL at 1] +2 Flag points\n"
            flags += 2

        # Special Attributes
        if self.attributes['averageMAG'] > 6 or self.attributes['averageRES'] > 6 or self.attributes['averageDEP'] > 6:
            # Find what they are.
            specAttRat = self.attributes['averageMAG']  # They're more likely to be Awakened anyways.
            specAttName = "MAG"
            if self.attributes['averageRES'] > specAttRat:
                specAttRat = self.attributes['averageRES']  # They're a Techno.
                specAttName = "RES"
            if self.attributes['averageDEP'] > specAttRat:
                specAttRat = self.attributes['averageDEP']  # They're an AI.
                specAttName = "DEP"

            if specAttRat == 7:
                output += "    [" + specAttName + " at " + str(specAttRat) + "] +2 Flag points\n"
                flags += 2
            elif specAttRat == 8:
                output += "    [" + specAttName + " at " + str(specAttRat) + "] +5 Flag points\n"
                flags += 5
            elif specAttRat == 9:
                output += "    [" + specAttName + " at " + str(specAttRat) + "] +9 Flag points\n"
                flags += 9
            elif specAttRat >= 10:
                output += "    [" + specAttName + " at " + str(specAttRat) + "] +10 Flag points\n"
                flags += 14

        if flags > 0:
            if self.verbose:
                print(output)
            self.accrued_flags += flags

    def CheckSkills(self):
        flags = int()
        output = "<Attributes>\n"

        # BOD Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['BODSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['BODSkills'][skill] == 0:
                auxVar = self.attributes['averageBOD'] - 1
            else:
                auxVar = self.skills['BODSkills'][skill] + self.attributes['averageBOD']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['BOD'][0] = currentPeak
            self.attributePeaks['BOD'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [BOD Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [BOD Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [BOD Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [BOD Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # AGI and Combat Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        # Normal AGI skills
        for skill in self.skills['AGISkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['AGISkills'][skill] == 0:
                if skill == 'Flight' or skill == 'Locksmith':
                    auxVar = 0
                else:
                    auxVar = self.attributes['averageAGI'] - 1
            else:
                auxVar = self.skills['AGISkills'][skill] + self.attributes['averageAGI']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Combat AGI skills
        for skill in self.skills['CombatSkills'].keys():
            # Check if they're defaultiong, some skills can't be defaulted in.
            # Highest Limb AGI skill
            if skill == 'Unarmed Combat':
                if self.skills['CombatSkills'][skill] == 0:
                    auxVar = self.attributes['highestLimbAGI'] - 1
                else:
                    auxVar = self.skills['CombatSkills'][skill] + self.attributes['highestLimbAGI']
            # Highest Arm AGI Skills
            elif self.skills['CombatSkills'][skill] == 0:
                if skill == 'Palming':
                    auxVar = 0
                else:
                    auxVar = self.attributes['highestArmAGI'] - 1
            else:
                auxVar = self.skills['CombatSkills'][skill] + self.attributes['highestArmAGI']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the AGI Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['AGI'][0] = currentPeak
            self.attributePeaks['AGI'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [AGI Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [AGI Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [AGI Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [AGI Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # REA Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['REASkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['REASkills'][skill] == 0:
                if skill == 'Pilot Aerospace' or skill == 'Pilot Aircraft' or skill == 'Pilot Walker':
                    auxVar = 0
                else:
                    auxVar = self.attributes['averageREA'] - 1
            else:
                auxVar = self.skills['REASkills'][skill] + self.attributes['averageREA']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['REA'][0] = currentPeak
            self.attributePeaks['REA'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [REA Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [REA Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [REA Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [REA Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # STR Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['STRSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['STRSkills'][skill] == 0:
                auxVar = self.attributes['averageSTR'] - 1
            else:
                auxVar = self.skills['STRSkills'][skill] + self.attributes['averageSTR']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['STR'][0] = currentPeak
            self.attributePeaks['STR'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [STR Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [STR Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [STR Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [STR Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # CHA Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['CHASkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['CHASkills'][skill] == 0:
                auxVar = self.attributes['averageCHA'] - 1
            else:
                auxVar = self.skills['CHASkills'][skill] + self.attributes['averageCHA']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['CHA'][0] = currentPeak
            self.attributePeaks['CHA'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [CHA Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [CHA Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [CHA Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [CHA Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # INT Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        # Rigger driving
        if not self.attributePeaks['REA'][1]:
            for skill in self.skills['REASkills'].keys():
                # Check if they are defaulting, some skills can't be defaulted in.
                if self.skills['REASkills'][skill] == 0:
                    if skill == 'Pilot Aerospace' or skill == 'Pilot Aircraft' or skill == 'Pilot Walker':
                        auxVar = 0
                    else:
                        auxVar = self.attributes['averageINT'] - 1
                else:
                    auxVar = self.skills['REASkills'][skill] + self.attributes['averageINT']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        for skill in self.skills['INTSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['INTSkills'][skill] == 0:
                auxVar = self.attributes['averageINT'] - 1
            else:
                auxVar = self.skills['INTSkills'][skill] + self.attributes['averageINT']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Hacking skills
        # Check if person is Techno and their Data/Lore
        dataLoreQuals = 'Neither'
        if self.talent == 'Technomancer':
            # Check if they have Data or Lore
            try:
                if self.qualities['Trust Data, Not Lore']:
                    dataLoreQuals = 'Data'
            except KeyError:
                try:
                    if self.qualities['Trust Lore, Not Data']:
                        dataLoreQuals = 'Lore'
                except KeyError:
                    pass
        else:
            pass
        if dataLoreQuals == 'Data':
            for skill in self.skills['HackSkills'].keys():
                # Defaulting
                if self.skills['HackSkills'][skill] == 0:
                    if skill == 'Electronic Warfare':
                        auxVar = 0
                    elif skill == 'Computer' or skill == 'Hacking':
                        auxVar = self.attributes['averageINT'] - 1
                # Hacking skills
                elif skill == 'Computer' or skill == 'Electronic Warfare' or skill == 'Hacking':
                    auxVar = self.skills['HackSkills'][skill] + self.attributes['averageINT']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        elif dataLoreQuals == 'Lore':
            for skill in self.skills['HackSkills'].keys():
                # Defaulting
                if self.skills['HackSkills'][skill] == 0:
                    if skill == 'Electronic Warfare' or skill == 'Software':
                        auxVar = 0
                    elif skill == 'Computer' or skill == 'Hacking' or skill == 'Cybercombat':
                        auxVar = self.attributes['averageINT'] - 1
                # Hacking skills
                elif skill != 'Hardware':
                    auxVar = self.skills['HackSkills'][skill] + self.attributes['averageINT']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        else:
            for skill in self.skills['HackSkills'].keys():
                # Defaulting
                if self.skills['HackSkills'][skill] == 0:
                    if skill == 'Electronic Warfare' or skill == 'Software':
                        auxVar = 0
                    elif skill == 'Computer' or skill == 'Hacking':
                        auxVar = self.attributes['averageINT'] - 1
                # Hacking Skills
                elif skill != 'Cybercombat' or skill != 'Hardware':
                    auxVar = self.skills['HackSkills'][skill] + self.attributes['averageINT']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['INT'][0] = currentPeak
            self.attributePeaks['INT'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [INT Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [INT Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [INT Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [INT Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # LOG Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        # Rigger Fine Manip
        if not self.attributePeaks['AGI'][1]:
            # Normal AGI skills
            for skill in self.skills['AGISkills'].keys():
                # Check if they are defaulting, some skills can't be defaulted in.
                if self.skills['AGISkills'][skill] == 0:
                    if skill == 'Flight' or skill == 'Locksmith':
                        auxVar = 0
                    else:
                        auxVar = self.attributes['averageLOG'] - 1
                else:
                    auxVar = self.skills['AGISkills'][skill] + self.attributes['averageLOG']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
            # Combat AGI skills
            for skill in self.skills['CombatSkills'].keys():
                # Check if they're defaultiong, some skills can't be defaulted in.
                # Highest Limb AGI skill
                if skill == 'Unarmed Combat':
                    if self.skills['CombatSkills'][skill] == 0:
                        auxVar = self.attributes['averageLOG'] - 1
                    else:
                        auxVar = self.skills['CombatSkills'][skill] + self.attributes['averageLOG']
                # Highest Arm AGI Skills
                elif self.skills['CombatSkills'][skill] == 0:
                    if skill == 'Palming':
                        auxVar = 0
                    else:
                        auxVar = self.attributes['averageLOG'] - 1
                else:
                    auxVar = self.skills['CombatSkills'][skill] + self.attributes['averageLOG']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        for skill in self.skills['LOGSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['LOGSkills'][skill] == 0:
                auxVar = self.attributes['averageLOG'] - 1
            else:
                auxVar = self.skills['LOGSkills'][skill] + self.attributes['averageLOG']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Hacking skills
        # Check if person is Techno and their Data/Lore
        dataLoreQuals = 'Neither'
        if self.talent == 'Technomancer':
            # Check if they have Data or Lore
            try:
                if self.qualities['Trust Data, Not Lore']:
                    dataLoreQuals = 'Data'
            except KeyError:
                try:
                    if self.qualities['Trust Lore, Not Data']:
                        dataLoreQuals = 'Lore'
                except KeyError:
                    pass
        else:
            pass
        if dataLoreQuals == 'Data':
            for skill in self.skills['HackSkills'].keys():
                # Defaulting
                if self.skills['HackSkills'][skill] == 0:
                    if skill == 'Electronic Warfare' or skill == 'Software':
                        auxVar = 0
                    elif skill == 'Computer' or skill == 'Hacking' or skill == 'Cybercombat':
                        auxVar = self.attributes['averageLOG'] - 1
                # Hacking skills
                elif skill != 'Hardware':
                    auxVar = self.skills['HackSkills'][skill] + self.attributes['averageLOG']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        elif dataLoreQuals == 'Lore':
            for skill in self.skills['HackSkills'].keys():
                # Defaulting
                if self.skills['HackSkills'][skill] == 0:
                    if skill == 'Electronic Warfare' or skill == 'Software':
                        auxVar = 0
                    elif skill == 'Computer' or skill == 'Hacking' or skill == 'Cybercombat':
                        auxVar = self.attributes['averageLOG'] - 1
                # Hacking skills
                elif skill != 'Hardware':
                    auxVar = self.skills['HackSkills'][skill] + self.attributes['averageLOG']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        else:
            for skill in self.skills['HackSkills'].keys():
                # Defaulting
                if self.skills['HackSkills'][skill] == 0:
                    if skill == 'Electronic Warfare' or skill == 'Software':
                        auxVar = 0
                    elif skill == 'Computer' or skill == 'Hacking':
                        auxVar = self.attributes['averageLOG'] - 1
                # Hacking Skills
                elif skill != 'Cybercombat' or skill != 'Hardware':
                    auxVar = self.skills['HackSkills'][skill] + self.attributes['averageLOG']
                # Check if that's the highest of all skills in the list.
                if auxVar > currentPeak:
                    currentPeak = auxVar
                    currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['LOG'][0] = currentPeak
            self.attributePeaks['LOG'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [LOG Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [LOG Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [LOG Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [LOG Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # WIL Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['WILSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['WILSkills'][skill] == 0:
                if skill == 'Astral Combat':
                    auxVar = 0
                else:
                    auxVar = self.attributes['averageWIL'] - 1
            else:
                auxVar = self.skills['WILSkills'][skill] + self.attributes['averageWIL']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['WIL'][0] = currentPeak
            self.attributePeaks['WIL'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [WIL Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [WIL Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [WIL Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [WIL Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # MAG Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['MAGSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['MAGSkills'][skill] == 0:
                auxVar = 0
            else:
                auxVar = self.skills['MAGSkills'][skill] + self.attributes['averageMAG']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['MAG'][0] = currentPeak
            self.attributePeaks['MAG'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [MAG Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [MAG Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [MAG Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [MAG Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # RES Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        for skill in self.skills['RESSkills'].keys():
            # Check if they are defaulting, some skills can't be defaulted in.
            if self.skills['RESSkills'][skill] == 0:
                auxVar = 0
            else:
                auxVar = self.skills['RESSkills'][skill] + self.attributes['averageRES']
            # Check if that's the highest of all skills in the list.
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = skill
        if self.skills['HackSkills']['Software'] != 0:
            auxVar = self.skills['HackSkills']['Software'] + self.attributes['averageRES']
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = 'Software'
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['RES'][0] = currentPeak
            self.attributePeaks['RES'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [RES Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [RES Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [RES Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [RES Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        # DEP Skills
        currentPeak = int()
        currentSkill = str()
        auxVar = int()
        if self.skills['HackSkills']['Software'] != 0:
            auxVar = self.skills['HackSkills']['Software'] + self.attributes['averageDEP']
            if auxVar > currentPeak:
                currentPeak = auxVar
                currentSkill = 'Software'
        # Now that we have the BOD Peak, check if it raises flags for this att.
        if currentPeak > 12:
            self.attributePeaks['DEP'][0] = currentPeak
            self.attributePeaks['DEP'][1] = True
            if 13 <= currentPeak <= 15:
                output += "    [DEP Peak: " + currentSkill + " at " + str(currentPeak) + "] +3 Flag points\n"
                flags += 3
            elif 16 <= currentPeak <= 17:
                output += "    [DEP Peak: " + currentSkill + " at " + str(currentPeak) + "] +7 Flag points\n"
                flags += 7
            elif 18 <= currentPeak <= 19:
                output += "    [DEP Peak: " + currentSkill + " at " + str(currentPeak) + "] +12 Flag points\n"
                flags += 12
            elif 20 <= currentPeak:
                output += "    [DEP Peak: " + currentSkill + " at " + str(currentPeak) + "] +18 Flag points\n"
                flags += 18

        if flags > 0:
            if self.verbose:
                print(output)
            self.accrued_flags += flags

    def CheckArmor(self):
        flags = int()
        output = "<Armor>\n"

        if self.armor - 25 > 0:
            flags += int((self.armor - 25) / 3)
            output += "    [" + str(self.armor) + " armor, 1 Flag for each 3 over 25] +" + str(flags) + " Flag points\n"

        if flags > 0:
            if self.verbose:
                print(output)
            self.accrued_flags += flags

    def CheckWareEssence(self):

        # Check awakened status
        if self.talent == 'Magician' \
                or self.talent == 'Aspected Magician' \
                or self.talent == 'Explorer' \
                or self.talent == 'Enchanter' \
                or self.talent == 'Apprentice' \
                or self.talent == 'Aware' \
                or self.talent == 'Adept' \
                or self.talent == 'Mystic Adept':
            # Ware flags for awakened are tripled.
            awakenedMult = 3
        else:
            awakenedMult = 1
        # Ware
        if self.ware is not None:
            flags = int()
            output = "<Ware>\n"

            for ware in self.ware.keys():
                if ware == 'Adapsin':
                    flags += 1 * awakenedMult
                    output += "    [Adapsin] +" + str(1 * awakenedMult) + " Flag points\n"
                elif ware == 'Pain Editor':
                    flags += 3 * awakenedMult
                    output += "    [Pain Editor] +" + str(3 * awakenedMult) + " Flag points\n"
                elif ware == 'Move-by-Wire':
                    if self.ware[ware] > 1:
                        flags += 1 * awakenedMult
                        output += "    [Move-by-Wire] +" + str(1 * awakenedMult) + " Flag points\n"
                elif ware.find('Genetic Optimization') != -1:
                    flags += 1 * awakenedMult
                    output += "    [Genetic Optimization] +" + str(1 * awakenedMult) + " Flag points\n"
                elif ware == 'Narco':
                    flags += 1 * awakenedMult
                    output += "    [Narco] +" + str(1 * awakenedMult) + " Flag points\n"
                elif ware == 'Gastric Neurostimulator':
                    flags += 2 * awakenedMult
                    output += "    [Gastric Neurostimulator] +" + str(2 * awakenedMult) + " Flag points\n"
                elif ware == 'Platelet Factories':
                    flags += 2 * awakenedMult
                    output += "    [Platelet Factories] +" + str(2 * awakenedMult) + " Flag points\n"
                else:
                    continue

            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

        # Awakened Essence
        if bool(self.essence) and awakenedMult == 3 and self.essence['Total'] < 6:
            flags = int()
            output = "<Awakened Essence Loss>\n"

            if 6 > self.essence['Total'] >= 5:
                flags += 2
                output += "    [5.9 - 5.0 Essence] +2 Flag points\n"
            elif 5 > self.essence['Total'] >= 4:
                flags += 4
                output += "    [4.9 - 4.0 Essence] +4 Flag points\n"
            elif 4 > self.essence['Total'] >= 3:
                flags += 6
                output += "    [3.9 - 3.0 Essence] +6 Flag points\n"
            elif 3 > self.essence['Total'] >= 2:
                flags += 8
                output += "    [2.9 - 2.0 Essence] +8 Flag points\n"
            elif 2 > self.essence['Total'] > 0:
                flags += 10
                output += "    [1.9 - 0.1 Essence] +10 Flag points\n"
            else:
                output += "    [Cyberzombie???]"

            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

        # Betaware/Deltaware
        if bool(self.essence):
            flags = int()
            output = "<Beta/Delta Base Essence>\n"

            try:
                if self.essence['Betaware'] > 0:
                    flags += int(self.essence['Betaware'])
                    output += "    [Betaware Essence] +" + str(int(self.essence['Betaware'])) + " Flag points\n"
            except KeyError:
                pass
            try:
                if self.essence['Deltaware'] > 0:
                    flags += int(self.essence['Deltaware'] * 2)
                    output += "    [Deltaware Essence] +" + str(int(self.essence['Deltaware'] * 2)) + " Flag points\n"
            except KeyError:
                pass
            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

    def CheckFociSpellsPowers(self):
        # Foci
        if self.foci is not None:
            flags = int()
            output = "<Foci>\n"
            for focus in self.foci:
                if focus[0] == 'Power Focus':
                    if 4 <= focus[1] <= 5:
                        flags += 1
                        output += "    [R" + str(focus[1]) + " " + str(focus[0]) + "] +1 Flag points\n"
                    elif 6 <= focus[1] <= 7:
                        flags += 2
                        output += "    [R" + str(focus[1]) + " " + str(focus[0]) + "] +2 Flag points\n"
                    elif 8 <= focus[1]:
                        flags += 4
                        output += "    [R" + str(focus[1]) + " " + str(focus[0]) + "] +4 Flag points\n"
                else:
                    if 6 <= focus[1] <= 7:
                        flags += 1
                        output += "    [R" + str(focus[1]) + " " + str(focus[0]) + "] +1 Flag points\n"
                    elif 8 <= focus[1] <= 9:
                        flags += 2
                        output += "    [R" + str(focus[1]) + " " + str(focus[0]) + "] +2 Flag points\n"
                    elif 10 <= focus[1]:
                        flags += 4
                        output += "    [R" + str(focus[1]) + " " + str(focus[0]) + "] +4 Flag points\n"

            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

        # Spells
        if self.spells is not None:
            flags = int()
            output = "<Spells>\n"
            try:
                if self.qualities['Dedicated Spellslinger']:
                    spellCount = self.spells - self.skills['MAGSkills']['Spellcasting']
                    if spellCount < 10:
                        pass
                    else:
                        flags += int(spellCount - 10)
                        output += "    [" + str(
                            spellCount) + " spells over 10, minus Dedicated Spellslinger spells] +" + str(
                            flags) + " Flag points\n"
            except KeyError:
                pass

            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

        # Adept Powers
        if self.adeptPowers is not None:
            flags = int()
            output = "<Adept Powers>\n"

            # Mystic Aptitude
            try:
                if self.adeptPowers['Mystic Aptitude'] >= 0:
                    flags += 2
                    output += "    [Mystic Aptitude] +2 Flag points\n"
            except KeyError:
                pass
            # Heightened Concentration
            try:
                if self.adeptPowers['Heightened Concentration'] >= 0:
                    flags += 1
                    output += "    [Heightened Concentration] +1 Flag points\n"
            except KeyError:
                pass

            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

    def CheckInitiateTradition(self):
        # Initiate Grade
        if (self.initiateGrade is not None) and (self.initiateGrade > 0):
            flags = int()
            output = "<Initiate Grade>\n"

            # Technos
            if self.talent == "Technomancer" and self.initiateGrade > 2:
                flags += self.initiateGrade - 2
                output += "    [Submersion Grade " + str(self.initiateGrade) + "] +" + str(self.initiateGrade - 2) + " Flag points\n"
            # Awakened
            else:
                awakenedFlags = int()
                if self.initiateGrade <= 3:
                    awakenedFlags = self.initiateGrade
                elif 4 <= self.initiateGrade <= 6:
                    awakenedFlags = 3 + ((self.initiateGrade - 3) * 2)
                elif self.initiateGrade <= 7:
                    awakenedFlags = 9
                    for i in range(7, self.initiateGrade + 1, 1):
                        awakenedFlags += math.ceil(i / 2)
                flags += awakenedFlags
                output += "    [Initiate Grade " + str(self.initiateGrade) + "] +" + str(awakenedFlags) + " Flag points\n"

            # Blood Mage
            if self.bloodMage:
                flags += 3
                output += "    [Blood Mage] +3 Flag points\n"
            # Toxic Mage
            if self.toxicMage:
                flags += 5
                output += "    [Toxic Mage] +5 Flag points\n"

            if flags > 0:
                if self.verbose:
                    print(output)
                self.accrued_flags += flags

    def __del__(self):
        self.qualities.clear()
        self.foci.clear()
        self.adeptPowers.clear()
        self.ware.clear()
