import Context
import Operations
import codewars_test as Test

Test.it("Basic tests")
Test.assert_equals(Operations.sumar(1, 2),3)
Test.assert_equals(Operations.sumar(2, 2),4)
Test.assert_equals(Operations.restar(1, 2),-1)
Test.assert_equals(Operations.restar(1, 7),-6)
