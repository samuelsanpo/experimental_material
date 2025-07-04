#from typing import List\n\n\ndef separate_paren_groups(paren_string: str) -> List[str]:\n    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\n    separate those group into separate strings and return the list of those.\n    Separate groups are balanced (each open brace is properly closed) and not nested within each other\n    Ignore any spaces in the input string.\n    >>> separate_paren_groups('( ) (( )) (( )( ))')\n    ['()', '(())', '(()())']\n    \"\"\"\n
from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    
    :param paren_string: str - The input string containing groups of parentheses
    :return: List[str] - A list of strings, each representing a separate group of parentheses
    """
    paren_string = paren_string.replace(" ", "")
    groups = []
    current_group = []
    balance = 0
    
    for char in paren_string:
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
        
        if balance == 0:
            groups.append(''.join(current_group))
            current_group = []
    
    return groups