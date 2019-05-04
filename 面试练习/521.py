__author__ = "那位先生Beer"
import collections
def findLUSlength(a, b ):
    if a == b:
        return -1
    res = collections.Counter(a)
    res2 = collections.Counter(b)
    print(type(res))
    print(res2.key())
findLUSlength('aabbddd','kkkkssddasdcsd')