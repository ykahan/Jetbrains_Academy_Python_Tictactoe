# write your code here
import re


def line_with_pipe(string):
    return "| " + string[0] \
           + " " + string[1] \
           + " " + string[2] \
           + " |"


def print_game(game_string):
    dashes = "-" * 9
    print(dashes)
    print(line_with_pipe(game_string[0:3]))
    print(line_with_pipe(game_string[3:6]))
    print(line_with_pipe(game_string[6:]))
    print(dashes)


def horizontal_win(game_string, letter):
    # checking if any row comprises all X's or all O's
    for i in range(0, 7, 3):
        if game_string[i] == letter \
                and game_string[i] == game_string[i + 1] \
                and game_string[i + 1] == game_string[i + 2]:
            return True
    return False


def vertical_win(game_string, letter):
    # checking if any column comprises all X's or all O's
    for i in range(0, 3, 1):
        if game_string[i] == letter \
                and game_string[i] == game_string[i + 3] \
                and game_string[i + 3] == game_string[i + 6]:
            return True
    return False


def diagonal_win(game_string, letter):
    # checking if either diagonal comprises all X's or all O's
    if game_string[0] == letter \
            and game_string[0] == game_string[4] \
            and game_string[4] == game_string[8]:
        return True
    if game_string[2] == letter \
            and game_string[2] == game_string[4] \
            and game_string[4] == game_string[6]:
        return True
    return False


def wins(game_string, letter):
    if horizontal_win(game_string, letter):
        return True
    if vertical_win(game_string, letter):
        return True
    if diagonal_win(game_string, letter):
        return True
    return False


def num_letter(game_string, letter):
    found_letters = re.finditer(letter, game_string)
    num_letters = list()
    for letter in found_letters:
        num_letters.append(letter.start())
    return len(num_letters)


def are_there_exactly_nine_cells(game_string):
    return len(game_string) == 9


def is_the_ratio_of_xs_and_os_acceptable(game_string):
    ratio_of_xs_and_os_is_acceptable = True
    # the numbers of Xs can differ from the number of Os
    # by at most 1, in either direction
    x_num = num_letter(game_string, "X")
    o_num = num_letter(game_string, "O")
    if x_num > o_num + 1 or x_num < o_num - 1:
        ratio_of_xs_and_os_is_acceptable = False

    return ratio_of_xs_and_os_is_acceptable


def not_both_sides_win(game_string):
    x_wins = wins(game_string, "X")
    y_wins = wins(game_string, "O")
    return True if not x_wins and y_wins else False


def game_state_possible(game_string):
    game_is_possible = not_both_sides_win(game_string)
    if game_is_possible:
        game_is_possible = is_the_ratio_of_xs_and_os_acceptable(game_string)
    if game_is_possible:
        game_is_possible = are_there_exactly_nine_cells(game_string)

    return game_is_possible


def get_game_state(game_string):
    possible = game_state_possible(game_string)
    if not possible:
        return "Impossible"
    if wins(game_string, "X"):
        return "X wins"
    if wins(game_string, "O"):
        return "O wins"
    x_num = num_letter(game_string, "X")
    o_num = num_letter(game_string, "O")
    if x_num + o_num == 9:
        return "Draw"
    else:
        return "Game not finished"


def is_cell_string_right_length(cell_string):
    # inputs should be exactly 3 characters long
    return len(cell_string) == 3


def only_digits(numbers):
    # inputs must be digits only
    for i in range(len(numbers)):
        if not numbers[i].isdigit():
            return False
    return True


def cast_list_elements_to_ints(source_list):
    for i in range(len(source_list)):
        source_list[i] = int(source_list[i])
    return source_list


def reduce_by_one(source_list):
    for i in range(len(source_list)):
        source_list[i] -= 1
    return source_list


def translate_tuple_for_game_string(numbers):
    index = 0
    index += numbers[1]
    index += numbers[0] * 3
    return index


def space_is_occupied(game_string, numbers):
    index = translate_tuple_for_game_string(numbers)
    return game_string[index] == "X" or game_string[index] == "O"


def only_valid_digits_used(numbers):
    if numbers[0] < 1 or numbers[0] > 3 or \
            numbers[1] < 1 or numbers[1] > 3:
        return False
    return True


def does_cell_string_have_space_between_digits(cell_string):
    cell_list = [x for x in cell_string]
    if cell_list[1] != " ":
        print("Contents: {" + cell_list[1] + "}")
        return False
    return True


def is_new_move_valid(game_string, cell_string):
    if not does_cell_string_have_space_between_digits(cell_string):
        return False
    if not is_cell_string_right_length(cell_string):
        return False
    numbers_list = [character for character in cell_string.replace(" ", "")]
    if not only_digits(numbers_list):
        return False
    numbers_list = cast_list_elements_to_ints(numbers_list)
    if not only_valid_digits_used(numbers_list):
        return False
    numbers_list = reduce_by_one(numbers_list)
    if space_is_occupied(game_string, numbers_list):
        return False
    return True


def invalid_move_message(game_string, cell_string):
    if not is_cell_string_right_length(cell_string):
        return "That response is not 3 characters long!"
    if not does_cell_string_have_space_between_digits(cell_string):
        return "There must be a space immediately after the first digit!"
    cell_string = cell_string.replace(" ", "")
    inputs_list = [character for character in cell_string]
    if not only_digits(inputs_list):
        return "You should enter numbers!"
    inputs_list = cast_list_elements_to_ints(inputs_list)
    if not only_valid_digits_used(inputs_list):
        return "Coordinates should be from 1 to 3!"
    inputs_list = cast_list_elements_to_ints(inputs_list)
    inputs_list = reduce_by_one(inputs_list)
    if space_is_occupied(game_string, inputs_list):
        return "This cell is occupied! Choose another one!"
    return "I'm stumped!"


def update_game_string(game_string, cell_string, x_turn):
    cell_string = cell_string.replace(" ", "")
    inputs_list = [character for character in cell_string]
    inputs_list = cast_list_elements_to_ints(inputs_list)
    inputs_list = reduce_by_one(inputs_list)
    index = translate_tuple_for_game_string(inputs_list)

    if x_turn:
        player = "X"
    else:
        player = "O"

    first_part_game_string = game_string[:index]
    last_part_game_string = game_string[index + 1:]
    game_string = first_part_game_string + player + last_part_game_string
    return game_string


def analyze_move(game_string, new_move_string):
    move_is_valid = is_new_move_valid(game_string, new_move_string)
    if not move_is_valid:
        print(invalid_move_message(game_string, new_move_string))
    return move_is_valid


def get_user_move():
    return input("Please enter a cell, using 2 integers to identify it")


def user_move(game_string, x_turn):
    valid_move_acquired = False
    new_move_string = ""
    while not valid_move_acquired:
        new_move_string = get_user_move()
        valid_move_acquired = analyze_move(game_string, new_move_string)
    return update_game_string(game_string, new_move_string, x_turn)


def play_game():
    # game_string = input("Enter cells:")
    # state = get_game_state(game_string)
    # print("Game string is: " + game_string)
    game_string = "         "
    game_in_progress = True
    x_turn = True
    while game_in_progress:
        game_string = user_move(game_string, x_turn)
        x_turn = not x_turn
        print_game(game_string)
        if wins(game_string, "X") \
                or wins(game_string, "O") \
                or " " not in game_string:
            game_in_progress = False
            winner = ""
            if wins(game_string, "X"):
                winner = "X"
            elif wins(game_string, "O"):
                winner = "O"
            if winner:
                print(f"{winner} wins")
            else:
                print("Draw")


play_game()
