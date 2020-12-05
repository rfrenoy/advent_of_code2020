import numpy as np
import math

def which_seat(vals):
    s = vals.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(f'0b{s}', 2)

def seat_from_str(s):
    return which_seat(s[:7]) * 8 + which_seat(s[7:])

if __name__ == '__main__':
    with open('data/day5.txt', 'r') as in_f:
        seats = [seat_from_str(line[:-1]) for line in in_f.readlines() if line != '\n']
    print(max(seats))
    print(set(set(np.arange(85, 884)).difference(seats)))
