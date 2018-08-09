"""Breadth-first and depth-first graph traversal implementations."""


def bfs(g, s):
  if s not in g.graph:
    return None

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