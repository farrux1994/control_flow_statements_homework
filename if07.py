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
    if a>0 and a%2==1:
        print('musbat toq raqam')
    elif a>0 and a%2==0:
        print('musbat juft raqan')
    if a%2==1:
        print('toq raqam')
    elif a!=0 and a%2==0:
        print('juft raqan')
    elif a==0:
        print('0 ga teng')
    return 0
y = main(0)