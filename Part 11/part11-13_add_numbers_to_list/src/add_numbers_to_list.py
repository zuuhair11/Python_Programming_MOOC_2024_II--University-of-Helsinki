# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list) -> None:
    if len(numbers) % 5 == 0:
        return None

    numbers.append(numbers[-1] + 1)
    add_numbers_to_list(numbers)


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 10, 11]
    add_numbers_to_list(numbers)
    print(numbers)
