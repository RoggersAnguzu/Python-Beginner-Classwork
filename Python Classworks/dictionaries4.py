sentence = "My mother favours my sister"
words = sentence.split()

replacements = {'My': 'your', 'my':'your'}

newwords = []

for word in words:
    if word in replacements:
        newwords.append(replacements[word])
    else:
        newwords.append(word)

response = " ".join(newwords)

print(response)
newwords2 = []
for word in words:
    newwords2.append(replacements.get(word, word))
response = " ".join(newwords2)
print(response)
