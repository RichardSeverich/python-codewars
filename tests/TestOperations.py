import unittest
import Context
import Operations

class SumTest(unittest.TestCase):
  def test_Sumar(self):
    self.assertEqual(Operations.sumar(1, 1), 2)
    self.assertTrue(Operations.sumar(1, 2) == 3)

  def test_Restar(self):
    self.assertEqual(Operations.restar(1, 1), 0)
    self.assertTrue(Operations.restar(1, 2) == -1)

if __name__ == '__main__':
  unittest.main()
