import turtle

SQUARE = 50
UPPER_BOUNDARY = 125
LEFT_BOUNDARY = -175
RIGHT_BOUNDARY = 175
LOWER_BOUNDARY = -175
ORIGIN_X = 20
ORIGIN_Y = 0
HEIGHT = 6
WIDTH = 7
MAX_POS_Y_HEIGHT = 100

starting_piece = True
connect = turtle.Turtle()
#game_state = []


def init_game():
    draw_board()
    create_board_state()
    create_game_listener()
    run_game()


def draw_board():
    ''' Function: draw_board
        Parameters: n, an int for # of squares
        Returns: nothing
        Does: Draws an nxn board with a yellow background
    '''

    turtle.setup(8 * SQUARE + SQUARE, 8 * SQUARE + SQUARE)
    turtle.screensize(HEIGHT * SQUARE, WIDTH * SQUARE)
    turtle.bgcolor('White')

    # Create the turtle to draw the board
    connect.penup()
    connect.speed(0)
    connect.hideturtle()

    # Line color is black, fill color is yellow
    connect.color("black", "yellow")

    # Move the turtle to the upper left corner
    corner = -WIDTH * SQUARE / 2
    connect.setposition(corner, corner)

    # Draw the yellow background
    connect.begin_fill()
    for i in range(4):
        connect.pendown()
        if i % 2 == 0:
            connect.forward(SQUARE * WIDTH)
        else:
            connect.forward(SQUARE * HEIGHT)
        connect.left(90)

    connect.end_fill()

    # Draw the horizontal lines
    for i in range(WIDTH):
        connect.setposition(corner, SQUARE * i + corner)
        draw_lines(connect, WIDTH)

    # Draw the vertical lines
    connect.left(90)
    for i in range(8):
        connect.setposition(SQUARE * i + corner, corner)
        draw_lines(connect, HEIGHT)


def draw_lines(turt, n):
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()


# Purpose
# This function takes the globally defined gate_state, and uses it to represent the game 'state'.  This may be most
# easily represented as a list of list
def create_board_state():
    global game_state
    game_state = []
    for i in range(7):
        game_state += [[None, None, None, None, None, None]]
    print(game_state)



def create_game_listener():
    turtle.onscreenclick(execute_move)


def execute_move(x, y):
    pos_x = translate_pos(x)
    pos_y = push_down_piece((pos_x, MAX_POS_Y_HEIGHT))
    valid_move = validate_move((pos_x, pos_y))

    if valid_move:
        draw_piece(pos_x, pos_y)
        evaluate_for_winner(int(pos_x), int(pos_y))
        evaluate_for_full_board()


def push_down_piece(pos):
    global game_state
    pos_x, pos_y = pos

    if game_state[get_row_index(pos_y)][get_column_index(pos_x)] is not None:
        return pos_y + 50
    elif get_row_index(pos_y) == 0:
        return pos_y
    else:
        return push_down_piece((pos_x, pos_y - 50))


def translate_pos(x):
    pos_x = (-((-x + SQUARE / 2) // SQUARE) * SQUARE) + 20 if x < 0 else (((x + SQUARE / 2) // SQUARE) * SQUARE) + 20
    return pos_x


def validate_move(pos):
    x, y = pos
    temp_x = get_column_index(x)
    temp_y = get_row_index(y)
    return pos_in_bounds(x, y) and game_state[temp_y][temp_x] is None


def pos_in_bounds(x, y):
    return RIGHT_BOUNDARY > x > LEFT_BOUNDARY and LOWER_BOUNDARY < y < UPPER_BOUNDARY


def get_column_index(x):
    if x // SQUARE >= 0:
        temp_x = int(x // SQUARE + 3)
    elif -x // SQUARE == 0:
        temp_x = 2
    elif -x // SQUARE == 1:
        temp_x = 1
    else:
        temp_x = 0

    return temp_x


def get_row_index(y):
    if y // SQUARE >= 0:
        temp_y = int(y // SQUARE + 3)
    elif -y // SQUARE == 3:
        temp_y = 0
    elif -y // SQUARE == 2:
        temp_y = 1
    else:
        temp_y = 2

    return temp_y


def draw_piece(x, y):
    global starting_piece, game_state

    if starting_piece:
        connect.color("black", "Red")
        starting_piece = False
        game_state[get_row_index(y)][get_column_index(x)] = False
    else:
        connect.color("black", "black")
        starting_piece = True
        game_state[get_row_index(y)][get_column_index(x)] = True

    connect.setposition(x, y)
    connect.pendown()
    connect.begin_fill()
    connect.circle(20)
    connect.end_fill()
    connect.penup()


def evaluate_for_winner(x, y):
    global game_state

    if is_winning_move((x, y)):
        end_game()


def is_winning_move(pos):
    return is_horizontal_win(pos) or is_vertical_win(pos) or is_diagonal_win(pos)


# def is_horizontal_win(pos):
    ###### Implement your logic here




    #################################

# Purpose
# This method determines if a position creates a winning combination of pieces
# Signature
# is_vertical_win :: ((Integer, Integer)) => Integer
# def is_vertical_win(pos):
#     global game_state
    ###### Implement your logic here




    #################################


# Purpose
# This method determines if a position creates a diagonal winning combination of pieces
# Signature
# is_diagonal_win :: ((Integer, Integer)) => Integer
# def is_diagonal_win(pos):
#     global game_state
    ###### Implement your logic here




    #################################

# Purpose
# This method determines if a position creates a winning diagonal combination of pieces, from the
# bottom right to the top left
# Signature
# is_right_to_left_win :: ((Integer, Integer)) => Integer
# def is_right_to_left_win(pos):
#     global game_state
    ###### Implement your logic here




    #################################

# Purpose
# This method determines if a position creates a winning diagonal combination of pieces, from the
# bottom left to the top right
# Signature
# is_left_to_right_win :: ((Integer, Integer)) => Integer
# def is_left_to_right_win(pos):
#     global game_state
    ###### Implement your logic here




    #################################


def evaluate_for_full_board():
    global game_state

    if board_full():
        end_game()

# Purpose
# This method determines if the board is full
# Signature
# board_full :: () => Boolean
# def board_full():
#     global game_state
    ###### Implement your logic here




    #################################


def end_game():
    global starting_piece

    turtle.onscreenclick(None)
    if board_full():
        print("The game is over, Tie!!!!")
    elif starting_piece:
        print("The game is over, BLACK wins!!!!")
    else:
        print("The game is over, RED wins!!!!")


def run_game():
    #turtle.exitonclick()
    turtle.done()


def main():
    init_game()


main()

