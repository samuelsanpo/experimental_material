#Write a python gcd function to check whether the given number is co-prime or not.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_coprime(x, y):
    return gcd(x, y) == 1
