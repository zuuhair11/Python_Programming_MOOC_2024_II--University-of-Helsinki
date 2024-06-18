# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------
def total_units(grocery_list: ShoppingList) -> int:
    total = 0
    for i in range(grocery_list.number_of_items()):
        total += grocery_list.amount(i + 1)

    return total


if __name__ == '__main__':
    # Instantiate new object
    grocery_list = ShoppingList()

    # Add items
    grocery_list.add("bananas", 10)
    grocery_list.add("apples", 5)
    grocery_list.add("pineapple", 1)

    # Calculate the total number of units listed
    print(total_units(grocery_list))
