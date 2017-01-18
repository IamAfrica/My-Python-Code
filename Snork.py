print "Please enter a sentence:",
sen = raw_input()
length = len(sen)
encrypted = sen.replace('a', str(length))
encrypted = encrypted.replace ('e', str(length + 1))
encrypted = encrypted.replace ('i', str(length + 2))
encrypted = encrypted.replace ('o', str(length + 3))
encrypted = encrypted.replace ('u', str(length + 4))
print "The encrypted sentence is %s." % encrypted

decrypted = encrypted.replace (str(length), 'a')
decrypted = decrypted.replace (str(length + 1), 'e')
decrypted = decrypted.replace (str(length + 2), 'i')
decrypted = decrypted.replace (str(length + 3), 'o')
decrypted = decrypted.replace (str(length + 4), 'u');

print "The decrypted sentence is %s." % decrypted,
