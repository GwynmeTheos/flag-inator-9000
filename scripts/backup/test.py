import xmltodict

with open("blodusmagus.chum5", mode="r", encoding="utf-8") as file:
    character = xmltodict.parse(file.read())

for limb in character['character']['cyberwares']['cyberware']:
    if limb['limbslot'] == 'arm':
        if limb['children']['cyberware']['name'] == "Customized Agility":
            print(limb['name'] + ": Rating " + limb['children']['cyberware']['rating'])
