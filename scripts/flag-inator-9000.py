# main.py

# The PEP is stupid.

# Imports
import xmltodict, os, math, gc
# Character data class
import characterClass


def ReadSettings():
    settings = dict()
    try:
        with open('settings.arisu', 'r', encoding='UTF-8') as f:
            for lines in f.readlines():
                name, value = lines.split("=", 1)
                settings[name.strip()] = value.strip()

        return settings
    except FileNotFoundError:
        return -1


def StoreSettings(settings):
    lines = list()
    try:
        with open('settings.arisu', 'w', encoding='UTF-8') as f:
            for keys in settings.keys():
                lines.append(str(keys) + "=" + str(settings[keys]) + '\n')
            f.writelines(lines)

        return 0
    except FileNotFoundError:
        return -1


def MainMenu(settings):
    while True:
        # Check settings dict if the verbose option is active.
        if settings['verbose'] == 'True':
            verbose = 'Y'
        elif settings['verbose'] == 'False':
            verbose = 'N'
        else:
            verbose = 'Y'

        os.system("CLS")
        print("+------------------------------> FLAG-INATOR 9000 <-----------------------------+", end='\n')
        print("|                                                                               |", end='\n')
        print("|      This app will auto-calculate the flag points of a given character.       |", end="\n")
        print("|                                                                               |", end='\n')
        print("|                 Current supported Chummer Version: 3.212 Stable               |", end='\n')
        print("+-------------------------------------------------------------------------------+", end='\n')
        print("| Please select an option from below by typing the character in parenthesis to  |", end="\n")
        print("| begin.                                                                        |", end="\n")
        print("|                                                                               |", end='\n')
        print("| Current Options:   [{}] Show complete Flag log                                 |".format(verbose), end='\n')
        print("| Saves Folder:      {:51s}        |".format(settings['folder']), end='\n')
        print("+-------------------------------------------------------------------------------+", end='\n')
        print()
        print("(S) Check flags of a single character", end="\n")
        print("(B) Check flags of several characters", end="\n")
        print("(O) App settings and options", end="\n")
        print("(H) Show help and Information", end="\n")
        print("(Q) Quit", end="\n")
        print()
        selection = str(input("Selection: ")).upper().strip()

        if selection == 'S':
            SingleCheck(settings)

        elif selection == 'B':
            BatchCheck(settings)

        elif selection == 'O':
            settings = Options(settings)

        elif selection == 'H':
            ShowHelp()

        elif selection == 'Q':
            break

        else:
            continue

    return settings


def SingleCheck(settings):
    # The user's selection needs to be recorded through loops, to make the UI work, as such, we initialize it here.
    command = ""
    # Change dir to the folder in the options.
    os.chdir(settings['folder'])
    # List of save files. str[]
    saveFiles = list()
    # Loop through the files within the directory and find the ones named .chum5
    for file in os.listdir():
        if file[-6:] == ".chum5":
            saveFiles.append(file)
    # Find the number of pages we will need to generate.
    pageNumber = int(math.floor(len(saveFiles) / 10))
    # Initialize the current page, this will change later as the user goes through each page.
    currentPage = 0

    while True:
        gc.collect()
        # Loop over the save files, to check for list IndexErrors. If there is a list Index Error, just append an empty string.
        savesToShow = list()
        for i in range((currentPage * 10 + 0), (currentPage * 10 + 10), 1):
            try:
                savesToShow.append(saveFiles[i])
            except IndexError:
                savesToShow.append("")

        os.system("CLS")
        print("+------------------------------> FLAG-INATOR 9000 <-----------------------------+", end='\n')
        print("|                                                                               |", end='\n')
        # Loop through range and show the 10 files.
        for i in range(0, 10, 1):
            print("|   [{:3s}] {:63s}       |".format(str(currentPage * 10 + i), savesToShow[i]), end='\n')
        print("|                                                                               |", end='\n')
        print("+-------------------------------------------------------------------------------+", end='\n')
        print()
        if pageNumber > 0 and pageNumber != currentPage:
            print("(N) Next page")
        if pageNumber > 0 and currentPage != 0:
            print("(P) Previous page")
        print("(B) Go to previous menu.")

        selection = input("\nSelection: ")

        if selection.upper() == "B":
            break

        elif selection.upper() == "N" and pageNumber != currentPage:
            currentPage += 1
            continue

        elif selection.upper() == "P" and currentPage != 0:
            currentPage -= 1
            continue

        else:
            try:
                with open(str(saveFiles[int(selection)]), mode="r", encoding="utf-8") as f:
                    character = characterClass.Character(xmltodict.parse(f.read()), settings)
                    f.close()
            # They wrote a letter, so it doesn't get turned into a char because the cast is to type int.
            except ValueError:
                input("\nInvalid selection. Press enter to continue...")
                continue
            # They wrote some random ass number
            except IndexError:
                input("\nInvalid number. Press enter to continue...")
                continue
            # Probably would happen if they deleted the save file while in the app.
            except FileNotFoundError:
                print("File not found or could not be opened.", end="\n")
                print("If this issue persists, call Arisu-sensei.", end="\n")
                input("Press enter to continue...")
                continue
            else:
                character.CheckFlags()
                input()
                del character


