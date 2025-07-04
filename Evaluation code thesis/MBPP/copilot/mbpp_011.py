#Write a function position_min to find all index positions of the minimum values in a given list.
def position_min(lst):
    """
    This function finds all index positions of the minimum values in a given list.
    
    :param lst: List[int] - A list of integers
    :return: List[int] - A list of indices where the minimum value occurs
    """
    if not lst:
        return []
    
    min_value = min(lst)
    return [i for i, value in enumerate(lst) if value == min_value]