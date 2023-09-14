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
    
    # Print different statements depending on whos turn it is
    if turn == 'Player': 
        player_mark = 'X'
        computer_mark = 'O'
        print(f"You play {player_mark} (first move) and computer plays {computer_mark}.") # Add different print statements for each scenario
        print("Computer plays strategically, not randomly.")
    else:
        player_mark = 'O'
        computer_mark = 'X'
        print(f"Computer plays {computer_mark} (first move) and you play {player_mark}")
        print("Computer plays strategically, not randomly.")
    printBoard()
    return (player_mark, computer_mark) # So player and computer mark can be updated outside the function
    
    

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    print('\n') # To have correct spacing
    print(f'{board[0]} | {board[1]} | {board[2]}' + '    0 | 1 | 2')
    print('--+---+--'+'    --+---+--') 
    print(f'{board[3]} | {board[4]} | {board[5]}' + '    3 | 4 | 5')
    print('--+---+--' + '    --+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}' + '    6 | 7 | 8')
    print('\n') 


def playerNextMove(player_mark) -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    while True:
        # Use try and except block so code doesn't stop with an error
        try:
            cell_num = int(input('Next move for X (state a valid cell num): '))
            if cell_num in range(0,9) and cell_num not in played:
                board[cell_num] = player_mark # Update to new mark instead of just 'X'
                played.add(cell_num) # Adds chosen number to played set
                print(f'You chose cell {cell_num}')
                printBoard()
                break
            else:
                print('Must enter a valid cell number')
        except:
            print('Must be an integer')

def computerNextMove(computer_mark) -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """

    best_score = -10 # Any random low score
    best_move = None

    # Check every combination
    for i in range(9):
        if i not in played:
            # Computer will play all scenarios until it finds best move
            board[i] = computer_mark
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    
    # Add best move
    board[best_move] = computer_mark 
    played.add(best_move)
    print(f"Computer chose cell {best_move}")
    printBoard()

# Create minimax algorithm for best computer decisions
def minimax(board, depth, maximizing): 
    # Check for wins/losses to exit recursive state
    if hasWon(player_mark):
        return -1 # Low point if player wins
    elif hasWon(computer_mark):
        return 1 # High point if computer wins
    if ' ' not in board:
        return 0
    
    # Try to get best move for computer
    if maximizing:
        best_score = -float('inf') # Can set any low score

        # Will try to play every combination and get best score using minimax algorithm
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer_mark
                score = minimax(board, 0, False) # Depth doesn't matter because limited number of moves
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        # Minimizing for player's turns
        best_score = float('inf') # Any high score
        for i in range(9):
            if board[i] == ' ':
                board[i] = player_mark
                score = minimax(board, 0, True)
                board[i] = ' '
                best_score = min(score, best_score) #Trying to minimize therefore min
        return best_score
                    


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
        if who == player_mark and turn == 'Player': # New winning conditions
            printBoard()
            print("You won! Thanks for playing.")
            played.clear() # Clear played set
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
    turn = random.choice(['Player', 'Computer'])  # Use random choice to pick random first turn
    
    player_mark, computer_mark = init()            # Assign player_mark and computer_mark using init
    while True:
        if turn == 'Player':
            playerNextMove(player_mark)            # User starts first
            if(terminate(player_mark)): break      # if {player_mark} won or a draw, print message and terminate
            turn = 'Computer' 
        else:
            computerNextMove(computer_mark)          # Computer plays first move         
            if(terminate(computer_mark)): break      # if {computer_mark} won or a draw, print message and terminate
            turn = 'Player'