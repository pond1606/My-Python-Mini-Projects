"""Tic Tac Toe upgraded version by Phan Huynh Thien Phuc
This tic tac toe board is 40x15! Online tutorials only make a 3x3 board. Come on, who plays
tic tac toe on a 3x3 board? This program also marks the latest move red so it's easy to see.
The AI in this game is pretty good but you can beat it easily if you know how to play tic tac toe."""

import random, colorama

def create_new_board():
    """Creates a blank new board."""
    board = []
    for x in range(40):
        board.append([])
        for y in range(15):
            board[x].append(' ')
    return board

def print_board(board):
    """Prints the given board in a nice format."""
    tens_digits_line = '     '  # Initial space
    for i in range(1, 4):
        tens_digits_line += (' ' * 19) + str(i)

    # Print numbers for the x axis (top)
    print(tens_digits_line)
    print('    ' + ('0 1 2 3 4 5 6 7 8 9 ' * 4))

    # Print 15 rows
    for row in range(15):
        # Single-digit numbers need extra space
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''

        board_row = ''
        for col in range(40):
            board_row += board[col][row] + '|'
        print(f"{extra_space}{row} |{board_row} {row}")

    # Print numbers for the x axis (bottom)
    print('    ' + ('0 1 2 3 4 5 6 7 8 9 ' * 4))
    print(tens_digits_line)

def let_player_choose_X_or_O():
    """Returns a list with player's letter as the first item, computer's letter as the second."""
    letter = ''
    while letter != 'X' and letter != 'O':
        letter = input("Do you want to be X or O? ").upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():
    """Returns who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def clear_color(board):
    """Returns a new board with no color."""
    no_color_board = []
    for x in range(40):
        no_color_board.append([])
        for y in range(15):
            if board[x][y] == f"{colorama.Fore.RED}X{colorama.Fore.RESET}":
                no_color_board[x].append('X')
            elif board[x][y] == f"{colorama.Fore.RED}O{colorama.Fore.RESET}":
                no_color_board[x].append('O')
            else:
                no_color_board[x].append(board[x][y])
    return no_color_board

def make_move(board, letter, x, y):
    board[x][y] = f"{colorama.Fore.RED}{letter}{colorama.Fore.RESET}"

def check_2_matches(board, letter):
    """Checks for this pattern "OO" and returns [x, y]. If there are no such patterns, returns None."""
    for x_start in range(40):
        for y_start in range(15):
            if board[x_start][y_start] == letter:  # Don't check empty tiles
                for x_offset, y_offset in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    x, y = x_start, y_start
                    x += x_offset
                    y += y_offset
                    if x in range(40) and y in range(15) and board[x][y] == letter:  # 2 matches
                        x += x_offset
                        y += y_offset
                        if x in range(40) and y in range(15) and is_empty(board, x, y):
                            # Make sure it's on board and empty
                            return [x, y]
                        else:
                            # Out of bounds/not empty, go for the opposite side
                            for i in range(3):  # Go back 3 times
                                x -= x_offset
                                y -= y_offset
                            if x in range(40) and y in range(15) and is_empty(board, x, y):
                                # Make sure it's on board and empty
                                return [x, y]

def check_3_matches_2_empty_sides(board, letter):
    """Checks for this pattern " OOO " and returns [x, y]. If there are no such patterns, returns None."""
    for x_start in range(40):
        for y_start in range(15):
            if board[x_start][y_start] == letter:  # Don't check empty tiles
                for x_offset, y_offset in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    x, y = x_start, y_start
                    x += x_offset
                    y += y_offset
                    if x in range(40) and y in range(15) and board[x][y] == letter:  # 2 matches
                        x += x_offset
                        y += y_offset
                        if x in range(40) and y in range(15) and board[x][y] == letter:  # 3 matches
                            x += x_offset
                            y += y_offset
                            if x in range(40) and y in range(15) and is_empty(board, x, y):
                                # 1 empty side
                                for i in range(4):  # Go back 4 times
                                    x -= x_offset
                                    y -= y_offset
                                if x in range(40) and y in range(15) and is_empty(board, x, y):
                                    # 2 empty sides, returns 1 side
                                    return [x, y]

def check_3_matches_empty_between(board, letter):
    """Checks for this pattern "OO O" and returns [x, y]. If there are no such patterns, returns None. """
    for x_start in range(40):
        for y_start in range(15):
            if board[x_start][y_start] == letter:  # Don't check empty tiles
                for x_offset, y_offset in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    x, y = x_start, y_start
                    x += x_offset
                    y += y_offset
                    if x in range(40) and y in range(15) and board[x][y] == letter:  # 2 matches
                        x += x_offset
                        y += y_offset
                        if x in range(40) and y in range(15) and is_empty(board, x, y):  # Empty tile
                            empty_x, empty_y = x, y
                            x += x_offset
                            y += y_offset
                            if x in range(40) and y in range(15) and board[x][y] == letter:  # 3 matches
                                return [empty_x, empty_y]

def is_winner(board, letter):
    """Returns True if there's a winner, otherwise returns False."""
    for x_start in range(40):
        for y_start in range(15):
            if board[x_start][y_start] == letter:  # Don't check empty tiles
                for x_offset, y_offset in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    x, y = x_start, y_start
                    x += x_offset
                    y += y_offset
                    if x in range(40) and y in range(15) and board[x][y] == letter:  # 2 matches
                        x += x_offset
                        y += y_offset
                        if x in range(40) and y in range(15) and board[x][y] == letter:  # 3 matches
                            x += x_offset
                            y += y_offset
                            if x in range(40) and y in range(15) and board[x][y] == letter:  # 4 matches
                                x += x_offset
                                y += y_offset
                                if x in range(40) and y in range(15) and board[x][y] == letter:  # 5 matches
                                    return True
    return False

