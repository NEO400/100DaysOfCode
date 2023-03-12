import art


def caesar(cipher_text, shift_amount, cipher_direction):
    # If the shift amount is higher than the number of letters,
    # e.g. with 26 letters, the result of a shift by 27 is the same as a shift by 1
    # If decoding, we shift in the opposite direction
    if cipher_direction == "decode":
        shift_amount = len(alphabet) - shift_amount

    text_out = ""
    for char in cipher_text:
        # If the character is a letter
        if char in alphabet:
            index_in = alphabet.index(char)
            index_out = index_in + shift_amount
            # If the new index would end up beyond the list, roll over to the beginning
            if index_out > len(alphabet) - 1:
                index_out -= len(alphabet)
            text_out += alphabet[index_out]
        else:
            # If the character is not a letter, just copy it
            text_out += char
    return text_out


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)

# Repeat unless the user enters "no"

while True:
    # Get the inputs, checking for validity when needed
    print("Type \"encode\" to encrypt, type \"decode\" to decrypt:")
    # Using a boolean (e.g. reverse = True) instead would be better, but since the assignment wants a string...
    direction = ""
    while True:
        direction = input("> ").lower()
        if direction == "encode" or direction == "decode":
            break
        else:
            print("Invalid choice. Please enter \"encode\" or \"decode\".")

    print("Type your message:")
    text = input("> ").lower()

    print("Type the shift number:")
    shift = 0
    while True:
        shift_str = input("> ")
        if shift_str.isdigit():
            shift = int(shift_str)
            # Reject 0, while it is technically a valid choice, it is not a very good one
            # Also reject any other number that would result in a shift by 0 characters (i.e. multiples of 26)
            if shift % len(alphabet) == 0:
                print(
                    f"Invalid choice. Shifting by {shift} would result in an identical message.")
            else:
                # Keep the shift value as it was entered, will deal with it later
                break
        else:
            print("Invalid choice. Please enter a positive integer.")

    # Already made sure that direction can either be "encode" or "decode", nothing else
    result = caesar(cipher_text=text, shift_amount=shift,
                    cipher_direction=direction)

    # Print the result, including the original shift value that the user entered
    print(
        f"The message \"{text}\" {direction}d using a shift of {shift} is \"{result}\".")

    # Condition to break out of the infinite loop
    print("Type \"yes\" if you want to go again. Otherwise type \"no\".")
    choice = input("> ").lower

    # Condition to break out of the infinite loop
    print("Type \"yes\" if you want to go again. Otherwise type \"no\".")
    choice = input("> ").lower()
    # Skip checking the input, just keep going until "no" is entered
    if choice == "no":
        break
print("Goodbye.")
