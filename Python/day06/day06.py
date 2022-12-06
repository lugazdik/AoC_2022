# link to source problem: https://adventofcode.com/2022/day/6

def read_file(path):
    with open(path, 'r') as file:
        return file.read().strip()


def find_last_index_of_n_distinct_characters(input_string, num_of_chars):
    for i in range(len(input_string) - num_of_chars + 1):
        if len(set(input_string[i:i+num_of_chars])) == num_of_chars:
            return i + num_of_chars


prepared_file = read_file('day06.txt')
print('Task1: ' + str(find_last_index_of_n_distinct_characters(prepared_file, 4)))
print('Task2: ' + str(find_last_index_of_n_distinct_characters(prepared_file, 14)))
