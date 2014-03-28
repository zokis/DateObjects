Date-Objects
============

Date Objects


Examples:

```
>>> from DateObjects import Year, Month, Day, Date
>>> from datetime import date
>>> d1 = Date(1991, 10, 15)
>>> y = Year(1991)
>>> m = Month(10)
>>> d = Day(25)
>>> d2 = Date(y, m, d)
>>> d3 = Date(datetime=date(1991, 10, 25))
>>> d1, d2, d3
(Date(1991, 10, 15), Date(1991, 10, 25), Date(1991, 10, 25))
>>> 
>>> d1.to_datetime()
datetime.date(1991, 10, 15)
>>> d1.day, d1.month, d1.year
(Day(15), Month(10), Year(1991))
>>> d1.is_first_day()
False
>>> d1.is_first_month()
False
>>> d1.is_last_day()
False
>>> d1.is_last_month()
False
>>> d1.is_leap()
False
>>> d4 = Date(2020, 1, 1)
>>> d4.is_first_day()
True
>>> d4.is_first_month()
True
>>> d4.is_leap()
True
>>> d4.month = Month(12)
>>> d4
Date(2020, 12, 1)
>>> d4.is_last_month()
True
>>> d4.month = 12
>>> d4.month
Month(12)
>>> d4.month.is_last()
True
>>> d4.is_last_month()
True
>>> d4.month = 13
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "DateObjects/dateobjects.py", line 108, in month
    date(int(self._year), new_month, int(self._day))
ValueError: month must be in 1..12
>>> Day(100)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "DateObjects/dateobjects.py", line 64, in __init__
    raise ValueError('day must be in 1..31')
ValueError: day must be in 1..31
>>> Month(100)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "DateObjects/dateobjects.py", line 46, in __init__
    raise ValueError('month must be in 1..12')
ValueError: month must be in 1..12
>>> d4
Date(2020, 12, 1)
>>> d4 + YearDelta(20)
Date(2040, 12, 1)
>>> YearDelta(20) + d4
Date(2040, 12, 1)
>>> d4 + YearDelta(-20)
Date(2000, 12, 1)
>>> d4 - YearDelta(20)
Date(2000, 12, 1)
>>> d4 = d4 - MonthDelta(10)
>>> d4
Date(2020, 2, 1)
>>> d4 + DayDelta(28)
Date(2020, 2, 29)
>>> d4 += MonthDelta(10)
>>> d4
Date(2020, 12, 1)
>>> d4 + DayDelta(28)
Date(2020, 12, 29)
>>> d4 + DayDelta(100) + MonthDelta(10) + YearDelta(10)
Date(2032, 1, 11)
>>> 
```
