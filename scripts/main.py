# main.py
# Flag-inator 9000

# built-in modules
import os, time, math
# third-party modules
import xmltodict
# project scripts
import char_data, talents, initiate_grades, wares, skills, attributes, spells, adept_powers, qualities, armor
import metatypes, awakened_essence, foci


def main():
    while True:
        os.system("CLS")
        print("""------------> WELCOME TO THE FLAG-INATOR 9000 <------------\n
Please type the full name of the file that you'd like to calculate the flag points of.
Exclude the \".chum5\" portion. Make sure the file is in the \"saves\" directory.
    \n""", end="")

        filename = input("File name: ")

        print("\n-----------------------------------------------------------")

        # Attempt to read and parse the Chummer file, if it doesn't work, send out an error message.
        try:
            with open(str('saves/' + filename + ".chum5"), mode="r", encoding="utf-8") as file:
                character = xmltodict.parse(file.read())
        except FileNotFoundError:
            print("""\nThis filename specified is wrong or the file is missing.\n
1) Make sure that the filename does NOT include the file extension: \".chum5\";
2) That the name is spelt correctly (case sensitive);
3) That the file is in the \"saves\" directory.

    If this issue persists, call Arisu-sensei.
    \n""", end="")

            input("Press enter to continue...")
            continue

        # The file has been read.

        # Initialize the flag counter.
        currentFlag = 0

        # Create the dictionaries for the skills and the character's attributes.
        skillsDict = char_data.createSkillDict()
        attributesDict = char_data.createAttributeDict(character)
        # If they have any Improvements that increase their skill rating, we need to find those.
        skillImprovements = char_data.createImprovementDict(character)

        # For performance checking.
        start_time = time.time()

        # Metatypes
        print("\n-> Qualities:\n\n", end="")
        currentFlag += metatypes.metatypeFlagCheck(character)

        # Awakened or Emerged?
        print("\n-> Priority Talent:\n\n", end="")
        currentFlag += talents.talentFlagCheck(character)

        # Initiation Grade
        print("\n-> Initiation Grade:\n\n", end="")
        currentFlag += initiate_grades.initiateFlagCheck(character)

        # Cyber/Bio/Gene/Nano'ware
        print("\n-> 'Ware:\n\n", end="")
        currentFlag += wares.wareFlagCheck(character)

        # Awakened Essence Loss
        print("\n-> Awakened Essence Loss:\n\n", end="")
        currentFlag += awakened_essence.awakenedEssenceFlagCheck(character)

        # Magical Foci
        print("\n-> Magical Foci:\n\n", end="")
        currentFlag += foci.focusFlagCheck(character)

        # Skill Ratings and Total Dicepool
        # print("\n-> Skills:\n\n", end="")
        # currentFlag += skills.skillFlagCheck(character, skillsDict, attributesDict, skillImprovements)

        # Attributes
        print("\n-> Attributes:\n\n", end="")
        currentFlag += attributes.attributeFlagCheck(character, attributesDict)

        # Spells
        print("\n-> Spells:\n\n", end="")
        currentFlag += spells.spellFlagCheck(character)

        # Adept Powers
        print("\n-> Adept Powers:\n\n", end="")
        currentFlag += adept_powers.adeptPowerFlagCheck(character)

        # Qualities
        print("\n-> Qualities:\n\n", end="")
        currentFlag += qualities.qualityFlagCheck(character)

        # Armor
        # print("\n-> Armor:\n\n", end="")
        # currentFlag += armor.armorFlagCheck(character)

        print("\n---> Current Flag: " + str(currentFlag) + " <---\n")
        print("--- Finished in %s seconds ---" % (time.time() - start_time))
        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()