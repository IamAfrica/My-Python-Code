#Jordan Darling made this 4/30/17
#Uses counting theory, loops, and statements to deduce a criminal

import Rad

suspects = ['Miss Scarlet', 'Col Mustard', 'Mr Green']
weapons = ['Pipe', 'Wrench', 'Candlestick']
p = []

# Adds suspects and weapons and combines them to make a list of all possiblities
def makep():
    for suspect in suspects:
        for weapon in weapons:
            p.append("%s %s" %(suspect, weapon))

# Removes the weapons and suspects from the list p
def sort(clue):
    for x in p:
        if clue in x.lower():
            p.remove(x)
    
def main():
    
    makep()
    
    while (len(p) > 1):
        print "%s possibilities left" % len(p)
        
        user = Rad.userString("Is the clue about a weapon or suspect (w or s)?:")
        
        if user.lower() == 'w':
            print "Enter the weapon that was not used %s:" % weapons
            notweapon = Rad.userString("")
            sort(notweapon.lower())
        elif user.lower() == 's':
            print "Enter the innocent suspect %s:" % suspects
            innocent = Rad.userString("")
            sort(innocent.lower())
        else:
            print "Mistakes were made"

    print "The criminal is...."
    for x in suspects:
        if x in p:
            print x
    
main()