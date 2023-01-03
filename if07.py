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
    if a>0:
        if a%2==1:
             print('musbat toq raqam')
    if a>0:
        if a%2==0:
             print('musbat juft raqam')
    if a<0:
        if a%2==1:
             print('salbiy toq raqam')
    if a>0:
        if a%2==0:
             print('salbiy juft raqam')
    if a==0:
        print('0 ga teng')
    return 0
y = main(5)