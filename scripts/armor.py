# Armor flag checker.


def armorFlagCheck(character):
    accruedFlags = 0

    armorDict = {'defaultArmor': 0}
    extraArmor = 0

    # First thing to do is to find the armors that person own.
    try:
        for armor in character['character']['armors']['armor']:
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
                    totalArmorValue += int(mods['armor'])

                armorDict[armor['name']] = totalArmorValue
    except TypeError:
        pass

    # Now that we have the armor in a dict. We need to figure out if they have 'ware that gives armor.
    try:
        for ware in character['character']['cyberwares']['cyberware']:
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
        for quality in character['character']['qualities']['quality']:
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
        for power in character['character']['powers']['power']:
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

    if highestArmorValue - 25 < 2:
        pass
    else:
        accruedFlags += int((highestArmorValue - 25) / 3)
        print('    [' + str(highestArmorValue) + ' armor, each 3 points of armor over 25] = +' + str(int((highestArmorValue - 25) / 3)) + ' Flag')

    return accruedFlags
