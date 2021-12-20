import random
from SecretWord import SecretWord

class WordGuess:

    def __init__(self, wordDic):
        #TODO: construct the WordGuess object by giving necessary attributes
        self.wordDic = wordDic
        self.allotted_guesses = 0
        self.guessed = []
        self.hint = ""
        

    def play(self):
        """ Plays out a single full game of Word Guess """
        #TODO: Plays out a single full game of Word Guess
        # randomly choose a word and update the hint attribute
        random_word = self.chooseSecretWord()
        self.hint = self.wordDic[random_word]
        print("A secret word has been randomly chosen!")
        # create two linkedlist, one is the sorted one, the other is the unsorted one
        unsorted_word = SecretWord()
        unsorted_word.setWord(random_word)
        sorted_word = SecretWord()
        sorted_word.setWord(random_word)
        sorted_word.sort()
        # calculate the edit distance and let the distance being the allotted_guess
        self.allotted_guesses = self.editDistance(str(unsorted_word), str(sorted_word))
        
        while True:
            # if there is no chance for guessing
            if self.allotted_guesses == 0:
                print("You are not able to solve the puzzle.")
                print("The secret word was: %s" %(str(unsorted_word)))
                break
            # if the player solve the puzzle correctly
            if unsorted_word.isSolved() == True:
                print("You solved the puzzle!")
                print("The secret word was: %s" %(str(unsorted_word)))
                break
            # keep printing the game progress
            print("You have %d guesses remaining" %(self.allotted_guesses))
            unsorted_word.printProgress()
            player_guess = self.getGuess()
            # if player wants hint
            if player_guess == "hint":
                print("Hint: %s" %(self.hint))
            else:
                correct_guess = unsorted_word.update(player_guess)
                if not correct_guess:
                    self.allotted_guesses -= 1
        

    def chooseSecretWord(self):
        """ Chooses the secret word that will be guessed """
        #TODO: randomly choose a word to be the secret word and return the word
        words = list(self.wordDic.keys())
        # randomly choose an integer
        choice = random.randint(0, len(words) - 1)
        return words[choice]
        

    def editDistance(self, s1, s2):
        """ Recursively returns the total number of insertions and deletions required to convert S1 into S2 """
        #TODO: calcueate the edit distance bewtween string s1 and s2 and return the value
        
        # base cases: if str1 or str2 is empty, there is as many insertion(deletion) as the length of str2 or str1
        if s1 == "":
            return len(s2)
        if s2 == "":
            return len(s1)
        
        # if the first letter of the two strings are the same, keep calling the funtion by ignoring the two first letters
        if s1[0] == s2[0]:
            return self.editDistance(s1[1:], s2[1:])
        else:
            # return the minimum between insertion action and deletion action
            return min(self.editDistance(s1[1:], s2) + 1, self.editDistance(s1, s2[1:]) + 1)
        

    def getGuess(self):
        """ Queries the user to guess a character in the secret word """
        #TODO: keep asking for player guess until player enter a letter has not been guessed
        while True:
            player_guess = input("Enter a character that has not been guessed or * for a hint: ")
            # if the player wants hint, the allotted_guesses subtract by one
            if player_guess == '*':
                self.allotted_guesses -= 1
                return "hint"
            # keep asking for input until the input has not been guessed
            else:
                if player_guess not in self.guessed:
                    self.guessed.append(player_guess)
                    return player_guess
                elif player_guess in self.guessed:
                    print("Invalid guess. You have already guessed this letter.")
