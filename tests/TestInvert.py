import codewars_test as test
import Context
import Invert

@test.it("Invet")
def basic_tests():
  test.describe("Basic test")
  test.assert_equals(Invert.reverse_letter("krishan"),"nahsirk")
  test.assert_equals(Invert.reverse_letter("ultr53o?n"),"nortlu")
  test.assert_equals(Invert.reverse_letter("ab23c"),"cba")
  test.assert_equals(Invert.reverse_letter("krish21an"),"nahsirk")