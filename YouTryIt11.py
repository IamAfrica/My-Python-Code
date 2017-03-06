import Rad
import random

def main():
    numGuess = 0
    ans = random.randrange(1, 11)
    keepGoing = True
    while keepGoing:
        guess = Rad.userInt("Enter a number from 1-10: ")
        numGuess = numGuess + 1
        if guess == ans:
            print "BITCH YOU GUESSED IT! It took %s guesses" % numGuess
            keepGoing = False
        if guess < ans:
            print "Your number is too low"
        if guess > ans:
            print "Your number is too high"
            
main()