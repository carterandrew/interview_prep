import unittest

def appendAndDelete(s, t, k):
    out = ''
    i = 0
    # have i characters matching the start of both strings
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    moves = 0
    # Need to delete at LEAST this many
    moves += len(s) - i
    moves_left = k - moves
    to_add = len(t) - i

    if moves_left > to_add and (moves_left - to_add) % 2 == 0:
        return 'Yes'
    elif (moves_left - to_add) >= i * 2:
        return 'Yes'
    elif moves_left == len(t) - i:
        return 'Yes'
    return 'No'


class TestAppendAndDelete(unittest.TestCase):

    def testCase0(self):
        self.assertEqual(appendAndDelete('hackerhappy', 'hackerrank', 9), 'Yes')

    def testCase1(self):
        self.assertEqual(appendAndDelete('aba', 'aba', 7), 'Yes')


if __name__ == '__main__':
    unittest.main()
