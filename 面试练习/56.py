s = [[2,3],[4,5],[6,7],[8,9],[1,10]]
s.sort(key = lambda a : a[1])
for i in range(len(s)):
    print(s[i])