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




