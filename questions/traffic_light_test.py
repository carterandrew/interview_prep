import unittest

import traffic_light

R = traffic_light.RED
G = traffic_light.GREEN
Y = traffic_light.YELLOW


class TestTrafficLight(unittest.TestCase):

  def testTick(self):
    state_map = {R: (G, 1)}
    light = traffic_light.Light('EW', R, 0, state_map)
    self.assertEqual(light.state, R)
    light.tick()
    self.assertEqual(light.state, G)
    self.assertEqual(light.time_in_state, 0)

  def testInvalidTimeInState(self):
    state_map = {R: (G, 1)}
    with self.assertRaises(AssertionError):
      light = traffic_light.Light('EW', R, -1)

    with self.assertRaises(AssertionError):
      light = traffic_light.Light('EW', R, 2, state_map)


class TestIntersection(unittest.TestCase):

  def testTick(self):
    state_map = {R: (G, 1), G: (R, 1)}
    light1 = traffic_light.Light('EW', R, 0, state_map)
    light2 = traffic_light.Light('EW', G, 0, state_map)
    intersection = traffic_light.Intersection(light1, light2)
    self.assertEqual(intersection.light1.state, R)
    self.assertEqual(intersection.light2.state, G)
    intersection.tick()
    self.assertEqual(intersection.light1.state, G)
    self.assertEqual(intersection.light2.state, R)

  def testTickInvalidState(self):
    state_map = {R: (G, 1), G: (R, 1)}
    allowable_states = {R: (G,), G: (G,)}
    light1 = traffic_light.Light('EW', R, 0, state_map)
    light2 = traffic_light.Light('EW', G, 0, state_map)
    intersection = traffic_light.Intersection(light1, light2, allowable_states)
    with self.assertRaises(traffic_light.InvalidLightStateError):
      intersection.tick()
    

if __name__ == '__main__':
  unittest.main()
