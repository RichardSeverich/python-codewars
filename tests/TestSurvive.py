import codewars_test as test
import Context
import Survive

@test.it("Survive")
def basic_tests():
  test.assert_equals(Survive.hero(10, 5), True)
  test.assert_equals(Survive.hero(7, 4), False)
  test.assert_equals(Survive.hero(4, 5), False)
  test.assert_equals(Survive.hero(100, 40), True)
  test.assert_equals(Survive.hero(1500, 751), False)
  test.assert_equals(Survive.hero(0, 1), False)