"""Simulates two traffic lights in an intersection.

Light cycle is:
  Green: 10 seconds
  Yellow: 2 seconds
  Red: 2 seconds (overlap with other light)
"""

RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'

STATE_MAP = {
    GREEN: (YELLOW, 10),
    YELLOW: (RED, 2),
    RED: (GREEN, 16),
}
ALLOWABLE_PAIRS = {
    GREEN: (RED,),
    YELLOW: (RED,),
    RED: (GREEN, YELLOW, RED),
}


class InvalidLightStateError(Exception):
  """Thrown if a light is not in an allowable state."""


class Light(object):

  def __init__(self, name, state, time_in_state, state_map=None):
    if not state_map:
      state_map = STATE_MAP
    assert time_in_state >= 0
    assert time_in_state < state_map[state][1]
    self.state_map = state_map
    self.name = name
    self.state = state
    self.time_in_state = time_in_state

  def tick(self):
    next_state, change_time = self.state_map[self.state]
    
    self.time_in_state += 1
    if self.time_in_state == change_time:
      self.state = next_state
      self.time_in_state = 0

  def __repr__(self):
    return '%s: %s for %s seconds' % (
        self.name, self.state, self.time_in_state)


class Intersection(object):

  def __init__(self, light1, light2, allowable_pairs=None):
    if not allowable_pairs:
      allowable_pairs = ALLOWABLE_PAIRS
    self.allowable_pairs = allowable_pairs
    self.light1 = light1
    self.light2 = light2

  def tick(self):
    self.light1.tick()
    self.light2.tick()
    if (self.light1.state not in self.allowable_pairs[self.light2.state] or
        self.light2.state not in self.allowable_pairs[self.light1.state]):
      raise InvalidLightStateError(self.__repr__())


  def __repr__(self):
    return '%s %s' % (str(self.light1), str(self.light2))


def main():
  light1 = Light('N/S', RED, 0)
  light2 = Light('E/W', RED, 14)
  intersection = Intersection(light1, light2)

  for t in range(60):
    print('%d -- %s' % (t, str(intersection))) 
    intersection.tick()


if __name__ == '__main__':
  main()
