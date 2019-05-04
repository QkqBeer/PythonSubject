__author__ = "那位先生Beer"


def repeatedSubstringPattern(s):
    if len(s) == 1:
        return False
    elif len( s ) <= 3 and len( set( s ) ) >= 2:
        return False
    elif len( s ) <= 3 and len( set( s ) ) == 1:
        return True
    elif len(s) != 1 and len(set(s)) == 1:
        return True
    f = []
    for i in range( 2, (len( s ) // 2) + 1 ):
        if len( s ) % i == 0:
            f.append( i )

    for i in range(len(f)):
        flag = True
        for j in range((len(s) // f[i])):
            if ''.join( s[0:f[i]]) != ''.join( s[j * f[i]:(j + 1) * f[i]]):
                flag = False
                break
        if flag == True:
            return True
    return False
print(repeatedSubstringPattern("abcabcabcabc"))