def is_full(board):
    """Returns True if the board is full, otherwise returns False."""
    for col in range(40):
        for row in range(15):
            if board[col][row] == ' ':
                return False
    return True

def is_empty(board, x, y):
    """Returns True if that tile is empty."""
    return board[x][y] == ' '

def get_player_move():
    """Ask the player for their move. Returns [x, y].
    Lots of input validation for the sake of the player."""
    while True:
        move = input("Enter a tile (0-39 0-14): ")
        if len(move) == 5 and move[2] == ' ':  # e.g. 34 12
            try:
                x = int(move[:2])
                y = int(move[3:])
                if is_empty(board, x, y):
                    return [x, y]
                else:
                    print("That's not an empty tile. Choose again.")
                    continue
            except ValueError:
                print("Please enter the x coordinate, then the y coordinate (e.g. 34 2).")
                continue
        if len(move) == 4 and move[2] == ' ':  # e.g. 23 2
            try:
                x = int(move[:2])
                y = int(move[-1])
                if is_empty(board, x, y):
                    return [x, y]
                else:
                    print("That's not an empty tile. Choose again.")
                    continue
            except ValueError:
                print("Please enter the x coordinate, then the y coordinate (e.g. 34 2).")
                continue
        if len(move) == 4 and move[1] == ' ':  # e.g. 2 12
            try:
                x = int(move[0])
                y = int(move[2:])
                if is_empty(board, x, y):
                    return [x, y]
                else:
                    print("That's not an empty tile. Choose again.")
                    continue
            except ValueError:
                print("Please enter the x coordinate, then the y coordinate (e.g. 34 2).")
                continue
        if len(move) == 3 and move[1] == ' ':  # e.g. 1 2
            try:
                x = int(move[0])
                y = int(move[2])
                if is_empty(board, x, y):
                    return [x, y]
                else:
                    print("That's not an empty tile. Choose again.")
                    continue
            except ValueError:
                print("Please enter the x coordinate, then the y coordinate (e.g. 34 2).")
                continue
        print("Please enter the x coordinate, then the y coordinate (e.g. 34 2).")

def get_computer_move(no_color_board, computer_letter, player_letter):
    """Returns [x, y] as the next computer's move."""
    # Make the winning move
    for x in range(40):
        for y in range(15):
            if is_empty(no_color_board, x, y):
                make_move(no_color_board, computer_letter, x, y)
                if is_winner(no_color_board, computer_letter):
                    return [x, y]
                else:
                    no_color_board[x][y] = ' '

    # Block the player's winning move
    for x in range(40):
        for y in range(15):
            if is_empty(no_color_board, x, y):
                make_move(no_color_board, player_letter, x, y)
                if is_winner(no_color_board, player_letter):
                    return [x, y]
                else:
                    no_color_board[x][y] = ' '

    # Block if the player has 3 matches with 2 empty sides
    if check_3_matches_2_empty_sides(no_color_board, player_letter):
        return check_3_matches_2_empty_sides(no_color_board, player_letter)

    # Block if the player has 3 matches with an empty tile between
    if check_3_matches_empty_between(no_color_board, player_letter):
        return check_3_matches_empty_between(no_color_board, player_letter)

    # If the computer has 3 matches, make it 4
    if check_3_matches_2_empty_sides(no_color_board, computer_letter):
        return check_3_matches_2_empty_sides(no_color_board, computer_letter)

    # If the computer has 2 matches, make it 3
    if check_2_matches(no_color_board, computer_letter):
        return check_2_matches(no_color_board, computer_letter)

    # Make a random move near the player
    for x_start in range(40):
        for y_start in range(15):
            if no_color_board[x_start][y_start] == player_letter:
                for x_offset, y_offset in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                    x, y = x_start, y_start
                    x += x_offset
                    y += y_offset
                    if x in range(40) and y in range(15) and is_empty(no_color_board, x, y):
                        # Make sure it's on board and empty
                        return [x, y]

    # If the computer goes first, just make a random move
    return [random.randint(0, 40), random.randint(0, 14)]

# Start the game
while True:
    board = create_new_board()
    print_board(board)
    player_letter, computer_letter = let_player_choose_X_or_O()
    turn = who_goes_first()
    print(f"The {turn} will go first.")
    while True:  # Playing loop
        if turn == 'player':  # Player's turn
            no_color_board = clear_color(board)
            x, y = get_player_move()
            make_move(no_color_board, player_letter, x, y)
            make_move(board, player_letter, x, y)
            print_board(no_color_board)
            if is_winner(clear_color(board), player_letter):
                print_board(no_color_board)
                print("Congratulations! You won!")
                break
            elif is_full(no_color_board):
                print_board(no_color_board)
                print("No more possible moves! It's a tie!")
                break
            else:
                turn = 'computer'
        else:  # Computer's turn
            no_color_board = clear_color(board)
            x, y = get_computer_move(no_color_board, computer_letter, player_letter)
            input("Press Enter to see the computer's move...")
            make_move(no_color_board, computer_letter, x, y)
            make_move(board, computer_letter, x, y)
            print_board(no_color_board)
            if is_winner(clear_color(board), computer_letter):
                print_board(no_color_board)
                print("You lose!!!!")
                break
            elif is_full(no_color_board):
                print_board(no_color_board)
                print("No more possible moves! It's a tie!")
                break
            else:
                turn = 'player'
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower().startswith('n'):
        print("Thanks for playing!")
        break