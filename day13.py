import numpy as np

def read_file(buff):
    lines = buff.readlines()
    timestamp = int(lines[0])
    bus_ids = [x 
            if x[-1] != '\n' else x[:-1]
            for x in lines[1].split(',')]
    return timestamp, bus_ids

def modulos(divisor, values):
    return np.array([divisor % int(v)
            if v != 'x' else 0
            for v in values])

def solve1(timestamp, bus_ids):
    currated_bus_ids = np.array([int(x) if x != 'x' else 100000
            for x in bus_ids])
    time_to_wait = currated_bus_ids - modulos(timestamp, bus_ids)
    earliest_bus_idx = np.argmin(time_to_wait)
    return time_to_wait[earliest_bus_idx] * currated_bus_ids[earliest_bus_idx]

def check_timestamp(timestamp, value, offset):
    return (timestamp + offset) % value == 0

def currated_bus_ids_and_offsets(bus_ids):
    offsets = list(np.arange(len(bus_ids)))
    x_indices = np.argwhere(np.array(bus_ids) == 'x').flatten()
    for x in x_indices:
        offsets.remove(x)
    currated_ids = np.array([int(x) for x in bus_ids if x != 'x'])
    return currated_ids, np.array(offsets)

def solve2(bus_ids):
    currated, offsets = currated_bus_ids_and_offsets(bus_ids)
    timestamp = 0
    while True:
        check = check_timestamp(timestamp, currated, offsets)
        if check.all():
            return timestamp
        else:
            if check.any():
                timestamp += np.lcm.reduce(currated[check])
            else:
                timestamp += 1

if __name__ == '__main__':
    with open('data/day13.txt', 'r') as in_f:
        t, ids = read_file(in_f)
        print(solve1(t, ids))
        print(solve2(ids))
