# Initiate Grade flag checker.

import math


def initiateFlagCheck(character):
    accruedFlags = 0

    if character['character']['magenabled'] == "True" and character['character']['initiategrade'] != "0":
        initiationGrade = int(character['character']['initiategrade'])
        try:
            for grade in range(1, initiationGrade + 1, 1):
                if 1 <= grade < 4:   # IG 1-3
                    accruedFlags += 1
                    print("    [Initiatiate Grade " + str(grade) + "] = +1 Flag")
                elif 4 <= grade < 7:   # IG 4-6
                    accruedFlags += 2
                    print("    [Initiatiate Grade " + str(grade) + "] = +2 Flag")
                elif 7 <= grade:   # IG 7+
                    accruedFlags += math.ceil(grade / 2)
                    print("    [Initiatiate Grade " + str(grade) + "] = +" + str(math.ceil(grade / 2)) + " Flag")
        except TypeError:
            pass
        try:
            for art in character['character']['arts']['art']:
                if art['name'] == "Blood Magic":
                    accruedFlags += 3
                    print("\n    [Blood Magic] = +3 Flag")
        except TypeError:
            pass

    return accruedFlags
