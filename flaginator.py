# Flag-inator 9000

import xmltodict

with open("Nyx_Neon_Jungle_Career.chum5", mode="r", encoding="utf-8") as file:
    doc = xmltodict.parse(file.read())

# for child in doc['character']['attributes']['attribute']:
#    print(child)
