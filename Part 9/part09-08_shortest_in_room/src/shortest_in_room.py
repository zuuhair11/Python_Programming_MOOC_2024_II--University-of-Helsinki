# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return not bool(self.persons)

    def print_contents(self):
        combined_height = sum(person.height for person in self.persons)
        length = len(self.persons)
        print('There are {} persons in the room, and their combined height is {} cm'.format(length, combined_height))

        for person in self.persons:
            print('{} ({} cm)'.format(person.name, person.height))

    def shortest(self):
        shortest_person = None

        for person in self.persons:
            if shortest_person == None or person.height < shortest_person.height:
                shortest_person = person

        return shortest_person
    
    def remove_shortest(self):
        # Utilizing the previous method
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)

        return shortest_person


if __name__ == '__main__':
    room = Room()

    room.add(Person('Lea', 183))
    room.add(Person('Kenya', 172))
    room.add(Person('Nina', 162))
    room.add(Person('Ally', 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f'Removed from room: {removed.name}')

    print()

    room.print_contents()
