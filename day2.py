def read_input_line(line):
    a, b = line.split(':')
    password = b.strip()
    aa = a.split(' ')
    policy_char = aa[1]
    policy_values = [int(x) for x in aa[0].split('-')]
    return (password, policy_char, *policy_values)

def satisfy_policy1(password, policy_char, l, h):
    return l <= password.count(policy_char) <= h

def satisfy_policy2(password, policy_char, l, h):
    a = password[l-1] == policy_char
    b = password[h-1] == policy_char
    return sum((a, b)) == 1


if __name__ == '__main__':
    with open('data/day2.txt', 'r') as in_f:
        lines = list(in_f.readlines())
        print(sum([satisfy_policy1(*read_input_line(line)) for line in lines]))
        print(sum([satisfy_policy2(*read_input_line(line)) for line in lines]))

