# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int) -> any:
    """First attempt - using Generator comprehensions"""
    return (''.join(random.choices(characters, k=length)) for _ in range(amount))

    """Second attempt - Generator comprehensions"""
    # return (''.join([random.choice(characters) for _ in range(length)]) for _ in range(amount))

    """Third attempt - Generator"""
    # for _ in range(amount):
    #     yield ''.join(random.choices(characters, k=length))


if __name__ == '__main__':
    wordgen = word_generator('abcdefg', 3, 5)
    for word in wordgen:
        print(word)
