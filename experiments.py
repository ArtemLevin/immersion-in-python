

def funcCounter(func):
    counter = 0

import os


os.chdir("seminar_tasks")

print(os.getcwd())


#
# for i in range (4):
#     os.mkdir(f"newDir_{i}")
# print(list(os.listdir(os.getcwd())))

# for dir in os.listdir(os.getcwd()):
#     os.chdir(dir)
#     with open("hello_1.txt", "w") as f:
#         print(f"Hello, {dir}", object=f)
#     os.mkdir("oneMoreDir")
#     os.chdir("..")
# print(list(os.walk(os.getcwd())))


def isObjectIsFolderOrFile():
    for object in list(os.listdir(os.getcwd())):
        print(f"Object {object} is directory") if os.path.isdir(object) else print(f"Object {object} is file")


def pathToObject():
    for object in list(os.listdir(os.getcwd())):
        print(f"Absolute path to object: {os.path.abspath(object)}")


def objectSize():
    for object in list(os.listdir(os.getcwd())):
        print(f"Size of the object: {os.stat(object).st_size}")



def folderWalk(objectInfo, sumSize):

    for object in list(os.listdir(os.getcwd())):
        if os.path.isdir(object):

            objectInfo.append([object, os.path.isdir(object), os.path.abspath(object), sumSize])
            os.chdir(object)
            folderWalk(objectInfo, sumSize)
            for object in list(os.listdir(os.getcwd())):
                if not os.path.isdir(object):
                    objectInfo.append([object, os.path.isdir(object), os.path.abspath(object), os.stat(object).st_size])
                    sumSize += os.stat(object).st_size
            os.chdir("..")
    return objectInfo

objDict = []
sumSize = 0

for el in folderWalk(objDict, sumSize):
    print(el)
    print()
