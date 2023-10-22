def params(**kwargs):
    myDict = {}
    for k, v in kwargs.items():
        try:
            hash(v)
        except:
            myDict[str(v)] = str(k)
        else:
            myDict[v] = k
    return myDict
print(params(a = True,
b = False,
c = True,
d = False))