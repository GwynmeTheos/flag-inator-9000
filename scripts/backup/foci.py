# Foci flag checker.


def focusFlagCheck(character):
    accruedFlags = 0

    try:
        for gear in character['character']['gears']['gear']:
            if gear['category'] == 'Foci':
                if int(gear['rating']) == 5 or int(gear['rating']) == 4:
                    accruedFlags += 1
                    print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +1 Flag")

                elif int(gear['rating']) == 6 or int(gear['rating']) == 7:
                    accruedFlags += 2
                    print("    [Ratitg " + gear['rating'] + " " + gear['name'] + "] = +2 Flag")

                elif int(gear['rating']) == 8 or int(gear['rating']) == 9:
                    accruedFlags += 3
                    print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +3 Flag")

                elif int(gear['rating']) >= 10:
                    accruedFlags += 5
                    print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +5 Flag")
    except TypeError:
        pass

    return accruedFlags
