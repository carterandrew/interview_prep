"""Breadth-first and depth-first graph traversal implementations."""


def bfs(g, s):
  """Breadth-first search. Returns list of vertices in order traversed."""
  if s not in g.graph:
    return []

  visited = {s: 1}
  out = [s]
  q = []
  q.extend(g.graph[s])

  while q:
    n = q.pop(0)
    if n in visited:
      continue
    visited[n] = 1
    out.append(n)
    q.extend(g.graph[n])

  return out
  

def dfs(g, s):
  """Depth-first search. Returns list of vertices in order traversed."""
  if s not in g.graph:
    return []
    
  visited = {s: 1}
  out = [s]
  stack = []
  stack.extend(g.graph[s])
  
  while stack:
    n = stack.pop()
    if n in visited:
      continue
    visited[n] = 1
    out.append(n)
    stack.extend(g.graph[n])

  return out
