#Write a python function find_Sum to find the sum of repeated elements in a given array.
def find_Sum(arr):
    """
    This function takes an array of integers and returns the sum of all elements that appear more than once.
    
    :param arr: List[int] - A list of integers
    :return: int - The sum of repeated elements
    """
    from collections import Counter
    
    # Count the occurrences of each element in the array
    counts = Counter(arr)
    
    # Calculate the sum of elements that appear more than once
    repeated_sum = sum(key for key, value in counts.items() if value > 1)
    
    return repeated_sum