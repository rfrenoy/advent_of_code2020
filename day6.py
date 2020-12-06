def read_input(in_f):
    res = []
    group = dict()
    nb_answers = 0
    for line in  in_f.readlines():
        if line != '\n':
            nb_answers += 1
            for l in line[:-1]:
                if l in group:
                    group[l] = group[l] + 1
                else:
                    group[l] = 1
        else:
            res.append((nb_answers, group))
            group = dict()
            nb_answers = 0
    return res

def first_solution(arr_of_dicts):
    res = 0
    for _, d in arr_of_dicts:
        res += len(d.keys())
    return res

def second_solution(arr_of_dicts):
    res = 0
    for nb_answers, d in arr_of_dicts:
        answered_by_all = [x for x in d.keys() if d[x] == nb_answers]
        res += len(answered_by_all)
    return res


if __name__ == '__main__':
    with open('data/day6.txt', 'r') as in_f:
        groups_answers = read_input(in_f)
        print(first_solution(groups_answers))
        print(second_solution(groups_answers))
