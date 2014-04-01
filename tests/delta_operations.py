import unittest

from DateObjects import DayDelta, MonthDelta, YearDelta


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


if __name__ == '__main__':
    unittest.main()
