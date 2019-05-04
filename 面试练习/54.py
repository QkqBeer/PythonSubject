__author__ = "那位先生Beer"
def solution(matrix):
    x = len(matrix)
    y = len(matrix[0])
    #分为四步画圈，将每一个step置为已访问过
    flag = 1
    count = 0
    reList = []
    while flag <= x * y:
        #first step
        for i in range(count, y - count):
            reList.append(matrix[count][i])
            print(matrix[count][i])
            flag += 1
        #second step
        for i in range(count + 1, x - count - 1):
            reList.append(matrix[i][y - count - 1])
            flag += 1
        for i in range(y - count - 1, -1 + count, -1):
            reList.append(matrix[x - count - 1][i])
            flag += 1
        for i in range(x - count - 2, count, -1):
            reList.append(matrix[i][count])
            flag += 1
        count += 1
    return reList[:x * y]
print(solution([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))

