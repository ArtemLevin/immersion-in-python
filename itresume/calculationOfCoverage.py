import re

sentence = 'Это тест из <1> <5> <10> <200> <34> <500> <111> <45> <630> <10700> большого количества чисел'
percentage = 5
def coveredUsers(sentence, percentage):

    clicks = [int(x) for x in re.findall('<(.*?)>', sentence)]
    print(*clicks)
    for i in range(len(clicks)):
        sentence = re.sub('<.*?>', f" {clicks[i]*100 / percentage :.2f}", sentence, count=1)

    return sentence

print(coveredUsers(sentence, percentage))