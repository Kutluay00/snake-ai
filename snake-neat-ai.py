import sys

main_snake = []
board_x = 0     # length of the board horizontally
board_y = 0     # length of the board vertically




def parse(string_array):
    return False


def move_right():
    block_modify = main_snake.pop()  # returns the last item
    head = main_snake[0]
    block_modify[0] = head[0] + 1  # increase the x-axis
    block_modify[1] = head[1]      # y-axis
    main_snake.insert(1, block_modify)
    return main_snake


def move_up():
    block_modify = main_snake.pop()  # returns the last item
    head = main_snake[0]
    block_modify[0] = head[0]        # x-axis
    block_modify[1] = head[1] - 1    # increase y-axis
    main_snake.insert(1, block_modify)
    return main_snake


def move_left():
    block_modify = main_snake.pop()  # returns the last item
    head = main_snake[0]
    block_modify[0] = head[0] - 1  # decrease the x-axis
    block_modify[1] = head[1]      # y-axis
    main_snake.insert(1, block_modify)
    return main_snake


def move_down():
    block_modify = main_snake.pop()  # returns the last item
    head = main_snake[0]
    block_modify[0] = head[0]        # x-axis
    block_modify[1] = head[1] + 1    # decrease y-axis
    main_snake.insert(1, block_modify)
    return main_snake


# Returns true if there is a duplicate pair of
# coordinates.
def is_there_duplicate():
    head = main_snake[0]
    if head in main_snake[1:]:
        return True
    else:
        return False


# Return true if the snake has eaten itself, false otherwise
def eaten_itself():
    return is_there_duplicate()


# Returns true if the snake hit the boundary
def is_out_of_boundary():
    head = main_snake[0]
    if head[0] > board_x or head[0] < 0 or head[1] > board_y or head[1] < 0:
        return True
    else:
        return False


if __name__ == "__main__":
    state_input = str(sys.argv[1])
    snake_state_input = parse(state_input)