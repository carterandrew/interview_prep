import unittest

def getMoneySpent(keyboards, drives, b):
    m = -1
    for k in keyboards:
        for d in drives:
            if k + d == b:
                return b
            elif k + d > m and k + d < b:
                m = k + d
    return m


class TestElectronicsShop(unittest.TestCase):

    def testCase0(self):
        self.assertEqual(getMoneySpent([3, 1], [5, 2, 8], 10), 9)

    def testCase1(self):
        self.assertEqual(getMoneySpent([4], [4], 5), -1)


if __name__ == '__main__':
    unittest.main()
