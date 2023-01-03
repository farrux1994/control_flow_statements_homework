def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """ 
    ans = ''
    if a>0 and b>0 and c>0:
        ans = 'there a, b, c'
    elif a>0 and b<0 and c>0:
        ans = 'two a, c'
    elif a>0 and b<0 and c<0:
        ans = 'one a'
    elif a>0 and b>0 and c<0:
        ans = 'two a, c'
    elif a<0 and b>0 and c>0:
        ans = 'two b, c'
    elif a<0 and b<0 and c>0:
        ans = 'one c'
    elif a<0 and b<0 and c<0:
        ans = '0'
    return ans

y = main(-2, 4, 1)
print(y)