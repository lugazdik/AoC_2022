# link to source problem: https://adventofcode.com/2022/day/11
from math import lcm


def read_file(path):
    monkeys = []
    with open(path, 'r') as file:
        monkey = []
        for line in file.readlines():
            if line.strip() != '':
                monkey.append(line.strip())
            else:
                monkeys.append(monkey)
                monkey = []
        monkeys.append(monkey)
    return monkeys


def initialize_monkeys(parsed_file):
    monkeys = []
    for monkey in parsed_file:
        monkey_name = int(monkey[0].split(' ')[1].replace(':', ''))
        starting_items = list(map(int, (monkey[1].split(':')[1].split(', '))))
        operation = monkey[2].split('= ')[1]
        test = int(monkey[3].split(' ')[-1])
        if_true = int(monkey[4].split(' ')[-1])
        if_false = int(monkey[5].split(' ')[-1])
        monkeys.append(Monkey(monkey_name, starting_items, operation, test, if_true, if_false))
    return monkeys


class Monkey:

    def __init__(self, name, starting_items, operation, test, if_true, if_false):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_items = 0


def simulate_game(monkeys, num_of_rounds, relief_div, task1=True):
    for one_round in range(num_of_rounds):
        for monkey in monkeys:
            for item in monkey.items:
                new_value = eval(monkey.operation.replace('old', str(item)))
                relief_value = new_value // relief_div if task1 else new_value % relief_div
                if relief_value % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(relief_value)
                else:
                    monkeys[monkey.if_false].items.append(relief_value)
                monkey.inspected_items += 1
            monkey.items = []


def task01(monkeys, num_of_rounds):
    simulate_game(monkeys, num_of_rounds, 3)
    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.inspected_items)
    sorted_inspected_items = sorted(inspected_items, reverse=True)
    return sorted_inspected_items[0] * sorted_inspected_items[1]


def task02(monkeys, num_of_rounds):
    tests_divisions = []
    for monkey in monkeys:
        tests_divisions.append(monkey.test)
    least_common_multiple = lcm(*tests_divisions)
    simulate_game(monkeys, num_of_rounds, least_common_multiple, task1=False)
    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.inspected_items)
    sorted_inspected_items = sorted(inspected_items, reverse=True)
    return sorted_inspected_items[0] * sorted_inspected_items[1]


prepared_file = read_file('day11.txt')
my_monkeys = initialize_monkeys(prepared_file)
print(f'Task01: {task01(my_monkeys, 20)}')
print(f'Task02: {task02(my_monkeys, 10000)}')
