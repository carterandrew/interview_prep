"""In-order, pre-order, and post-order tree traversal."""

class Node(object):

  def __init__(self, val):
    self.left = None
    self.right = None
    self.value = val


def inOrder(root):
  if not root:
    return
  out = []
  l = inOrder(root.left)
  if l:
    out.extend(l)
  out.append(root.value)
  r = inOrder(root.right)
  if r:
    out.extend(r)
  return out


def preOrder(root):
  if not root:
    return
  out = [root.value]
  l = preOrder(root.left)
  if l:
    out.extend(l)
  r = preOrder(root.right)
  if r:
    out.extend(r)
  return out


def postOrder(root):
  if not root:
    return
  out = []
  l = postOrder(root.left)
  if l:
    out.extend(l)
  r = postOrder(root.right)
  if r:
    out.extend(r)
  out.append(root.value)
  return out