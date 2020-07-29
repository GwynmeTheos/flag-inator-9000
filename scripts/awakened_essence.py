# Awakened Essence flag checker.


def awakenedEssenceFlagCheck(character):
    accruedFlags = 0

    if character['character']['prioritytalent'] != 'Mundane' and character['character']['prioritytalent'] != 'Technomancer':
        if 6.0 == float(character['character']['totaless']):
            return 0
        elif 6.0 > float(character['character']['totaless']) >= 5.0:
            accruedFlags += 2
            print("    [Awakened at 5.9 to 5.0 Essence] = +2 Flag")

        elif 5.0 > float(character['character']['totaless']) >= 4.0:
            accruedFlags += 4
            print("    [Awakened at 4.9 to 4.0 Essence] = +4 Flag")

        elif 4.0 > float(character['character']['totaless']) >= 3.0:
            accruedFlags += 6
            print("    [Awakened at 3.9 to 3.0 Essence] = +6 Flag")

        elif 3.0 > float(character['character']['totaless']) >= 2.0:
            accruedFlags += 8
            print("    [Awakened at 2.9 to 2.0 Essence] = +8 Flag")

        elif 2.0 > float(character['character']['totaless']) >= 0.1:
            accruedFlags += 10
            print("    [Awakened at 1.9 to 0.1 Essence] = +10 Flag")

        else:
            print("    [Cyberzombie???]")

    return accruedFlags
