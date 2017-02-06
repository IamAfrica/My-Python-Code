file = open('LandOfCon.txt', 'r')
discarded = []
for line in file:
    words = line.split(" ")
    for word in words:
        temp = word.replace(".", "")
        temp = word.replace(",", "")
        if len(word) == 4:
            discarded.append(temp)
        else:
            print word + " ",

print "\n\nDiscarded words: %s" % discarded