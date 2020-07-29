# Initiate Grade flag checker.

import math


def initiateFlagCheck(character):
    accruedFlags = 0

    if character['character']['magenabled'] == "True" and character['character']['initiategrade'] != "0":
        initiationGrade = int(character['character']['initiategrade'])
        try:
            for grade in range(1, initiationGrade + 1, 1):
                if 1 <= grade < 4:
                    accruedFlags += 1
                    print("    [Initiatiate Grade " + str(grade) + "] = +1 Flag")
                elif 4 <= grade < 7:
                    accruedFlags += 2
                    print("    [Initiatiate Grade " + str(grade) + "] = +2 Flag")
                elif 7 <= grade:
                    accruedFlags += math.ceil(grade / 2)
                    print("    [Initiatiate Grade " + str(grade) + "] = +" + str(math.ceil(grade / 2)) + " Flag")
        except TypeError:
            pass
        try:
            for art in character['character']['arts']['art']:
                if art['name'] == "Blood Magic":
                    accruedFlags += 5
                    print("\n    [Blood Magic] = +5 Flag")
        except TypeError:
            pass

    return accruedFlags
