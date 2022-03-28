import unittest
from ..calc import do_calculation
from ..operators import Operator


class TestCalculations(unittest.TestCase):

    def test_add(self):
        op, num1, num2, result = do_calculation('add 2 5')
        self.assertEqual(op, Operator.ADD)
        self.assertEqual(num1, 2)
        self.assertEqual(num2, 5)
        self.assertEqual(result, 7)

        op, num1, num2, result = do_calculation('ADD 100 -5')
        self.assertEqual(op, Operator.ADD)
        self.assertEqual(num1, 100)
        self.assertEqual(num2, -5)
        self.assertEqual(result, 95)

        op, num1, num2, result = do_calculation('ADD sdf')
        self.assertEqual(result, '')

    def test_sub(self):
        op, num1, num2, result = do_calculation('sub 12.4 0.4')
        self.assertEqual(op, Operator.SUB)
        self.assertEqual(num1, 12.4)
        self.assertEqual(num2, 0.4)
        self.assertEqual(result, 12.0)

        op, num1, num2, result = do_calculation('SUB 0.2 -0.8')
        self.assertEqual(op, Operator.SUB)
        self.assertEqual(num1, 0.2)
        self.assertEqual(num2, -0.8)
        self.assertEqual(result, 1.0)

        op, num1, num2, result = do_calculation('sub 1 2 3')
        self.assertEqual(result, '')

    def test_mul(self):
        op, num1, num2, result = do_calculation('mul 3 4')
        self.assertEqual(op, Operator.MUL)
        self.assertEqual(num1, 3)
        self.assertEqual(num2, 4)
        self.assertEqual(result, 12)

        op, num1, num2, result = do_calculation('MUL 15 -0.5')
        self.assertEqual(op, Operator.MUL)
        self.assertEqual(num1, 15)
        self.assertEqual(num2, -0.5)
        self.assertEqual(result, -7.5)

        op, num1, num2, result = do_calculation('mul 1 2sdf')
        self.assertEqual(result, '')

    def test_truediv(self):
        op, num1, num2, result = do_calculation('truediv 14 2')
        self.assertEqual(op, Operator.TRUEDIV)
        self.assertEqual(num1, 14)
        self.assertEqual(num2, 2)
        self.assertEqual(result, 7)

        op, num1, num2, result = do_calculation('TRUEDIV 1 3')
        self.assertAlmostEqual(result, 0.33333333)

        op, num1, num2, result = do_calculation('TRUEDIV 100 0')
        self.assertEqual(result, '')

    def test_floordiv(self):
        op, num1, num2, result = do_calculation('floordiv 123 100')
        self.assertEqual(op, Operator.FLOORDIV)
        self.assertEqual(num1, 123)
        self.assertEqual(num2, 100)
        self.assertEqual(result, 1)

        op, num1, num2, result = do_calculation('FLOORDIV 100 0')
        self.assertEqual(result, '')

    def test_pow(self):
        op, num1, num2, result = do_calculation('pow 3.2 3')
        self.assertEqual(op, Operator.POW)
        self.assertEqual(num1, 3.2)
        self.assertEqual(num2, 3)
        self.assertAlmostEqual(result, 32.768)

        op, num1, num2, result = do_calculation('POW 64 0.5')
        self.assertEqual(result, 8)

        op, num1, num2, result = do_calculation('POW 64 -0.5')
        self.assertEqual(result, 0.125)

    def test_mod(self):
        op, num1, num2, result = do_calculation('mod 123 120')
        self.assertEqual(op, Operator.MOD)
        self.assertEqual(num1, 123)
        self.assertEqual(num2, 120)
        self.assertEqual(result, 3)

        op, num1, num2, result = do_calculation('MOD 3 10')
        self.assertEqual(result, 3)

        op, num1, num2, result = do_calculation('MOD 3 0')
        self.assertEqual(result, '')

    def test_copysign(self):
        op, num1, num2, result = do_calculation('copysign 3 5')
        self.assertEqual(op, Operator.COPYSIGN)
        self.assertEqual(num1, 3)
        self.assertEqual(num2, 5)
        self.assertEqual(result, 3)

        op, num1, num2, result = do_calculation('copysign 3 -5')
        self.assertEqual(result, -3)

        op, num1, num2, result = do_calculation('COPYSIGN -3 -5')
        self.assertEqual(result, -3)

    def test_log(self):
        op, num1, num2, result = do_calculation('log 16 2')
        self.assertEqual(op, Operator.LOG)
        self.assertEqual(num1, 16)
        self.assertEqual(num2, 2)
        self.assertEqual(result, 4)

        op, num1, num2, result = do_calculation('LOG 16 16')
        self.assertEqual(result, 1)

        op, num1, num2, result = do_calculation('LOG -16 4')
        self.assertEqual(result, '')

        op, num1, num2, result = do_calculation('LOG 16 1')
        self.assertEqual(result, '')

        op, num1, num2, result = do_calculation('LOG 16 -4')
        self.assertEqual(result, '')

    def test_hypot(self):
        op, num1, num2, result = do_calculation('hypot 4 3')
        self.assertEqual(op, Operator.HYPOT)
        self.assertEqual(num1, 4)
        self.assertEqual(num2, 3)
        self.assertEqual(result, 5)

        op, num1, num2, result = do_calculation('HYPOT 6 8')
        self.assertEqual(result, 10)

        op, num1, num2, result = do_calculation('HYPOT 0 0')
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()