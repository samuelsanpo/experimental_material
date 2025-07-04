#\n\ndef sum_squares(lst):\n    \"\"\"You are given a list of numbers.\n    You need to return the sum of squared numbers in the given list,\n    round each element in the list to the upper int(Ceiling) first.\n    Examples:\n    For lst = [1,2,3] the output should be 14\n    For lst = [1,4,9] the output should be 98\n    For lst = [1,3,5,7] the output should be 84\n    For lst = [1.4,4.2,0] the output should be 29\n    For lst = [-2.4,1,1] the output should be 6\n    \n\n    \"\"\"\n
import math

def sum_squares(lst):
    return sum(math.ceil(x)**2 for x in lst)
