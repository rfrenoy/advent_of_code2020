import unittest
from io import StringIO
from day4 import read_input, missing_keys, passing_key_rule

class TestDay4(unittest.TestCase):
    def test_read_input_should_correctly_create_dicts_from_input(self):
        # Given
        inp = StringIO("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017

iyr:2013 ecl:amb

""")

        expected = [{'ecl': 'gry',
            'pid': '860033327',
            'eyr': 2020,
            'hcl': '#fffffd',
            'byr': 1937,
            'iyr': 2017},
            {'iyr': 2013,
                'ecl': 'amb'}]
        # When
        res = read_input(inp)

        # Then
        self.assertListEqual(res, expected)

    def test_missing_key_should_return_the_diff_between_keyset_and_dict_keys(self):
        # Given
        inp = {'byr': []}
        keyset = set(['byr', 'iyr'])
        expected = set(['iyr'])

        # When
        m = missing_keys(inp, keyset)

        #Then
        self.assertSetEqual(m, expected)

    def test_passsing_key_rule_should_return_true_when_no_missing_key_or_only_cid(self):
        # Given
        d = {'a': [], 'cid': 5}
        keyset_true = set(['a'])
        keyset_false = set(['b', 'cid'])

        # When
        t = passing_key_rule(d, keyset_true)
        f = passing_key_rule(d, keyset_false)

        # Then
        self.assertTrue(t)
        self.assertFalse(f)
