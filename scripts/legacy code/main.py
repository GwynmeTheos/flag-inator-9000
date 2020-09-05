# Main
# Flag-inator 9000

# built-in modules
import os, time, math
# third-party modules
import xmltodict
# project scripts
import char_data, talents, initiate_grades, wares, skills, attributes, spells, adept_powers, qualities
import metatypes, awakened_essence, foci, armor


def checkCharacterFlags(character):
    # Initialize the flag counter.
    currentFlag = 0

    # Create the dictionaries for the skills and the character's attributes.
    skillsDict = char_data.createSkillDict(character)
    attributesDict = char_data.createAttributeDict(character)
    talent = char_data.findTalent(character)
    # If they have any Improvements that increase their skill rating, we need to find those.
    # skillImprovements = char_data.createImprovementDict(character)

    # For performance checking.
    start_time = time.time()

    # Metatypes
    print("\n-> Metatype:\n\n", end="")
    currentFlag += metatypes.metatypeFlagCheck(character)

    # Awakened or Emerged?
    print("\n-> Priority Talent:\n\n", end="")
    currentFlag += talents.talentFlagCheck(talent)

    # Initiation Grade
    print("\n-> Initiation Grade:\n\n", end="")
    currentFlag += initiate_grades.initiateFlagCheck(character)

    # Cyber/Bio/Gene/Nano'ware
    print("\n-> 'Ware:\n\n", end="")
    currentFlag += wares.wareFlagCheck(character)

    # Awakened Essence Loss
    print("\n-> Awakened Essence Loss:\n\n", end="")
    currentFlag += awakened_essence.awakenedEssenceFlagCheck(talent, character)

    # Magical Foci
    print("\n-> Magical Foci:\n\n", end="")
    currentFlag += foci.focusFlagCheck(character)

    # Skill Ratings and Total Dicepool
    print("\n-> Skills:\n\n", end="")
    currentFlag += skills.skillFlagCheck(skillsDict, attributesDict)

    # Attributes
    print("\n-> Attributes:\n\n", end="")
    currentFlag += attributes.attributeFlagCheck(character, attributesDict)

    # Spells
    print("\n-> Spells:\n\n", end="")
    currentFlag += spells.spellFlagCheck(character, skillsDict)

    # Adept Powers
    print("\n-> Adept Powers:\n\n", end="")
    currentFlag += adept_powers.adeptPowerFlagCheck(character)

    # Qualities
    print("\n-> Qualities:\n\n", end="")
    currentFlag += qualities.qualityFlagCheck(talent, character)

    # Armor
    print("\n-> Armor:\n\n", end="")
    currentFlag += armor.armorFlagCheck(character)

    print("\n---> Current Flag: " + str(currentFlag) + " <---\n")
    print("--- Finished in %s seconds ---" % (time.time() - start_time))


def main():
    while True:
        os.system("CLS")
        print("------------> WELCOME TO THE FLAG-INATOR 9000 <------------", end="\n\n")
        print("This app will auto-calculate the flag points of a character.", end="\n")
        print("Please select an option from below by typing the character in parenthesis.", end="\n\n")

        print("(S)ingle character flag checking", end="\n")
        print("(B)atch flag checking", end="\n")
        print("(I)nformation", end="\n")
        print("(Q)uit app", end="\n\n")

        selection = str(input("Selection: ")).upper()

        if selection == "S":
            os.chdir("../saves")
            saveFiles = list()
            # Loop through the files withing the directory and find the ones named .chum5
            for file in os.listdir():
                if file[-6:] == ".chum5":
                    saveFiles.append(file)
            # Find the number of pages we will need to generate.
            pageNumber = int(math.ceil(len(saveFiles) / 10))
            currentPage = 1

            while True:
                os.system("CLS")
                print("\n-----------------------------------------------------------", end="\n\n")

                print("Please choose an item from the list below: ", end="\n\n")

                print("[B] Go back to previous screen.", end="\n")
                print("[A] Show all saves in a single page.", end="\n\n")

                if pageNumber > 1 and pageNumber != currentPage:
                    print("[N]ext page", end="\n")
                if pageNumber > 1 and currentPage != 1:
                    print("[P]revious page", end="\n")
                print()
                for file in range(0, 10, 1):
                    key = (10 * (currentPage - 1)) + file
                    try:
                        print("[" + str(key) + "] " + str(saveFiles[key]), end="\n")
                    except IndexError:
                        continue

                selection = input("\nSelection: ")

                if selection.upper() == "A":
                    pass
                elif selection.upper() == "B":
                    break
                elif selection.upper() == "N" and pageNumber != currentPage:
                    currentPage += 1
                    continue
                elif selection.upper() == "P" and currentPage != 1:
                    currentPage -= 1
                    continue
                else:
                    try:
                        with open(str(saveFiles[int(selection)]), mode="r", encoding="utf-8") as f:
                            checkCharacterFlags(xmltodict.parse(f.read()))
                    except ValueError:
                        input("\nInvalid selection. Press enter to continue...")
                        continue
                    except IndexError:
                        input("\nInvalid selection. Press enter to continue...")
                        continue
                    except FileNotFoundError:
                        print("File not found or could not be opened.", end="\n")
                        print("If this issue persists, call Arisu-sensei.", end="\n")
                        continue

                input("\nPress enter to continue...")
        elif selection == "B":
            os.system("CLS")
            print("\n-----------------------------------------------------------", end="\n\n")

            print("Please create a folder in the \"saves\" folder and input the folder's name below.", end="\n")
            print("Leave it empty to check the \"saves\" folder. (May cause severe slowness.)")
            print("B returns to previous menu screen.", end="\n\n")
            folder = str(input("Folder name: "))

            if folder.upper() == "B":
                continue
            elif folder == "":
                try:
                    os.chdir("../saves")
                except FileNotFoundError:
                    print("Saves folder could not be found, please create it or contact Arisu-sensei.", end="\n")
                else:
                    for file in os.listdir():
                        if file[-6:] == ".chum5":
                            try:
                                with open(str(file), mode="r", encoding="utf-8") as f:
                                    checkCharacterFlags(xmltodict.parse(f.read()))
                            except FileNotFoundError:
                                print("File name: " + file + " not found or could not be opened.", end="\n")
                                print("If this issue persists, call Arisu-sensei.", end="\n")
                        else:
                            continue
            else:
                try:
                    os.chdir("../saves/" + folder)
                except FileNotFoundError:
                    print("Specified folder could not be found, please create it or contact Arisu-sensei.", end="\n")
                else:
                    for file in os.listdir():
                        if file[-6:] == ".chum5":
                            try:
                                with open(str(file), mode="r", encoding="utf-8") as f:
                                    checkCharacterFlags(xmltodict.parse(f.read()))
                            except FileNotFoundError:
                                print("File name: " + file + " not found or could not be opened.", end="\n")
                                print("If this issue persists, call Arisu-sensei.", end="\n")
                        else:
                            continue

            input("\nPress enter to continue...")
        elif selection == "I":
            os.system("CLS")
            print("\n-----------------------------------------------------------", end="\n\n")

            input("\nPress enter to continue...")
        elif selection == "Q":
            os.system("CLS")
            input("\nPress enter to continue...")
            quit()
        else:
            continue

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
