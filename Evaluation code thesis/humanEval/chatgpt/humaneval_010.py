#\ndef sort_array(arr):\n    \"\"\"\n    In this Kata, you have to sort an array of non-negative integers according to\n    number of ones in their binary representation in ascending order.\n    For similar number of ones, sort based on decimal value.\n\n    It must be implemented like this:\n    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]\n    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]\n    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]\n    \"\"\"\n
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
