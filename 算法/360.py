__author__ = "那位先生Beer"
def solution():
    n = input()
    s = n.strip().split('/')
    N = int(s[0])
    S = s[1].split(',')
    res = []
    for i in range(len(S)):
        news = S[i].split('-')
        if len(news) > 1:
            for i in range(int(news[0]), int(news[1]) + 1):
                res.append(i)
        else:
            res.append(int(news[0]))
    dic = {}
    for i in range(len(res)):
        t = res[i] % N
        if t in dic:
            dic[t].append(res[i])
        else:
            dic[t] = []
            dic[t].append(res[i])
    M = 0
    MItem = 0
    for item in dic:
        if len(dic[item]) > M:
            M = len(dic[item])
            MItem = item
    r = str(M)+'-'+str(MItem)+'-'+str(dic[MItem][M - 1])
    b  = dic[item]
    newM = list(set(b))
    newM.sort()
    for k in range(len(newM) - 2, -1, -1):
        r = r + " " + str(newM[k])
    print(r)
solution()
