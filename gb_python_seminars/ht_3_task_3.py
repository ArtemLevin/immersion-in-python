import itertools

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0


myBackpack = []
for item in items:
    if items[item] < max_weight:
        myBackpack.append({item: items[item]})
for i in range(2, len(items) + 1):
    backpack_i = list(itertools.combinations(items, i))
    itemDict = {}
    for combination in backpack_i:
        for item in combination:
            itemDict[item] = items[item]
        if sum(itemDict.values()) < max_weight:
            myBackpack.append(itemDict)
        itemDict = {}
print(myBackpack, "\n")
