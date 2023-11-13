import os
import pickle
import json
import re

res = [re.findall("\".*(\.json)\"", x) for x in os.listdir(os.getcwd())]
print (res)
def json_to_pickle():
    counter = 1
    for anyFile in os.listdir(os.getcwd()):
        if anyFile[-4:] == 'json':
            with open(anyFile, "r") as f:
                json_file = json.load(f)
            with open(f"pickleFile_{counter}", "wb") as pickle_file:
                pickle.dump(json_file, pickle_file)
            counter += 1
            with open(f"pickleFile_1", "rb") as f:
                res = pickle.load(f)
                print(res)