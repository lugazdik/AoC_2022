# link to source problem: https://adventofcode.com/2022/day/5

def read_file(path):
    crates = [[], [], [], [], [], [], [], [], []]
    instructions = []
    with open(path, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith(' 1') or line == '':
                continue
            elif line.startswith('move'):
                line_split = line.strip().split(' ')
                instructions.append([int(line_split[1]), int(line_split[3]), int(line_split[5])])
            else:
                column = 0
                for i in range(1, len(line), 4):
                    if line[i].isalpha():
                        crates[column].append(line[i])
                    column += 1
        for i in range(len(crates)):
            crates[i].reverse()
        return crates, instructions


def find_top_crates(grid):
    result = ''
    for col in grid:
        if col:
            result += col[-1]
    return result


def task01():
    grid, instructions = read_file('day05.txt')
    for instr in instructions:
        for i in range(instr[0]):
            item = grid[instr[1] - 1].pop()
            grid[instr[2] - 1].append(item)
    return find_top_crates(grid)


def task02():
    grid, instructions = read_file('day05.txt')
    for ins in instructions:
        take = grid[ins[1]-1][-ins[0]:]
        grid[ins[1]-1] = grid[ins[1]-1][:-ins[0]]
        grid[ins[2]-1] += take
    return find_top_crates(grid)


print('Task1: ' + str(task01()))
print('Task2: ' + str(task02()))
