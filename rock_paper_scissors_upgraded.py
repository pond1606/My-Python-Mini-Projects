"""Rock, paper, scissors upgraded version by Phan Huynh Thien Phuc
Using ASCII art makes the game much cooler! Link to the art:
https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
Please type only r, p, s or q (rock, paper, scissor and quit respectively)."""

import random

elements = {
'r':"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
'p':"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
's':"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}

while True:
    player_move = input("(r)ock, (p)aper or (s)cissor? (press q to quit)")
    if player_move == 'q':
        break
    computer_move = random.choice(['r', 'p', 's'])
    print("Computer chose: ")
    print(elements[computer_move])
    print("You chose: ")
    print(elements[player_move])

    # Determine the result
    if player_move == computer_move:
        print("Tie!")
    if player_move == 'r':
        if computer_move == 'p':
            print("You lose!")
        elif computer_move == 's':
            print("You win!")
    if player_move == 'p':
        if computer_move == 'r':
            print("You win!")
        elif computer_move == 's':
            print("You lose!")
    if player_move == 's':
        if computer_move == 'r':
            print("You lose!")
        elif computer_move == 'p':
            print("You win!")

print("Thanks for playing!")