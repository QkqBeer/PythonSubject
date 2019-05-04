__author__="那位先生Beer"
def isSushu(num):
    flag = True
    for i in range( 2, num // 2 + 1 ):
        if (num % i) == 0:
            flag = False
            break
    return flag
def isTrue(i, num):
    flag = 1
    while i ** flag < num:
        flag += 1
    if i ** flag == num:
        return True
    else:
        return False
def solution(N):
    count = 0
    res = []
    for i in range(2, N + 1):
        if isSushu(i):
            res.append(i)
            count += 1
        else:
            for j in range(len(res)):
                if isTrue(res[j], i):
                    count += 1
                    break
    return count
print(solution(41))



