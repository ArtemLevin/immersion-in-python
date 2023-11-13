import csv
import json
import re
with open("users.csv", "r", newline='') as csvFile:
    csv_reader = csv.reader(csvFile, dialect="excel-tab")

    for line in list(csv_reader)[1:]:

        for element in line:
            element = element.split(",")
            element[1] = f"{str(0)*(10 - len(element[1]))}{element[1]}"
            element[2] = element[2].capitalize()
            element.append(str(hash(element[1] + element[2])))
            line =",".join(element)
            print(line)