import unittest

from rational_number import Rational, decimal_to_rational


class TestMethodsArithmetic(unittest.TestCase):

    def test_true_value1(self):
        self.assertTrue(Rational(1, 5))
        self.assertTrue(Rational(0, 5))
        self.assertTrue(Rational(-1, 5))
        self.assertTrue(Rational(1, -5))
        self.assertTrue(Rational(-1, -5))

    def test_wrong_value(self):
        with self.assertRaises(IOError):
            Rational(2, 0)
        with self.assertRaises(IOError):
            Rational(0, 0)
        with self.assertRaises(IOError):
            Rational(1.2, 2)
        with self.assertRaises(IOError):
            Rational(1, 1.2)

    def test_add(self):
        self.assertEqual(Rational(1, 1) + Rational(1, 1), Rational(2, 1))
        self.assertEqual(Rational(-1, 1) + Rational(1, 1), Rational(0, 1))
        self.assertEqual(Rational(1, -1) + Rational(1, 1), Rational(0, 1))
        self.assertEqual(Rational(-1, 1) + Rational(1, -1), Rational(-2, 1))
        self.assertEqual(Rational(0, 1) + Rational(0, 1), Rational(0, 1))
        self.assertEqual(Rational(55432, 55) + Rational(789, 4), Rational(265123, 220))

    def test_sub(self):
        self.assertEqual(Rational(1, 1) - Rational(1, 1), Rational(0, 1))
        self.assertEqual(Rational(-1, 1) - Rational(1, 1), Rational(-2, 1))
        self.assertEqual(Rational(1, -1) - Rational(1, 1), Rational(-2, 1))
        self.assertEqual(Rational(1, 1) - Rational(1, -1), Rational(2, 1))
        self.assertEqual(Rational(0, 1) - Rational(1, 1), Rational(-1, 1))
        self.assertEqual(Rational(55432, 55) - Rational(789, 4), Rational(178333, 220))

    def test_mul(self):
        self.assertEqual(Rational(1, 1) * Rational(1, 1), Rational(1, 1))
        self.assertEqual(Rational(2, 3) * Rational(2, 1), Rational(4, 3))
        self.assertEqual(Rational(-2, 3) * Rational(-2, 1), Rational(4, 3))
        self.assertEqual(Rational(2, -3) * Rational(2, 1), Rational(-4, 3))
        self.assertEqual(Rational(0, 3) * Rational(2, 1), Rational(0, 3))
        self.assertEqual(Rational(55432, 55) * Rational(789, 4), Rational(43735848, 220))

    def test_truediv(self):  # /
        self.assertEqual(Rational(1, 1) / Rational(1, 1), Rational(1, 1))
        self.assertEqual(Rational(2, 1) / Rational(-2, 1), Rational(-2, 2))
        self.assertEqual(Rational(6, 3) / Rational(3, 4), Rational(24, 9))
        with self.assertRaises(ZeroDivisionError):
            Rational(5, 1) / Rational(0, 1)
        self.assertEqual(Rational(55432, 55) / Rational(789, 4), Rational(221728, 43395))

    def test_floordiv(self):  # div
        self.assertEqual(Rational(1, 1) // Rational(1, 1), 1)
        self.assertEqual(Rational(2, 1) // Rational(-2, 1), -1)
        self.assertEqual(Rational(8, 3) // Rational(3, 4), 3)
        self.assertEqual(Rational(8, 3) // Rational(3, -4), -4)
        with self.assertRaises(ZeroDivisionError):
            Rational(5, 1) // Rational(0, 1)
        self.assertEqual(Rational(789, 4) // Rational(432, 55), 25)

    def test_mod(self):
        self.assertEqual(Rational(1, 1) % Rational(1, 1), 0)
        self.assertEqual(Rational(2, 1) % Rational(-2, 1), 0)
        self.assertEqual(Rational(8, 3) % Rational(3, 4), 5)
        self.assertEqual(Rational(8, 3) % Rational(3, -4), -4)
        with self.assertRaises(ZeroDivisionError):
            Rational(5, 1) % Rational(0, 1)
        self.assertEqual(Rational(789, 4) % Rational(432, 55), 195)

    def tests_compare(self):
        self.assertTrue(Rational(54, 2) == Rational(108, 4))
        self.assertTrue(Rational(54, 2) != Rational(104, 4))
        self.assertTrue(Rational(54, 2) <= Rational(108, 4))
        self.assertTrue(Rational(54, 2) >= Rational(104, 4))
        self.assertTrue(Rational(3, 2) > Rational(2, 3))
        self.assertFalse(Rational(3, 2) < Rational(2, 3))


class TestMethodsReduction(unittest.TestCase):
    def test_1(self):
        a = Rational(2, 2)
        a.reduction()
        self.assertEqual(a, Rational(1, 1))

    def test_2(self):
        a = Rational(145325, 55)
        a.reduction()
        self.assertEqual(a, Rational(29065, 11))

    def test_3(self):
        a = Rational(0, 55)
        a.reduction()
        self.assertEqual(a, Rational(0, 55))

    def test_4(self):
        a = Rational(111, 55)
        a.reduction()
        self.assertEqual(a, Rational(111, 55))


class TestMethodsConvert(unittest.TestCase):
    def test_to_decimal(self):
        self.assertEqual(Rational(4, 27).to_decimal_str(), "0.(148)")
        self.assertEqual(Rational(3, 27).to_decimal_str(), "0.(1)")
        self.assertEqual(Rational(-7, 27).to_decimal_str(), "-0.(259)")
        self.assertEqual(Rational(183498, 36).to_decimal_str(), "5097.1(6)")
        self.assertEqual(Rational(1, 3).to_decimal_str(), "0.(3)")
        self.assertEqual(Rational(5, -3).to_decimal_str(), "-1.(6)")
        self.assertEqual(Rational(-5, 5).to_decimal_str(), "-1.0")
        self.assertEqual(Rational(3870, 36).to_decimal_str(), "107.5")
        self.assertEqual(Rational(0, 36).to_decimal_str(), "0.0")
        with self.assertRaises(IOError):
            Rational(36, 0).to_decimal_str()

    def test_to_rational(self):
        self.assertEqual(decimal_to_rational("0.(148)"), Rational(4, 27))
        self.assertEqual(decimal_to_rational("0.(1)"), Rational(3, 27))
        self.assertEqual(decimal_to_rational("-0.(259)"), Rational(-7, 27))
        self.assertEqual(decimal_to_rational("5097.1(6)"), Rational(91747, 18))
        self.assertEqual(decimal_to_rational("0.(3)"), Rational(1, 3))
        self.assertEqual(decimal_to_rational("-1.(6)"), Rational(5, -3))
        self.assertEqual(decimal_to_rational("-1.0"), Rational(-5, 5))
        self.assertEqual(decimal_to_rational("107.5"), Rational(3870, 36))
        self.assertEqual(decimal_to_rational("0.0"), Rational(0, 1))
        self.assertEqual(decimal_to_rational("0.1"), Rational(1, 10))
        self.assertEqual(decimal_to_rational("5.27"), Rational(527, 100))


if __name__ == '__main__':
    unittest.main()
