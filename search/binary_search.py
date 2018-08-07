"""Binary search implementations."""


def iterative_s(l, x):
  """Searches for x in sorted list l, returning the index of x or None.

  Assumes that l only contains distinct values. If l contains duplicate x
  values then an arbitrary matching index will be returned.

  Iterative implementation.
  """
  if not l:
    return
  if len(l) == 1:
    return 0 if l[0] == x else None

  low = 0
  high = len(l) - 1
  mid = (high - low) // 2

  while low <= high:
    if x > l[mid]:
      low = mid + 1
    elif x < l[mid]:
      high = mid - 1
    else:
      return mid
    mid = low + ((high - low) // 2)


def recursive_s(l, x, low=None, high=None, mid=None):
  """Searches for x in sorted list l, returning the index of x or None.

  Assumes that l only contains distinct values. If l contains duplicate x
  values then an arbitrary matching index will be returned.

  Recursive implementation.
  """
  if not l:
    return
  if len(l) == 1:
    return 0 if l[0] == x else None

  if low is None:
    low = 0
  if high is None:
    high = len(l) - 1
  if mid is None:
    mid = (high - low) // 2

  if low > high:
    return
  if x > l[mid]:
    low = mid + 1
    return recursive_s(l, x, low, high, low + ((high - low) // 2))
  elif x < l[mid]:
    high = mid - 1
    return recursive_s(l, x, low, high, low + ((high - low) // 2))
  else:
    return mid