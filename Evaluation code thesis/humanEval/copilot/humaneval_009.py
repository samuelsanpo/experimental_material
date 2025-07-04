#\ndef tri(n):\n    \"\"\"Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in \n    the last couple centuries. However, what people don't know is Tribonacci sequence.\n    Tribonacci sequence is defined by the recurrence:\n    tri(1) = 3\n    tri(n) = 1 + n / 2, if n is even.\n    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.\n    For example:\n    tri(2) = 1 + (2 / 2) = 2\n    tri(4) = 3\n    tri(3) = tri(2) + tri(1) + tri(4)\n           = 2 + 3 + 3 = 8 \n    You are given a non-negative integer number n, you have to a return a list of the \n    first n + 1 numbers of the Tribonacci sequence.\n    Examples:\n    tri(3) = [1, 3, 2, 8]\n    \"\"\"\n
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    
    if n < 0:
        return []
    
    result = []
    
    for i in range(n + 1):
        if i == 0:
            result.append(1)
        elif i == 1:
            result.append(3)
        elif i % 2 == 0:
            result.append(1 + i // 2)
        else:
            result.append(result[i - 1] + result[i - 2] + result[i - (i - 1)])
    
    return result