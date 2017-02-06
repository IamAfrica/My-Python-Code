import Rad

sentence = Rad.userString("Please enter a sentence:")
words = sentence.split(' ')
largeWords = []
mergWords = []
medWords = []
smallWords = []

for word in words:
    if len(word) > 5:
        largeWords.append(word)
    elif len(word) > 4:
        mergWords.append(word)
    elif len(word) > 3:
        medWords.append(word)
    else:
        smallWords.append(word)

print largeWords
print mergWords
print medWords
print smallWords