def read_input(in_f):
    res = []
    group = []
    for line in  in_f.readlines():
        if line != '\n':
            group.append({l for l in line[:-1]})
        else:
            res.append(group)
            group = []
    return res

def _solution(groups, func):
    return sum(len(func(*g)) for g in groups)

def first_solution(groups):
    return _solution(groups, set.union)

def second_solution(groups):
    return _solution(groups, set.intersection)


if __name__ == '__main__':
    with open('data/day6.txt', 'r') as in_f:
        groups_answers = read_input(in_f)
        print(first_solution(groups_answers))
        print(second_solution(groups_answers))
