def get_length(num):
    """
    A integer is given. Return the number of digits in it.

    Args:
        num (int): an interger value

    Returns:
        int: the number of digits
    """
    # return number of digits in integer
    return len(str(num))

print(get_length(324))