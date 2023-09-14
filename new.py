# student name: Arshvir Singh
# student number: 62273818

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    print('\n') # To have correct spacing
    print(f'{board[0]} | {board[1]} | {board[2]}' + '    0 | 1 | 2')
    print('--+---+--'+'    --+---+--') 
    print(f'{board[3]} | {board[4]} | {board[5]}' + '    3 | 4 | 5')
    print('--+---+--' + '    --+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}' + '    6 | 7 | 8')
    print('\n') 


def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    while True:
        # Use try and except block so code doesn't stop with an error
        try:
            cell_num = int(input('Next move for X (state a valid cell num): '))
            if cell_num in range(0,9) and cell_num not in played:
                board[cell_num] = 'X'
                played.add(cell_num) # Adds chosen number to played set
                print(f'You chose cell {cell_num}')
                printBoard()
                break
            else:
                print('Must enter a valid cell number')
        except:
            print('Must be an integer')

def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    # let comp only choose between values that are avaliable
    comp_cell_num = [i for i in range(9) if board[i] == ' ']
    if comp_cell_num:
        move = random.choice(comp_cell_num) # Pick random avaliable number
        board[move] = 'O'
        played.add(move)
        print(f'Computer chose cell {comp_cell_num}')
        printBoard()

def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
    return ((board[0] == who and board[1] == who and board[2] == who) or # across the top
    (board[3] == who and board[4] == who and board[5] == who) or # across the middle
    (board[6] == who and board[7] == who and board[8] == who) or # across the bottom
    (board[1] == who and board[4] == who and board[7] == who) or # down the middle
    (board[0] == who and board[3] == who and board[6] == who) or # down the left side
    (board[2] == who and board[5] == who and board[8] == who) or # down the right side
    (board[2] == who and board[4] == who and board[6] == who) or # diagonal
    (board[0] == who and board[4] == who and board[8] == who)) # diagonal

def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    if hasWon(who):
        if who == 'X':
            printBoard()
            print("You won! Thanks for playing.")
            played.clear() #clear played set
            return True
        else:
            printBoard()
            print("You lost! Thanks for playing.")
            played.clear()
            return True
        
    elif ' ' not in board:
        printBoard()
        print("A draw! Thanks for playing.")
        played.clear() 
        return True

if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate