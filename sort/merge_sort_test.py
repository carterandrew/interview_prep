import random
import unittest

import merge_sort

class TestMergesort(unittest.TestCase):

  def testEmptyArray(self):
    self.assertIsNone(merge_sort.sort([]))

  def testSingleElementArray(self):
    arr = [1]
    self.assertEqual(merge_sort.sort(arr), arr)
  
  def testTwoElementArray(self):
    arr = [1, 2]
    self.assertEqual(merge_sort.sort(arr), arr)
    arr = [2, 1]
    self.assertEqual(merge_sort.sort(arr), [1, 2])

  def testThreeElementArray(self):
    arr = [1, 2, 3]
    arr_sorted = arr
    self.assertEqual(merge_sort.sort(arr), arr_sorted)
    arr = [3, 1, 2]
    self.assertEqual(merge_sort.sort(arr), arr_sorted)

  def testLargeArray(self):
    arr = [random.randint(0, 100000) for i in range(10000)]
    self.assertEqual(merge_sort.sort(arr), sorted(arr))


if __name__ == '__main__':
  unittest.main()