import unittest


def digits(x):
    """Convert an integer into a list of digits.

    Args:
        x: The number whose digits we want

    Returns:
        A list of digits, in order, of ``x``.

    >>> digits(4586378)
    [4,5,8,6,3,7,8]
    """

    digs = []
    while x != 0:
        div, mod = divmod(x, 10)
        digs.append(mod)
        x = mod
    return digs


def is_palindrome(x):
    """Determine if an integer is a palindrome.

    Args:
        x: The number to check for palindromicity

    Returns:
        True if the digits of ``x`` are palindrome,
        False, otherwise.

    >>> is_palindrome(1234)
    False
    >>>> is_palindrome(2468642)
    True
    """
    digs = digits(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
    return True
