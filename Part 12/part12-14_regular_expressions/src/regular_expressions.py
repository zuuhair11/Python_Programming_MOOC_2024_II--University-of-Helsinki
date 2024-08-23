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


def all_vowels(my_string: str) -> bool:
    """First attempt"""
    return (re.search(r'\b[aeiou]+\b', my_string))

    """Second attempt"""
    return bool(re.match(r'\b[aeiou]+\b', my_string))

    """Third attempt"""
    return bool(re.fullmatch(r'[aeiou]+', my_string))


if __name__ == '__main__':
    print(all_vowels('eioueioieoieou')) # True
    print(all_vowels('autoooo'))        # False
