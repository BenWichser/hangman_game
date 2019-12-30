# Author: Ben Wichser
# Date: 20191229
# Project:  A simple hangman game in Python, using a list of crossword words as
# list of legal words.  See Readme.md for more information.


import random


class Hangman:
    """
    Hangman game.

    Public attributes:
        self.guessed_list = list of strings - list of correct guesses, in word
            order
        self.wrong_guesses = set of letters guessed that are incorrect
        self.available_guesses = set of letters that remain available to guess.

    Public methods:
        play_game - plays the game
    """

    def __init__(self, word_list):
        """
        Init method.
        Accepts:
            word_list = list of legal English words.
        Creates:
            self._word = word to be guessed
            self.guessed_list = empty list for storing letters in word that
                are already guessed.
            self.all_guesses = empty list for storing all letters that are
                guessed.
            self.wrong_guesses = empty set for storing letter guessed
                that are incorrect.
            self.available_guesses = set of all alphabet. To be reduced as
                guesses are made.
        Returns nothing.
        """
        self._word = self.__word_selector(word_list)
        self.guessed_list = ['' for i in range(len(self._word))]
        self.all_guesses = []
        self.wrong_guesses = set()
        self.available_guesses = self.__alphabet_builder()

    def __str__(self):
        """Class reporter"""
        return "Hangman game object"

    def play_game(self):
        """
        Public method.
        Accepts self.
        Plays the game.
        Returns True if player wins and False if player loses.
        """
        self._word = self._word.upper()
        wrong_guess_limit = self.__difficulty_selector(self._word)
        while True:
            self.print_status(wrong_guess_limit)
            this_guess = self.__get_guess()
            self.available_guesses.remove(this_guess)
            self.all_guesses.append(this_guess)
            self.__guess_check(self._word, this_guess)
            if '' not in self.guessed_list:
                # game won
                print('You won!  The word was', self._word)
                return True
            elif len(self.wrong_guesses) == wrong_guess_limit:
                # game lost
                print('You lost.  The word was', self._word)
                return False

    def print_status(self, wrong_guess_limit):
        """
        Public method.
        Accepts:
            self = instance of Hangman class
            wrong_guess_limit = int -- number of incorrect guesses allowed.
        Prints the current situation.
        Returns True
        """
        if len(self.all_guesses) == 0:
            article = 'your first'
        else:
            article = 'your next'
        print('\n\nBefore you make', article, 'guess, here\'s the situation:')
        print('1) This is the word, as far as you have figured out so far:')
        print('    ', end = '')
        for char in self.guessed_list:
            if char == '':
                print('___', end=' ')
            else:
                print('_'+char+'_', end=' ')
        print('\n')
        print('2)  These are the letters you have already guessed:')
        print('    ', end = '')
        for letter in self.all_guesses:
            print(letter, end = ' ')
        print('\n')
        number_left = wrong_guess_limit - len(self.wrong_guesses)
        if number_left == 1:
            guess = 'guess'
        else:
            guess = 'guesses'
        print('3) You have', number_left, 'incorrect', guess, 'until you lose.'
              )
        return True

    def __word_selector(self, word_list):
        """
        Private method.
        Accepts:
            self -- instance of Hangman class
            word_list -- list of available words
        Returns a random word from self.word_list
        """
        word = random.choice(word_list)
        return word

    def __difficulty_selector(self, word):
        """
        Private method.
        Accepts:
            self = Hangman object
            word = word to guess (string)
        Asks player for number of incorrect guesses they would like to be
        allowed before they lose.
        Returns the number of guesses the player will allow themselves.
        """
        print('WELCOME TO OUR HANGMAN GAME')
        print('The word you will be guessing is', len(word),
              'letters long.')
        s = 'How many incorrect answers would you like to be allowed'
        t = 'before you lose? '
        print(s)
        wrong_guess_limit = int(input(t))
        return wrong_guess_limit

    def __alphabet_builder(self):
        """Private method.  Accepts self. Returns set with all alphabet UC"""
        alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y', 'Z'}
        return alphabet

    def __get_guess(self):
        """
        Private method.
        Accepts:
            self - instance of Hangman class
        Returns:
            this_guess = string - uppercase version of the player's guess.
        """
        raw_guess = input('What letter would you like to guess? ')
        while raw_guess.upper() not in self.available_guesses:
            print('Alas,', raw_guess, 'is not one of the letters left to guess.'
                  )
            raw_guess = input('What letter would you like to guess? ')
        guess = raw_guess.upper()
        return guess

    def __guess_check(self, word, this_guess):
        """
        Private method.
        Accepts:
            self = instance of Hangman class
            word = string - word we are checking against.
            this_guess = string -  current guess
        Modifies self.wrong_guesses and self.guessed_list, as appropriate.
        Returns True if this_guess is in word.  Returns False otherwise.
        """
        if this_guess in word:
            for i in range(len(word)):
                if this_guess == word[i]:
                    self.guessed_list[i] = this_guess
            return True
        else:
            self.wrong_guesses.add(this_guess)
            return False


def word_list_maker(filename):
    """
    Creates a list of acceptable words.

    Accepts:
        filename -- string: path of file to read

    Returns:
        word_list -- list of words in file
    """

    fin = open(filename, 'r')
    word_list = [line.strip() for line in fin]
    return word_list


if __name__ == '__main__':
    filename = './words.txt'
    word_list = word_list_maker(filename)
    hangman = Hangman(word_list)
    hangman.play_game()
#     print(hangman)
#     for word in word_list:
#         print(word)
