import re

initialString = "bar(((foo)bar(ham)))(ham(toybar(yes)))"


def rotate(initialString):
    for word in re.findall('\((\w*)\)', initialString):
        initialString = re.sub(word, word[::-1], initialString, 1)
    return initialString


print(rotate(initialString))
