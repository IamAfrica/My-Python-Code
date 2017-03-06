import Rad

def main():
    keepGoing = True
    while keepGoing:
        msg = Rad.userString("Enter a message (enter exit to quit): ")
        if msg == 'quit':
            keepGoing = False
        else:
            print msg
main()