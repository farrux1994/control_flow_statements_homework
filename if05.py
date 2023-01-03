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
    ans = ''
    if a>0 and b<0 and c>0:
        ans = '1'
    if a>0 and b<0 and c<0:
        ans = '2'
    if a>0 and b>0 and c<0:
        ans = '1'
    if a<0 and b>0 and c>0:
        ans = '1'
    if a<0 and b<0 and c>0:
        ans = '2'
    if a<0 and b<0 and c<0:
        ans = '3'
    return ans

y = main(-2, 4, 1)
print(y)