def BatchCheck(settings):
    pass


def Options(settings):
    while True:
        os.system("CLS")
        print("+------------------------------> FLAG-INATOR 9000 <-----------------------------+", end='\n')
        print("|                                                                               |", end='\n')
        print("|  Verbose logging of Flags: {:5s}                                              |".format(settings['verbose']), end='\n')
        print("|  Save files folder: {:57s} |".format(settings['folder']), end='\n')
        print("|                                                                               |", end='\n')
        print("|                                                                               |", end='\n')
        print("+-------------------------------------------------------------------------------+", end='\n')
        print()
        print("(V) Turn verbose logging on and off.")
        print("(F) Change save file folder.")
        print("(B) Go to previous menu.")

        selection = str(input("Selection: ")).upper().strip()
        if selection == 'B':
            return settings

        elif selection == 'V':
            if settings['verbose'] == 'True':
                settings['verbose'] = 'False'
            elif settings['verbose'] == 'False':
                settings['verbose'] = 'True'
            else:
                settings['verbose'] = 'True'

        elif selection == 'F':
            print()
            print('Please copy and paste absolute or relative path to the folder.')
            print('Eg.: "../saves/" or "C:/Users/My_name/Desktop/ChummerSaves/"')
            print()
            print('Typing "DEFAULT" returns it to the default value.')
            print()
            newFolder = input("Folder name: ")
            if newFolder.upper() == 'DEFAULT':
                settings['folder'] = '../saves/'
            else:
                settings['folder'] = newFolder
        else:
            continue

    return settings


def ShowHelp():
    while True:
        os.system("CLS")
        print("+------------------------------> FLAG-INATOR 9000 <-----------------------------+", end='\n')
        print("|                                                                               |", end='\n')
        print("|                 App created by Arisu-sensei in August, 2020.                  |", end="\n")
        print("|                           Current app version: Stable 1                       |", end='\n')
        print("|                 Current supported Chummer Version: 3.212 Stable               |", end='\n')
        print("|                                                                               |", end='\n')
        print("|           The Flag Point Document can be found in the following link:         |", end="\n")
        print("|                            http://tiny.cc/zaoqsz                              |", end="\n")
        print("|                                                                               |", end='\n')
        print("+-------------------------------------------------------------------------------+", end='\n')
        print()
        print("(B) Go to previous menu.")

        selection = str(input("Selection: ")).upper().strip()
        if selection == 'B':
            return
        else:
            continue


def main():
    # Read user settings.
    settings = ReadSettings()
    if settings == -1:
        print("FileNotFoundError exception raised while reading or saving settings file.", end='\n\n')
        print("Check to see if the file is in the folder.", end='\n\n')
        print("If this problem persists, screenshot this window and message Arisu-sensei.", end='\n\n')

    # Initialize the main application.
    settings = MainMenu(settings)

    # If user quits properly, save settings file.
    settings = StoreSettings(settings)
    if settings == -1:
        print("FileNotFoundError exception raised while reading or saving settings file.", end='\n\n')
        print("Check to see if the file is in the folder.", end='\n\n')
        print("If this problem persists, screenshot this window and message Arisu-sensei.", end='\n\n')


if __name__ == '__main__':
    main()
