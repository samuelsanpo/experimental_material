#\ndef get_closest_vowel(word):\n    \"\"\"You are given a word. Your task is to find the closest vowel that stands between \n    two consonants from the right side of the word (case sensitive).\n    \n    Vowels in the beginning and ending doesn't count. Return empty string if you didn't\n    find any vowel met the above condition. \n\n    You may assume that the given string contains English letter only.\n\n    Example:\n    get_closest_vowel(\"yogurt\") ==> \"u\"\n    get_closest_vowel(\"FULL\") ==> \"U\"\n    get_closest_vowel(\"quick\") ==> \"\"\n    get_closest_vowel(\"ab\") ==> \"\"\n    \"\"\"\n
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2, 0, -1):
        if (word[i] in vowels and
            word[i-1] not in vowels and
            word[i+1] not in vowels):
            return word[i]
    return ""
