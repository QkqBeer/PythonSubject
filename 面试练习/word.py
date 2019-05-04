def lengthOfLastWord(s ):
    """
    :type s: str
    :rtype: int
    """
    wordList = s.split( " " )
    print(wordList)
    for i in range( len( wordList ) ):
        if wordList[len( wordList ) - i - 1] != '':
            return len( wordList[len( wordList ) - i - 1] )
        else:
            continue
print(lengthOfLastWord('a  b  '))