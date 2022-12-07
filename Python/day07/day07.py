# link to source problem: https://adventofcode.com/2022/day/7

class MyDirectory:

    def __init__(self, name='', size=0, parent=None, contents=[]):
        self.name = name
        self.size = size
        self.parent = parent
        self.contents = contents

    def update_size(self):
        content_size = 0
        for item in self.contents:
            content_size += item.size
        if self.size < content_size:
            self.size = content_size

    def insert_file_or_dir(self, item):
        self.size += item.size
        self.contents.append(item)


def read_file(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(line.strip().split(' '))
    return result


def build_tree(instructions):
    root = MyDirectory('/')
    current_dir = root
    for entry in instructions:
        if entry[0] == '$':
            if entry[1] == 'cd':
                if entry[2] == '/':
                    # go to root
                    current_dir = root
                elif entry[2] == '..':
                    # go to parent
                    current_dir = current_dir.parent
                    current_dir.update_size()
                else:
                    # go to entry[2]
                    for item in current_dir.contents:
                        if item.name == entry[2]:
                            current_dir = item
            elif entry[1] == 'ls':
                # list dirs, maybe empty?
                pass
        elif entry[0] == 'dir':
            # directory, entry[1] = name
            dir_already_exist = False
            for item in current_dir.contents:
                if item.name == entry[1]:
                    dir_already_exist = True
                    break
            if not dir_already_exist:
                new_dir = MyDirectory(entry[1], 0, current_dir, [])
                current_dir.insert_file_or_dir(new_dir)
        else:
            # file: entry[0] = size, entry[1] = name
            file_already_exist = False
            for item in current_dir.contents:
                if item.name == entry[1]:
                    file_already_exist = True
                    break
            if not file_already_exist:
                new_file = MyDirectory(entry[1], int(entry[0]), current_dir, [])
                current_dir.insert_file_or_dir(new_file)
    return root


def print_tree(node, start_string):
    print(start_string, node.name, node.size, len(node.contents))
    for item in node.contents:
        print_tree(item, '  ' + start_string)


def find_dirs_bellow_limit(node, size_limit):
    result = 0
    for item in node.contents:
        if len(item.contents) != 0 and item.size <= size_limit:
            result += item.size
        result += find_dirs_bellow_limit(item, size_limit)
    return result


def find_dir_to_delete(node, required_size):
    # find smallest size bigger than required_size
    smallest_size = node.size if node.size > required_size else None
    for item in node.contents:
        if len(item.contents) != 0:
            if required_size <= item.size < smallest_size:
                smallest_size = item.size
            tmp = find_dir_to_delete(item, required_size)
            if tmp and tmp < smallest_size:
                smallest_size = tmp
    return smallest_size


prepared_file = read_file('day07.txt')
dir_root = build_tree(prepared_file)
dir_root.update_size()
# print_tree(dir_root, '-')
print(f'Task01: {find_dirs_bellow_limit(dir_root, 100000)}')
print(f'Task02: {find_dir_to_delete(dir_root, (dir_root.size + 30000000) - 70000000)}')
