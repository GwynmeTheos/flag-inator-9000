# Foci flag checker.


def focusFlagCheck(character):
    accruedFlags = 0

    try:
        for gear in character['character']['gears']['gear']:
            if gear['category'] == 'Foci':
                if int(gear['rating']) == 4 or int(gear['rating']) == 5:
                    if gear['name'] == "Power Focus":
                        accruedFlags += 1
                        print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +1 Flag")
                    else:
                        continue

                elif int(gear['rating']) == 6 or int(gear['rating']) == 7:
                    if gear['name'] == "Power Focus":
                        accruedFlags += 2
                        print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +2 Flag")
                    else:
                        accruedFlags += 1
                        print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +1 Flag")

                elif int(gear['rating']) == 8 or int(gear['rating']) == 9:
                    if gear['name'] == "Power Focus":
                        accruedFlags += 4
                        print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +4 Flag")
                    else:
                        accruedFlags += 2
                        print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +2 Flag")

                elif int(gear['rating']) >= 10:
                    accruedFlags += 4
                    print("    [Rating " + gear['rating'] + " " + gear['name'] + "] = +4 Flag")
    except TypeError:
        pass

    return accruedFlags
