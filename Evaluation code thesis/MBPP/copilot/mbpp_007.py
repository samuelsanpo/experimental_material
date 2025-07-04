#Write a function extract_string to extract specified size of strings from a give list of string values.
def extract_string(string_list, size):
    """
    This function extracts strings of a specified size from a given list of string values.
    
    :param string_list: List[str] - A list of strings
    :param size: int - The specified size of strings to extract
    :return: List[str] - A list of strings that match the specified size
    """
    if not string_list or size < 0:
        return []
    
    # Use list comprehension to filter strings by size
    extracted_strings = [s for s in string_list if len(s) == size]
    
    return extracted_strings