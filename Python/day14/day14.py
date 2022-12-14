# link to source problem: https://adventofcode.com/2022/day/14
# could use some refactor

def read_file(path):
    with open(path, 'r') as file:
        rock_coords = []
        for line in file.readlines():
            split_line = line.strip().split(' -> ')
            rocks = []
            for item in split_line:
                rocks.append(tuple(map(int, item.split(','))))
            rock_coords.append(rocks)
        return rock_coords


def setup_cave(parsed_file):
    cave = set()
    max_y = 0
    for rock in parsed_file:
        previous_coord = None
        for coord in rock:
            if coord[1] > max_y:
                max_y = coord[1]
            if previous_coord:
                if previous_coord[0] == coord[0]:
                    index_change = - 1 if coord[1] > previous_coord[1] else 1
                    for y in range(coord[1], previous_coord[1], index_change):
                        cave.add((coord[0], y))
                else:
                    index_change = - 1 if coord[0] > previous_coord[0] else 1
                    for x in range(coord[0], previous_coord[0], index_change):
                        cave.add((x, coord[1]))
            else:
                cave.add(coord)
            previous_coord = coord
    return cave, max_y


def move_sand_grain(rocks, sand, current_pos):
    down = (current_pos[0], current_pos[1] + 1)
    if down not in sand and down not in rocks:
        return down
    left = (current_pos[0] - 1, current_pos[1] + 1)
    if left not in sand and left not in rocks:
        return left
    right = (current_pos[0] + 1, current_pos[1] + 1)
    if right not in sand and right not in rocks:
        return right
    return None


def task01(rocks, max_y):
    sand = set()
    start_position = (500, 0)
    current_position = start_position
    while True:
        next_position = move_sand_grain(rocks, sand, current_position)
        if next_position is None:
            sand.add(current_position)
            current_position = start_position
        else:
            current_position = next_position
        if current_position[1] >= max_y:
            break
    return sand


def task02(rocks, max_y):
    sand = set()
    start_position = (500, 0)
    current_position = start_position
    while True:
        next_position = move_sand_grain(rocks, sand, current_position)
        if next_position is None or next_position[1] == max_y:
            sand.add(current_position)
            current_position = start_position
        else:
            current_position = next_position
        if (500, 0) in sand:
            break
    return sand


prepared_file = read_file('day14.txt')
my_cave, max_depth = setup_cave(prepared_file)
task1_set = task01(my_cave, max_depth)
task2_set = task02(my_cave, max_depth + 2)
print(f'Task01: {len(task1_set)}')
print(f'Task02: {len(task2_set)}')
