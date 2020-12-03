import math
import functools


def read_input(buff):
    return [x[:-1] for x in buff.readlines()][:-1]

def required_width(nb_lines, slope):
    return math.ceil((nb_lines) * slope + 1)

def _width(m):
    return len(m[0])

def _height(m):
    return len(m)

def duplicate_input(arr, multiplicator):
    res = []
    for line in arr:
        res.append(''.join(line * multiplicator))
    return res

def elements(mat, slope_down, slope_right):
    for i in range(1, _height(mat)):
        return ''.join([mat[slope_down * i][slope_right*i]
            for i in range(1, math.ceil(_height(mat)/slope_down))])

if __name__ == "__main__":
    with open('data/day3.txt', 'r') as in_f:
        f = read_input(in_f)
    res = []
    for slope_down, slope_right in ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1)):
        slope = slope_right / slope_down
        w, h = _width(f), _height(f)
        rw = required_width(h, slope)
        mul = math.ceil(rw / w)
        mat = duplicate_input(f, mul)
        w2, h2 = _width(mat), _height(mat)
        elts = elements(mat, slope_down, slope_right)
        res.append(elts.count('#'))
    print(functools.reduce(lambda a, b: a*b, res))
