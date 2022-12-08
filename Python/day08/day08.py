# link to source problem: https://adventofcode.com/2022/day/8

def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(list(map(int, [*line.strip()])))
    return result


def get_column(grid, i):
    # returns matrix column
    return [row[i] for row in grid]


def get_sub_array(array, index, left_half=True):
    # returns either left or right half of a list based on index
    return array[:index] if left_half else array[index+1:]


def position_visible(grid, row, column):
    # tree is visible if it is bigger than any tree in the facing direction
    max_array = fill_max_array(grid, row, column)
    return grid[row][column] > max_array[0] or \
        grid[row][column] > max_array[1] or \
        grid[row][column] > max_array[2] or \
        grid[row][column] > max_array[3]


def fill_max_array(grid, row, column):
    # max_top, max_bottom, max_left, max_right
    col = get_column(grid, column)
    result = [-1, -1, -1, -1]
    result[0] = max(get_sub_array(col, row, True), default=-1)
    result[1] = max(get_sub_array(col, row, False), default=-1)
    result[2] = max(get_sub_array(grid[row], column, True), default=-1)
    result[3] = max(get_sub_array(grid[row], column, False), default=-1)
    return result


def task01(parsed_file):
    count_visible = 0
    for row in range(len(parsed_file)):
        for column in range(len(parsed_file[row])):
            if position_visible(parsed_file, row, column):
                count_visible += 1
    return count_visible


def calculate_score(array_to_compare, value, reverse=False):
    my_range = range(len(array_to_compare) - 1, -1, -1) if reverse else range(len(array_to_compare))
    score = 0
    for i in my_range:
        score += 1
        if array_to_compare[i] >= value:
            break
    return score


def find_viewing_score(grid, row, column, direction):
    score = 0
    value = grid[row][column]
    if direction == 'top':
        score += calculate_score(get_sub_array(get_column(grid, column), row, True), value, True)
    elif direction == 'bottom':
        score += calculate_score(get_sub_array(get_column(grid, column), row, False), value, False)
    elif direction == 'left':
        score += calculate_score(get_sub_array(grid[row], column, True), value, True)
    elif direction == 'right':
        score += calculate_score(get_sub_array(grid[row], column, False), value, False)
    return score


def find_total_viewing_score(grid, row, column):
    total_score = 1
    for direction in ['top', 'bottom', 'left', 'right']:
        total_score *= find_viewing_score(grid, row, column, direction)
    return total_score


def task02(parsed_file):
    max_viewing_score = 0
    for row in range(len(parsed_file)):
        for column in range(len(parsed_file[row])):
            if (viewing_score := find_total_viewing_score(parsed_file, row, column)) > max_viewing_score:
                max_viewing_score = viewing_score
    return max_viewing_score


prepared_file = read_file('day08.txt')
print(f'Task01: {task01(prepared_file)}')
print(f'Task02: {task02(prepared_file)}')
