# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        cents = '0' + str(self.__cents) if self.__cents < 10 else self.__cents
        return f'{self.__euros}.{cents} eur'
    
    def __eq__(self, another: 'Money') -> bool:
        return (self.__euros == another.__euros) and (self.__cents == another.__cents)
    
    def __ne__(self, another: 'Money') -> bool:
        return self.__euros + self.__cents != another.__euros + another.__cents
    
    def __lt__(self, another: 'Money') -> bool:
        return (self.__euros + self.__cents) < (another.__euros + another.__cents)
    
    def __gt__(self, another: 'Money') -> bool:
        return self.__euros + self.__cents > another.__euros + another.__cents
    
    def __add__(self, another: 'Money') -> 'Money':
        self_cents = '0' + str(self.__cents) if self.__cents < 10 else self.__cents
        another_cents = '0' + str(another.__cents) if another.__cents < 10 else another.__cents
        cents = (float('0.' + str(self_cents)) + float('0.' + str(another_cents)))
        helper = str(cents).split('.')[1] + '0' if int(str(cents).split('.')[1]) < 10 else str(cents).split('.')[1]
        print(helper)
        return Money(self.__euros + another.__euros + int(cents), int(helper))
    
    def __sub__(self, another: 'Money') -> 'Money':
        self_cents = '0' + str(self.__cents) if self.__cents < 10 else self.__cents
        another_cents = '0' + str(another.__cents) if another.__cents < 10 else another.__cents
        cents = float(f'{(float('0.' + str(self_cents)) - float('0.' + str(another_cents))):.2}')
        helper = str(cents).split('.')[1] + '0' if int(str(cents).split('.')[1]) < 10 else str(cents).split('.')[1]
        print('ggg', (helper))
        if self.__euros - another.__euros >= 0:
            if cents >= 0:
                return Money(self.__euros - another.__euros, helper)
            else:
                n, d = str(1 - cents).split('.')

                if int(n) == 1:
                    raise ValueError('a negative result is not allowed')
                
                return Money(self.__euros - another.__euros - int(n), 100 - int(d))
        else:
            raise ValueError('a negative result is not allowed')


if __name__ == '__main__':
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    e1 = Money(15, 95)
    e2 = Money(15, 95)
    e1 = Money(1, 0)
    e2 = Money(1, 0)
    e1 = Money(4, 5)
    e2 = Money(0, 50)
    e1 = Money(15, 95)
    e2 = Money(1, 55)
    e1 = Money(4, 5)
    e2 = Money(4, 6)

    e3 = e1 + e2
    e4 = e1 - e2

    print('==>', e3)
    print('==>', e4)

    e5 = e2-e1
