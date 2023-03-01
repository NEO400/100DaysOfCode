# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# Use the choice() function from random module to select a random word from the Word_list
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Ask user to enter a letter, convert it to lowercase to standardize comparison
guess = input("Guess a Letter:").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:  # If the guessed letter matches the current letter in the loop
        print("Right")
    else:
        print("Wrong")
