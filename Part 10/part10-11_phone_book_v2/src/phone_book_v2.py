# Write your solution here:
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self) -> str:
        return self.__name

    def numbers(self) -> list:
        return self.__numbers

    def address(self) -> str:
        return self.__address

    def add_number(self, new_number: str) -> None:
        self.__numbers.append(new_number)

    def add_address(self, new_address: str) -> None:
        self.__address = new_address


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str) -> None:
        if not name in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_number(number)

    def add_address(self, name: str, new_address: str) -> None:
        if name not in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_address(new_address)

    def get_entry(self, name: str) -> list:
        if not name in self.__persons:
            return None

        return self.__persons[name]

    def all_entries(self) -> dict:
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print('commands: ')
        print('0 exit')
        print('1 add number')
        print('2 search')
        print('3 add address')

    def add_number(self) -> None:
        name: str = input('name: ')
        number: str = input('number: ')
        self.__phonebook.add_number(name, number)

    def add_address(self) -> None:
        name: str = input('name: ')
        address: str = input('address: ')

        self.__phonebook.add_address(name, address)

    def search(self) -> None:
        name: str = input('name: ')
        person: Person = self.__phonebook.get_entry(name)

        if person is not None:
            address: str = person.address()
            numbers: list = person.numbers()

            if not len(numbers):
                print('number unknown')
            else:
                for number in person.numbers():
                    print(number)

            if address == None:
                print('address unknown')
            else:
                print(address)
        else:
            print('number unknown')
            print('address unknown')

    def execute(self) -> None:
        self.help()

        while True:
            print('')
            command = input('command: ')
            if command == '0':
                break
            elif command == '1':
                self.add_number()
            elif command == '2':
                self.search()
            elif command == '3':
                self.add_address()
            else:
                self.help()


# # when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
