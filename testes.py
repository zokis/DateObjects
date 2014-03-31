import unittest

from datetime import date

from DateObjects import Date, Day, Month, Year, DayDelta, MonthDelta, YearDelta


class TestDayDeltaDate(unittest.TestCase):

    def test_DayDelta_add_Date(self):
        self.assertEqual(Date(1, 1, 10), DayDelta(9) + Date(1, 1, 1))

    def test_Date_add_DayDelta(self):
        self.assertEqual(Date(1, 1, 10), Date(1, 1, 1) + DayDelta(9))

    def test_february_leap_year_27_add_3(self):
        self.assertEqual(Date(1992, 3, 1), Date(1992, 2, 27) + DayDelta(3))

    def test_february_not_leap_year_27_add_3(self):
        self.assertEqual(Date(1991, 3, 2), Date(1991, 2, 27) + DayDelta(3))

    def test_1992_to_2021(self):
        leap_year = 366
        not_leap_year = 365

        expected = Date(2021, 1, 1)
        test_date = Date(1991, 1, 1)
        for intyear in range(1992, 2022):
            year = Year(intyear)
            if year.is_leap():
                test_date += DayDelta(leap_year)
            else:
                test_date += DayDelta(not_leap_year)

        self.assertEqual(expected, test_date)

    def test_add_365_days(self):
        self.assertEqual(Date(2, 1, 1), Date(1, 1, 1) + DayDelta(365))
        self.assertEqual(Date(1993, 2, 28), Date(1992, 2, 29) + DayDelta(365))

    def test_remove_365_days(self):
        self.assertEqual(Date(1, 1, 1), Date(2, 1, 1) - DayDelta(365))
        self.assertEqual(Date(1, 1, 1), Date(2, 1, 1) + DayDelta(-365))

        self.assertEqual(Date(1991, 3, 1), Date(1992, 2, 29) - DayDelta(365))
        self.assertEqual(Date(1991, 3, 1), Date(1992, 2, 29) + DayDelta(-365))

    def test_add_366_days_in_a_leap_year(self):
        self.assertEqual(Date(2021, 1, 1), Date(2020, 1, 1) + DayDelta(366))
        self.assertEqual(Date(1992, 2, 29), Date(1991, 2, 28) + DayDelta(366))

    def test_remove_366_days_in_a_leap_year(self):
        self.assertEqual(Date(2018, 12, 31), Date(2020, 1, 1) - DayDelta(366))
        self.assertEqual(Date(2018, 12, 31), Date(2020, 1, 1) + DayDelta(-366))

        self.assertEqual(Date(1991, 2, 28), Date(1992, 2, 29) - DayDelta(366))
        self.assertEqual(Date(1991, 2, 28), Date(1992, 2, 29) + DayDelta(-366))

    def test_remove_day_2020_3_1(self):
        self.assertEqual(Date(2020, 2, 29), Date(2020, 3, 1) - DayDelta(1))
        self.assertEqual(Date(2020, 2, 29), Date(2020, 3, 1) + DayDelta(-1))

    def test_remove_day_2021_3_1(self):
        self.assertEqual(Date(2021, 2, 28), Date(2021, 3, 1) - DayDelta(1))
        self.assertEqual(Date(2021, 2, 28), Date(2021, 3, 1) + DayDelta(-1))


class TestMonthDeltaDate(unittest.TestCase):

    def test_DayDelta_add_Date(self):
        self.assertEqual(Date(1, 2, 1), MonthDelta(1) + Date(1, 1, 1))

    def test_Date_add_DayDelta(self):
        self.assertEqual(Date(1, 2, 1), Date(1, 1, 1) + MonthDelta(1))

    def test_february_leap_year_add_3(self):
        self.assertEqual(Date(1992, 2, 29), Date(1991, 11, 29) + MonthDelta(3))

    def test_february_not_leap_year_27_add_3(self):
        self.assertEqual(Date(1991, 5, 27), Date(1991, 2, 27) + MonthDelta(3))

    def test_1992_to_2021(self):
        expected = Date(2021, 1, 1)
        test_date = Date(1991, 1, 1)

        self.assertEqual(expected, test_date + MonthDelta(30 * 12))

    def test_add_12_months(self):
        self.assertEqual(Date(2, 1, 1), Date(1, 1, 1) + MonthDelta(12))
        self.assertEqual(Date(1993, 2, 28), Date(1992, 2, 29) + MonthDelta(12))

    def test_remove_12_months(self):
        self.assertEqual(Date(1, 1, 1), Date(2, 1, 1) - MonthDelta(12))
        self.assertEqual(Date(1, 1, 1), Date(2, 1, 1) + MonthDelta(-12))

        self.assertEqual(Date(1991, 2, 28), Date(1992, 2, 29) - MonthDelta(12))
        self.assertEqual(Date(1991, 2, 28), Date(1992, 2, 29) + MonthDelta(-12))

    def test_add_12_months_in_a_leap_year(self):
        self.assertEqual(Date(2021, 1, 1), Date(2020, 1, 1) + MonthDelta(12))
        self.assertEqual(Date(1992, 2, 28), Date(1991, 2, 28) + MonthDelta(12))

    def test_remove_12_months_in_a_leap_year(self):
        self.assertEqual(Date(2019, 1, 1), Date(2020, 1, 1) - MonthDelta(12))
        self.assertEqual(Date(2019, 1, 1), Date(2020, 1, 1) + MonthDelta(-12))

        self.assertEqual(Date(1991, 2, 28), Date(1992, 2, 29) - MonthDelta(12))
        self.assertEqual(Date(1991, 2, 28), Date(1992, 2, 29) + MonthDelta(-12))

    def test_remove_month_2020_3_31(self):
        self.assertEqual(Date(2020, 2, 29), Date(2020, 3, 31) - MonthDelta(1))
        self.assertEqual(Date(2020, 2, 29), Date(2020, 3, 31) + MonthDelta(-1))

    def test_remove_month_2021_3_31(self):
        self.assertEqual(Date(2021, 2, 28), Date(2021, 3, 31) - MonthDelta(1))
        self.assertEqual(Date(2021, 2, 28), Date(2021, 3, 31) + MonthDelta(-1))


