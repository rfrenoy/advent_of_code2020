import numpy as np
import math

def divide(values, front_or_back):
    if front_or_back in ['L', 'F']:
        return values[:math.ceil(int(len(values)/2))]
    elif front_or_back in ['R', 'B']:
        return values[int(len(values)/2):]

def which_seat(vals):
    nb_values = 128 if vals[0] in ['F', 'B'] else 8
    seat_ids = np.arange(nb_values)
    for val in vals:
        seat_ids = divide(seat_ids, val)
    return seat_ids

def seat_from_str(s):
    row = which_seat(s[:7])[0]
    column = which_seat(s[7:])[0]
    return row * 8 + column


if __name__ == '__main__':
    with open('data/day5.txt', 'r') as in_f:
        seats = [seat_from_str(line[:-1]) for line in in_f.readlines() if line != '\n']
    print(max(seats))
    print(set(set(np.arange(85, 884)).difference(seats)))
