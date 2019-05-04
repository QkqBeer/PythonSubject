__author__ = "那位先生Beer"
n = 5
reList = [[-1 for j in range(5)] for i in range(5)]
flag = 1
m = 5 * 5
count = 0
while flag <= m:
    for i in range( count, n - count ):
        reList[count][i] = flag
        flag += 1
        # second step
    for i in range( count + 1, n - count - 1 ):
        reList[i][n - count - 1] = flag
        flag += 1

    if flag < m:
        for i in range( n - count - 1, -1 + count, -1 ):
            reList[n - count - 1][i] = flag
            flag += 1
    for i in range( n - count - 2, count, -1 ):
        reList[i][count] = flag
        flag += 1
    count += 1
print(reList)