import random

def hangman():
    # List of words to choose from
    words = ['python', 'hangman', 'challenge', 'programming', 'code', 'developer']
    
    # Randomly choose a word from the list
    word_to_guess = random.choice(words)
    guessed_letters = set()
    correct_letters = set(word_to_guess)
    
    max_attempts = 6
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print(f"You have {attempts_left} incorrect guesses. Good luck!\n")

    # Game loop
    while attempts_left > 0 and correct_letters:
        # Display current word progress
        display_word = [letter if letter in guessed_letters else '_' for letter in word_to_guess]
        print('Word:', ' '.join(display_word))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts_left}")
        
        # Get user's guess
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            correct_letters.remove(guess)
            print("Good guess!\n")
        else:
            attempts_left -= 1
            print("Wrong guess!\n")

    # End of game
    if not correct_letters:
        print(f"Congratulations! You guessed the word '{word_to_guess}' correctly!")
    else:
        print(f"Game over! The word was '{word_to_guess}'.")

# Run the game
if __name__ == "__main__":
    hangman()
