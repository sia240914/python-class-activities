# 1) Create a dictionary `theBoard` to represent the Tic-Tac-Toe board:
#    a) Keys are positions ('7' to '9' for top row, '4' to '6' for middle, '1' to '3' for bottom).
#    b) Values start as a blank space ' ' to show empty cells.the_board
# 2) Create an empty list `board_keys` to store all the board keys (positions).
the_board={'7':' ','8':' ','9':' ',
           '4':' ','5':' ','6':' ',
           '1':' ','2':' ','3':' ',}
board_keys=[ ]
for key in the_board:
    board_keys.append(key)
# 3) Use a loop to add every key from `theBoard` into `board_keys`.
#    (This helps reset the board later when restarting the game.)

# 4) Define a function `printBoard(board)` to display the current board:
#    a) Print the top row using keys '7', '8', '9'
#    b) Print a separator line "-+-+-"
#    c) Print the middle row using keys '4', '5', '6'
#    d) Print another separator line "-+-+-"
#    e) Print the bottom row using keys '1', '2', '3'
def printboard(board):
    print(board[' 7 ' ]+'|'+board[' 8 ' ]+'|'+board[' 9 ' ]+'|')
    print('-+-+-')
    print(board[' 4 ' ]+'|'+board[' 5 ' ]+'|'+board[' 6 ' ]+'|')
    print('-+-+-')
    print(board[' 1 ' ]+'|'+board[' 2 ' ]+'|'+board[' 3 ' ]+'|')
    print('-+-+-')


def game ():
    
    turn='X'
    count=0
    for i in range (10):
        printboard(the_board)
        print( "its your turn" +turn+ "move to which place")
        move=input()

        if(the_board[move] ==' '):
            the_board[move]=turn
            count=count+1
        else:
            print("this block is filled","move to which place")
 
    



# 5) Define the main function `game()` which controls the full gameplay.

# 6) Inside `game()`:
#    a) Set `turn = 'X'` to start with player X.
#    b) Set `count = 0` to track how many valid moves have been made.

# 7) Use a loop `for i in range(10)` to run the game turns:
#    a) Print the board using `printBoard(theBoard)`.
#    b) Ask the current player where they want to move.
#    c) Take the input move and store it in `move`.

# 8) Validate the move:
#    a) If `theBoard[move]` is empty (' '), place the current player's symbol there.
#    b) Increase `count` by 1 for a valid move.
#    c) Else, print a message that the place is already filled and continue to the next iteration.

# 9) After at least 5 moves (`if count >= 5`), start checking for a winner:
#    a) Check 3 horizontal win conditions (top, middle, bottom rows).
#    b) Check 3 vertical win conditions (left, middle, right columns).
#    c) Check 2 diagonal win conditions.
#    d) If any win condition is true:
#       i) Print the final board.
#       ii) Print "Game Over" and announce the winner (`turn`).
#       iii) Stop the game loop using `break`.

# 10) If `count == 9` and no one has won:
#     a) Print "Game Over" and declare it as a tie.

# 11) Switch turns after every valid move:
#     a) If current player is 'X', change `turn` to 'O'.
#     b) Otherwise, change `turn` back to 'X'.

# 12) After the round ends, ask the user if they want to play again:
#     a) Take input in `restart`.
#     b) If restart is "y" or "Y":
#        i) Reset every position in `theBoard` back to blank space using `board_keys`.
#        ii) Call `game()` again to restart.

# 13) Use `if __name__ == "__main__":` to start the game only when this file is run directly,
#     and then call `game()`.