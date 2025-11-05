9import random

# --- Create Game Board ---
board = [" " for _ in range(9)]

def print_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

# --- Check for Winner ---
def check_winner(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

# --- Player Move ---
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please choose a number between 1 and 9.")
            elif board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        except ValueError:
            print("Enter a valid number (1-9).")

# --- Computer Move (Random AI) ---
def computer_move():
    print("Computer is thinking...")
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

# --- Check if Board is Full ---
def is_full():
    return " " not in board

# --- Main Game Loop ---
def main():
    print("Welcome to Tic-Tac-Toe AI 🤖 (You = X, Computer = O)")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner("X"):
            print("🎉 You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        computer_move()
        print_board()
        if check_winner("O"):
            print("💻 Computer wins!")
            break
        if is_full():
            print("It's a draw!")
            break

main()
