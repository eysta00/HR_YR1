import unittest

def funky_time(x):
    return x + 1

class PIZZA_TIME(unittest.TestCase):

    def test_a_pizza(self):
        self.assertEqual(funky_time(3),5)


its_a_boy = PIZZA_TIME()
its_a_boy.test_a_pizza()