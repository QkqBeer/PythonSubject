__author__ = "那位先生Beer"


def combine(n, k ):
    S = [i + 1 for i in range( n )]
    val = []
    reList = []
    def build( S, val):
        if len( val ) == k:
            reList.append(val[:])
        else:
            for i in range( len( S ) ):
                val.append( S[i] )
                build( S[i + 1:], val)
                val.pop()

    build(S, val)
    return reList
print(combine(4, 2))