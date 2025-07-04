#from typing import List\n\n\ndef separate_paren_groups(paren_string: str) -> List[str]:\n    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\n    separate those group into separate strings and return the list of those.\n    Separate groups are balanced (each open brace is properly closed) and not nested within each other\n    Ignore any spaces in the input string.\n    >>> separate_paren_groups('( ) (( )) (( )( ))')\n    ['()', '(())', '(()())']\n    \"\"\"\n
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    s = paren_string.replace(" ", "")
    groups = []
    balance = 0
    start = 0
    for i, ch in enumerate(s):
        if ch == '(':
            if balance == 0:
                start = i
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance == 0:
                groups.append(s[start:i+1])
    return groups
