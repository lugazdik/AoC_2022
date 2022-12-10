# link to source problem: https://adventofcode.com/2022/day/10

def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            split_line = line.strip().split(' ')
            result.append([split_line[0], int(split_line[1])]) if len(split_line) == 2 else result.append(split_line)
    return result


def task01(parsed_file):
    cycle = 0
    x_register = 1
    result = 0
    for instruction in parsed_file:
        cycle += 1
        if cycle % 40 == 20:
            result += cycle * x_register
        if instruction[0] == 'addx':
            cycle += 1
            if cycle % 40 == 20:
                result += cycle * x_register
            x_register += instruction[1]
    return result


def append_symbol(cycle, position):
    return '#'if abs(cycle % 40 - position) <= 1 else '.'


def print_line(cycle, line):
    if cycle % 40 == 0:
        print(line)
        line = ''
    return line


def increase_cycle(cycle, position, line):
    line += append_symbol(cycle, position)
    cycle += 1
    return cycle, print_line(cycle, line)


def task02(parsed_file):
    cycle = 0
    sprite_position = 1
    my_string = ''
    for instruction in parsed_file:
        cycle, my_string = increase_cycle(cycle, sprite_position, my_string)
        if instruction[0] == 'addx':
            cycle, my_string = increase_cycle(cycle, sprite_position, my_string)
            sprite_position += instruction[1]
    print_line(cycle, my_string)


prepared_file = read_file('day10.txt')
print(f'Task01: {task01(prepared_file)}')
task02(prepared_file)
