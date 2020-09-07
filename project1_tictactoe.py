import random

# Help from https://inventwithpython.com/chapter10.html
# https://www.simplifiedpython.net/python-tic-tac-toe-using-artificial-intelligence/
# https://courses.ischool.berkeley.edu/i90/f11/resources/chapter06/tic-tac-toe.py


# Game instructions
print("""Welcome to Tic Tac Toe!
Make your move according to this playing board.
Goal of the game is to get 3 of the same value in
a row, column, or diagonal.

            7 | 8 | 9
            ---------
            4 | 5 | 6
            ---------
            1 | 2 | 3  

May the odds be ever in your favor!
-----------------------------------------------
""")


def game_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def winning_combo(space, letter):
    # Winning combo sets
    return ((space[7] == letter and space[8] == letter and space[9] == letter) or
            (space[4] == letter and space[5] == letter and space[6] == letter) or
            (space[1] == letter and space[2] == letter and space[3] == letter) or
            (space[7] == letter and space[4] == letter and space[1] == letter) or
            (space[8] == letter and space[5] == letter and space[2] == letter) or
            (space[9] == letter and space[6] == letter and space[3] == letter) or
            (space[7] == letter and space[5] == letter and space[3] == letter) or
            (space[9] == letter and space[5] == letter and space[1] == letter))


def firstPlayer():
    # Random guessing game with human player to see if he/she gets to go first.
    number = random.randint(1, 3)
    guess = int(input("Try to beat me. Guess a number between 1 and 3: "))
    if guess != number:
        print(
            f"Too bad! Correct number was {number}. I will go first. ")
        computer = "X"
        human = "O"
    else:
        print("Darn. You guessed it! Fine...you will go first. ")
        human = "X"
        computer = "O"
    return computer, human


def space_available(board, move):
    # check if space if available.
    return board[move] == ' '


def place_move(board, letter, move):
    # Place player letter on the board.
    board[move] = letter


def full_board(board):
    # Return True if board is full else return False.
    for i in range(1, 10):
        if space_available(board, i):
            return False
    return True


def human_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_available(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

# Duplication board for the computer to evaluate and execute its moves.


def dup_board(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def computer_move(board):

    for i in range(1, 10):
        # Find winning move and move there.
        board_copy = dup_board(board)
        if space_available(board_copy, i):
            place_move(board_copy, computer_letter, i)
            if winning_combo(board_copy, computer_letter):
                return i

    for i in range(1, 10):
        # If human playing is going to have a winning move then try to block.
        board_copy = dup_board(board)
        if space_available(board_copy, i):
            place_move(board_copy, human_letter, i)
            if winning_combo(board_copy, human_letter):
                return i

    while True:
        # if the move is blank, go ahead and return, otherwise try again
        move = random.randint(1, 9)
        if board[move] == " ":
            return move
            break


while True:
    reset_board = [" "] * 10
    computer_letter, human_letter = firstPlayer()
    turn = "X"
    game_is_playing = True

    while game_is_playing:
        # Human turn. move and place human letter.
        if turn == human_letter:
            game_board(reset_board)
            move = human_move(reset_board)
            place_move(reset_board, human_letter, move)

            if winning_combo(reset_board, human_letter):
                # if winning then print
                game_board(reset_board)
                print("You won.")
                game_is_playing = False
            else:
                if full_board(reset_board):
                    game_board(reset_board)
                    print("Tie. ")
                    break
                else:
                    turn = computer_letter
        else:
            # Computer turn.
            move = computer_move(reset_board)
            place_move(reset_board, computer_letter, move)

            if winning_combo(reset_board, computer_letter):
                game_board(reset_board)
                print("Computer won.")
                game_is_playing = False
            else:
                if full_board(reset_board):
                    game_board(reset_board)
                    print("It's a tie")
                    break
                else:
                    turn = human_letter

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
