# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.euros = euros
        self.cents = cents

    def __str__(self):
        cents = '0' + str(self.cents) if self.cents < 10 else self.cents
        return f'{self.euros}.{cents} eur'
    
    def __eq__(self, another: 'Money') -> bool:
        return (self.euros == another.euros) and (self.cents == another.cents)
    
    def __ne__(self, another: 'Money') -> bool:
        return self.euros + self.cents != another.euros + another.cents
    
    def __lt__(self, another: 'Money') -> bool:
        return self.euros + self.cents < another.euros + another.cents
    
    def __gt__(self, another: 'Money') -> bool:
        return self.euros + self.cents > another.euros + another.cents


if __name__ == '__main__':
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)
