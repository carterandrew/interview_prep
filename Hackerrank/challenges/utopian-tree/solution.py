import unittest

def utopianTree(n):
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    return height


class testUtopianTree(unittest.TestCase):

    def testNoGrowth(self):
        self.assertEqual(utopianTree(0), 1)

    def testOneCycle(self):
        self.assertEqual(utopianTree(1), 2)

    def testFourCycles(self):
        self.assertEqual(utopianTree(4), 7)


if __name__ == '__main__':
    unittest.main()
