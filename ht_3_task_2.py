from collections import Counter

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
text = 'Hello world! Hello Python~ Hello again_'

newText = text.lower()
print(newText)
for element in newText:
    if element in punc:
        newText = newText.replace(element, "")
print(newText)
newText =  newText.split()
print(newText)
top_ten = Counter(newText).most_common(10)
print(list(top_ten))

text = "Python is an interpreted, high-level, general-purpose programming language. " \
       "Created by Guido van Rossum and first released in 1991, " \
       "Python's design philosophy emphasizes code readability " \
       "with its notable use of significant whitespace. Its language " \
       "constructs and object-oriented approach aim to help programmers" \
       " write clear, logical code for small and large-scale projects."




import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже
from collections import Counter

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

newText = text.lower()
for element in newText:
    if element in punc:
        newText = newText.replace(element, "")
newText =  newText.split()
top_ten = Counter(newText).most_common(10)
print(list(top_ten))