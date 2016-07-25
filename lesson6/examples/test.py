import unittest
from my_code import square

class TestSquare(unittest.TestCase):
  def test_one(self):
      self.assertEqual(square(1), 1)

  def test_negative(self):
      self.assertEqual(square(-3), 9)

  def test_five(self):
      self.assertEqual(square(5), 25)

if __name__ == '__main__':
    unittest.main()
