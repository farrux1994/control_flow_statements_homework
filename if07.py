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
    elif a>0:
        if a%2==0:
             print('musbat juft raqam')
    elif a<0:
        if a%2==1:
             print('salbiy toq raqam')
    elif a>0:
        if a%2==0:
             print('salbiy juft raqam')
    else:
        print('0 ga teng')
    return 0
y = main(0)