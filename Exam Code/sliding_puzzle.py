# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:(index + DIM)]
        print(row)
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()
    
def get_move():
    ''' gets users move'''
    move = int(input(""))
    if move in [QUIT]:
        return None
    else:
        return move

def move_board(puzzle_board, move):
    ''' Takes in puzzle board and a move, checks wether it is a valid move or not and
    changes the the puzzle board accordingly'''
    for row in puzzle_board:
        if EMPTYSLOT in row:
            empty_pos = (puzzle_board.index(row),row.index(EMPTYSLOT))
        if move in row:
            move_pos = (puzzle_board.index(row),row.index(move))
    
    if move_pos[0] == empty_pos[0] and move_pos[1] + 1 == empty_pos[1] or move_pos[0] == empty_pos[0] and move_pos[1] - 1 == empty_pos[1]: #Checks if the move is in the same row and is next to an empy space
        puzzle_board[move_pos[0]][move_pos[1]] = 0
        puzzle_board[empty_pos[0]][empty_pos[1]] = move
        return puzzle_board
    elif move_pos[1] == empty_pos[1] and move_pos[0] + 1 == empty_pos[0] or move_pos[1] == empty_pos[1] and move_pos[0] - 1 == empty_pos[0]:#Checks if the move is in the same collum and is next to an empy space
        puzzle_board[move_pos[0]][move_pos[1]] = 0
        puzzle_board[empty_pos[0]][empty_pos[1]] = move
        return puzzle_board
    else:
        return puzzle_board


def main():
    puzzle_board = initialize_board()
    display(puzzle_board)
    move = get_move()
    while move:
        puzzle_board = move_board(puzzle_board,move)
        display(puzzle_board)
        move = get_move()

main()