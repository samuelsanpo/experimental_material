#\ndef check_if_last_char_is_a_letter(txt):\n    '''\n    Create a function that returns True if the last character\n    of a given string is an alphabetical character and is not\n    a part of a word, and False otherwise.\n    Note: \"word\" is a group of characters separated by space.\n\n    Examples:\n    check_if_last_char_is_a_letter(\"apple pie\") \u279e False\n    check_if_last_char_is_a_letter(\"apple pi e\") \u279e True\n    check_if_last_char_is_a_letter(\"apple pi e \") \u279e False\n    check_if_last_char_is_a_letter(\"\") \u279e False \n    '''\n
def check_if_last_char_is_a_letter(txt):
    txt = txt.rstrip()  # Remove trailing spaces
    if not txt:
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    # Check if last char is separated by space (i.e., last word length == 1)
    words = txt.split(' ')
    return len(words[-1]) == 1
