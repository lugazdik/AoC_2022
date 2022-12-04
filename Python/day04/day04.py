# link to source problem: https://adventofcode.com/2022/day/4


def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            intervals = line.strip().split(',')
            first = intervals[0].split('-')
            second = intervals[1].split('-')
            result.append([[int(first[0]), int(first[1])], [int(second[0]), int(second[1])]])
        return result


def does_fully_contain(a, b, x, y):
    return (a <= x <= b and a <= y <= b) or (x <= a <= y and x <= b <= y)


def does_overlap(a, b, x, y):
    return a <= x <= b or a <= y <= b or x <= a <= y or x <= b <= y


def task01(parsed_input):
    count_total_overlaps = 0
    for pair in parsed_input:
        if does_fully_contain(pair[0][0], pair[0][1], pair[1][0], pair[1][1]):
            count_total_overlaps += 1
    return count_total_overlaps


def task02(parsed_input):
    count_overlaps = 0
    for pair in parsed_input:
        if does_overlap(pair[0][0], pair[0][1], pair[1][0], pair[1][1]):
            count_overlaps += 1
    return count_overlaps


prepared_file = read_file('day04.txt')
print('Task1: ' + str(task01(prepared_file)))
print('Task2: ' + str(task02(prepared_file)))
