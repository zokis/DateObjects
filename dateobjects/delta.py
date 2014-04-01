import calendar

from datetime import date, timedelta

from .dateobjects import Date, PartDate


class Delta(PartDate):

    def __neg__(self):
        return self.__class__(-self.get_inner())

    def __sub__(self, other):
        value = self.get_inner()

        self.set_inner(-value)
        new = self.__add__(other)
        self.set_inner(value)
        return new

    def __add__(self, other):
        self_value = self.get_inner()
        other_value = int(other)
        return self.__class__(self_value + other_value)


class YearDelta(Delta):
    inner = '_years'

    def __add__(self, other):
        try:
            return Date(int(other.year)+self._years, other.month, other.day)
        except ValueError:
            new_date = date(int(other.year), int(other.month), int(other.day))
            new_date = new_date + (date(new_date.year + self._years, 1, 1) - date(new_date.year, 1, 1))
            return Date(new_date.year, new_date.month, new_date.day)
        except AttributeError:
            return super(YearDelta, self).__add__(other)


class MonthDelta(Delta):
    inner = '_months'

    def __add__(self, other):
        try:
            month = int(other.month) + self._months - 1
            year = int(other.year) + month / 12
            month = month % 12 + 1
            day = min(int(other.day), calendar.monthrange(year, month)[1])
            return Date(year, month, day)
        except:
            return super(MonthDelta, self).__add__(other)


class DayDelta(Delta):
    inner = '_days'

    def __add__(self, other):
        try:
            new_date = date(other.year, other.month, other.day) + timedelta(days=self._days)
            return Date(new_date.year, new_date.month, new_date.day)
        except:
            return super(DayDelta, self).__add__(other)
