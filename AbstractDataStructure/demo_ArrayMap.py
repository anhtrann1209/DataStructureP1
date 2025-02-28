from ArrayMap import ArrayMap

#concept of set, no duplicates
liscense_plates = ArrayMap()
liscense_plates.put("BAT 1", "Bruce Wayne")
liscense_plates.put("BMT2164", "Major Boothroyd")
#replace to new owner
liscense_plates.put("BMT2164", "James Bond")
liscense_plates.put("4711-EA", "James Bond")
#values can be the same but not keys

print(liscense_plates.get("BAT 1"))

#allow iteration
for k in liscense_plates.keys():
    if k.startswith("B"):
        print(k)
for v in liscense_plates.values():
    if v.startswith("B"):
        print(v)

