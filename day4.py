def read_input(buf):
    res = []
    d = dict()
    for line in buf.readlines():
        line = line[:-1]
        if line == '':
            res.append(d)
            d = dict()
        else:
            for full_elt in line.split(' '):
                divided_elt = full_elt.split(':')
                if len(divided_elt) == 2:
                    key = divided_elt[0]
                    val = divided_elt[1]
                    if key != 'pid':
                        try:
                            val = int(val)
                        except:
                            pass
                    d[key] = val
    return res

def missing_keys(d, keyset):
    return keyset.difference(set(d.keys()))

def passing_key_rule(d, keyset):
    return missing_keys(d, keyset) in [set(['cid']), set()]

def is_four_digits(s):
    return len(str(s)) == 4

def passing_byr_rule(byr):
    return is_four_digits(byr) and 1920 <= byr <= 2002

def passing_iyr_rule(iyr):
    return is_four_digits(iyr) and 2010 <= iyr <= 2020

def passing_eyr_rule(eyr):
    return is_four_digits(eyr) and 2020 <= eyr <= 2030

def is_int(val):
    try:
        int(val)
        return True
    except:
        return False

def passing_hgt_rule(hgt):
    if not isinstance(hgt, str):
        return False
    if len(hgt) < 3:
        return False
    hgt_prefix = hgt[-2:]
    hgt_val = hgt[:-2]
    if hgt_prefix not in ['cm', 'in']:
        return False
    if not is_int(hgt_val):
        return False
    hgt_val = int(hgt_val)
    if hgt_prefix == 'cm':
        return 150 <= hgt_val <= 193
    if hgt_prefix == 'in':
        return 59 <= hgt_val <= 76
    return True

def passing_hcl_rule(hcl):
    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False
    for l in hcl[1:]:
        if not (ord('a') <= ord(l) <= ord('f')) and not (ord('0') <= ord(l) <= ord('9')):
            return False
    return True

def passing_ecl_rule(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def passing_pid_rule(pid):
    if len(d['pid']) != 9:
        return False
    try:
        int(d['pid'])
    except:
        return False
    return True

def passport_passing_through2(d, keyset):
    return passing_key_rule(d, keyset) and passing_byr_rule(d['byr']) \
            and passing_iyr_rule(d['iyr']) and passing_eyr_rule(d['eyr']) \
            and passing_hgt_rule(d['hgt']) and passing_hcl_rule(d['hcl']) \
            and passing_ecl_rule(d['ecl']) and passing_pid_rule(d['pid'])


if __name__ == '__main__':
    keyset = set(['byr', 'iyr', 'hgt', 'cid',
            'ecl', 'pid', 'eyr', 'hcl'])
    with open('data/day4.txt', 'r') as in_f:
        dicts = read_input(in_f)
        res1 = 0
        res2 = 0
        for d in dicts:
            if passing_key_rule(d, keyset):
                res1 += 1
            if passport_passing_through2(d, keyset):
                res2 += 1

    print(res1, res2)
