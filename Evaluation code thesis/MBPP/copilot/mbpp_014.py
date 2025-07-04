#Write a function group_keyvalue to group a sequence of key-value pairs into a dictionary of lists.
def group_keyvalue(pairs):
    """
    This function groups a sequence of key-value pairs into a dictionary of lists.
    
    :param pairs: List[Tuple[Any, Any]] - A list of key-value pairs
    :return: Dict[Any, List[Any]] - A dictionary where each key maps to a list of values
    """
    grouped = {}
    
    for key, value in pairs:
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(value)
        
    return grouped