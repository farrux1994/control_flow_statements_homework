def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a>0 and b>0 and c>0:
            print('manfiy son yo\'q')
    elif a>0 and b<0 and c>0:
        print('1 ta')
    elif a>0 and b<0 and c<0:
        print('2 ta')
    elif a>0 and b>0 and c<0:
        print('1 ta')
    elif a<0 and b>0 and c>0:
        print('1 ta')
    elif a<0 and b<0 and c>0:
        print('2 ta')
    elif a<0 and b<0 and c<0:
        print('3 ta')
    return 0

y = main(-2, 4, 1)