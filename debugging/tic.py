def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Value can only be numerical such as 0, 1 or 2! Try again.")
            continue

        if (row > 2 or row < 0):
            print("You can only choose 0, 1 or 2! Try again.")
            continue

        try:
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Value can only be numerical such as 0, 1 or 2! Try again.")
            continue
        
        if (col > 2 or col < 0):
            print("You can only choose 0, 1 or 2! Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            return

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            return

        player = "O" if player == "X" else "X"


tic_tac_toe()
