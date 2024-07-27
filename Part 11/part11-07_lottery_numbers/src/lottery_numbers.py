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

    def hits_in_place(self, numbers: list) -> list:
        # return [numbers[i] if numbers[i] == self.__weeks[i] else -1 for i in range(len(numbers))]
        return [number if number in self.__weeks else -1 for number in numbers]


if __name__ == '__main__':
    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]

    print(week8.hits_in_place(my_numbers))
