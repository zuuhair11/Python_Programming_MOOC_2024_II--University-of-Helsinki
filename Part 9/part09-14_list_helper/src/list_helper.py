# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None

        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item

        return max_item

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)

        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1

        return doubles


if __name__ == '__main__':
    numbers = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
