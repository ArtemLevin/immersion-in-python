import json
import csv
import os

from seminar_tasks.seminar_8.seminar_8_task_1 import user_id_by_access_level

FILENAME = "users.json"

user_id_by_access_level()

with (
    open(FILENAME,"r") as jsonFile,
    open("users.csv", "w") as csvFile ):

    jsonFileContent = json.load(jsonFile)
    print(jsonFileContent)
    all_data =[["access value", "id", "name"]]
    for x in jsonFileContent.keys():
        for el in jsonFileContent[x]:
            all_data.append([x, list(el.items())[0][0], list(el.items())[0][1]])
    print(all_data)
    csv_writer=csv.writer(csvFile, dialect="excel", delimiter=",")
    csv_writer.writerows(all_data)