#Write a function larg_nnum to get the n largest items from a dataset.
def larg_nnum(arr, n):
    """
    This function returns the n largest items from a dataset.
    
    :param arr: List[int] - A list of integers
    :param n: int - The number of largest items to return
    :return: List[int] - A list containing the n largest items
    """
    if not arr or n <= 0:
        return []
    
    # Sort the array in descending order and return the first n elements
    return sorted(arr, reverse=True)[:n]