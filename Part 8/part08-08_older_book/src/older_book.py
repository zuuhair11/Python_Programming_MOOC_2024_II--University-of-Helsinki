# DO NOT CHANGE CLASS Book!
# Write your solution after the class!
class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------
def older_book(book_1: Book, book_2: Book):
    same = True

    if book_1.year < book_2.year:
        older = book_1
        same = False
    elif book_2.year < book_1.year:
        older = book_2
        same = False

    if same:
        print(f'{book_1.name} and {book_2.name} were published in {book_1.year}')
    else:
        print('{} is older, it was published in {}'.format(older.name, older.year))


if __name__ == '__main__':
    python = Book('Fluent Python', 'Luciano Ramalho', 'programming', 2015)
    everest = Book('High Adventure', 'Edmund Hillary', 'autobiography', 1956)
    norma = Book('Norma', 'Sofi Oksanen', 'crime', 2015)

    older_book(python, everest)
    older_book(python, norma)
