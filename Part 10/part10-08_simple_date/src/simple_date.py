# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, dd: int, mm: int, yy: int) -> None:
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self) -> str:
        return '%d.%d.%d' % (self.dd, self.mm, self.yy)

    # Comparisons are easier now, when date converted into days
    def __convert_to_days(self) -> int:
        return self.yy * 360 + self.mm * 30 + self.dd

    # Converst days back to date
    def __to_date(self, n_days: int) -> 'SimpleDate':
        years: int = n_days // 360
        months: int = n_days // 30
        days: int = n_days - (months * 30)
        months -= years * 12

        return SimpleDate(days, months, years)

    def __lt__(self, another: 'SimpleDate') -> bool:
        return self.__convert_to_days() < another.__convert_to_days()

    def __gt__(self, another: 'SimpleDate') -> bool:
        return self.__convert_to_days() > another.__convert_to_days()

    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.__convert_to_days() == another.__convert_to_days()

    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.__convert_to_days() != another.__convert_to_days()

    def __add__(self, n_days: int) -> 'SimpleDate':
        return self.__to_date(self.__convert_to_days() + n_days)

    def __sub__(self, another: 'SimpleDate') -> int:
        return abs(self.__convert_to_days() - another.__convert_to_days())


if __name__ == '__main__':
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = d1 + 3
    # d4 = d2 + 400
    # d3 = SimpleDate(28, 12, 1985)
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
