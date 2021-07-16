"""Bagels Remake by Phan Huynh Thien Phuc
In Bagels, you have to guess a secret three-digit number.
The game offers hints in response to your guess:
"Pico": One digit is correct but in the wrong position
"Fermi": One digit is correct and in the right position
"Bagels": No digit is correct

This remake version doesn't tell you "Pico", "Fermi", "Bagels",
it will tell you exactly what happened. For example:
Correct digit(s) but in wrong position: 2
Correct digit(s) and in right position: 1

That would be straight to the point, right?"""

import random

# Generate a random three-digit number
max_guesses = 10  # Change this number to increase/decrease difficulty
secret_number = random.randint(100, 999)
print(f"I'm thinking of a three-digit number. You have {max_guesses} guesses to get it.")

while max_guesses != 0:
    guess = ''
    right_position = 0
    wrong_position = 0
    print(f"Guess #{11 - max_guesses}")
    
    # Make sure the player guessed a three-digit number
    while True:
        guess = input("Guess a three-digit number: ")
        try:
            guess = int(guess)
            if len(str(guess)) == 3:
                break
            else:
                continue
        except ValueError:
            pass
        
    max_guesses -= 1
    
    # Check for correct digit in right/wrong position
    for i in range(3):
        if str(guess)[i] == str(secret_number)[i]:
            right_position += 1
        if str(guess)[i] in str(secret_number) and str(guess)[i] != str(secret_number)[i]:
            wrong_position += 1

    # Give hints
    if right_position == 3:
        break
    else:
        print(f"Correct digit(s) but in wrong position: {wrong_position}\n"
              f"Correct digit(s) and in right position: {right_position}")

# Two cases after breaking the loop
if guess == secret_number:
    print("You win!")
else:
    print(f"Out of guesses! You lose! The number is {secret_number}.")
