class Graph(object):
  """Represents a graph using an adjacency list."""
  
  def __init__(self):
    self.graph = {}
    
  def addEdge(self, s, e):
    if s not in self.graph:
      self.graph[s] = []
    if e is None:
      return
    if e not in self.graph:
      self.graph[e] = []
    self.graph[s].append(e)