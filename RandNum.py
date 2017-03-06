import random
import Rad

def main():
    ans = random.randrange(1, 11)
    keepGoing = True
    while keepGoing:
        guess = Rad.userInt("Enter a number from 1-10: ")
        if guess == ans:
            print "BITCH YOU GUESSED IT"
            keepGoing = False
main()