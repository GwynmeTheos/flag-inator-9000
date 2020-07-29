# Talent flag checker script


def talentFlagCheck(character):
    accruedFlags = 0

    if character['character']['prioritytalent'] == "Technomancer":
        accruedFlags += 3
        print("    [Technomancer] = +3 Flag")

    elif character['character']['prioritytalent'] == "Aspected Magician":
        accruedFlags += 1
        print("    [Aspected Magician] = +1 Flag")

    elif character['character']['prioritytalent'] == "Adept":
        accruedFlags += 2
        print("    [Adept] = +2 Flag")

    elif character['character']['prioritytalent'] == "Magician":
        accruedFlags += 3
        print("    [Magician] = +3 Flag")

    elif character['character']['prioritytalent'] == "Mystic Adept":
        accruedFlags += 7
        print("    [Mystic Adept] = +7 Flag")

    return accruedFlags
