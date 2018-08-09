"""Merge sort recursive implementation."""


def _merge(left, right):
  out = []
  l = left.pop(0)
  r = right.pop(0)
  while l is not None or r is not None:
    if r is None:
      out.append(l)
      out.extend(left)
      l = None
    elif l is None:
      out.append(r)
      out.extend(right)
      r = None
    elif l <= r:
      out.append(l)
      try:
        l = left.pop(0)
      except IndexError:
        l = None
    else:
      out.append(r)
      try:
        r = right.pop(0)
      except IndexError:
        r = None
  return out


def sort(arr):
  """Sorts using the merge sort algorithm."""
  if not arr:
    return None
  if len(arr) == 1:
    return arr

  mid = len(arr) // 2
  left = sort(arr[0:mid])
  right = sort(arr[mid:])
  return _merge(left, right)