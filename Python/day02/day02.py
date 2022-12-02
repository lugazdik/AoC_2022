# link to source problem: https://adventofcode.com/2022/day/2

# lose = 0, draw = 3, win = 6
# A,X = rock = 1, B,Y = paper = 2, C,Z = scissors = 3
dict_of_points_task1 = {'A X': 4, 'A Y': 8, 'A Z': 3,
                        'B X': 1, 'B Y': 5, 'B Z': 9,
                        'C X': 7, 'C Y': 2, 'C Z': 6}

# X = lose = 0, Y = draw = 3, Z = win = 6
# A= rock = 1, B = paper = 2, C = scissors = 3
dict_of_points_task2 = {'A X': 3, 'A Y': 4, 'A Z': 8,
                        'B X': 1, 'B Y': 5, 'B Z': 9,
                        'C X': 2, 'C Y': 6, 'C Z': 7}


def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(line.strip())
        return result


def evaluate_points(parsed_input, task1=True):
    sum_of_points = 0
    for line in parsed_input:
        sum_of_points += dict_of_points_task1[line] if task1 else dict_of_points_task2[line]
    return sum_of_points


prepared_file = read_file('day02.txt')
print("Task1: " + str(evaluate_points(prepared_file, True)))
print("Task2: " + str(evaluate_points(prepared_file, False)))
