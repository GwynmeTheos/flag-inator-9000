# Talent flag checker script


def talentFlagCheck(talent):
    accruedFlags = 0

    if talent == 'Technomancer':
        accruedFlags += 3
        print("    [Technomancer] = +3 Flag")

    elif talent == 'Aspected Magician':
        accruedFlags += 1
        print("    [Aspected Magician] = +1 Flag")

    elif talent == 'Adept':
        accruedFlags += 2
        print("    [Adept] = +2 Flag")

    elif talent == 'Magician':
        accruedFlags += 3
        print("    [Magician] = +3 Flag")

    elif talent == 'Mystic Adept':
        accruedFlags += 7
        print("    [Mystic Adept] = +7 Flag")

    return accruedFlags
