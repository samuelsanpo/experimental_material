#\ndef pluck(arr):\n    \"\"\"\n    \"Given an array representing a branch of a tree that has non-negative integer nodes\n    your task is to pluck one of the nodes and return it.\n    The plucked node should be the node with the smallest even value.\n    If multiple nodes with the same smallest even value are found return the node that has smallest index.\n\n    The plucked node should be returned in a list, [ smalest_value, its index ],\n    If there are no even values or the given array is empty, return [].\n\n    Example 1:\n        Input: [4,2,3]\n        Output: [2, 1]\n        Explanation: 2 has the smallest even value, and 2 has the smallest index.\n\n    Example 2:\n        Input: [1,2,3]\n        Output: [2, 1]\n        Explanation: 2 has the smallest even value, and 2 has the smallest index. \n\n    Example 3:\n        Input: []\n        Output: []\n    \n    Example 4:\n        Input: [5, 0, 3, 0, 4, 2]\n        Output: [0, 1]\n        Explanation: 0 is the smallest value, but  there are two zeros,\n                     so we will choose the first zero, which has the smallest index.\n\n    Constraints:\n        * 1 <= nodes.length <= 10000\n        * 0 <= node.value\n    \"\"\"\n
def pluck(arr):
    """Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: