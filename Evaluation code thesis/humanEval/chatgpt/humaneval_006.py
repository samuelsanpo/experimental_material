#\n\ndef prime_fib(n: int):\n    \"\"\"\n    prime_fib returns n-th number that is a Fibonacci number and it's also prime.\n    >>> prime_fib(1)\n    2\n    >>> prime_fib(2)\n    3\n    >>> prime_fib(3)\n    5\n    >>> prime_fib(4)\n    13\n    >>> prime_fib(5)\n    89\n    \"\"\"\n
def prime_fib(n: int):
    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a
