import random
board = [" " for _ in range(9)]
current_player = "X"  # Player is X, Computer is O
def print_board(): 
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    
def random_move(board):
    empty_spaces = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty_spaces) if empty_spaces else None
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
#start the game
for turn in range (9): 
    print_board()

    if current_player == "X":
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue 
        board[move] = current_player

    if check_winner(board, current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break
        # Switch player only if no winner
    current_player = "O" if current_player == "X" else "X"  
    if current_player == "O":
        move = random_move(board)
        print(f"Computer chose position {move + 1}")
        board[move] = current_player

        if check_winner(board, current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"