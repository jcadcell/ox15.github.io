import random
import sys
"""
Letter Guessing Game
"""

class Game(object):
    def __init__(self):
        # Split a string of uppercase letters into a list.
        self.stop = False
        self.length = 4
        self.score = 5
        self.vowels = "A,E,I,O,U".split(",")
        self.cons = "B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z".split(",")
        self.WORDLIST_FILENAME = "words.txt"
        try:
            print("Loading word list from file: "+self.WORDLIST_FILENAME)
            # inFile: file
            inFile = open(self.WORDLIST_FILENAME, 'r')
        except FileNotFoundError:
            print("File not found:", self.WORDLIST_FILENAME)
            sys.exit()
        else:
            # wordList: list of strings
            self.wordList = []
            for line in inFile:
                self.wordList.append(line.strip())
            print("  ", len(self.wordList), "words loaded.")

    def getScore(self):
        if self.score > 0:
            print("Your score is", str(self.score))
        else:
            print("You have 0 points. Game over.")
            self.stop=True

    def getWord(self, length):
        try: self.length = int(input("How long do you want the word to be? "))
        except ValueError: self.length=3
        print(self.length)
        self.stop=False
        print("Finding a valid "+str(self.length)+"-letter word...")
        print("Word length is", self.length)
        self.word = random.choice(self.wordList)
        while True:
            print(self.length)
            if len(self.word) == length:
                return self.word
            elif len(self.word) != length:
                print(self.word, "is not valid")
                self.word = random.choice(self.wordList)



    def makeChoices(self):
        self.wordChoices=""
        for i in range(0,self.length):
            if self.word[i] in self.cons:
                self.letterChoices = self.word[i] + \
                random.choice(self.vowels) + random.choice(self.cons)
            elif self.word[i] in self.vowels:
                self.letterChoices = self.word[i] + \
                random.choice(self.cons) + random.choice(self.cons)
            self.wordChoices = self.wordChoices \
            +"\n"+''.join(sorted(self.letterChoices))
        print("Word choices\n"+self.wordChoices)
        self.guess()

    def guess(self):
        while True:
            if self.stop == True: break
            guess = str(input("Enter your guess: ")).upper()
            if guess == self.word:
                print("You guessed right, the word was "+self.word)
                self.score += 3
                self.getScore()
                self.play()
            elif guess==".":
                print("The word was "+self.word)
                self.stop=True
                self.play()
            else:
                print("No, try again")
                self.score -= 1
                self.getScore()


    def play(self):
        while self.stop == False:
            mode = input("Type '.' to quit or press enter to play")
            if mode == ".":
                self.getScore()
                break
            else:
                self.word = self.getWord(self.length)
                print("Found", self.word)
                print("Word length is", self.length)
                self.makeChoices()

g=Game()

class TestGame(object):
    def testGetWord(self):
        test=Game()
        word=test.getWord(3)
        if len(word) != 3:
            print("Word length is "+str(len(word))+", not 3")
            return False
        print("PASS: "+word+" is "+str(len(word))+" letters long")
        return True
    def testGetWord2(self):
        test=Game()
        self.length=3
        self.stop=False
        print("Word length is", self.length)
        self.word = random.choice(g.wordList)
        while True:
            print(self.length)
            if len(self.word) == self.length:
                return True
            elif len(self.word) != self.length:
                print(self.word, "is not valid")
                self.word = random.choice(g.wordList)




t=TestGame()
success = t.testGetWord2()

if success:
    # Play the game
    print("Success!")
    g=Game()
    g.play()
else:
    print("FAIL: Testing getWord(length) failed!")

g=Game()
g.play()
