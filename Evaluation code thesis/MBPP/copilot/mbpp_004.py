#Write a python gcd function to check whether the given number is co-prime or not.
def gcd(a, b):
    """
    This function computes the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    
    :param a: int - First number
    :param b: int - Second number
    :return: int - The GCD of the two numbers
    """
    while b:
        a, b = b, a % b
    return a