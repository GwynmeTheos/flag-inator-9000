# Character class

class Character:
    accrued_flags = int()
    # Character talent and metatype/variancy
    talent = str()
    meta = dict()
    # Stuff everyone has.
    attributes = dict()
    skills = dict()
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
        pass

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
                    self.ware['name'] = {'Essence': float(essence), 'Grade': ware['grade'], 'Rating': int(ware['rating'])}
                # Special Formating: Rating * x.y
                elif ware['ess'].find('Rating * ') != -1:
                    essence = ware['ess'].replace('Rating * ', '')
                    essence = float(essence) * int(ware['rating'])
                    self.ware['name'] = {'Essence': float(essence), 'Grade': ware['grade'], 'Rating': int(ware['rating'])}
                else:
                    self.ware['name'] = {'Essence': float(ware['ess']), 'Grade': ware['grade'], 'Rating': int(ware['rating'])}
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
                if ware['Grade'] == 'Betaware' or ware['Grade'] == 'Betaware (Adapsin)':
                    betaCount += ware['Essence']
            self.essence['Betaware'] = betaCount
            # Delta
            deltaCount = float()
            for ware in self.ware.keys():
                if ware['Grade'] == 'Deltaware' or ware['Grade'] == 'Deltaware (Adapsin)':
                    deltaCount += ware['Essence']
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
            self.bloodMage = None
        # Toxic Mage
        try:
            if save_file['character']['tradition']['name'] == 'Toxic':
                self.toxicMage = True
        except TypeError:
            self.toxicMage = None

    def CheckFlags(self):
        pass

    def CheckMetatype(self):
        pass
