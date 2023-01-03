def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x = a//10
    y = a%10
    z = int("%s%s"%(y,x))
    if z <= a:
        ans = True
    else: ans = False
    return ans
y = main(57)
print(y)