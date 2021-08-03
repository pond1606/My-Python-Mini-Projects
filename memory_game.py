"""Memory Game by Phan Huynh Thien Phuc
You will see 9 cards on the screen. After 5 seconds (you can change this number on line 39),
they'll disappear and you'll have to guess the number of a given card. What a cool game
to train your memory! Remember to run this using the terminal so it can print nicely."""

import random, time

def print_cards(symbols_list):
    """Prints all 9 cards in a nice format."""
    print(f""" 
          1     2     3
         ___   ___   ___
        |   | |   | |   |
        |{symbols_list[0] * 3}| |{symbols_list[1] * 3}| |{symbols_list[2] * 3}|
        |___| |___| |___|

          4     5     6
         ___   ___   ___
        |   | |   | |   |
        |{symbols_list[3] * 3}| |{symbols_list[4] * 3}| |{symbols_list[5] * 3}|
        |___| |___| |___|

          7     8     9
         ___   ___   ___
        |   | |   | |   |
        |{symbols_list[6] * 3}| |{symbols_list[7] * 3}| |{symbols_list[8] * 3}|
        |___| |___| |___|
        """)

print("""You will see 9 cards on the screen. After 5 seconds,
they'll disappear and you'll have to guess the number of a given card.""")

while True:
    symbols = ['♀', 'Δ', '○', '□', '♪', '♫', '☼', '☺', '♂']  # You can change these symbols
    random.shuffle(symbols)  # Shuffle the list to make it random
    input("Press Enter when you're ready...")
    print("\n" * 30)  # Print 30 newlines to hide the last gameplay
    print_cards(symbols)
    time.sleep(5)  # Wait 5 secs
    answer = random.randint(1, 9)  # Ask a random card
    print("\n" * 30)  # Print 30 newlines to hide the cards
    while True:  # Ask for the player's guess
        guess = input(f"""Which number is this card? (1-9)
         ___ 
        |   |
        |{symbols[answer - 1] * 3}|
        |___|

""")
        # Make sure the player entered a number from 1 to 9
        if guess not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Please enter a number from 1 to 9.")
            continue
        guess = int(guess)
        break

    if guess == answer:
        print("That's correct!")
    else:
        print(f"You're wrong! It's card number {answer}.")

    print_cards(symbols)  # Print the cards again for the player to see

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower().startswith('n'):
        print("Thanks for playing!")
        break
