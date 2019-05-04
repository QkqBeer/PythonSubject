__author__ = "那位先生Beer"


def toGoatLatin( S ):
    """
    :type S: str
    :rtype: str
    """
    newS = S.split( ' ' )
    for i in range( len( newS ) ):
        if newS[i][0].lower() not in ['a', 'e', 'i', 'o', 'u']:
            newS[i] = newS[i][1:] + newS[i][0] + 'm' + ((i + 2) * 'a')
        else:
            newS[i] = newS[i] + 'm' + ((i + 2) * 'a')
    print(' '.join( newS ))
toGoatLatin("The quick brown fox jumped over the lazy dog")