import unittest

def hurdleRace(k, height):
    max_height = max(height)
    if k >= max_height:
        return 0
    return max_height - k


class testHurdleRace(unittest.TestCase):

    def testNoDoses(self):
        self.assertEqual(hurdleRace(3, [1, 2, 3]), 0)

    def testTwoDoses(self):
        self.assertEqual(hurdleRace(3, [1, 2, 5]), 2)


if __name__ == '__main__':
    unittest.main()
