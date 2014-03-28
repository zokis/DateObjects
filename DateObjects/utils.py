def r(x):
    def inner(*args, **kwargs):
        return x
    return inner


def get_days_of_february(year=None):
    if year and year.is_leap():
        return 29
    return 28