class TestYerDeltaDate(unittest.TestCase):

    def test_1992_to_2021(self):
        self.assertEqual(Date(2021, 1, 1), Date(1992, 1, 1) + YearDelta(29))

    def test_YearDelta_add_Date(self):
        self.assertEqual(Date(2, 1, 1), YearDelta(1) + Date(1, 1, 1))

    def test_Date_add_YearDelta(self):
        self.assertEqual(Date(2, 1, 1), Date(1, 1, 1) + YearDelta(1))

    def test_add_1_year(self):
        self.assertEqual(Date(2, 1, 1), Date(1, 1, 1) + YearDelta(1))
        self.assertEqual(Date(1993, 2, 28), Date(1992, 2, 28) + YearDelta(1))

    def test_remove_1_year(self):
        self.assertEqual(Date(1, 1, 1), Date(2, 1, 1) - YearDelta(1))
        self.assertEqual(Date(1, 1, 1), Date(2, 1, 1) + YearDelta(-1))

        self.assertEqual(Date(1991, 3, 1), Date(1992, 2, 29) - YearDelta(1))
        self.assertEqual(Date(1991, 3, 1), Date(1992, 2, 29) + YearDelta(-1))

    def test_add_1_year_in_a_leap_year(self):
        self.assertEqual(Date(2021, 1, 1), Date(2020, 1, 1) + YearDelta(1))
        self.assertEqual(Date(1992, 2, 28), Date(1991, 2, 28) + YearDelta(1))
        self.assertEqual(Date(1992, 3, 1), Date(1991, 3, 1) + YearDelta(1))

    def test_remove_1_year_in_a_leap_year(self):
        self.assertEqual(Date(2019, 1, 1), Date(2020, 1, 1) - YearDelta(1))
        self.assertEqual(Date(2019, 1, 1), Date(2020, 1, 1) + YearDelta(-1))

        self.assertEqual(Date(1991, 3, 1), Date(1992, 2, 29) - YearDelta(1))
        self.assertEqual(Date(1991, 3, 1), Date(1992, 2, 29) + YearDelta(-1))

    def test_remove_year_2020_3_1(self):
        self.assertEqual(Date(2019, 3, 1), Date(2020, 3, 1) - YearDelta(1))
        self.assertEqual(Date(2019, 3, 1), Date(2020, 3, 1) + YearDelta(-1))

    def test_remove_year_2021_3_1(self):
        self.assertEqual(Date(2020, 3, 1), Date(2021, 3, 1) - YearDelta(1))
        self.assertEqual(Date(2020, 3, 1), Date(2021, 3, 1) + YearDelta(-1))


class TestDayDeltaOperations(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(DayDelta(1), DayDelta(1))

    def test_ne(self):
        self.assertNotEqual(DayDelta(1), DayDelta(2))

    def test_lt(self):
        self.assertLess(DayDelta(1), DayDelta(2))

    def test_le(self):
        self.assertLessEqual(DayDelta(1), DayDelta(2))
        self.assertLessEqual(DayDelta(2), DayDelta(2))

    def test_gt(self):
        self.assertGreater(DayDelta(2), DayDelta(1))

    def test_ge(self):
        self.assertGreaterEqual(DayDelta(2), DayDelta(1))
        self.assertGreaterEqual(DayDelta(2), DayDelta(2))


class TestMonthDeltaOperations(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(MonthDelta(1), MonthDelta(1))

    def test_ne(self):
        self.assertNotEqual(MonthDelta(1), MonthDelta(2))

    def test_lt(self):
        self.assertLess(MonthDelta(1), MonthDelta(2))

    def test_le(self):
        self.assertLessEqual(MonthDelta(1), MonthDelta(2))
        self.assertLessEqual(MonthDelta(2), MonthDelta(2))

    def test_gt(self):
        self.assertGreater(MonthDelta(2), MonthDelta(1))

    def test_ge(self):
        self.assertGreaterEqual(MonthDelta(2), MonthDelta(1))
        self.assertGreaterEqual(MonthDelta(2), MonthDelta(2))


class TestYearDeltaOperations(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(YearDelta(1), YearDelta(1))

    def test_ne(self):
        self.assertNotEqual(YearDelta(1), YearDelta(2))

    def test_lt(self):
        self.assertLess(YearDelta(1), YearDelta(2))

    def test_le(self):
        self.assertLessEqual(YearDelta(1), YearDelta(2))
        self.assertLessEqual(YearDelta(2), YearDelta(2))

    def test_gt(self):
        self.assertGreater(YearDelta(2), YearDelta(1))

    def test_ge(self):
        self.assertGreaterEqual(YearDelta(2), YearDelta(1))
        self.assertGreaterEqual(YearDelta(2), YearDelta(2))


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
