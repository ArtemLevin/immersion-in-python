def decToHex(num):
    controlNum = num

    hexDict = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    hexList = []
    i = 0
    while num:
        num, part = divmod(num, 16)
        hexList.append(str(part))
        i += 1

    for i in range(len(hexList)):
        if hexList[i] in hexDict.keys():
            hexList[i] = hexDict[hexList[i]]

    print (f'Шестнадцатиричиное представление числа: {"".join(hexList[::-1])}')
    print (f'Проверка: {hex(controlNum)}')

decToHex(num)