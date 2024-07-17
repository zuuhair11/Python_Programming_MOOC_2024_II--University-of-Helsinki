# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__get_euros = euros
        self.__get_cents = cents

    def __get_euros(self):
        return self.__get_euros

    def __get_cents(self):
        return self.__get_cents

    def __str__(self):
        cents = '0' + str(self.__get_cents) if self.__get_cents < 10 else self.__get_cents
        return f'{self.__get_euros}.{cents} eur'
    
    def __eq__(self, another: 'Money') -> bool:
        return (self.__get_euros == another.__get_euros) and (self.__get_cents == another.__get_cents)
    
    def __ne__(self, another: 'Money') -> bool:
        return self.__get_euros + self.__get_cents != another.__get_euros + another.__get_cents
    
    def __lt__(self, another: 'Money') -> bool:
        return (self.__get_euros + self.__get_cents) < (another.__get_euros + another.__get_cents)
    
    def __gt__(self, another: 'Money') -> bool:
        return self.__get_euros + self.__get_cents > another.__get_euros + another.__get_cents
    
    def __add__(self, another: 'Money') -> 'Money':
        self_cents = '0' + str(self.__get_cents) if self.__get_cents < 10 else self.__get_cents
        another_cents = '0' + str(another.__get_cents) if another.__get_cents < 10 else another.__get_cents
        cents = (float('0.' + str(self_cents)) + float('0.' + str(another_cents)))
        helper = str(cents).split('.')[1] + '0' if int(str(cents).split('.')[1]) < 10 else str(cents).split('.')[1]
        print(helper)
        return Money(int(self.__get_euros + another.__get_euros + int(cents)), int(helper))
    
    def __sub__(self, another: 'Money') -> 'Money':
        self_cents = '0' + str(self.__get_cents) if self.__get_cents < 10 else self.__get_cents
        another_cents = '0' + str(another.__get_cents) if another.__get_cents < 10 else another.__get_cents
        cents = (f'{(float('0.' + str(self_cents)) - float('0.' + str(another_cents))):.2}')
        helper = str(cents).split('.')[1] + '0' if int(str(cents).split('.')[1]) < 10 else str(cents).split('.')[1]
        print('ggg', (cents))
        if self.__get_euros - another.__get_euros >= 0:
            if float(cents) >= 0:
                print('pppppppp', cents)
                if len(cents.split('.')[1]) == 1:
                    return Money(int(self.__get_euros - another.__get_euros), int(helper))
                else:
                    return Money(int(self.__get_euros - another.__get_euros), int(cents.split('.')[1]))
            else:
                n, d = str(1 - float(cents)).split('.')

                if int(n) == 1 and self.__get_euros - another.__get_euros == 0:
                    raise ValueError('a negative result is not allowed')
                
                return Money(int(self.__get_euros - another.__get_euros - int(n)), int(100 - int(d)))
        else:
            raise ValueError('a negative result is not allowed')


if __name__ == '__main__':
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    # e1 = Money(15, 95)
    # e2 = Money(15, 95)
    # e1 = Money(1, 0)
    # e2 = Money(1, 0)
    # e1 = Money(4, 5)
    # e2 = Money(0, 50)
    e1 = Money(15, 95)
    e2 = Money(1, 55)
    # e1 = Money(4, 5)
    # e2 = Money(4, 6)
    # e1 = Money(3, 95)
    # e2 = Money(3, 90)

    e3 = e1 + e2
    e4 = e1 - e2

    print('==>', e3)
    print('==>', e4)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)


    # e5 = e2-e1
    print(e1)
    e1.euros = 1000
    print(e1)
