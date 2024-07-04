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

    def __str__(self):
        stored_weight = sum(item.weight() for item in self.__items)

        return f'{len(self.__items)} items ({stored_weight} kg)'


if __name__ == '__main__':
    book = Item('ABC Book', 2)
    phone = Item('Nokia 3210', 1)
    brick = Item('Brick', 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)
