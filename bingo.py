"""Bingo by Phan Huynh Thien Phuc
You and the computer will have a 5x5 card with numbers on it. Each turn, a random number
will be drawn. If you have it on your card, mark it X. You will win if you have 5 X
in a column, row or diagonal line. You lose if the computer has it first. The tile
in the middle of the card is always X. You don't have to do anything, just press Enter
and wait for your luck. Bingo has lots of variations but we'll keep it simple."""

import random

def create_board():
    """Returns a brand new bingo card."""
    board = []
    list_of_num = []
    for i in range(5):
        board.append([])
        for j in range(5):
            if i == 0:
                start_num = 1
                end_num = 15
            elif i == 1:
                start_num = 16
                end_num = 30
            elif i == 2:
                start_num = 31
                end_num = 45
            elif i == 3:
                start_num = 46
                end_num = 60
            elif i == 4:
                start_num = 61
                end_num = 75
            new_num = random.randint(start_num, end_num)
            while new_num in list_of_num:
                new_num = random.randint(start_num, end_num)
            list_of_num.append(new_num)
            # Make all tiles 3-letter long
            new_num = str(new_num)
            if len(new_num) == 1:
                board[i].append(' ' + new_num + ' ')
            elif len(new_num) == 2:
                board[i].append(' ' + new_num)
    board[2][2] = ' X '  # Free space in the middle of the board
    return board

def print_board(board):
    """Prints the card in a nice format."""
    print(" B   I   N   G   O")
    for i in range(5):
        for j in range(5):
            if j == 4:
                print(board[j][i])
            else:
                print(f"{board[j][i]}|", end='')

def is_winner(board):
    """Returns True if the given card has 5 X in a row, column or diagonal line."""
    # Vertical
    for i in board:
        number_of_X = i.count(' X ')
        if number_of_X == 5:
            return True
    # Horizontal
    return ((board[0][0] == ' X ' and board[1][0] == ' X ' and board[2][0] == ' X ' and board[3][0] == ' X ' and board[4][0] == ' X ') or
    (board[0][1] == ' X ' and board[1][1] == ' X ' and board[2][1] == ' X ' and board[3][1] == ' X ' and board[4][1] == ' X ') or
    (board[0][2] == ' X ' and board[1][2] == ' X ' and board[2][2] == ' X ' and board[3][2] == ' X ' and board[4][2] == ' X ') or
    (board[0][3] == ' X ' and board[1][3] == ' X ' and board[2][3] == ' X ' and board[3][3] == ' X ' and board[4][3] == ' X ') or
    (board[0][4] == ' X ' and board[1][4] == ' X ' and board[2][4] == ' X ' and board[3][4] == ' X ' and board[4][4] == ' X ') or
    # Diagonal
    (board[0][0] == ' X ' and board[1][1] == ' X ' and board[2][2] == ' X ' and board[3][3] == ' X ' and board[4][4] == ' X ') or
    (board[4][0] == ' X ' and board[3][1] == ' X ' and board[2][2] == ' X ' and board[1][3] == ' X ' and board[0][4] == ' X '))

def check_on_card(number, board):
    """Checks if a number is on the card. If so, marks it X."""
    for i in range(5):
        for j in range(5):
            if board[i][j].strip() == str(number):
                board[i][j] = ' X '
    return board

while True:
    # Initialize the game
    all_numbers = [i for i in range(1, 76)]
    computer_card = create_board()
    player_card = create_board()
    input("Press Enter to start the game now...")
    while True:
        # Print the cards
        print("Computer's card:")
        print_board(computer_card)
        print("Your card:")
        print_board(player_card)

        # Check if there's a winner
        if is_winner(computer_card) and not is_winner(player_card):
            print("You lose!")
            break
        elif is_winner(player_card) and not is_winner(computer_card):
            print("You win!")
            break
        elif is_winner(player_card) and is_winner(computer_card):
            print("It's a tie! How amazing is that!")
            break

        # Draw a number
        input("Press Enter to draw a random number...")
        new_num = random.choice(all_numbers)
        all_numbers.remove(new_num)
        input(f"It is {new_num}!")

        # Check if that number is on cards
        computer_card = check_on_card(new_num, computer_card)
        player_card = check_on_card(new_num, player_card)

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower().startswith('n'):
        print("Thanks for playing!")
        break