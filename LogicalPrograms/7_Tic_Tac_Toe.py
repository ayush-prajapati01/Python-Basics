'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to Simulate Tic Tac Toe Game

'''


def print_board(board):
    """
    Description:
        Prints the current state of the Tic Tac Toe board.
    Parameter:
        board: Current state of the board
    Return:
        None
    """
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")
            

def make_move(board, position, current_player):
    """
    Description:
        Makes a move on the board if the position is valid.
    Parameters:
        board: The current state of the board
        position: The position where the player wants to move
        current_player: The player making the move 
    Return:
        bool: Move Successfull or not
    """
    if board[position-1] == ' ':
        board[position-1] = current_player
        return True
    return False


def check_winner(board):
    """
    Description:
        Checks if there's a winner or if the game is a draw.
    Parameter:
        board: state of board
    Return:
        str: 'X' or 'O' if there's a winner, 'Draw' if it's a draw, or None 
    """
    # Checking rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
        
    # Checking columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    
    # Checking diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    
    # Check for no empty spaces
    if ' ' not in board:
        return 'Draw'
    return None


def switch_player(current_player):
    """
    Description:
        Switches the current player.
    Return:
        str: The new current player ('X' or 'O')
    """
    return 'O' if current_player == 'X' else 'X'


def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print("Enter positions 1-9 to make your move:")
    print_board(board)

    while True:
        position = int(input(f"Player {current_player}, enter your move (1-9): "))
        
        if 1 <= position <= 9:
            if make_move(board, position, current_player):
                print_board(board)
                winner = check_winner(board)
                if winner:
                    if winner == 'Draw':
                        print("It's a draw!")
                    else:
                        print(f"Player {winner} wins!")
                    break
                current_player = switch_player(current_player)
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid position. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
