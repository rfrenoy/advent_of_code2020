def read_file(buff):
    return [int(x) for x in buff.readlines()]


def is_sum(numbers, idx, preamble):
    for i in range(idx - preamble, idx - 1):
        for j in range(idx - preamble + 1, idx):
            if numbers[i] + numbers[j] == numbers[idx]:
                return True
    return False


def solve1(numbers, preamble):
    for idx in range(preamble, len(numbers)):
        if not is_sum(numbers, idx, preamble):
            return numbers[idx]


def solve2(numbers, target):
    for i, curr_nb in enumerate(numbers):
        used = [curr_nb]
        for next_nb in numbers[i+1:]:
            used.append(next_nb)
            res = sum(used)
            if res == target:
                return min(used) + max(used)
            if res > target:
                break


if __name__ == '__main__':
    with open('data/day9.txt', 'r') as in_f:
        PREAMBLE = 25
        numbers = read_file(in_f)
        res1 = solve1(numbers, PREAMBLE)
        res2 = solve2(numbers, res1)
        print(res1, res2)
