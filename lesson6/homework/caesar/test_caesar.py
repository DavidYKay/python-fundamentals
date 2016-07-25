import unittest
from caesar import cipher

class TestCaesar(unittest.TestCase):
  def test_abcd(self):
      self.assertEqual(cipher(3, "abcd"), "defg")

if __name__ == '__main__':
    unittest.main()
