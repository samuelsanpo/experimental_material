#\n\ndef how_many_times(string: str, substring: str) -> int:\n    \"\"\" Find how many times a given substring can be found in the original string. Count overlaping cases.\n    >>> how_many_times('', 'a')\n    0\n    >>> how_many_times('aaa', 'a')\n    3\n    >>> how_many_times('aaaa', 'aa')\n    3\n    \"\"\"\n
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlapping cases.
    
    :param string: str - The original string to search within
    :param substring: str - The substring to count occurrences of
    :return: int - The number of times the substring appears in the string, including overlaps
    """
    if not string or not substring:
        return 0
    
    count = 0
    start = 0
    
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move one character forward to allow for overlapping matches
    
    return count