# link to source problem: https://adventofcode.com/2022/day/1


def read_file(path):
    result = []
    with open(path, 'r') as file:
        elf_calories = []
        for line in file.readlines():
            if line == '\n':
                result.append(elf_calories)
                elf_calories = []
                continue
            else:
                elf_calories.append(int(line.strip()))
        return result


def task01(parsed_input):
    max_calories = 0
    for item in parsed_input:
        sum_of_calories = sum(item)
        if sum_of_calories > max_calories:
            max_calories = sum_of_calories
    return max_calories


def task02(parsed_input):
    sums_of_calories = []
    for item in parsed_input:
        sums_of_calories.append(sum(item))
    sums_of_calories = sorted(sums_of_calories, reverse=True)
    return sums_of_calories[0] + sums_of_calories[1] + sums_of_calories[2]


prepared_file = read_file('day01.txt')
print(prepared_file)
print(task01(prepared_file))
print(task02(prepared_file))
