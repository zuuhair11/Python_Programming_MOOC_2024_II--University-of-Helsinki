def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    
    # Get ride of the first character if it's not any bracket
    if not my_string[0] in '()[]':
        return balanced_brackets(my_string[1:])

    # Get ride of the last character if it's not any bracket
    if not my_string[-1] in '()[]':
        return balanced_brackets(my_string[:-1])
    
    # Now we know that the first and the last characters are brackets
    # Check if they are pair
    if my_string[0] == '(' and my_string[-1] == ')':
        return balanced_brackets(my_string[1:-1])

    if my_string[0] == '[' and my_string[-1] == ']':
        return balanced_brackets(my_string[1:-1])
    
    # They are not!
    return False


if __name__ == '__main__':
    ok = balanced_brackets('([([])])')
    print(ok) # True

    ok = balanced_brackets('(python version [3.7]) please use this one!')
    print(ok) # True

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets('(()]')
    print(ok) # False

    ok = balanced_brackets("([bad egg)]")
    print(ok) # False
