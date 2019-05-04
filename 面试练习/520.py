__author__ = "那位先生Beer"


def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if len(word) == 1:
        return True
    return word.upper() == word or word.lower() == word or word[0].upper() + word[1:].lower() == word
print(detectCapitalUse('FlaG'))