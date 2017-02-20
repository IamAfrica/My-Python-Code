d = {}
for line in open('Splits.txt'):
    t = line.split(',')
    n = t[0].strip()
    a = t[1].strip()
    d[n] = a
    

print "Enter a name:",
q = raw_input()
print d[q]