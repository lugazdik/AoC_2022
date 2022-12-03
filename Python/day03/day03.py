# link to source problem: https://adventofcode.com/2022/day/2

def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(line.strip())
        return result


# a to z = 1-26, A to Z = 27-52
def find_priority(character):
    return ord(character) - ord('A') + 27 if character.isupper() else ord(character) - ord('a') + 1


def task01(parsed_input):
    sum_of_priorities = 0
    for line in parsed_input:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        same_character = set(first_half).intersection(set(second_half)).pop()
        sum_of_priorities += find_priority(same_character)
    return sum_of_priorities


def task02(parsed_input):
    sum_of_priorities = 0
    for i in range(0, len(parsed_input), 3):
        same_character = set(parsed_input[i]).intersection(set(parsed_input[i+1])).intersection(set(parsed_input[i+2])).pop()
        sum_of_priorities += find_priority(same_character)
    return sum_of_priorities


prepared_file = read_file('day03.txt')
print('Task1: ' + str(task01(prepared_file)))
print('Task2: ' + str(task02(prepared_file)))
