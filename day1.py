import functools


def create_array(buf):
    return [int(x) for x in buf.split('\n') if x != '']

def sums_to_value(args, val):
    return sum(args) == val

def find_values_adding_up_to_value(arr, nb_values, val):
    if nb_values not in [2, 3]:
        raise NotImplemented('only available with nb_values of 2 and 3')

    if nb_values == 2:
        for i, first in enumerate(arr):
            for second in arr[i+1:]:
                if first + second == val:
                    return [first, second]
    if nb_values == 3:
        for i, first in enumerate(arr):
            for second in arr[i+1:]:
                for third in arr[i+2:]:
                    if first + second + third == val:
                        return [first, second, third]

    return None

if __name__ == "__main__":
    with open('data/day1.txt', 'r') as in_f:
        ar = create_array(in_f.read())
    vals = find_values_adding_up_to_value(ar, 3, 2020)
    if vals:
        print(functools.reduce(lambda a, b: a*b, vals))

