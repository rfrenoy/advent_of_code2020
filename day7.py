import numpy as np


def read_file(buff):
    return [x.split('bags') for x in buff.readlines()]


def occurences_bigger_bag(lines, bag, bag_set=None):
    bag_set = bag_set or {}
    bigger_bags = []
    for line in lines:
        if bag in line and line.index(bag) > 0:
            bigger_bags.append(' '.join(line.split(' ')[:2]))
    occ = set(bag_set)
    for b in bigger_bags:
        occ = occ.union(occurences_bigger_bag(lines, b))
    return set(bigger_bags).union(set(occ))

def number_bags(lines, bag, res):
    for line in lines:
        if bag in line and line.index(bag) == 0:
            values = []
            colors = []
            splitted_line = line.split(' ')
            for i, w in enumerate(splitted_line):
                try:
                    values.append(int(w))
                    colors.append(' '.join([splitted_line[i+1], splitted_line[i+2]]))
                except:
                    continue
            if len(values) == 0:
                return 1
            return 1 + sum(np.multiply(values, [number_bags(lines, x, 0) for x in colors]))

if __name__ == '__main__':
    with open('data/dummy_day7.txt', 'r') as in_f:
        bag = 'vibrant plum'
        lines = in_f.readlines()
        print(len(occurences_bigger_bag(lines, bag)))
        print(number_bags(lines, bag, 0) -1)
