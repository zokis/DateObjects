import unittest

from datetime import date

from dateobjects import Date, Day, Month, Year


class TestDayOperations(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Day(1), Day(1))

    def test_ne(self):
        self.assertNotEqual(Day(1), Day(2))

    def test_lt(self):
        self.assertLess(Day(1), Day(2))

    def test_le(self):
        self.assertLessEqual(Day(1), Day(2))
        self.assertLessEqual(Day(2), Day(2))

    def test_gt(self):
        self.assertGreater(Day(2), Day(1))

    def test_ge(self):
        self.assertGreaterEqual(Day(2), Day(1))
        self.assertGreaterEqual(Day(2), Day(2))

    def test_is_first(self):
        self.assertTrue(Day(1).is_first())
        self.assertFalse(Day(2).is_first())

    def test_is_last(self):
        self.assertFalse(Day(1).is_last())
        self.assertTrue(Day(31).is_last())
        self.assertTrue(Day(28).is_last(month=Month(2)))
        self.assertTrue(Day(29).is_last(month=Month(2), year=Year(2020)))

    def test_invalid_day(self):
        self.assertRaises(ValueError, lambda: Day(0))
        self.assertRaises(ValueError, lambda: Day(32))


class TestMonthOperations(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Month(1), Month(1))

    def test_ne(self):
        self.assertNotEqual(Month(1), Month(2))

    def test_lt(self):
        self.assertLess(Month(1), Month(2))

    def test_le(self):
        self.assertLessEqual(Month(1), Month(2))
        self.assertLessEqual(Month(2), Month(2))

    def test_gt(self):
        self.assertGreater(Month(2), Month(1))

    def test_ge(self):
        self.assertGreaterEqual(Month(2), Month(1))
        self.assertGreaterEqual(Month(2), Month(2))

    def test_is_first(self):
        self.assertTrue(Month(1).is_first())
        self.assertFalse(Month(2).is_first())

    def test_is_last(self):
        self.assertFalse(Month(1).is_last())
        self.assertTrue(Month(12).is_last())

    def test_get_last_day(self):
        self.assertEqual(Month(1).get_last_day(), 31)
        self.assertEqual(Month(2).get_last_day(), 28)
        self.assertEqual(Month(2).get_last_day(year=Year(1991)), 28)
        self.assertEqual(Month(2).get_last_day(year=Year(1992)), 29)
        self.assertEqual(Month(3).get_last_day(), 31)
        self.assertEqual(Month(4).get_last_day(), 30)
        self.assertEqual(Month(5).get_last_day(), 31)
        self.assertEqual(Month(6).get_last_day(), 30)
        self.assertEqual(Month(7).get_last_day(), 31)
        self.assertEqual(Month(8).get_last_day(), 31)
        self.assertEqual(Month(9).get_last_day(), 30)
        self.assertEqual(Month(10).get_last_day(), 31)
        self.assertEqual(Month(11).get_last_day(), 30)
        self.assertEqual(Month(12).get_last_day(), 31)

    def test_invalid_month(self):
        self.assertRaises(ValueError, lambda: Month(0))
        self.assertRaises(ValueError, lambda: Month(13))


class TestYearOperations(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Year(1), Year(1))

    def test_ne(self):
        self.assertNotEqual(Year(1), Year(2))

    def test_lt(self):
        self.assertLess(Year(1), Year(2))

    def test_le(self):
        self.assertLessEqual(Year(1), Year(2))
        self.assertLessEqual(Year(2), Year(2))

    def test_gt(self):
        self.assertGreater(Year(2), Year(1))

    def test_ge(self):
        self.assertGreaterEqual(Year(2), Year(1))
        self.assertGreaterEqual(Year(2), Year(2))

    def test_is_leap(self):
        self.assertTrue(Year(2020).is_leap())
        self.assertTrue(Year(1992).is_leap())
        self.assertFalse(Year(1991).is_leap())


