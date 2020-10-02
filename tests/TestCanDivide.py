import codewars_test as test
import Context
import CanDivide

@test.it("Can divide")
def basic_tests():
  test.assert_equals(CanDivide.is_divide_by(-12, 2, -6), True)
  test.assert_equals(CanDivide.is_divide_by(-12, 2, -5), False)
  test.assert_equals(CanDivide.is_divide_by(45, 1, 6), False)
  test.assert_equals(CanDivide.is_divide_by(45, 5, 15), True)
  test.assert_equals(CanDivide.is_divide_by(4, 1, 4), True)
  test.assert_equals(CanDivide.is_divide_by(15, -5, 3), True)
