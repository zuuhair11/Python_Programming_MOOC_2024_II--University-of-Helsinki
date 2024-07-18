# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, dd: int, mm: int, yy: int) -> None:
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self) -> str:
        return '%d.%d.%d' % (self.dd, self.mm, self.yy)

    def __lt__(self, another: 'SimpleDate') -> bool:
        if self.yy < another.yy:
            return True
        elif self.yy == another.yy:
            if self.mm < another.mm:
                return True
            elif self.mm == another.mm:
                if self.dd < another.dd:
                    return True
                elif self.dd > another.dd:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, another: 'SimpleDate') -> bool:
        if self.yy > another.yy:
            return True
        elif self.yy == another.yy:
            if self.mm > another.mm:
                return True
            elif self.mm == another.mm:
                if self.dd > another.dd:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, another: 'SimpleDate') -> bool:
        return self.dd == another.dd and self.mm == another.mm and self.yy == another.yy

    def __ne__(self, another: 'SimpleDate') -> bool:
        return self.dd != another.dd or self.mm != another.mm or self.yy != another.yy
    
    def __add__(self, n_days: int) -> 'SimpleDate':
        new_d = SimpleDate(self.dd, self.mm, self.yy)

        for _ in range(n_days):
            new_d.dd += 1

            if new_d.dd > 30:
                new_d.dd = 1
                new_d.mm += 1

                if new_d.mm > 12:
                    new_d.mm = 1
                    new_d.yy += 1

        return new_d


if __name__ == '__main__':
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = d1 + 3
    d4 = d2 + 400
    # d3 = SimpleDate(28, 12, 1985)

    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    print(d1)
    print(d2)
    print(d3)
    print(d4)
