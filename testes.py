import unittest

from datetime import date

from DateObjects import Date


class TestDateOperations(unittest.TestCase):

    def test_eq(self):
        self.assertTrue(Date(1991, 10, 25) == Date(1991, 10, 25))
        self.assertFalse(Date(1991, 10, 25) == Date(1992, 10, 25))
        self.assertFalse(Date(1991, 10, 25) == Date(1991, 10, 26))
        self.assertFalse(Date(1991, 10, 25) == Date(1991, 11, 25))

    def text_lt(self):
        self.assertFalse(Date(1991, 10, 25) < Date(1991, 10, 25))
        self.assertTrue(Date(1991, 10, 25) < Date(1992, 10, 25))
        self.assertTrue(Date(1991, 10, 25) < Date(1991, 10, 26))
        self.assertTrue(Date(1991, 10, 25) < Date(1991, 11, 25))

    def text_le(self):
        self.assertTrue(Date(1991, 10, 25) <= Date(1991, 10, 25))
        self.assertTrue(Date(1991, 10, 25) <= Date(1992, 10, 25))
        self.assertTrue(Date(1991, 10, 25) <= Date(1991, 10, 26))
        self.assertTrue(Date(1991, 10, 25) <= Date(1991, 11, 25))

    def text_ne(self):
        self.assertFalse(Date(1991, 10, 25) != Date(1991, 10, 25))
        self.assertTrue(Date(1991, 10, 25) != Date(1992, 10, 25))
        self.assertTrue(Date(1991, 10, 25) != Date(1991, 10, 26))
        self.assertTrue(Date(1991, 10, 25) != Date(1991, 11, 25))

    def text_gt(self):
        self.assertFalse(Date(1991, 10, 25) > Date(1991, 10, 25))
        self.assertTrue(Date(1991, 11, 25) > Date(1991, 10, 25))
        self.assertTrue(Date(1991, 10, 26) > Date(1991, 10, 25))
        self.assertTrue(Date(1992, 10, 25) > Date(1991, 10, 25))

    def text_ge(self):
        self.assertTrue(Date(1991, 10, 25) >= Date(1991, 10, 25))
        self.assertTrue(Date(1991, 11, 25) >= Date(1991, 10, 25))
        self.assertTrue(Date(1991, 10, 26) >= Date(1991, 10, 25))
        self.assertTrue(Date(1992, 10, 25) >= Date(1991, 10, 25))

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

    def is_last_day(self):
        self.assertTrue(Date(1991, 2, 28).is_last_day())
        self.assertTrue(Date(2020, 2, 29).is_last_day())
        self.assertFalse(Date(1991, 2, 1).is_last_day())
        self.assertFalse(Date(2020, 2, 28).is_last_day())

    def is_last_month(self):
        self.assertFalse(Date(1991, 10, 25).is_last_day())
        self.assertTrue(Date(1991, 12, 25).is_last_day())

    def is_first_day(self):
        self.assertFalse(Date(1991, 10, 2).is_last_day())
        self.assertTrue(Date(1991, 10, 1).is_last_day())

    def is_first_month(self):
        self.assertFalse(Date(1991, 12, 2).is_last_day())
        self.assertTrue(Date(1991, 1991, 2).is_last_day())

    def is_leap(self):
        self.assertFalse(Date(1201, 1, 1).is_last_day())
        self.assertFalse(Date(1330, 1, 1).is_last_day())
        self.assertFalse(Date(1646, 1, 1).is_last_day())
        self.assertTrue(Date(1288, 1, 1).is_last_day())
        self.assertTrue(Date(1460, 1, 1).is_last_day())
        self.assertTrue(Date(1772, 1, 1).is_last_day())

    def test_invalid_date(self):
        self.assertRaises(ValueError, lambda: Date(1991, 0, 1))
        self.assertRaises(ValueError, lambda: Date(1991, 13, 1))
        self.assertRaises(ValueError, lambda: Date(1991, 1, 0))
        self.assertRaises(ValueError, lambda: Date(1991, 1, 32))


if __name__ == '__main__':
    unittest.main()
