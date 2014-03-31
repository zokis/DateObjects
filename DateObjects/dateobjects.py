from datetime import date, timedelta
from .utils import get_days_of_february, r


class PartDate(object):

    def __init__(self, value):
        self.set_inner(value)

    def get_inner(self):
        return getattr(self, self.inner)

    def set_inner(self, value):
        setattr(self, self.inner, value)

    def __int__(self):
        return int(self.get_inner())

    def __eq__(self, other):
        return int(self) == int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __ne__(self, other):
        return int(self) != int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self)


class Year(PartDate):
    inner = '_year'

    def is_leap(self):
        new_date = date(self._year, 3, 1)
        return (new_date - timedelta(days=1)).day == 29


class Month(PartDate):
    inner = '_month'

    days = {
        1: r(31),
        2: get_days_of_february,
        3: r(31),
        4: r(30),
        5: r(31),
        6: r(30),
        7: r(31),
        8: r(31),
        9: r(30),
        10: r(31),
        11: r(30),
        12: r(31),
    }

    def __init__(self, month):
        super(Month, self).__init__(month)
        if self._month <= 0 or self._month >= 13:
            raise ValueError('month must be in 1..12')

    def is_first(self):
        return self._month == 1

    def is_last(self):
        return self._month == 12

    def get_last_day(self, year=None):
        return self.days[self._month](year)


class Day(PartDate):
    inner = '_day'

    def __init__(self, day):
        super(Day, self).__init__(day)
        if self._day <= 0 or self._day >= 32:
            raise ValueError('day must be in 1..31')

    def is_first(self):
        return self._day == 1

    def is_last(self, month=None, year=None):
        if month is None:
            return self._day == 31
        else:
            return self._day == month.get_last_day(year)


class Date(object):
    def __init__(self, year=Year(0), month=Month(1), day=Day(1), datetime=None):
        if datetime is None:
            self._year = int(year)
            self._month = int(month)
            self._day = int(day)
            date(self._year, self._month, self._day)
        else:
            self._year = datetime.year
            self._month = datetime.month
            self._day = datetime.day

    def to_datetime(self):
        return date(self._year, self._month, self._day)

    @property
    def day(self):
        return Day(self._day)

    @day.setter
    def day(self, day):
        new_day = int(day)
        date(self._year, self._month, new_day)
        self._day = new_day

    @property
    def month(self):
        return Month(self._month)

    @month.setter
    def month(self, month):
        new_month = int(month)
        date(self._year, new_month, self._day)
        self._month = new_month

    @property
    def year(self):
        return Year(self._year)

    @year.setter
    def year(self, year):
        new_year = int(year)
        date(new_year, self._month, self._day)
        self._year = new_year

    def get_last_day_of_month(self):
        return self.month.get_last_day(self.year)

    def is_last_day(self):
        return self._day == self.get_last_day_of_month()

    def is_last_month(self):
        return self.month.is_last()

    def is_first_day(self):
        return self.day.is_first()

    def is_first_month(self):
        return self.month.is_first()

    def is_leap(self):
        return self.year.is_leap()

    def __repr__(self):
        return "Date(%d, %d, %d)" % (self.year, self.month, self.day)

    def __add__(self, other):
        return other + self

    def __sub__(self, other):
        return other - self

    def __eq__(self, other):
        return self.to_datetime() == other.to_datetime()

    def __lt__(self, other):
        return self.to_datetime() < other.to_datetime()

    def __le__(self, other):
        return self.to_datetime() <= other.to_datetime()

    def __ne__(self, other):
        return self.to_datetime() != other.to_datetime()

    def __gt__(self, other):
        return self.to_datetime() > other.to_datetime()

    def __ge__(self, other):
        return self.to_datetime() >= other.to_datetime()
