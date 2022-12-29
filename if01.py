def main(a):
    """
    If the number is positive, increase it to 1, else leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a:
        a += 1
    else: a = a
    return int(a)
y = main(1)
print(y)
