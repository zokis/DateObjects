import calendar

from datetime import date, timedelta

from .dateobjects import Date


class Delta(object):

    def __init__(self, v):
        setattr(self, self.inner, v)

    def __neg__(self):
        return self.__class__(-getattr(self, self.inner))

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%d)" % (name, getattr(self, self.inner))

    def __sub__(self, other):
        value = getattr(self, self.inner)

        setattr(self, self.inner, -value)
        new_date = self.__add__(other)
        setattr(self, self.inner, value)
        return new_date


class YearDelta(Delta):
    inner = '_years'

    def __add__(self, other):
        try:
            return Date(int(other.year)+self._years, other.month, other.day)
        except:
            new_date = date(int(other.year), int(other.month), int(other.day))
            new_date = new_date + (date(new_date.year + self._years, 1, 1) - date(new_date.year, 1, 1))
        return Date(new_date.year, new_date.month, new_date.day)


class MonthDelta(Delta):
    inner = '_months'

    def __add__(self, other):
        month = int(other.month) + self._months - 1
        year = int(other.year) + month / 12
        month = month % 12 + 1
        day = min(int(other.day), calendar.monthrange(year, month)[1])
        return Date(year, month, day)


class DayDelta(Delta):
    inner = '_days'

    def __add__(self, other):
        new_date = date(other.year, other.month, other.day) + timedelta(days=self._days)
        return Date(new_date.year, new_date.month, new_date.day)
