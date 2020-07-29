# Metatype flag checker.


def metatypeFlagCheck(character):
    accruedFlags = 0

    # Elf
    if character['character']['metatype'] == 'Elf':
        accruedFlags += 2
        print("    [Elf] = +2 Flag")

    elif character['character']['metavariant'] == 'Dryad':
        accruedFlags += 5
        print("    [Elf: Dryad] = +5 Flag")

    elif character['character']['metavariant'] == 'Nocturna':
        accruedFlags += 6
        print("    [Elf: Nocturna] = +6 Flag")

    # Human
    elif character['character']['metavariant'] == 'Nartaki':
        accruedFlags += 3
        print("    [Human: Nartaki] = +3 Flag")

    # Ork
    elif character['character']['metavariant'] == 'Oni':
        accruedFlags += 1
        print("    [Ork: Oni] = +1 Flag")

    # Dwarf
    elif character['character']['metavariant'] == 'Gnome':
        accruedFlags += 5
        print("    [Dwarf: Gnome] = +5 Flag")

    # AI
    elif character['character']['metatype'] == 'A.I.':
        accruedFlags += 15
        print("    [A.I.] = +15 Flag")

    # Naga
    elif character['character']['metatype'] == 'Naga':
        accruedFlags += 14
        print("    [Naga] = +14 Flag")

    # Sasquatch
    elif character['character']['metatype'] == 'Sasquatch':
        accruedFlags += 10
        print("    [Sasquatch] = +10 Flag")

    # Centaur
    elif character['character']['metatype'] == 'Centaur':
        accruedFlags += 12
        print("    [Centaur] = +12 Flag")

    # Shapeshifter
    elif character['character']['metatypecategory'] == 'Shapeshifter':
        accruedFlags += 7
        print("    [Shapeshifter] = +7 Flag")

    return accruedFlags
