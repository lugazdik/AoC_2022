# link to source problem: https://adventofcode.com/2022/day/13
from functools import cmp_to_key


def read_file(path):
    with open(path, 'r') as file:
        pairs = []
        for pair in file.read().split('\n\n'):
            pairs.append(list(map(eval, (pair.split('\n')))))
        return pairs


def compare(first, second):
    first_int = isinstance(first, int)
    second_int = isinstance(second, int)

    if first_int and second_int:
        return first - second

    if first_int:
        return compare([first], second)
    if second_int:
        return compare(first, [second])

    for x, y in zip(first, second):
        res = compare(x, y)
        if res != 0:
            return res
    return len(first) - len(second)


def task01(parsed_file):
    sum_of_indexes = 0
    for index, pair in enumerate(parsed_file):
        if compare(pair[0], pair[1]) <= 0:
            sum_of_indexes += index + 1
    return sum_of_indexes


def task02(parsed_file):
    two_array, six_array = [[2]], [[6]]
    all_packets = [two_array, six_array]
    for pair in parsed_file:
        all_packets.append(pair[0])
        all_packets.append(pair[1])
    all_packets.sort(key=cmp_to_key(compare))
    return (all_packets.index(two_array) + 1) * (all_packets.index(six_array) + 1)


prepared_file = read_file('day13.txt')
print(f'Task01: {task01(prepared_file)}')
print(f'Task02: {task02(prepared_file)}')
