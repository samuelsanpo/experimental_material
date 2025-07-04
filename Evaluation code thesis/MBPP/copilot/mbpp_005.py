#Write a function intersection_nested_lists to find the nested list elements which are present in another list.
def intersection_nested_lists(nested_list, other_list):
    """
    This function finds the elements in a nested list that are also present in another list.
    
    :param nested_list: List[List[int]] - A nested list of integers
    :param other_list: List[int] - A list of integers to check against
    :return: List[int] - A list of elements that are present in both the nested list and the other list
    """
    if not nested_list or not other_list:
        return []
    
    # Flatten the nested list
    flat_list = [item for sublist in nested_list for item in sublist]
    
    # Use set for faster lookup
    other_set = set(other_list)
    
    # Find intersection
    intersection = [item for item in flat_list if item in other_set]
    
    return intersection