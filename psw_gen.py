import string
import random

def psw_gen(length, digits, uppercase, lowercase, symbols):
    password = ""
    required_characters = []
    character_count = {}

    if digits:
        digit = random.choice(string.digits)
        required_characters.append(digit)
        character_count[digit] = character_count.get(digit, 0) + 1
        password += string.digits

    if uppercase:
        upper = random.choice(string.ascii_uppercase)
        required_characters.append(upper)
        character_count[upper] = character_count.get(upper, 0) + 1
        password += string.ascii_uppercase

    if lowercase:
        lower = random.choice(string.ascii_lowercase)
        required_characters.append(lower)
        character_count[lower] = character_count.get(lower, 0) + 1
        password += string.ascii_lowercase

    if symbols:
        symbol = random.choice(string.punctuation)
        required_characters.append(symbol)
        character_count[symbol] = character_count.get(symbol, 0) + 1
        password += string.punctuation

    if not required_characters:
        return "No characters selected to generate a password."

    # Fill the rest of the password length with random characters
    while len(required_characters) < length:
        char = random.choice(password)
        required_characters.append(char)
        character_count[char] = character_count.get(char, 0) + 1

    # Shuffle the password
    random.shuffle(required_characters)

    # Convert the list to a string
    final = ''.join(required_characters)

    # Print the character count for each character
    print("Character counts:", character_count)

    return final


# User input
length = int(input("Please enter the number of characters: "))
digits = input("Do you want your password to contain numbers? (Y/N): ").upper() == "Y"
symbols = input("Do you want your password to contain symbols? (Y/N): ").upper() == "Y"
lowercase = input("Do you want your password to include lowercase letters? (Y/N): ").upper() == "Y"
uppercase = input("Do you want your password to include uppercase letters? (Y/N): ").upper() == "Y"

# Generate password
final = psw_gen(length, digits, lowercase, uppercase, symbols)

# Print the result
if final:
    print("Here's your password:", final)
