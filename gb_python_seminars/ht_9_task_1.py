import csv
import json
from random import randint

FILE_NAME = "quadro.csv"


# def generate_csv_file(FILE_NAME, rows):
#     with open(f"{FILE_NAME}", "a") as csv_f:
#         text = [(randint(1, 100), randint(1, 100), randint(1, 100)) for i in range(rows+1)]
#         csv_writer = csv.writer(csv_f)
#         for line in text:
#             csv_writer.writerow(line)
#
# # generate_csv_file(FILE_NAME, 10)
#
# def save_to_json(myFunc):
#     def wrapper(*args):
#         with open(f"{args[0]}", "r") as csv_file:
#             csv_reader = csv.reader(csv_file)
#             quadroDict = {}
#             for i, line in enumerate(csv_reader):
#                 quadroDict[i] = myFunc(*line)
#             with open("results.json", "w") as json_writer:
#                 json.dump(quadroDict, json_writer)


def find_root(fileName):
    with open(f"{fileName}", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        rootList = []
        for line in csv_reader:
            if line:
                a, b, c = [int(x) for x in line]
                D = b ** 2 - 4 * a * c
                if D < 0:
                    rootList.append([a, b, c, None])
                elif D == 1:
                    rootList.append([a, b, c, -b / (2 * a)])
                else:
                    rootList.append([a, b, c, (((-b + D ** 0.5) / (2 * a)), ((-b - D ** 0.5) / (2 * a)))])
        return rootList


print(find_root(FILE_NAME))
