# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if not self.numbers:
            return 0.0
        else:
            return self.get_sum() / self.count_numbers()


print('Please type in integer numbers:')
stats = NumberStats()
even = NumberStats()
odd = NumberStats()

while True:
    number = int(input())

    if number == -1:
        print('Sum of numbers:', stats.get_sum())
        print('Mean of numbers:', stats.average())
        print('Sum of even numbers: %d' %even.get_sum())
        print('Sum of odd numbers: {}'.format(odd.get_sum()))
        break

    stats.add_number(number)
    if number % 2 == 0:
        even.add_number(number)
    else:
        odd.add_number(number)
