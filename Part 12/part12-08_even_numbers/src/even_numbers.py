# Write your solution here
def even_numbers(beginning: int, maximum: int) -> any:
    if beginning % 2 != 0:
        beginning += 1

    while beginning <= maximum:
        yield beginning
        beginning += 2


if __name__ == '__main__':
    for number in even_numbers(2, 10):
        print(number)
