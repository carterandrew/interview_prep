import unittest

import traversal


class TestTreeTraversal(unittest.TestCase):

  def setUp(self):
    root = traversal.Node(1)
    root.left = traversal.Node(2)
    root.right = traversal.Node(3)
    root.left.left = traversal.Node(4)
    root.left.right = traversal.Node(5)
    root.right.left = traversal.Node(6)
    root.right.right = traversal.Node(7)
    self.root = root

  def testInOrder(self):
    self.assertEqual(traversal.inOrder(self.root), [4, 2, 5, 1, 6, 3, 7])

  def testPreOrder(self):
    self.assertEqual(traversal.preOrder(self.root), [1, 2, 4, 5, 3, 6, 7])

  def testPostOrder(self):
    self.assertEqual(traversal.postOrder(self.root), [4, 5, 2, 6, 7, 3, 1])


if __name__ == '__main__':
  unittest.main()