import unittest

def surfaceArea(A):
    rows = len(A)
    cols = len(A[0])
    top = rows * cols
    bottom = top
    left = 0
    for r in range(rows):
        prev = 0
        for c in range(cols):
            if A[r][c] > prev:
                left += A[r][c] - prev
            prev = A[r][c]
    right = left
    front = 0
    for c in range(cols):
        prev = 0
        for r in range(rows):
            if A[r][c] > prev:
                front += A[r][c] - prev
            prev = A[r][c]
    back = front
    return bottom + top + left + right + front + back

class TestSurfaceArea(unittest.TestCase):

    def testCase0(self):
        self.assertEqual(surfaceArea([[1]]), 6)

    def testCase1(self):
        A = [[1, 3, 4],
             [2, 2, 3],
             [1, 2, 4]]
        self.assertEqual(surfaceArea(A), 60)


if __name__ == '__main__':
    unittest.main()
