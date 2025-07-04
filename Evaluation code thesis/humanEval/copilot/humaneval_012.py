#\n\ndef sum_squares(lst):\n    \"\"\"You are given a list of numbers.\n    You need to return the sum of squared numbers in the given list,\n    round each element in the list to the upper int(Ceiling) first.\n    Examples:\n    For lst = [1,2,3] the output should be 14\n    For lst = [1,4,9] the output should be 98\n    For lst = [1,3,5,7] the output should be 84\n    For lst = [1.4,4.2,0] the output should be 29\n    For lst = [-2.4,1,1] the output should be 6\n    \n\n    \"\"\"\n
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    return sum((round(x) ** 2 for x in lst))