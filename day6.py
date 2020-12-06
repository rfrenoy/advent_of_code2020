def read_input(in_f):
    return [[set(l) for l in person_answer.split('\n')]
            for person_answer in in_f.read().split('\n\n')]

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
