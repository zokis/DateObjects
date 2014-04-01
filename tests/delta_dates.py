import unittest


from dateobjects import Date, Year, DayDelta, MonthDelta, YearDelta


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


if __name__ == '__main__':
    unittest.main()
