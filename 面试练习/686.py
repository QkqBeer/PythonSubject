__author__ = "那位先生Beer"

import copy
def repeatedStringMatch( self, A, B ):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    if set( A ) < set( B ):
        return -1
    if len( A ) > len( B ):
        if A.count( B ) >= 1:
            return 1
        else:
            return 2 if (A * 2).count( B ) >= 1 else -1
    count = 1
    cp = copy( A )
    while B not in A:
        A += cp
        count += 1
        if len( A ) >= 3 * len( B ):
            return -1
    return count


print(repeatedStringMatch("abcd", "cdabcdab"))