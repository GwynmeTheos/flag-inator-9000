# Quality flag checker.


def qualityFlagCheck(talent, character):
    accruedFlags = 0

    try:
        inDebtQual = 0
        shivaArmsQual = 0
        dayJobQual = ""
        dayJobMod = 0
        fameQual = ""
        fameMod = 0

        for quality in character['character']['qualities']['quality']:
            # Archivist
            if quality['name'] == 'Archivist':
                accruedFlags += 2
                print("    [Archivist] = +2 Flag")

            # Metagenic

            elif quality['name'] == 'Astral Hazing' and talent == 'Mundane':
                accruedFlags += 6
                print("    [Astral Hazing] = +6 Flag")

            elif quality['name'] == 'Metagenetic Improvement (Body)' or \
                    quality['name'] == 'Metagenetic Improvement (Agility)' or \
                    quality['name'] == 'Metagenetic Improvement (Reaction)' or \
                    quality['name'] == 'Metagenetic Improvement (Strength)' or \
                    quality['name'] == 'Metagenetic Improvement (Charisma)' or \
                    quality['name'] == 'Metagenetic Improvement (Intuition)' or \
                    quality['name'] == 'Metagenetic Improvement (Logic)' or \
                    quality['name'] == 'Metagenetic Improvement (Willpower)':
                accruedFlags += 4
                print("    [" + quality['name'] + "] = +2 Flag")

            elif quality['name'] == 'Impaired Attribute (Body)' or \
                    quality['name'] == 'Impaired Attribute (Agility)' or \
                    quality['name'] == 'Impaired Attribute (Reaction)' or \
                    quality['name'] == 'Impaired Attribute (Strength)' or \
                    quality['name'] == 'Impaired Attribute (Charisma)' or \
                    quality['name'] == 'Impaired Attribute (Intuition)' or \
                    quality['name'] == 'Impaired Attribute (Logic)' or \
                    quality['name'] == 'Impaired Attribute (Willpower)':
                accruedFlags += 2
                print("    [" + quality['name'] + "] = +2 Flag")

            elif quality['name'] == 'Symbiosis':
                accruedFlags += 1
                print("    [Symbiosis] = +1 Flag")

            elif quality['name'] == 'Shiva Arms (Pair)':
                shivaArmsQual += 1

            # Prototype Transhuman
            elif quality['name'] == 'Prototype Transhuman':
                accruedFlags += 5
                print("    [Prototype Transhuman] = +5 Flag")

            # Day Job + Fame
            elif quality['name'] == 'Day Job (10 hrs)' and (dayJobQual != 'Day Job (20 hrs)' or dayJobQual != 'Day Job (40 hrs)'):
                dayJobQual = quality['name']
                dayJobMod = 0

            elif quality['name'] == 'Day Job (20 hrs)' and dayJobQual != 'Day Job (40hrs)':
                dayJobQual = quality['name']
                dayJobMod = 2

            elif quality['name'] == 'Day Job (40 hrs)':
                dayJobQual = quality['name']
                dayJobMod = 5

            elif quality['name'] == 'Fame: Local' and not (fameQual == 'Fame: National' or fameQual == 'Fame: Megacorporate' or fameQual == 'Fame: Global'):
                fameQual = quality['name']
                fameMod = 3

            elif quality['name'] == 'Fame: National' and not (fameQual == 'Fame: Megacorporate' or fameQual == 'Fame: Global'):
                fameQual = quality['name']
                fameMod = 7

            elif quality['name'] == 'Fame: Megacorporate' and not (fameQual == 'Fame: Global'):
                fameQual = quality['name']
                fameMod = 10

            elif quality['name'] == 'Fame: Global':
                fameQual = quality['name']
                fameMod = 12

            # HMHVV
            elif quality['name'] == 'Carrier (HMHVV Strain II)' or quality['name'] == 'Carrier (HMHVV Strain III)':
                accruedFlags += 5
                print("    [" + quality['name'] + "] = +5 Flag")

            # Strain Ia and I
            elif quality['name'] == 'Infected: Banshee' or \
                    quality['name'] == 'Infected: Dzoo-Noo-Qua' or \
                    quality['name'] == 'Infected: Goblin' or \
                    quality['name'] == 'Infected: Mutaqua' or \
                    quality['name'] == 'Infected: Nosferatu' or \
                    quality['name'] == 'Infected: Sukuyan (Human)' or \
                    quality['name'] == 'Infected: Sukuyan (Non-Human)' or \
                    quality['name'] == 'Infected: Vampire (Human)' or \
                    quality['name'] == 'Infected: Vampire (Non-Human)' or \
                    quality['name'] == 'Infected: Wendigo':
                accruedFlags += 16
                print("    [" + quality['name'] + "] = +16 Flag")

            # Strain II
            elif quality['name'] == 'Infected: Fomoraig' or \
                    quality['name'] == 'Infected: Bandersnatch' or \
                    quality['name'] == 'Infected: Gnawer' or \
                    quality['name'] == 'Infected: Grendel' or \
                    quality['name'] == 'Infected: Harvester' or \
                    quality['name'] == 'Infected: Loup-Garou':
                accruedFlags += 14
                print("    [" + quality['name'] + "] = +14 Flag")

            # Strain III
            elif quality['name'] == 'Infected: Ghoul (Human)' or \
                    quality['name'] == 'Infected: Ghoul (Dwarf)' or \
                    quality['name'] == 'Infected: Ghoul (Elf)' or \
                    quality['name'] == 'Infected: Ghoul (Ork)' or \
                    quality['name'] == 'Infected: Ghoul (Sasquatch)' or \
                    quality['name'] == 'Infected: Ghoul (Troll)':
                accruedFlags += 12
                print("    [" + quality['name'] + "] = +12 Flag")

            # Exceptional Attribute
            elif quality['name'] == 'Exceptional Attribute':
                accruedFlags += 2
                print("    [Exceptional Attribute (" + quality['extra'] + ")] = +2 Flag")

            # Dracoform
            elif quality['name'] == 'Latent Dracomorphosis':
                accruedFlags += 5
                print("    [Latent Dracomorphosis] = +5 Flag")

            elif quality['name'] == 'Dracoform (Eastern Drake)' or \
                    quality['name'] == 'Dracoform (Feathered Drake)' or \
                    quality['name'] == 'Dracoform (Sea Drake)' or \
                    quality['name'] == 'Dracoform (Western Drake)':
                accruedFlags += 19
                print("    [" + quality['name'] + "] = +19 Flag")

            # In Debt
            elif quality['name'] == 'In Debt':
                inDebtQual += 1

        # In Debt 3-5
        if 3 <= inDebtQual < 6:
            accruedFlags += 2
            print("    [In Debt 3-5] = +2 Flag")
        # In Debt 6-8
        elif 6 <= inDebtQual < 9:
            accruedFlags += 4
            print("    [In Debt 6-8] = +4 Flag")
        # In Debt 9-11
        elif 9 <= inDebtQual < 12:
            accruedFlags += 6
            print("    [In Debt 9-11] = +6 Flag")
        # In Debt 12-14
        elif 12 <= inDebtQual < 15:
            accruedFlags += 8
            print("    [In Debt 12-14] = +8 Flag")
        # In Debt 15
        elif inDebtQual == 15:
            accruedFlags += 10
            print("    [In Debt 15] = +10 Flag")

        # Shiva Arms
        if shivaArmsQual != 0:
            accruedFlags += shivaArmsQual
            print("    [Shiva Arms " + str(shivaArmsQual) + "] = +" + str(shivaArmsQual) + " Flag")

        # Fame + Day Job
        if fameQual == "" or dayJobQual == "":
            pass
        else:
            accruedFlags += dayJobMod + fameMod
            print("    [" + dayJobQual + " with " + fameQual + "] = +" + str(dayJobMod + fameMod) + " Flag")

    except TypeError:
        pass

    return accruedFlags
