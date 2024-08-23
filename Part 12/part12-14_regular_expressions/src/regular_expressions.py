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
    # return bool(re.match('^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', my_string))


def all_vowels(my_string: str) -> bool:
    """First attempt"""
    return bool(re.search(r'\b[aeiou]+\b', my_string))

    """Second attempt"""
    return bool(re.match(r'\b[aeiou]+\b', my_string))

    """Third attempt"""
    return bool(re.fullmatch(r'[aeiou]+', my_string))


def time_of_day(my_string: str) -> bool:
    """
    Returns True if the string matches the pattern, False otherwise.

    >>> time_of_day('12:43:01')
    True
    >>> time_of_day('AB:01:CD')
    False
    >>> time_of_day('17:59:59')
    True
    >>> time_of_day('33:66:77')
    False
    >>> time_of_day('00:00:00')
    True
    >>> time_of_day('23:59:59')
    True
    """

    """First attempt"""
    return re.fullmatch(r'([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])', my_string) is not None

    """Second attempt"""
    return re.search(r'^([01][0-9]|2[0-3])(:[0-5][0-9]){2}$', my_string) is not None


if __name__ == '__main__':
    print(time_of_day('12:43:01')) # True
    print(time_of_day('AB:01:CD')) # False
    print(time_of_day('17:59:59')) # True
    print(time_of_day('33:66:77')) # False
