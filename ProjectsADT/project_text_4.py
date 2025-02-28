import random
from hash_map import HashMap  # Your provided HashMap implementation
from hash_set import HashSet  # Assume a similar implementation for HashSet

def load_dictionary(file_path: str) -> HashMap:
    words_dictionary = HashMap()
    with open(file_path, "r") as file:
        for line in file:
            word = line.strip()
            if not word:
                continue
            word_length = len(word)
            if words_dictionary.get(word_length) is None:
                words_dictionary.put(word_length, [word])
            else:
                words_dictionary.get(word_length).append(word)
    return words_dictionary

def choose_word(length: int, words_dictionary: HashMap):
    word_list = words_dictionary.get(length)
    return random.choice(word_list) if word_list else None

def main():
    words_dictionary = load_dictionary("Dictionary.txt")
    
    word_length = int(input("What is the word length: "))
    chances = int(input("How many guesses would you like: "))
    
    correct_word = choose_word(word_length, words_dictionary)
    if not correct_word:
        print(f"No words of length {word_length} found in the dictionary.")
        return
    
    guessed_letters = HashSet()
    remaining_chances = chances
    word_guessed = ["_" for _ in range(word_length)]

    print("Let's start the game!")
    print(" ".join(word_guessed))

    while remaining_chances > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        
        if guessed_letters.contains(guessed_letters, guess):
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.add(guessed_letters, guess)
        
        if guess in correct_word:
            print(f"Good guess! '{guess}' is in the word.")
            for idx, letter in enumerate(correct_word):
                if letter == guess:
                    word_guessed[idx] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            remaining_chances -= 1
        
        print(" ".join(word_guessed))
        print(f"Remaining chances: {remaining_chances}")
        
        if "_" not in word_guessed:
            print("Congratulations! You guessed the word correctly.")
            return
    
    print(f"Game over! The correct word was '{correct_word}'.")

if __name__ == "__main__":
    main()
