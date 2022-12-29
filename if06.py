def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a>0 and b>0 and c>0:
            print('3 ta musbat son bor')
    elif a>0 and b<0 and c>0:
        print('2 ta musbat 1 ta manfiy son bor')
    elif a>0 and b<0 and c<0:
        print('1 ta musbat 2 ta manfiy son bor')
    elif a>0 and b>0 and c<0:
        print('2 ta musbat 1 ta manfiy son bor')
    elif a<0 and b>0 and c>0:
        print('2 ta ta musbat 1 ta manfiy son bor')
    elif a<0 and b<0 and c>0:
        print('1 ta musbat 2 ta manfiy son bor')
    elif a<0 and b<0 and c<0:
        print('musbat va manfiy son yo\'q')
    return 0

y = main(-2, 4, 1)