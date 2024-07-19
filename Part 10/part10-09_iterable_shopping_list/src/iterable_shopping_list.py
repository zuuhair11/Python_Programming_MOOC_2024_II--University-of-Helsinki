# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]

    def __iter__(self) -> 'ShoppingList':
        self.n = 0
        return self

    def __next__(self) -> tuple:
        if self.n < len(self.products):
            product: tuple = self.products[self.n]
            self.n += 1

            return product
        else:
            raise StopIteration


if __name__ == '__main__':
    shopping_list = ShoppingList()
    shopping_list.add('bananas', 10)
    shopping_list.add('apples', 5)
    shopping_list.add('pineapple', 1)

    for product in shopping_list:
        print(f'{product[0]}: {product[1]} units')
