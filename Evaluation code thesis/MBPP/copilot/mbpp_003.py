#Write a function specified_element to extract every specified element from a given two dimensional list.
def specified_element(lst, element):
    """
    This function extracts every specified element from a given two-dimensional list.
    
    :param lst: List[List[Any]] - A two-dimensional list
    :param element: Any - The element to extract
    :return: List[Any] - A list of all occurrences of the specified element
    """
    result = []
    
    for sublist in lst:
        for item in sublist:
            if item == element:
                result.append(item)
                
    return result