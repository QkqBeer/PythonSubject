__author__ = "那位先生Beer"
import sys

def countNode(dic, i):
    count = 0
    if i in dic:
        for j in range(len(dic[i])):
            s = dic[i]
            count += countNode(dic, s[j])
        return count + len( s )
    else:
        return 0


def solution(dic):
    N = int( input() )
    list1 = []
    dic = {}
    while len( set( list1 ) ) < N:
        line = sys.stdin.readline().strip()
        list2 = list( map( int, line.split() ) )
        m, n = list2[0], list2[1]
        list1.append( m )
        list1.append( n )
        if n in dic:
            dic[n].append( m )
        else:
            dic[n] = [m]
    print(dic)
    res = []
    for i in range(len(dic[1])):
        t = countNode(dic, dic[1][i])
        if t == 0:
            res.append(1)
        else:
            res.append(t + 1)
    count = 0
    while len(res) > 0:
        count += 1
        if len(res) >= 2:
            indexMax = res.index(max(res))
            indexMin = res.index(min(res))
            res[indexMax] -= 1
            res[indexMin] -= 1
        else:
            res[0] -= 1
        if 0 in res:
            res.remove(0)
    print(count)

solution({1:[2,6,7], 2:[3], 3:[4,5]})


