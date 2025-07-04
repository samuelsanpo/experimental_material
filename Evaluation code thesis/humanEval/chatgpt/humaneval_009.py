#\ndef tri(n):\n    \"\"\"Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in \n    the last couple centuries. However, what people don't know is Tribonacci sequence.\n    Tribonacci sequence is defined by the recurrence:\n    tri(1) = 3\n    tri(n) = 1 + n / 2, if n is even.\n    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.\n    For example:\n    tri(2) = 1 + (2 / 2) = 2\n    tri(4) = 3\n    tri(3) = tri(2) + tri(1) + tri(4)\n           = 2 + 3 + 3 = 8 \n    You are given a non-negative integer number n, you have to a return a list of the \n    first n + 1 numbers of the Tribonacci sequence.\n    Examples:\n    tri(3) = [1, 3, 2, 8]\n    \"\"\"\n
def tri(n):
    # According to examples, tri(1)=3, tri(2)=2, tri(4)=3
    # The docstring example output tri(3) = [1,3,2,8] shows tri(0)=1 assumed
    # We'll implement accordingly, using memoization to handle tri(n+1) in odd case.

    memo = {}

    def trib(n):
        if n == 0:
            return 1
        if n == 1:
            return 3
        if n == 2:
            return 2
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            val = 1 + n // 2
        else:
            # tri(n) = tri(n-1) + tri(n-2) + tri(n+1)
            # To avoid infinite recursion, compute tri(n+1) carefully
            # We'll compute tri(n+1) only if n+1 <= maximum index in our calculation
            # But since this is recursion, we will compute tri(n+1) recursively.
            val = trib(n-1) + trib(n-2) + trib(n+1)
        memo[n] = val
        return val

    # To avoid infinite recursion for tri(n+1) when n is odd, limit calculation to n+1 by iterative approach:
    # Since tri(n+1) requires tri(n+2), etc, we'll instead calculate from bottom up for 0..n+1.

    # So implement bottom-up approach:

    seq = [0] * (n + 2)  # to cover tri(n+1)
    seq[0] = 1
    seq[1] = 3
    seq[2] = 2

    for i in range(3, n + 2):
        if i % 2 == 0:
            seq[i] = 1 + i // 2
        else:
            seq[i] = seq[i - 1] + seq[i - 2] + seq[i + 1] if i + 1 <= n + 1 else 0

    # Because seq[i] depends on seq[i+1], which is not known yet, the above bottom-up doesn't work directly.
    # The original recurrence with tri(n+1) on the right side is not standard and leads to circular dependency.

    # To solve this, we can try to rewrite the recurrence or solve iteratively from higher indexes downward.
    # Since tri(n+1) is on the right for odd n, and tri(n+1) depends on tri(n+2), etc, it's complex.

    # Alternative approach: implement memoized recursion with cache and detect max needed n, handle with LRU cache and maxdepth.

    from functools import lru_cache

    @lru_cache(None)
    def trib_rec(m):
        if m == 0:
            return 1
        if m == 1:
            return 3
        if m == 2:
            return 2
        if m % 2 == 0:
            return 1 + m // 2
        else:
            return trib_rec(m - 1) + trib_rec(m - 2) + trib_rec(m + 1)

    # To avoid infinite recursion, limit recursion depth by max m <= n+1.
    # So redefine trib_rec to return 0 if m > n+1

    def trib_safe(m):
        if m > n + 1:
            return 0
        if m == 0:
            return 1
        if m == 1:
            return 3
        if m == 2:
            return 2
        if m % 2 == 0:
            return 1 + m // 2
        else:
            return trib_safe(m - 1) + trib_safe(m - 2) + trib_safe(m + 1)

    # Compute first n+1 numbers using trib_safe

    return [trib_safe(i) for i in range(n + 1)]
