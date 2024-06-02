# 1) Define main function
# 2) Define board state inside a main function
# 3) Create a board
# 4) Ask user to input the white piece on the board (pawn or rook)
# 5) Ask user to input black pieces (up to 16, the same number as there are pieces in total in the game)
# 6) At least one balck piece should be added, and if user does not want to add another black piece, user should input "done"
# 7) After pieces have been added, the confirmation or error message should be printed out
# 8) After figures have been added to the board, the program should print which black pieces could be taken by the white piece


def main():
    board = get_new_board()
    create_board(board)

    x, y, white_piece = ask_user_for_white_piece(board)
    board[x][y] = white_piece
    create_board(board)

    black_pieces = ask_user_for_black_pieces(board)
    for bx, by, black_piece in black_pieces:
        board[bx][by] = black_piece
    create_board(board)

    possible_captures = check_captures(board, x, y, white_piece)
    print_possible_captures(possible_captures)


def get_new_board():
    board = []
    for i in range(8):
        row = ["__"] * 8
        board.append(row)
    return board


def create_board(board):
    for i, row in enumerate(board):
        print(8 - i, end=": ")
        for col in row:
            print(col, end=" ")
        print("\n")
    print("  a  b  c  d  e  f  g  h")


def ask_user_for_white_piece(board):
    while True:
        user_input = (
            input(
                "Enter the piece and position for white figure e.g 'pawn a2' (you can choose only between rook and pawn): "
            )
            .strip()
            .lower()
        )
        parts = user_input.split()
        if len(parts) != 2:
            print(
                "Invalid input. Please enter the coordinates in the format 'piece a2':"
            )
            continue

        piece, position = parts
        if piece not in ["pawn", "rook"]:
            print("Invalid piece. Please choose between 'pawn' or 'rook': ")
            continue

        if (
            len(position) != 2
            or position[0] not in "abcdefgh"
            or position[1] not in "12345678"
        ):
            print("Invalid position. Please enter a valid position like 'a2':")
            continue

        column, row = position[0], position[1]
        x = 8 - int(row)
        y = ord(column) - ord("a")

        if board[x][y] != "__":
            print("Position already occupied. Please choose a different position:")
            continue

        piece_symbol = "PW" if piece == "pawn" else "RW"
        return [x, y, piece_symbol]


def ask_user_for_black_pieces(board):
    black_pieces = []
    piece_count = {
        "pawn": 0,
        "rook": 0,
        "king": 0,
        "queen": 0,
        "bishop": 0,
        "knight": 0,
    }

    while len(black_pieces) < 16:
        user_input = (
            input(
                "Enter the piece and position for black figures (e.g pawn a2), or type 'done' to finish: "
            )
            .strip()
            .lower()
        )
        if user_input == "done":
            break

        parts = user_input.split()
        if len(parts) != 2:
            print(
                "Invalid input. Please enter the coordinates in the format 'piece a2':"
            )
            continue

        piece, position = parts
        if piece not in ["pawn", "rook", "king", "queen", "bishop", "knight"]:
            print(
                "Invalid piece. Please choose between 'pawn', 'rook', 'king', 'queen', 'bishop' or 'knight': "
            )
            continue

        if piece == "pawn" and piece_count[piece] >= 8:
            print("Cannot place more than 8 pawns:")
            continue
        elif piece in ["rook", "bishop", "knight"] and piece_count[piece] >= 2:
            print(f"Cannot place more than 2 {piece}s:")
            continue
        elif piece in ["queen", "king"] and piece_count[piece] >= 1:
            print(f"Cannot place more than 1 {piece}:")
            continue

        if (
            len(position) != 2
            or position[0] not in "abcdefgh"
            or position[1] not in "12345678"
        ):
            print("Invalid position. Please enter a valid position like 'a2':")
            continue

        column, row = position[0], position[1]
        x = 8 - int(row)
        y = ord(column) - ord("a")

        if board[x][y] != "__":
            print("Position already occupied. Please choose a different position:")
            continue

        piece_symbol = {
            "pawn": "PB",
            "rook": "RB",
            "king": "KB",
            "queen": "QB",
            "bishop": "BB",
            "knight": "NB",
        }[piece]
        black_pieces.append([x, y, piece_symbol])
        piece_count[piece] += 1
        print(f"Added {piece} at {position}.")

        if len(black_pieces) >= 16:
            print("Maximum number of black pieces reached")

    return black_pieces


def check_captures(board, white_x, white_y, white_piece):
    captures = []
    directions = []

    if white_piece == "PW":
        directions = [(-1, -1), (-1, 1)]
        for dx, dy in directions:
            x, y = white_x + dx, white_y + dy
            if (
                0 <= x < 8
                and 0 <= y < 8
                and board[x][y] != "__"
                and board[x][y][1] == "B"
            ):
                captures.append((x, y, board[x][y]))
    elif white_piece == "RW":
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            x, y = white_x, white_y
            while True:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):
                    break
                if board[x][y] == "__":
                    continue
                if board[x][y][1] == "B":
                    captures.append((x, y, board[x][y]))
                break

    return captures


def print_possible_captures(captures):
    if captures:
        print("The white piece can capture the following black pieces:")
        for x, y, piece in captures:
            column_letter = ["a", "b", "c", "d", "e", "f", "g", "h"][y]
            position = column_letter + str(8 - x)
            print(f"{piece} at {position}")
    else:
        print("The white piece cannot capture any black pieces.")


if __name__ == "__main__":
    main()
