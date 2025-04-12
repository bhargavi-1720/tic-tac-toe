
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    # Check rows
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2]:
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8]:
        return board[0]
    if board[2] == board[4] == board[6]:
        return board[2]
    
    return None

def tic_tac_toe():
    board = [str(i) for i in range(1,10)]
    current_player = "X"
    winner = None
    moves = 0

    print("Welcome to Tic-Tac-Toe!")
    print("Enter a number (1-9) to make your move.\n")
    
    while not winner and moves < 9:
        print_board(board)
        try:
            move = int(input(f"\nPlayer {current_player}'s turn: ")) - 1
            
            if move < 0 or move > 8 or board[move] in ["X", "O"]:
                print("Invalid move! Try again.")
                continue
                
            board[move] = current_player
            moves += 1
            winner = check_winner(board)
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Please enter a valid number (1-9)!")

    print_board(board)
    
    if winner:
        print(f"\nPlayer {winner} wins!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