class TestDateOperations(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(Date(1991, 10, 25), Date(1991, 10, 25))

    def test_ne(self):
        self.assertNotEqual(Date(1991, 10, 25), Date(1992, 10, 25))
        self.assertNotEqual(Date(1991, 10, 25), Date(1991, 10, 26))
        self.assertNotEqual(Date(1991, 10, 25), Date(1991, 11, 25))

    def test_lt(self):
        self.assertFalse(Date(1991, 10, 25) < Date(1991, 10, 25))
        self.assertLess(Date(1991, 10, 25), Date(1992, 10, 25))
        self.assertLess(Date(1991, 10, 25), Date(1991, 10, 26))
        self.assertLess(Date(1991, 10, 25), Date(1991, 11, 25))

    def test_le(self):
        self.assertLessEqual(Date(1991, 10, 25), Date(1991, 10, 25))
        self.assertLessEqual(Date(1991, 10, 25), Date(1992, 10, 25))
        self.assertLessEqual(Date(1991, 10, 25), Date(1991, 10, 26))
        self.assertLessEqual(Date(1991, 10, 25), Date(1991, 11, 25))

    def test_gt(self):
        self.assertFalse(Date(1991, 10, 25) > Date(1991, 10, 25))
        self.assertGreater(Date(1991, 11, 25), Date(1991, 10, 25))
        self.assertGreater(Date(1991, 10, 26), Date(1991, 10, 25))
        self.assertGreater(Date(1992, 10, 25), Date(1991, 10, 25))

    def test_ge(self):
        self.assertGreaterEqual(Date(1991, 10, 25), Date(1991, 10, 25))
        self.assertGreaterEqual(Date(1991, 11, 25), Date(1991, 10, 25))
        self.assertGreaterEqual(Date(1991, 10, 26), Date(1991, 10, 25))
        self.assertGreaterEqual(Date(1992, 10, 25), Date(1991, 10, 25))

    def test_to_datetime(self):
        self.assertEqual(Date(1991, 10, 25).to_datetime(), date(1991, 10, 25))

    def test_get_last_day_of_month(self):
        self.assertEqual(Date(1991, 1, 1).get_last_day_of_month(), 31)
        self.assertEqual(Date(2020, 2, 1).get_last_day_of_month(), 29)
        self.assertEqual(Date(2021, 2, 1).get_last_day_of_month(), 28)
        self.assertEqual(Date(2021, 3, 1).get_last_day_of_month(), 31)
        self.assertEqual(Date(2021, 4, 1).get_last_day_of_month(), 30)
        self.assertEqual(Date(2021, 5, 1).get_last_day_of_month(), 31)
        self.assertEqual(Date(2021, 6, 1).get_last_day_of_month(), 30)
        self.assertEqual(Date(2021, 7, 1).get_last_day_of_month(), 31)
        self.assertEqual(Date(2021, 8, 1).get_last_day_of_month(), 31)
        self.assertEqual(Date(2021, 9, 1).get_last_day_of_month(), 30)
        self.assertEqual(Date(2021, 10, 1).get_last_day_of_month(), 31)
        self.assertEqual(Date(2021, 11, 1).get_last_day_of_month(), 30)
        self.assertEqual(Date(2021, 12, 1).get_last_day_of_month(), 31)

    def test_is_last_day(self):
        self.assertTrue(Date(1991, 2, 28).is_last_day())
        self.assertTrue(Date(2020, 2, 29).is_last_day())
        self.assertFalse(Date(1991, 2, 1).is_last_day())
        self.assertFalse(Date(2020, 2, 28).is_last_day())

    def test_is_last_month(self):
        self.assertFalse(Date(1991, 10, 25).is_last_day())
        self.assertTrue(Date(1991, 12, 31).is_last_day())

    def test_is_first_day(self):
        self.assertFalse(Date(1991, 10, 2).is_last_day())
        self.assertTrue(Date(1991, 10, 31).is_last_day())
        self.assertTrue(Date(1991, 2, 28).is_last_day())
        self.assertTrue(Date(1992, 2, 29).is_last_day())

    def test_is_first_month(self):
        self.assertFalse(Date(1991, 1, 2).is_last_month())
        self.assertTrue(Date(1991, 12, 28).is_last_month())

    def test_is_leap(self):
        self.assertFalse(Date(1201, 1, 1).is_leap())
        self.assertFalse(Date(1330, 1, 1).is_leap())
        self.assertFalse(Date(1646, 1, 1).is_leap())
        self.assertTrue(Date(1288, 1, 1).is_leap())
        self.assertTrue(Date(1460, 1, 1).is_leap())
        self.assertTrue(Date(1772, 1, 1).is_leap())

    def test_invalid_date(self):
        self.assertRaises(ValueError, lambda: Date(1991, 0, 1))
        self.assertRaises(ValueError, lambda: Date(1991, 13, 1))
        self.assertRaises(ValueError, lambda: Date(1991, 1, 0))
        self.assertRaises(ValueError, lambda: Date(1991, 1, 32))


if __name__ == '__main__':
    unittest.main()
