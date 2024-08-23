# Write your solution here
import re

def is_dotw(my_string: str) -> bool:
    """First attempt"""
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    matched = re.search(r'[A-Z][a-z]{2}$', my_string)
    if matched:
        return matched.group() in week

    return False

    """Second attempt"""
    return bool(re.match('^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', my_string))


if __name__ == '__main__':
    print(is_dotw('Mon')) # True
    print(is_dotw('Fri')) # True
    print(is_dotw('Tui')) # False
