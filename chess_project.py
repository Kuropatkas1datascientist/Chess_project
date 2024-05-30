# 1) Define main function
# 2) Define board state inside a main function
# 3) Create a board
# 4) Ask user to input the white piece on the board (pawn or rook)
# 5) Ask user to input black pieces (up to 16, the same number as there are pieces in total in the game)
# 6) At least one balck piece should be added, and if user does not want to add another black piece, user should input "done"
# 7) After pieces have been added, the confirmation or error message should be printed out
# 8) After figures have been added to the board, the program should print which black pieces could be taken by the white piece


def main(): # Defining main function
    board = get_new_board() # Function which defines the state of the board
    create_board(board) # Function which creates the actual chess board

    x, y, white_piece = ask_user_for_white_piece(board) # Defining a function, which asks user to iput a white figure (pawn or rook)
    board[x][y] = white_piece # Placing white piece on the board
    create_board(board) # Calling 'create_board' to update the status of the board after the white figure has been placed

    black_pieces = ask_user_for_black_pieces(board) # Defining a function, which asks user to input black pieces (up to 16)
    for x, y, black_piece in black_pieces: # Placing black pieces on the board
        board[x][y] = black_piece
    create_board(board) # Calling 'create_board' again to update the status of the board after black pieces have been placed

    possible_captures = check_captures(board, x, y, white_piece) # After pieces have been placed, the program should check which black pieces could be taken by thewhite piece
    print_possible_captures(possible_captures) # Printing possible captures


def get_new_board():
    board = [0,0,0,0,0,0,0,0] # Creating a list named board to represent the chess board element, which will later be replaced with a list representing a row on the chessboard.
    for i in range(len(board)): # The loop iterates over the list, which has 8 elements, each element represents a string with two spaces. The string represents an empty square on a chess board.
        board[i] = ["__"] * 8
    return board

def create_board(board):      # Creating a 'create_board' function, which will print an 8x8 grid, representing a chessboard.
    for i, row in enumerate(board):  # By enumerating over each row in a function, I add the index to each row.
        print(8-i, end = ": ")       # As indexing starts with 0, by subtracting 'i' from 8 I get row numbers in descending order from 8 to 1, excluding 0.
        for j, col in enumerate(row):
            print(col, end = " ")    # Here I print column headers at the bottom of the chess board, leaving a space at the end.
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h") # I create 3 string spaces to alighn column headers with the row at first and then 2 string spaces between column labels.


def ask_user_for_white_piece(board):
    while True: # Starting the infinite loop, which would ask user for the input until valid details are provided
        user_input = input("Enter the piece and position for white figure e.g 'pawn a2'(you can choose only between rook and pawn): ").strip().lower() # Asking user for the input, converting to lowercase and removing any white spaces
        parts = user_input.split() # Splitting the 'user_input' into two parts ('piece' and 'position')
        if len(parts) != 2: # Checking if input contains exactly two parts ('pice' and 'position')
            print("Invalid input. Please enter the coordinates in the format 'piece a2':") # If input does not meet the criteria of the line above, call for user input in the correct format
            continue

        piece, position = parts # Check if user input follows the predefined input criteria (allowing to choose white piece only between rook and pawn)
        if piece not in ["pawn", "rook"]:
            print("Invalid piece. Please choose between 'pawn' or 'rook': ") # If piece is not in the list above, call for user input asking to choose between 'pawn' or 'rook'
            continue

        if len(position) !=2 or position[0] not in "abcdefgh" or position[1] not in "12345678": # Checking if position is printed in the valid format, if not the code asks user to input the position in the right format
            print("Invalid position. Please enter a valid position like 'a2':")
            continue

        column, row = position[0], position[1] # Adjusting positions on the board, so they are written with the right index
        x = 8 - int(row)  # Convert row to board index (0, 7)
        y = ord(column) - ord('a')  # Convert column to board index (0, 7)

        if board[x][y] != "__": # Checking if the position on the board is already occupied
            print("Position already occupied. Please choose a different position:") # If yes, asking user to choose different position to place the white piece
            continue

        piece_symbol = 'PW' if piece == "pawn" else "RW" # Returning the piece symbol ('PW' for pawn, "RW" for rook)
        return [x, y, piece_symbol] # Returning board indices and the chosen piece symbol


