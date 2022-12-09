# link to source problem: https://adventofcode.com/2022/day/9

def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            split_line = line.strip().split(' ')
            result.append([split_line[0], int(split_line[1])])
    return result


def move_knot(knot_one, knot_two):
    if abs(knot_one[0] - knot_two[0]) > 1:
        knot_two[0] = knot_two[0] + 1 if knot_one[0] > knot_two[0] else knot_two[0] - 1
        if abs(knot_one[1] - knot_two[1]) >= 1:
            knot_two[1] = knot_two[1] + 1 if knot_one[1] > knot_two[1] else knot_two[1] - 1
        return True
    elif abs(knot_one[1] - knot_two[1]) > 1:
        knot_two[1] = knot_two[1] + 1 if knot_one[1] > knot_two[1] else knot_two[1] - 1
        if abs(knot_one[0] - knot_two[0]) >= 1:
            knot_two[0] = knot_two[0] + 1 if knot_one[0] > knot_two[0] else knot_two[0] - 1
        return True
    return False


def simulate_direction(instruction, knots):
    tail_moves = set()
    for _ in range(instruction[1]):
        if instruction[0] in ['R', 'L']:
            knots[0][0] = knots[0][0] + 1 if instruction[0] == 'R' else knots[0][0] - 1
        else:
            knots[0][1] = knots[0][1] + 1 if instruction[0] == 'U' else knots[0][1] - 1
        for index in range(1, len(knots)):
            if not move_knot(knots[index - 1], knots[index]):
                break
            if index == len(knots) - 1:
                tail_moves.add((knots[index][0], knots[index][1]))
    return tail_moves


def solve_puzzle(parsed_file, num_of_knots):
    knot_positions = [[0, 0] for _ in range(num_of_knots)]
    visited_by_tail = {(0, 0)}
    for instruction in parsed_file:
        visited_by_tail = visited_by_tail.union(simulate_direction(instruction, knot_positions))
    return len(visited_by_tail)


prepared_file = read_file('day09.txt')
print(f'Task01: {solve_puzzle(prepared_file, 2)}')
print(f'Task02: {solve_puzzle(prepared_file, 10)}')
