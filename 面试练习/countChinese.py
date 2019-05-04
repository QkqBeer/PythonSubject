#coding:utf-8
f = open('qkq.txt', encoding='utf-8')
c = f.read()
dic = {}
for i in range(len(c)):
    if c[i] in dic:
        dic[c[i]] += 1
    else:
        dic[c[i]] = 1

print(dic)

