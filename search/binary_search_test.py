import random
import unittest

import binary_search

SEARCH_METHODS = (binary_search.iterative_s, binary_search.recursive_s)


class TestBinarySearch(unittest.TestCase):

  def testSearchEmptyList(self):
    l = []
    for search in SEARCH_METHODS:
      self.assertIsNone(search(l, 1))

  def testSearchSingleElement(self):
    l = [1]
    for search in SEARCH_METHODS:
      self.assertIsNone(search(l, 0))
      self.assertEqual(search(l, 1), 0)
      self.assertIsNone(search(l, 2))

  def testSearchTwoElements(self):
    l = [1, 2]
    for search in SEARCH_METHODS:
      self.assertIsNone(search(l, 0))
      self.assertEqual(search(l, 1), 0)
      self.assertEqual(search(l, 2), 1)
      self.assertIsNone(search(l, 3))

  def testSearchThreeElements(self):
    l = [1, 2, 3]
    for search in SEARCH_METHODS:
      self.assertIsNone(search(l, 0))
      self.assertEqual(search(l, 1), 0)
      self.assertEqual(search(l, 2), 1)
      self.assertEqual(search(l, 3), 2)
      self.assertIsNone(search(l, 4))

  def testSearchLargeRandomList(self):
    l = []
    used = {}
    for i in range(1000000):
      k = random.randint(1, 100000000)
      while k in used:
        k = random.randint(1, 100000000)
      used[k] = 1
      l.append(k)
    l = sorted(l)
    for search in SEARCH_METHODS:
      self.assertIsNone(search(l, 0))
      i = random.randint(0, len(l))
      x = l[i]
      self.assertEqual(search(l, x), i)
      self.assertIsNone(search(l, 100001))


if __name__ == '__main__':
  unittest.main()