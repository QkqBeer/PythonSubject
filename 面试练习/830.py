__author__ = "那位先生Beer"


def largeGroupPositions(S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    count = 1
    reList = []
    for i in range( 1, len( S ) ):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count >= 3:
                reList.append([i - count, i - 1])
            count = 1
    if count >= 3:
        reList.append([len(S) - count, len(S) - 1])
    print(reList)
largeGroupPositions("aaa")

