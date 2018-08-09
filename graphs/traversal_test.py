import unittest

import graph
import traversal


class TestBFSTraversal(unittest.TestCase):
  
  def setUp(self):
    self.g = graph.Graph()

  def testStartNotInGraph(self):
    self.g.addEdge(1, 2)
    self.assertEqual(traversal.bfs(self.g, 4), [])

  def testSingleNode(self):
    self.g.addEdge(1, None)
    self.assertEqual(traversal.bfs(self.g, 1), [1])
  
  def testTwoNodes(self):
    self.g.addEdge(1, 2)
    self.assertEqual(traversal.bfs(self.g, 1), [1, 2])
    self.assertEqual(traversal.bfs(self.g, 2), [2])

  def testThreeNodes(self):
    self.g.addEdge(1, 2)
    self.g.addEdge(1, 3)
    self.assertEqual(traversal.bfs(self.g, 1), [1, 2, 3])
    self.assertEqual(traversal.bfs(self.g, 2), [2])
    self.assertEqual(traversal.bfs(self.g, 3), [3])
    self.g.addEdge(2, 3)
    self.assertEqual(traversal.bfs(self.g, 1), [1, 2, 3])
    
  def testFourNodes(self):
    self.g.addEdge(0, 1)
    self.g.addEdge(0, 2)
    self.g.addEdge(1, 2)
    self.g.addEdge(2, 0)
    self.g.addEdge(2, 3)
    self.g.addEdge(3, 3)
    self.assertEqual(traversal.bfs(self.g, 2), [2, 0, 3, 1])


class TestDFSTraversal(unittest.TestCase):
  
  def setUp(self):
    self.g = graph.Graph()

  def testStartNotInGraph(self):
    self.g.addEdge(1, 2)
    self.assertEqual(traversal.dfs(self.g, 4), [])

  def testSingleNode(self):
    self.g.addEdge(1, None)
    self.assertEqual(traversal.dfs(self.g, 1), [1])
  
  def testTwoNodes(self):
    self.g.addEdge(1, 2)
    self.assertEqual(traversal.dfs(self.g, 1), [1, 2])
    self.assertEqual(traversal.dfs(self.g, 2), [2])

  def testThreeNodes(self):
    self.g.addEdge(1, 2)
    self.g.addEdge(1, 3)
    self.assertEqual(traversal.dfs(self.g, 1), [1, 3, 2])
    self.assertEqual(traversal.dfs(self.g, 2), [2])
    self.assertEqual(traversal.dfs(self.g, 3), [3])
    self.g.addEdge(2, 3)
    self.assertEqual(traversal.dfs(self.g, 1), [1, 3, 2])
    
  def testFourNodes(self):
    self.g.addEdge(0, 1)
    self.g.addEdge(0, 2)
    self.g.addEdge(1, 2)
    self.g.addEdge(2, 0)
    self.g.addEdge(2, 3)
    self.g.addEdge(3, 3)
    self.assertEqual(traversal.dfs(self.g, 0), [0, 2, 3, 1])

if __name__ == '__main__':
  unittest.main()