def ask_user_for_black_pieces(board): # Defining the function which will ask for the user input after white piece has been placed
    black_pieces = [] # creating a list to store black pieces
    piece_count = {"pawn": 0, "rook": 0, "king": 0, "queen": 0, "bishop": 0, "knight": 0} # initializing the dictionary to count which and how many black pieces were placed

    while len(black_pieces) < 16: # Initializing the loop, which continues when up to 16 black pieces were placed on the board
        user_input = input("Enter the piece and position for black figures (e.g pawn a2), or type 'done' to finish: ") # calling for user input
        if user_input == 'done': # If user input is 'done' after placing at least 1 and at most 16 black pieces, break the code
            break

        parts = user_input.split() # Splitting the 'user_input' into two parts ('piece' and 'position')
        if len(parts) != 2: # # Checking if input contains exactly two parts ('pice' and 'position')
            print("Invalid input. Please enter the coordinates in the format 'piece a2':") # If input does not meet the criteria of the line above, call for user input in the correct format
            continue

        piece, position = parts # Check if user input follows the predefined input criteria
        if piece not in ["pawn", "rook", "king", "queen", "bishop", "knight"]:
            print("Invalid piece. Please choose between 'pawn', 'rook', 'king', 'queen', 'bishop' or 'knight': ") # Checks if the selected figure is in the list of black pieces
            continue


        if piece == "pawn" and piece_count[piece] >= 8: # No more than 8 black 'pawns' could be printed
            print("Cannot place more than 8 pawns:")
            continue
        elif piece in ["rook", "bishop", "knight"] and piece_count[piece] >= 2: # No more than 2 black pieces (rook, bishop, knight) could be printed
            print(f"Cannot place more than 2 {piece}s:")
            continue
        elif piece in ["queen", "king"] and piece_count[piece] >=1: # No more than 1 black king and 1 black queen could be printed
            print(f"Cannot place more than 1 {piece}:")
            continue


        if len(position) !=2 or position[0] not in "abcdefgh" or position[1] not in "12345678": # Checking if position is printed in the valid format, if not the code asks user to input the position in the right format
            print("Invalid position. Please enter a valid position like 'a2':")
            continue

        column, row = position[0], position[1]  # Adjusting positions on the board, so they are written with the right index
        x = 8 - int(row)  # # Convert row to board index (0, 7)
        y = ord(column) - ord('a')  # Convert column to board index (0, 7)

        if board[x][y] != "__": # Checking if the position on the board is already occupied
            print("Position already occupied. Please choose a different position:") # If yes, asking user to choose different position to place the white piece
            continue

        piece_symbol = {  # Creating a dictionary to represent pieces by a shorter format
            "pawn" : "PB",
            "rook" : "RB",
            "king" : "KB",
            "queen" : "QB",
            "bishop" : "BB",
            "knight" : "NB"
        }[piece] # Getting the piece symbol based on piece type
        black_pieces.append([x, y, piece_symbol]) # Adding the piece to the list of black pieces
        piece_count[piece] += 1 # Incrementing a piece count to avoid duplicates and confirm that black piece was placed on the board
        print(f"Added {piece} at {position}.") # Printing the confirmation text

        if len(black_pieces) >= 16: # Check if the maximum number of black pieces has been reached
            print("Maximum number of black pieces reached") # If yes, notify the user

    return black_pieces # Return the list of black pieces


def check_captures(board, white_x, white_y, white_piece):
    captures = [] # Creating a list to store possible captures of the white piece
    directions = [] # Creating a list to store possible moves based on the piece type ('pawn' or 'rook')

    if white_piece == "PW":
        directions = [(-1, -1), (-1, 1)]  # Diagonal captures for a pawn
    elif white_piece == "RW":
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Horizontal and vertical captures for a rook

    for dx, dy in directions: # Iterating over each possible direction
        x, y = white_x + dx, white_y + dy # Calculating the next position in the current direction
        if 0 <= x < 8 and 0 <= y < 8 and board[x][y] != "__" and board[x][y][1] == "B": # checking if there is a black piece within the board
            captures.append((x, y, board[x][y])) # Adding captured figures to the list

    return captures # Returning the list of possible captures


def print_possible_captures(captures): # Defining the function which checks if there are available pieces to capture and if there are, prints the name and the position of the black piece
    if captures:
        print("The white piece can capture the following black pieces:")
        for x, y, piece in captures:
            column_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][y] # Converting index to column letter
            position = column_letter + str(8 - x) # Converting x index to row number
            print(f"{piece} at {position}") # Printing the available pieces and positions if there are options for the capture
    else:
        print("The white piece cannot capture any black pieces.") # If there are no available options to capture, it is printed that there are no available black pieces to capture


if __name__ == "__main__": # Calling the main function to execute the program
    main()

