def get_sum_digits(num):
    """
    A integer is given. Return the sum of digits in it.
    
    Args:
        num (int): an integer value
    
    Returns:
        int: the sum of digits
    """
    # return sum of digits in integer
    if len(str(num))==1:
        return num
    if len(str(num))==2:
        return num//10+num%10
    if len(str(num))==3:
        return num//100+(num//10)%10+num%10
    
print(get_sum_digits(154))