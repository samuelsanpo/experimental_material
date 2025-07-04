#Write a function count_pairs to count all the distinct pairs having a difference of k in any array.
def count_pairs(arr, k):
    """
    This function counts all distinct pairs in the array that have a difference of k.
    
    :param arr: List[int] - A list of integers
    :param k: int - The difference to check for
    :return: int - The count of distinct pairs with the given difference
    """
    if not arr or k < 0:
        return 0
    
    seen = set(arr)
    count = 0
    
    for num in seen:
        if (num + k) in seen:
            count += 1
            
    return count