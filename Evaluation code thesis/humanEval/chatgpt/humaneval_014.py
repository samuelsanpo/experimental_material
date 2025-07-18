#\ndef pluck(arr):\n    \"\"\"\n    \"Given an array representing a branch of a tree that has non-negative integer nodes\n    your task is to pluck one of the nodes and return it.\n    The plucked node should be the node with the smallest even value.\n    If multiple nodes with the same smallest even value are found return the node that has smallest index.\n\n    The plucked node should be returned in a list, [ smalest_value, its index ],\n    If there are no even values or the given array is empty, return [].\n\n    Example 1:\n        Input: [4,2,3]\n        Output: [2, 1]\n        Explanation: 2 has the smallest even value, and 2 has the smallest index.\n\n    Example 2:\n        Input: [1,2,3]\n        Output: [2, 1]\n        Explanation: 2 has the smallest even value, and 2 has the smallest index. \n\n    Example 3:\n        Input: []\n        Output: []\n    \n    Example 4:\n        Input: [5, 0, 3, 0, 4, 2]\n        Output: [0, 1]\n        Explanation: 0 is the smallest value, but  there are two zeros,\n                     so we will choose the first zero, which has the smallest index.\n\n    Constraints:\n        * 1 <= nodes.length <= 10000\n        * 0 <= node.value\n    \"\"\"\n
def pluck(arr):
    smallest_even = None
    index = -1
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if smallest_even is None or val < smallest_even:
                smallest_even = val
                index = i
    return [smallest_even, index] if smallest_even is not None else []
