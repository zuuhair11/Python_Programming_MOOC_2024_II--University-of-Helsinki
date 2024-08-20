# Write your solution here
def search(products: list, criterion: callable) -> list:
    return [ product for product in products if criterion(product) ]


if __name__ == '__main__':
    products = [
        ('banana', 5.95, 12), 
        ('apple', 3.95, 3), 
        ('orange', 4.50, 2), 
        ('watermelon', 4.95, 22), 
        ('kale', 0.99, 1)
    ]

    for product in search(products, lambda p: p[1] < 4):
        print(product)
