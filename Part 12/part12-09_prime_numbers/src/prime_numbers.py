# Write your solution here
def prime_numbers() -> any:
    number = 2

    def is_prime(number: int) -> bool:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    while True:
        if is_prime(number):
            yield number

        number += 1

    # num = 2
    # primes = []

    # while True:
    #     is_prime = True

    #     for prime in primes:
    #         if num % prime == 0:
    #             is_prime = False
    #             break

    #     if is_prime:
    #         primes.append(num)
    #         yield num
    #     num += 1


if __name__ == '__main__':
    numbers = prime_numbers()
    for _ in range(8):
        print(next(numbers))
