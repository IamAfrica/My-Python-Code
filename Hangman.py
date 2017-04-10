import Rad
import random

# ---------------------------------------------------------
# Selects a random word from a file and returns it
# ---------------------------------------------------------
def pickWord():
    words = []
    f = open('HangManWords.txt')
    for w in f:
        w = w.strip()
        words.append(w)
    r = random.randrange(0, len(words))
    return words[r]
    
# ---------------------------------------------------------
# Displays the current board showing where letters have been guessed
# ---------------------------------------------------------

def displayBoard(board):
    for ch in board:
        print "%s " % ch,
    print
    
# ---------------------------------------------------------
# Asks user for letter and returns it
# ---------------------------------------------------------

def askUserForLetter():
    l = Rad.userString("Please enter a letter:")
    return l

def updateBoard(board, word, letter):
    missed = letter not in word
        
    for i in range(0, len(word)):
        if word[i] == letter:
            board[i] = letter
    return missed

def testForGameOver(board):
    return "*" not in board

def main():
    word = pickWord()
    board = []
    for ch in word:
        board.append('*')
    print board
    misses = 0
    gameOver = False
    while gameOver != True:
        displayBoard(board)
        letter = askUserForLetter()
        if updateBoard(board, word, letter) == True:
            misses = misses + 1
            print "The word doesn't contain %s. You have %s misse(s)." %(letter, misses)
            
        gameOver = testForGameOver(board)
        
    print "Ya did it"
    print "The word is %s" % word
    print "You had %s wrong guesses" % misses
    
main()