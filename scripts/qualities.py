# Quality flag checker.


def qualityFlagCheck(character):
    accruedFlags = 0

    try:
        inDebtQual = 0

        for quality in character['character']['qualities']['quality']:
            # Archivist
            if quality['name'] == 'Archivist':
                accruedFlags += 5
                print("    [Archivist] = +5 Flag")

            # Astral Hazing
            elif quality['name'] == 'Astral Hazing' and character['character']['prioritytalent'] == 'Mundane':
                accruedFlags += 6
                print("    [Astral Hazing] = +6 Flag")

            # Prototype Transhuman
            elif quality['name'] == 'Prototype Transhuman':
                accruedFlags += 5
                print("    [Prototype Transhuman] = +5 Flag")

            # Day Job
            elif quality['name'] == 'Day Job (10 hrs)':
                accruedFlags += 1
                print("    [Day Job (10 hrs)] = +1 Flag")

            elif quality['name'] == 'Day Job (20 hrs)':
                accruedFlags += 3
                print("    [Day Job (20 hrs)] = +3 Flag")

            elif quality['name'] == 'Day Job (40 hrs)':
                accruedFlags += 5
                print("    [Day Job (40 hrs)] = +5 Flag")

            # Fame
            elif quality['name'] == 'Fame: Local':
                accruedFlags += 3
                print("    [Fame: Local] = +3 Flag")

            elif quality['name'] == 'Fame: National':
                accruedFlags += 5
                print("    [Fame: National] = +5 Flag")

            elif quality['name'] == 'Fame: Megacorporate':
                accruedFlags += 7
                print("    [Fame: Megacorporate] = +7 Flag")

            elif quality['name'] == 'Fame: Global':
                accruedFlags += 9
                print("    [Fame: Global] = +9 Flag")

            # SURGE
            elif quality['name'] == 'Changeling (Class I SURGE)':
                accruedFlags += 2
                print("    [Changeling (Class I SURGE)] = +2 Flag")

            elif quality['name'] == 'Changeling (Class II SURGE)':
                accruedFlags += 4
                print("    [Changeling (Class II SURGE)] = +4 Flag")

            elif quality['name'] == 'Changeling (Class III SURGE)':
                accruedFlags += 6
                print("    [Changeling (Class III SURGE)] = +6 Flag")

            # HMHVV
            elif quality['name'] == 'Carrier (HMHVV Strain II)':
                accruedFlags += 5
                print("    [Carrier (HMHVV Strain II)] = +5 Flag")

            elif quality['name'] == 'Carrier (HMHVV Strain III)':
                accruedFlags += 5
                print("    [Carrier (HMHVV Strain III)] = +5 Flag")

            elif quality['name'] == 'Infected: Bandersnatch':
                accruedFlags += 14
                print("    [Infected: Bandersnatch] = +14 Flag")

            elif quality['name'] == 'Infected: Banshee':
                accruedFlags += 16
                print("    [Infected: Banshee] = +16 Flag")

            elif quality['name'] == 'Infected: Dzoo-Noo-Qua':
                accruedFlags += 16
                print("    [Infected: Dzoo-Noo-Qua] = +16 Flag")

            elif quality['name'] == 'Infected: Fomoraig':
                accruedFlags += 14
                print("    [Infected: Fomoraig] = +14 Flag")

            elif quality['name'] == 'Infected: Ghoul (Human)':
                accruedFlags += 12
                print("    [Infected: Ghoul (Human)] = +12 Flag")

            elif quality['name'] == 'Infected: Ghoul (Dwarf)':
                accruedFlags += 12
                print("    [Infected: Ghoul (Dwarf)] = +12 Flag")

            elif quality['name'] == 'Infected: Ghoul (Elf)':
                accruedFlags += 12
                print("    [Infected: Ghoul (Elf)] = +12 Flag")

            elif quality['name'] == 'Infected: Ghoul (Ork)':
                accruedFlags += 12
                print("    [Infected: Ghoul (Ork)] = +12 Flag")

            elif quality['name'] == 'Infected: Ghoul (Sasquatch)':
                accruedFlags += 12
                print("    [Infected: Ghoul (Sasquatch)] = +12 Flag")

            elif quality['name'] == 'Infected: Ghoul (Troll)':
                accruedFlags += 12
                print("    [Infected: Ghoul (Sasquatch)] = +12 Flag")

            elif quality['name'] == 'Infected: Gnawer':
                accruedFlags += 14
                print("    [Infected: Gnawer] = +14 Flag")

            elif quality['name'] == 'Infected: Goblin':
                accruedFlags += 16
                print("    [Infected: Goblin] = +16 Flag")

            elif quality['name'] == 'Infected: Grendel':
                accruedFlags += 14
                print("    [Infected: Grendel] = +14 Flag")

            elif quality['name'] == 'Infected: Harvester':
                accruedFlags += 14
                print("    [Infected: Harvester] = +14 Flag")

            elif quality['name'] == 'Infected: Loup-Garou':
                accruedFlags += 14
                print("    [Infected: Loup-Garou] = +14 Flag")

            elif quality['name'] == 'Infected: Mutaqua':
                accruedFlags += 16
                print("    [Infected: Mutaqua] = +16 Flag")

            elif quality['name'] == 'Infected: Nosferatu':
                accruedFlags += 16
                print("    [Infected: Nosferatu] = +16 Flag")

            elif quality['name'] == 'Infected: Sukuyan (Human)':
                accruedFlags += 16
                print("    [Infected: Sukuyan (Human)] = +16 Flag")

            elif quality['name'] == 'Infected: Sukuyan (Non-Human)':
                accruedFlags += 16
                print("    [Infected: Sukuyan (Non-Human)] = +16 Flag")

            elif quality['name'] == 'Infected: Vampire (Human)':
                accruedFlags += 16
                print("    [Infected: Vampire (Human)] = +16 Flag")

            elif quality['name'] == 'Infected: Vampire (Non-Human)':
                accruedFlags += 16
                print("    [Infected: Vampire (Non-Human)] = +16 Flag")

            elif quality['name'] == 'Infected: Wendigo':
                accruedFlags += 16
                print("    [Infected: Wendigo] = +16 Flag")

            # Exceptional Attribute
            elif quality['name'] == 'Exceptional Attribute':
                accruedFlags += 2
                print("    [Exceptional Attribute (" + quality['extra'] + ")] = +2 Flag")

            # Dracoform
            elif quality['name'] == 'Latent Dracomorphosis':
                accruedFlags += 19
                print("    [Latent Dracomorphosis] = +19 Flag")

            elif quality['name'] == 'Dracoform (Eastern Drake)':
                accruedFlags += 19
                print("    [Dracoform (Eastern Drake)] = +19 Flag")

            elif quality['name'] == 'Dracoform (Feathered Drake)':
                accruedFlags += 19
                print("    [Dracoform (Feathered Drake)] = +19 Flag")

            elif quality['name'] == 'Dracoform (Sea Drake)':
                accruedFlags += 19
                print("    [Dracoform (Sea Drake)] = +19 Flag")

            elif quality['name'] == 'Dracoform (Western Drake)':
                accruedFlags += 19
                print("    [Dracoform (Western Drake)] = +19 Flag")

            # In Debt
            elif quality['name'] == 'In Debt':
                inDebtQual += 1

        # In Debt 3-5
        if 3 <= inDebtQual < 6:
            accruedFlags += 2
            print("    [In Debt 3-5] = +2 Flag")
        # In Debt 6-8
        elif 6 <= inDebtQual < 8:
            accruedFlags += 4
            print("    [In Debt 6-8] = +4 Flag")
        # In Debt 9-11
        elif 9 <= inDebtQual < 11:
            accruedFlags += 6
            print("    [In Debt 9-11] = +6 Flag")
        # In Debt 12-14
        elif 12 <= inDebtQual < 14:
            accruedFlags += 8
            print("    [In Debt 12-14] = +8 Flag")
        # In Debt 15
        elif inDebtQual == 15:
            accruedFlags += 10
            print("    [In Debt 15] = +10 Flag")

    except TypeError:
        pass

    return accruedFlags
