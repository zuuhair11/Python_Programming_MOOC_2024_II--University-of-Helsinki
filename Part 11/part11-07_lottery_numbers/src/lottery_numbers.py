# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, weeks: list) -> None:
        self.week = week
        self.weeks = weeks

    @property
    def week(self) -> int:
        return self.__week

    @property
    def weeks(self) -> list:
        return self.__weeks

    @week.setter
    def week(self, n_week: int) -> None:
        if type(n_week) != int:
            raise ValueError('The week should be an integer!')

        self.__week = n_week

    @weeks.setter
    def weeks(self, n_weeks: list) -> None:
        if type(n_weeks) != list:
            raise ValueError('The weeks should be formatted in a list')
        
        self.__weeks = n_weeks

    def number_of_hits(self, numbers: list) -> int:
        return len([number for number in numbers if number in self.__weeks])


if __name__ == '__main__':
    week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
    numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(numbers))
