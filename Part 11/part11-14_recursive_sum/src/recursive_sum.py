# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int) -> int:
    if number <= 1:
        return 1

    return number + recursive_sum(number - 1)


if __name__ == '__main__':
    result = recursive_sum(3)
    print(result) # 6

    result = recursive_sum(5)
    print(result) # 15
