# Import the necessary modules
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Select a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize the game
end_of_game = False
lives = 6

# Display the game logo
print(logo)

# Display the solution (for testing purposes only)
print(f'Pssst, the solution is {chosen_word}.')

# Initialize the display
display = []
for _ in range(word_length):
    display += "_"

# Loop until the end of the game
while not end_of_game:
    # Ask the user to make a guess
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed the letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # Update the display with the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the word, decrement the lives
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display the current status of the word
    print(f"{' '.join(display)}")

    # If the word has been fully guessed, end the game and declare victory
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current status of the hangman
    print(stages[lives])
