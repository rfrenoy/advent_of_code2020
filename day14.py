import copy
import re
import numpy as np


def read_file(buff):
    for line in buff.readlines():
        line = line[:-1]
        if 'mask' in line:
            yield (-1, line.split(' ')[-1])
        else:
            memory_idx = int(line[line.find('[')+1:line.find(']')])
            value = int(line.split(' ')[-1])
            yield (memory_idx, value)


def update_string(s, idx, val):
    return s[:idx] + val + s[idx+1:]


def update(current_memory, mask, value):
    bit_repr = format(current_memory, 'b').zfill(36)
    bit_value = format(value, 'b').zfill(36)
    for i, mask_value in enumerate(mask):
        if mask_value == 'X':
            bit_repr = update_string(bit_repr, i, bit_value[i])
        else:
            bit_repr = update_string(bit_repr, i, mask_value)
    return int(bit_repr, base=2)


def update2(mem_idx, mask, value):
    bit_repr = format(mem_idx, 'b').zfill(36)
    for i, mask_value in enumerate(mask):
        if mask_value == '0':
            continue
        elif mask_value == '1':
            bit_repr = update_string(bit_repr, i, '1')
        else:
            bit_repr = update_string(bit_repr, i, mask_value)
    res = []
    nbit_repr = np.array([x for x in bit_repr])
    xs = np.argwhere(nbit_repr == 'X').flatten()
    possible_values = [format(i, 'b').zfill(len(xs)) for i in range(2**len(xs))]
    for pb in possible_values:
        a = copy.copy(nbit_repr)
        for i, x in enumerate(xs):
            a[x] = pb[i]
        res.append(''.join(list(a)))
    return [int(x, base=2) for x in res]


if __name__ == '__main__':
    memory1 = [0] * 100000
    memory2 = dict()
    mask = ''
    with open('data/day14.txt', 'r') as in_f:
        for mem_idx, value in read_file(in_f):
            if mem_idx == -1:
                mask = value
            else:
                memory1[mem_idx] = update(memory1[mem_idx], mask, value)
                for address in update2(mem_idx, mask, value):
                    memory2[address] = value
    print(sum(memory1))
    print(sum(list(memory2.values())))
