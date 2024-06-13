# Write your solution here
def get_average(person: dict) -> float:
    values = person.values()
    total = 0
    for value in values:
        if type(value) == int:
            total += value

    return total / len(values)


def smallest_average(*persons: dict) -> dict:
    smallest = {}

    for person in persons:
        if len(smallest) == 0 or get_average(smallest) > get_average(person):
            smallest = person

    return smallest


if __name__ == '__main__':
    person1 = { 'name': 'Mary', 'result1': 2, 'result2': 3, 'result3': 3 }
    person2 = { 'name': 'Gary', 'result1': 5, 'result2': 1, 'result3': 8 }
    person3 = { 'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1 }

    print(smallest_average(person1, person2, person3))
