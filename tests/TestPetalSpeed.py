import codewars_test as test
import Context
import PetalSpeed

@test.it("Petals time")
def basic_tests():
    test.assert_approx_equals(PetalSpeed.time(5), 80)
    test.assert_approx_equals(PetalSpeed.time(10), 40)
    test.assert_approx_equals(PetalSpeed.time(-1), 0)
