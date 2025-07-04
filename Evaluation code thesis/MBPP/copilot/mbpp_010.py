#Write a function text_match_word that matches a word at the end of a string, with optional punctuation.
def text_match_word(string, word):
    """
    This function checks if a given word matches the end of a string, allowing for optional punctuation.
    
    :param string: str - The input string to check
    :param word: str - The word to match at the end of the string
    :return: bool - True if the word matches at the end of the string, False otherwise
    """
    # Strip any trailing whitespace and punctuation from the string
    stripped_string = string.rstrip()
    
    # Check if the stripped string ends with the specified word
    return stripped_string.endswith(word)