import copy

def read_file(buff):
    res = []
    for line in buff.readlines():
        action = line.split(' ')[0]
        sign = line[4]
        value = int(line[5:])
        res.append([action, sign, value, False])
    return res


def jump(sign, value):
    if sign == '+':
        return value
    else:
        return -value


def run(instructions):
    curr = 0
    res = 0
    instructions_copy = copy.deepcopy(instructions)
    while curr < len(instructions_copy):
        instruction = instructions_copy[curr]
        if instruction[3] == True:
            return res
        instruction[3] = True
        if instruction[0] == 'acc':
            res = res + jump(*instruction[1:3])
            curr = curr + 1
        elif instruction[0] == 'jmp':
            curr = curr + jump(*instruction[1:3])
        else:
            curr = curr + 1
    return res


def dry_run(instructions):
    curr = 0
    instructions_copy = copy.deepcopy(instructions)
    while curr < len(instructions_copy):
        instruction = instructions_copy[curr]
        if instruction[3] == True:
            return False
        instruction[3] = True
        if instruction[0] == 'jmp':
            curr = curr + jump(*instruction[1:3])
        else:
            curr = curr + 1
    return True


def brute_force(instructions):
    switcher = {'jmp': 'nop',
                'nop': 'jmp',
                'acc': 'acc'}
    for i in range(len(instructions)):
        instructions_copy = copy.deepcopy(instructions)
        instructions_copy[i][0] = switcher[instructions[i][0]]
        if dry_run(instructions_copy):
            return run(instructions_copy)

if __name__ == '__main__':
    with open('data/day8.txt', 'r') as in_f:
        instructions = read_file(in_f)
        print(run(instructions))
        print(brute_force(instructions))
