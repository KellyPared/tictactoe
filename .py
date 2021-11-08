from collections import Counter

enter_cells = list(" " * 9)
counter = 0
winner = False
COORDS = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 3),
]

X_WINS = ['X', 'X', 'X']
O_WINS = ['O', 'O', 'O']

def movement(turn):
    if position == (1, 1):
        enter_cells[0] = turn
    elif position == (1, 2):
        enter_cells[1] = turn
    elif position == (1, 3):
        enter_cells[2] = turn
    elif position == (2, 1):
        enter_cells[3] = turn
    elif position == (2, 2):
        enter_cells[4] = turn
    elif position == (2, 3):
        enter_cells[5] = turn
    elif position == (3, 1):
        enter_cells[6] = turn
    elif position == (3, 2):
        enter_cells[7] = turn
    elif position == (3, 3):
        enter_cells[8] = turn
    # after moves complete, update and return the board
    return update_board()


def update_board():
    # given enter_cells and coords, update the board
    return dict(zip(COORDS, enter_cells))


def winning_combos(enter_cells):
    update_board()
    horizontal_1 = [enter_cells[0], enter_cells[1], enter_cells[2]]
    horizontal_2 = [enter_cells[3], enter_cells[4], enter_cells[5]]
    horizontal_3 = [enter_cells[6], enter_cells[7], enter_cells[8]]
    vertical_3 = [enter_cells[2], enter_cells[5], enter_cells[8]]
    vertical_2 = [enter_cells[1], enter_cells[4], enter_cells[7]]
    vertical_1 = [enter_cells[0], enter_cells[3], enter_cells[6]]
    diagonal_1 = [enter_cells[0], enter_cells[4], enter_cells[8]]
    diagonal_2 = [enter_cells[2], enter_cells[4], enter_cells[6]]

    horizontal_winning_combinations = [
        enter_cells[0:3],
        enter_cells[3:6],
        enter_cells[6:9],
    ]
    vertical_winning_combinations = [
        [enter_cells[0], enter_cells[3], enter_cells[6]],
        [enter_cells[1], enter_cells[4], enter_cells[7]],
        [enter_cells[2], enter_cells[5], enter_cells[8]],
    ]
    diagonal_winning_combinations = [
        [enter_cells[0], enter_cells[4], enter_cells[8]],
        [enter_cells[2], enter_cells[4], enter_cells[6]],
    ]
    common_winning_combinations = [
        horizontal_winning_combinations,
        vertical_winning_combinations,
        diagonal_winning_combinations,
    ]

    return common_winning_combinations

def print_board():
    update_board()
    print("---------")
    print(f"| {enter_cells[0]} {enter_cells[1]} {enter_cells[2]} |")
    print(f"| {enter_cells[3]} {enter_cells[4]} {enter_cells[5]} |")
    print(f"| {enter_cells[6]} {enter_cells[7]} {enter_cells[8]} |")
    print("---------")

print_board()    
while winner == False:
    counter += 1
    if counter >= 10:
        print("Draw")
        break
    try:
        coord_1, coord_2 = input("Enter the coordinates: ").strip().split(" ")
        position = (int(coord_1), int(coord_2))
        if int(coord_1) > 3 or int(coord_2) > 3:
            print("Coordinates should be from 1 to 3!")
            counter -=1
        board = update_board()
        winning_combination = winning_combos(enter_cells)
        results = Counter(board.values())
        
    except ValueError:
        print("You should enter numbers!")

    if board.get(position) == "X" or board.get(position) == "O":
        print("This cell is occupied! Choose another one!")
        counter -= 1

    else:
        
        
        if counter % 2 == 1:
            turn = "X"
            board = movement(turn)
            winning_combination = winning_combos(enter_cells)
            print_board()
            for combos in winning_combination:
                if X_WINS in combos:
                    print("X wins")
                    winner = True
                    break
        else:
            turn = "O"
            board = movement(turn)
            winning_combination = winning_combos(enter_cells)
            print_board()
            for combos in winning_combination:
                if O_WINS in combos:
                    print("O wins")
                    winner = True
                    break
