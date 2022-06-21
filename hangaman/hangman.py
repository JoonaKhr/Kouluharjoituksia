import random as rand
from os import system

class Hangman:
    def __init__(self, wordlist):
        self.lives = 3
        self.guess = ''
        self.uniqueLetters, self.corrects, self.wrongs, self.wordlist = [], [], [], wordlist
        self.victory, self.lose = False, False
        self.start_game()

    @classmethod
    def from_csv(cls, file):
        wordlist = []
        with open(file, "r", encoding="utf8") as f:
            for line in f:
                wordlist.append(line)
        return cls(wordlist)
    #Create a list with all the unique letters in the selected word
    def uniqueLettersFunc(self, word):
        for elem in word:
            if elem not in self.uniqueLetters:
                self.uniqueLetters.append(elem)
    #Display word dashed until correct letters are guessed
    def displayWordDashed(self, word):
        for elem in word:
            if elem not in self.corrects:
                print('_', end='')
            else:
                print(elem, end='')
    #Add the guessed letter in either the 'self.corrects' list or the 'self.wrongs' list
    def addWordInList(self, guess):
        if guess not in self.corrects and guess in self.uniqueLetters:
            self.corrects.append(guess)
            self.corrects.sort()
        elif guess not in self.wrongs and guess not in self.uniqueLetters:
            self.wrongs.append(guess)
    #Cost one life on wrong guess and end the game on losing all lives
    def costLife(self, guess, word):
        self.lives
        if guess not in word:
            self.lives -= 1
    def pickRandomWord(self):
        randNumber = rand.randint(0, len(self.wordlist)-1)
        return self.wordlist[randNumber].strip()

    def start_game(self):
        #Put the unique letters in the word in a new list and sort said list
        word = self.pickRandomWord()
        self.uniqueLettersFunc(word)
        self.uniqueLetters.sort()
        while self.victory == False and self.lose == False:
            #Clear the screen every time a new guess is made so the terminal doesn't get cluttered
            system('cls')
            try:
                self.displayWordDashed(word)
                print('\nYou have guessed correctly: ', self.corrects, ' and wrongly: ', self.wrongs)
                print('Lives left: ', self.lives)
                self.guess = input('Please input a single letter\n').upper()[0]
                self.addWordInList(self.guess)
                #Check whether the player won with the last quess by comparing the sorted self.uniqueLetters and sorted self.corrects lists
                self.victory = self.uniqueLetters == self.corrects
            except:
                continue
            #Cost one life on wrong guess and check whether the player lost their last life
            self.costLife(self.guess, word)
            if self.lives == 0:
                self.lose = True
                #Clear the screen and display either the win or loss text
        system('cls')
        if self.victory == True:
            print('Congrats! You Won!')
        else:
            print(f'You lost! The word was: {word}')

Hangman.from_csv(r"D:\Atom\Projects\Python\hangaman\wordlist.txt")