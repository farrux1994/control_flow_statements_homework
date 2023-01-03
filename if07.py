def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    ans = ''
    if a>0 and a%2==1:
        ans = 'positive odd number'
    if a>0 and a%2==0:
        ans = 'positive even number'
    if a<0 and a%2==1:
        ans = 'negative odd number'
    if a<0 and a%2==0:
        ans = 'negative even number'
    elif a==0:
        ans = 'the number is zero'
    return ans
y = main(0)
print(y)