#Write a function extract_string to extract specified size of strings from a give list of string values.
def extract_string(strings, size):
    return [s for s in strings if len(s) == size]
