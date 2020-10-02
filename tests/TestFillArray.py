import codewars_test as test
import Context
import FillArray

@test.it("Filling an array Tests")
def basic_tests():
    test.assert_equals(FillArray.arr(4), [0,1,2,3])
    test.assert_equals(FillArray.arr(0), [])
    test.assert_equals(FillArray.arr(), [])
