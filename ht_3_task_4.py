from collections import Counter

lst = [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7]
duplicatesList = []
duplicates = Counter(lst).most_common()
for item in duplicates:
    if item[1] > 1:
        duplicatesList.append(item[0])
sorted(duplicatesList)