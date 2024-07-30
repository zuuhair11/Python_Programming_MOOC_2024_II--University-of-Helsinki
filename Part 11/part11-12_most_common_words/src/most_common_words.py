# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int) -> dict:
    with open(filename, mode='r') as file:
        content = file.read()

        # remove line breaks and punctuation
        content = content.replace('\n', ' ')
        for punctuation_mark in string.punctuation:
            content = content.replace(punctuation_mark, '')

        words: list = content.split(' ')
        return { word: words.count(word) for word in words if words.count(word) >= lower_limit }


if __name__ == '__main__':
    common_words: dict = most_common_words('comprehensions.txt', 3)
    print(common_words)
