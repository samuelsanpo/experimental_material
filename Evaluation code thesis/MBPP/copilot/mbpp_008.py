#Write a function count_odd to find number of odd elements in the given list using lambda function.
def count_odd(lst):
    """
    This function counts the number of odd elements in a given list using a lambda function.
    
    :param lst: List[int] - A list of integers
    :return: int - The count of odd elements in the list
    """
    if not lst:
        return 0
    
    # Use filter with a lambda function to count odd numbers
    odd_count = len(list(filter(lambda x: x % 2 != 0, lst)))
    
    return odd_count