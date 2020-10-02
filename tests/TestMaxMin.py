import codewars_test as test
import Context
import MaxMin

@test.it("Max and Min")
def basic_tests():
  test.assert_equals(MaxMin.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");