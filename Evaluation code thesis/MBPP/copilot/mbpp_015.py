#Write a python function frequency_Of_Largest to find the frequency of the largest value in a given array.
def frequency_Of_Largest(arr):
    """
    This function finds the frequency of the largest value in a given array.
    
    :param arr: List[int] - A list of integers
    :return: int - The frequency of the largest value in the array
    """
    if not arr:
        return 0
    
    # Find the maximum value in the array
    max_value = max(arr)
    
    # Count how many times the maximum value appears in the array
    frequency = arr.count(max_value)
    
    return frequency