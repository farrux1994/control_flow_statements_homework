def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    ans = ''
    if a>9 and a%2==1:
        ans = 'two-digit odd number'
    if a>0 and a%2==0:
        ans = 'two-digit even number'
    if a>99 and a%2==1:
        ans = 'three-digit odd number'
    if a>99 and a%2==0:
        ans = 'three-digit even number'
    return ans
y = main(57)
print(y)