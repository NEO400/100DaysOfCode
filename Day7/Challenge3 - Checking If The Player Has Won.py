# Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Use a while loop to let the user guess again.
while True:
    guess = input("Guess a letter: ").lower()

    # Check that the guess is a single letter.
    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    # Check that the guess hasn't been made before.
    if guess in display:
        print("You've already guessed that letter.")
        continue

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    # Check if the game has ended
    if "_" not in display:
        print("Congratulations, you've won!")
        break
