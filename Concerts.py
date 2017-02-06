import Rad

file = open('concerts.txt', 'r')
band = Rad.userString("Enter the band you want to follow:")

for line in file:
    if band in line:
        print line,
        
print "\n Haaaaave fun"