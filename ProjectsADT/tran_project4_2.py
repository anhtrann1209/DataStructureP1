"""
Malicious Hangman (Part 2):
User input a letters and the words will not be choosen until the parition contain the letter.
Game will select the largest number of partition words group.
After re-assign the possible vocabulary list (surviving word) delay making words.

File Name: tran_project4_2.py
Author: Anh Tran
Date: 5/18/24
Course: COMP1353 - Data Structures and Algorithms I
Assignment: Project 4 - Malicious Hangman pt 1
Collaborators: Pluto and Andy Dang
"""

"""Example:
guesses letter: j
*****: 9 words
j****: 1 words
****h: 2 words
guesses letter: s
Force the game to choose letter that can survive. 
"""

from hash_set import HashSet
from LINKLIST import doublell
from random import choice

class PlayGame:
    def __init__(self):
        """
        Initializes value for PlayGame class
        """
        self.letter_guess = ""
        self.dictionary = {}
        self.set = set() 
        

    def check_letter(self, guess_letter: str) -> bool:
        """
        Check if the letter input is correct.
        parameters: guesses_letter
        returns: True if letter correct, else False
        """
        #check to see if letter in the guesses.
        if self.letter_guess in guess_letter:
            #find every letter by index.
            for i in range(len(guess_letter)):
                #if letter match up change dictionary at that letter to letter input
                if self.letter_guess == guess_letter[i]:
                    self.dictionary[i] = self.letter_guess 
            return True
        return False


    def check_word(self, guesses_letter: str):
        """
        Check if user wins if all letters match with chosen word
        parameters: guess letters
        returns: True if all matches, else False
        """
        # Check if the letter was re-entered.
        if self.letter_guess in self.set:
            print("Sorry you already guessed this letter")
            return None
        else:
            # If the letter has not yet been entered
            self.set.add(self.letter_guess)
            # Check if the letter is correct -> return True
            if self.check_letter(guesses_letter):
                print(f"Letter {self.letter_guess} is correct!")
                return True
            else:
                print(f"Letter {self.letter_guess} is incorrect")
                return False
        

    def load_file() -> dict:
        """
        Read file and seperate words by length of words, and turn word to lower case.
        Parameters: None
        Returns: dictionary with key as length, and all words with same length as value
        """
        with open("Dictionary.txt", "r") as a_file:
            word_dictionary = {}
            for line in a_file:
                # Convert all words to lower case
                word = line.lower().strip()
                # Let the length of the word be key() and values are the words with the same length.
                if len(word) not in word_dictionary:
                    word_dictionary[len(word)] = []
                word_dictionary[len(word)].append(word) 
        return word_dictionary

    def chosen_word(new_dict: dict, word_length: int) -> str:
        """
        Pick a word from user choosen length.
        parameters: dictionary from load_file, choosen word_length.
        returns: return the choosen word 
        """
        hangman_word = "" 
        # If the length, key exists in the new dictionary
        if word_length in new_dict: 
            #choose random word using choice with the value at the key of word length
            hangman_word = choice(new_dict[word_length]) 
            print(hangman_word) 
            return hangman_word
        else:
            # Length beyond the existing word
            print(f"Word length does not exist.")
            return None 

    def formatting(self, word: str) -> str:
        """
        Format printing with dash, and replace dash with correct letter
        parameters: word
        returns: string with correct place for letter input.
        """ 

        formatted_word = ""
        for i in range(len(word)):
            if i in self.dictionary and self.dictionary[i] is not None:
                # Add the letter to formatted_word string
                formatted_word += self.dictionary[i]
                # Print on the same line
                print(self.dictionary[i], end=" ")
            else:
                # If the letter is in an incorrect place, place a dash
                formatted_word += "-"
                print("-", end=" ")     
        return formatted_word

def hangman_game(correct_word: str, num_guess: int):
    """
    Create a new Hangman game.
    parameters: correct_word, chances
    returns: lose or win will print after chances run out.
    """
    # Start game contains all its function
    game = PlayGame()
    # Amount of incorrect answers
    incorrect_guesses = 0 
    guess_amount = 0

    while incorrect_guesses < num_guess: 
        user_letter = str(input("Guess a letter: ")) 
        guess_amount += 1 
        if len(user_letter) != 1:
            print("You cannot input more than one letter.")
        else:
            game.letter_guess = user_letter
            result = game.check_word(correct_word) 
            if result is False:
                incorrect_guesses += 1
            game_spawn = game.formatting(correct_word)
            print() 
            
            if game_spawn == correct_word: 
                print(f"\nYou won within {guess_amount} times.") 
                return
            print(f"Remaining number of guesses: {num_guess - incorrect_guesses}.")
    print(f"Game over. You ran out of guesses! The correct word was {correct_word}")


def main():
    print("Instructions on playing Hangman.\nChoose a word length and number of guesses.\nInput guessed letters, no repetition.\n")

    while True:
        new_dict = PlayGame.load_file() 
        while True: 
            try:
                # Test user input whether it was a number or not, else except value error and re-enter
                word_length = int(input("What is the word length: "))
                break
            except ValueError:
                print("Please enter a valid word length: ")

        # Choose a word given a chosen word function in PlayGame class
        chosen_word = PlayGame.chosen_word(new_dict, word_length) 
        while True:
            try:
                # Test user input, and only valid if user inputs a digit and proceed to exit the loop.
                chances = int(input("How many guesses would you like: ")) 
                # Number of chances must be greater than word length.
                if chances < word_length:
                    print("Please enter an amount of guesses greater than the chosen word length: ")
                else:
                    break

            except ValueError:
                print("Please enter a valid number of guesses.")

        # Passed in random chosen word, and the number of guesses user wanted.
        hangman_game(chosen_word, chances) 

        # After the game ends, player whether loss or win
        play = str(input("Would you like to play again? (yes/no): "))

        # Ask player if they want to play again
        if play.lower() != "yes" and play.lower() != "no":
            print("Please type 'yes' or 'no'")
            play = str(input("Would you like to play again? (yes/no): ")) 
        if play.lower() == 'no':
            break
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
