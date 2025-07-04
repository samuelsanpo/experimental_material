#\ndef check_if_last_char_is_a_letter(txt):\n    '''\n    Create a function that returns True if the last character\n    of a given string is an alphabetical character and is not\n    a part of a word, and False otherwise.\n    Note: \"word\" is a group of characters separated by space.\n\n    Examples:\n    check_if_last_char_is_a_letter(\"apple pie\") \u279e False\n    check_if_last_char_is_a_letter(\"apple pi e\") \u279e True\n    check_if_last_char_is_a_letter(\"apple pi e \") \u279e False\n    check_if_last_char_is_a_letter(\"\") \u279e False \n    '''\n
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") => False
    check_if_last_char_is_a_letter("apple pi e") => True
    check_if_last_char_is_a_letter("apple pi e ") => False
    check_if_last_char_is_a_letter("") => False 
    '''
    txt = txt.rstrip()  # Remove trailing spaces
    if not txt:  # Check if the string is empty after stripping
        return False
    
    last_char = txt[-1]  # Get the last character
    if last_char.isalpha():  # Check if it is an alphabetical character
        # Check if the last character is not part of a word (i.e., not followed by a space)
        return len(txt) == 1 or txt[-2] == ' '
    
    return False