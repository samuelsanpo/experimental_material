#from typing import List\n\n\ndef filter_by_substring(strings: List[str], substring: str) -> List[str]:\n    \"\"\" Filter an input list of strings only for ones that contain given substring\n    >>> filter_by_substring([], 'a')\n    []\n    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')\n    ['abc', 'bacd', 'array']\n    \"\"\"\n
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.
    
    :param strings: List[str] - A list of strings to filter
    :param substring: str - The substring to search for in each string
    :return: List[str] - A list of strings that contain the specified substring
    """
    if not strings or not substring:
        return []
    
    # Use list comprehension to filter strings containing the substring
    filtered_strings = [s for s in strings if substring in s]
    
    return filtered_strings