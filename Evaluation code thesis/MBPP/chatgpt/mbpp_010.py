#Write a function text_match_word that matches a word at the end of a string, with optional punctuation.
import re

def text_match_word(text, word):
    pattern = rf"{re.escape(word)}[.,;:!?]?$"
    return bool(re.search(pattern, text))
