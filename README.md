# hangman_game
 A simple hangman (word-guessing) game in Python, using a list of crossword words
 
 ## Word List
 The list of crossword words is taken from Allen Downey's code example repository associated with his book _Think Python_ (2nd Edition).  https://github.com/AllenDowney/ThinkPython2/blob/master/code/words.txt.
 
 ## Game Play
 1. A word is chosen at random from the list in words.txt (a list of crossword words).
 2. The user is provided the length of the word, and is asked how many incorrect guesses they should be allowed.
 3. The user continues to make guesses.  After each guess, the known information about the word is updated, the user is provided an updated list of prior guesses, and the user is given updated information about how many guesses they have left.
 4. User wins if they guess all letters in the word before their number of incorrect guesses.  User loses otherwise.
 
 ## To Do
 1) Provide screen updates
 2) Create stick-figure-style hangman graphics (would likely need to come with limiting user input as to how many incorrect guesses are allowed).
