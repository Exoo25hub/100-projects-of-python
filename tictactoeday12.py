import random

# Initialize board
board = [" " for _ in range(9)]

# Function to display the board
def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")

# Function to check for a winner
def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full (draw)
def is_draw():
    return " " not in board

# Minimax algorithm for the hardest bot
def minimax(is_maximizing):
    scores = {"X": -1, "O": 1, "draw": 0}
    
    # Check if the game is over
    if check_winner("O"):
        return scores["O"]
    if check_winner("X"):
        return scores["X"]
    if is_draw():
        return scores["draw"]

    if is_maximizing:  # Bot's turn (maximize score)
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  # Player's turn (minimize score)
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function for best bot move using Minimax
def bot_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "  # Undo move

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

# Main game loop
def tic_tac_toe():
    current_player = "X"  # Player is X, Bot is O

    while True:
        print_board()
        
        if current_player == "X":
            try:
                move = int(input("Your turn (1-9): ")) - 1
                if board[move] != " " or move not in range(9):
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Invalid input! Enter a number from 1-9.")
                continue
        else:
            print("Bot is thinking...")
            move = bot_move()

        board[move] = current_player  # Place move

        if check_winner(current_player):  # Check win condition
            print_board()
            print(f"Player {current_player} wins! 🎉" if current_player == "X" else "Bot wins! 🤖")
            break
        
        if is_draw():  # Check draw condition
            print_board()
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
