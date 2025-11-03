import math
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(b, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False

def is_draw(b):
    return " " not in b

def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number from 1-9.")

def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("You win! Congratulations!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("AI wins! Better luck next time!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
