Date-Objects
============

Date Objects


Examples:

Date Examples:
```
>>> from DateObjects import Date
>>> from datetime import date
>>> d1 = Date(1991, 10, 15)
>>> d2 = Date(datetime=date(1991, 10, 25))
>>> from DateObjects import Day, Month, Year
>>> d = Day(25)
>>> m = Month(10)
>>> y = Year(1991)
>>> d3 = Date(y, m, d)
>>> d1, d2, d3
(Date(1991, 10, 15), Date(1991, 10, 25), Date(1991, 10, 25))
>>> d1 == d2
False
>>> d2 == d3
True
>>> d1 < d2
True
>>> d1 <= d2
True
>>> d1 != d2
True
>>> d1 >= d2
False
>>> d1 > d2
False
>>> d1.month = 12
>>> d1.month
Month(12)
>>> d1.month = Month(12)
>>> d1.month
Month(12)
>>> d1.is_first_month()
False
>>> d1.is_last_month()
True
>>> d1.day = 31
>>> d1.is_first_day()
False
>>> d1.is_last_day()
True
>>> d1.is_leap()
False
>>> d1.year = 2020
>>> d1.is_leap()
True
>>> d1.to_datetime()
datetime.date(2020, 12, 31)
```

Day Examples:
```
>>> from DateObjects import Day
>>> Day(0)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "DateObjects/dateobjects.py", line 82, in __init__
    raise ValueError('day must be in 1..31')
ValueError: day must be in 1..31
>>> d1 = Day(10)
>>> d2 = Day(25)
>>> d1 == d2
False
>>> d1 < d2
True
>>> d1 <= d2
True
>>> d1 > d2
False
>>> d1 >= d2
False
>>> d1 != d2
True
>>> d1, d2
(Day(10), Day(25))
>>> d1.is_first()
False
>>> d1.is_last()
False
>>> d1 = Day(28)
>>> d1.is_last(Month(2))
True
>>> d1.is_last(Month(2), year=Year(2020))
False
>>> d1
Date(1991, 12, 31)
>>> d1.is_leap()
False
>>> d1.year = 2020
>>> d1.is_leap()
True
```

Month Examples:
```
>>> from DateObjects import Month
>>> Month(90)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "DateObjects/dateobjects.py", line 64, in __init__
    raise ValueError('month must be in 1..12')
ValueError: month must be in 1..12
>>> m1 = Month(10)
>>> m2 = Month(12)
>>> m1, m2
(Month(10), Month(12))
>>> m1 > m2
False
>>> m1 >= m2
False
>>> m1 < m2
True
>>> m1 <= m2
True
>>> m1 != m2
True
>>> m1 == m2
False
>>> m1.is_first()
False
>>> m1.is_last()
False
```

Year Examples:
```
>>> from DateObjects import Year
>>> y1 = Year(1991)
>>> y2 = Year(1992)
>>> y1.is_leap()
False
>>> y2.is_leap()
True
>>> y1 > y2
False
>>> y1 >= y2
False
>>> y1 < y2
True
>>> y1 <= y2
True
>>> y1 == y2
False
>>> y1 != y2
True
```

Delta Examples:
```
>>> from DateObjects import Date, DayDelta, MonthDelta, YearDelta
>>> d = Date(1992, 2, 28)
>>> d
Date(1992, 2, 28)
>>> d + DayDelta(1)
Date(1992, 2, 29)
>>> d + DayDelta(2)
Date(1992, 3, 1)
>>> d + MonthDelta(2)
Date(1992, 4, 28)
>>> d + YearDelta(2)
Date(1994, 2, 28)
>>> d
Date(1992, 2, 28)
>>> d + DayDelta(-1)
Date(1992, 2, 27)
>>> d - DayDelta(1)
Date(1992, 2, 27)
>>> DayDelta(1) + d
Date(1992, 2, 29)
>>> DayDelta(1) - d
Date(1992, 2, 27)
>>> DayDelta(-1) + d
Date(1992, 2, 27)
```
