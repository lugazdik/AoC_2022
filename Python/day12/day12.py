# link to source problem: https://adventofcode.com/2022/day/12
from collections import deque


def read_file(path):
    grid = []
    start_coords = (0, 0)
    end_coords = (0, 0)
    with open(path, 'r') as file:
        row = 0
        for line in file.read().split('\n'):
            if (col := line.find('S')) != -1:
                start_coords = (row, col)
            if (col := line.find('E')) != -1:
                end_coords = (row, col)
            grid.append([*line])
            row += 1
        return grid, start_coords, end_coords


def find_elevation(letter):
    if letter == 'S':
        return ord('a')
    if letter == 'E':
        return ord('z')
    return ord(letter)


def find_valid_neighbours(grid, current_pos, visited):
    current_elevation = find_elevation(grid[current_pos[0]][current_pos[1]])
    possible_neighbours = [(current_pos[0] + 1, current_pos[1]),
                           (current_pos[0] - 1, current_pos[1]),
                           (current_pos[0], current_pos[1] + 1),
                           (current_pos[0], current_pos[1] - 1)]
    valid_neighbours = []
    for pos in possible_neighbours:
        if 0 <= pos[0] < len(grid) \
                and 0 <= pos[1] < len(grid[0]) \
                and find_elevation(grid[pos[0]][pos[1]]) - current_elevation <= 1\
                and pos not in visited:
            valid_neighbours.append(pos)
    return valid_neighbours


def BFS(parsed_file, start, end):
    my_queue = deque()
    visited = set()
    my_queue.append({'coords': start, 'num_visited': 0})
    while my_queue:
        node = my_queue.popleft()
        if node['coords'] in visited:
            continue
        visited.add(node['coords'])

        if node['coords'] == end:
            return node['num_visited']

        successors = find_valid_neighbours(parsed_file, node['coords'], visited)
        for succ in successors:
            my_queue.append({'coords': succ, 'num_visited': node['num_visited'] + 1})
    return -1


def task02(parsed_file, start, end):
    min_length = BFS(parsed_file, start, end)
    for row_index, row in enumerate(parsed_file):
        for column_index, column in enumerate(row):
            if parsed_file[row_index][column_index] == 'a':
                length = BFS(parsed_file, (row_index, column_index), end)
                if length != -1 and length < min_length:
                    min_length = length
    return min_length


prepared_file, s_coords, e_coords = read_file('day12.txt')
print(f'Task01: {BFS(prepared_file, s_coords, e_coords)}')
print(f'Task02: {task02(prepared_file, s_coords, e_coords)}')
