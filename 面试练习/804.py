__author__ = "那位先生Beer"


def uniqueMorseRepresentations( words ):
    """
    :type words: List[str]
    :rtype: int
    """
    wordCode = set()
    code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
            ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    for i in range( len( words ) ):
        s = words[i]
        password = ''
        for j in range( len( s ) ):
            t = ord( s[j] ) % 97
            password += code[t]
        wordCode.add(password)
    print(len(wordCode))
uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])