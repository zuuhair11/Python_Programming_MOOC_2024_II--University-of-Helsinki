# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return '{} ({} kg)'.format(self.__name, self.__weight)


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, new_item: Item):
        stored_weight = sum(item.weight() for item in self.__items)

        if (stored_weight + new_item.weight()) <= self.__max_weight:
            self.__items.append(new_item)

    def print_items(self):
        for item in self.__items:
            print('{} ({} kg)'.format(item.name(), item.weight()))

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None

        heaviest = None
        for item in self.__items:
            if heaviest is None or item.weight() > heaviest.weight():
                heaviest = item

        return heaviest

    def __str__(self):
        end_s = 's' if len(self.__items) != 1 else ''

        return f'{len(self.__items)} item{end_s} ({self.weight()} kg)'


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, new_suitcase: Suitcase):
        if (self.weight() + new_suitcase.weight()) > self.__max_weight:
            return

        self.__suitcases.append(new_suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def weight(self):
        p = 0
        for suitcase in self.__suitcases:
            p += suitcase.weight()

        return p

    def __str__(self):
        end_s = 's' if len(self.__suitcases) != 1 else ''
        return f'{len(self.__suitcases)} suitcase{end_s}, space for {self.__max_weight - self.weight()} kg'


if __name__ == '__main__':
    book = Item('ABC Book', 2)
    phone = Item('Nokia 3210', 1)
    brick = Item('Brick', 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print('The suitcases in the cargo hold contain the following items:')
    cargo_hold.print_items()
