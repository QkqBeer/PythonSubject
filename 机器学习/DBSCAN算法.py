import xlrd
import math
import numpy as np
import pylab as plt

data = xlrd.open_workbook('DBSCAN聚类数据集.xlsx')
table = data.sheets()[0]

nrows = table.nrows #行数

ncols = table.ncols #列数
data=[]
for i in range(1,nrows):
    rowValues= table.row_values(i) #某一行数据
    for item in rowValues:
        data.append(item)

#数据处理 dataset是100个样本（chlorides，free sulfur dioxide）的列表
dataset = [(int(data[i]), int(data[i+1])) for i in range(0, len(data), 2)]

#计算欧几里得距离,a,b分别为两个元组
def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))




#算法模型
def DBSCAN(D, e, Minpts):
    #初始化核心对象集合T,聚类个数k,聚类集合C, 未访问集合P,
    T = set(); k = 0; C = []; P = set(D)
    for d in D:
        if len([ i for i in D if dist(d, i) <= e]) >= Minpts:
            T.add(d)
    #开始聚类
    while len(T):
        P_old = P
        o = list(T)[np.random.randint(0, len(T))]
        P = P - set(o)
        Q = []; Q.append(o)
        while len(Q):
            q = Q[0]
            Nq = [i for i in D if dist(q, i) <= e]
            if len(Nq) >= Minpts:
                S = P & set(Nq)
                Q += (list(S))
                P = P - S
            Q.remove(q)
        k += 1
        Ck = list(P_old - P)
        T = T - set(Ck)
        C.append(Ck)
    return C
# 画图
def draw(C):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(C)):
        coo_X = []    #x坐标列表
        coo_Y = []    #y坐标列表
        for j in range(len(C[i])):
            coo_X.append(C[i][j][0])
            coo_Y.append(C[i][j][1])
        plt.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)

    plt.legend(loc='upper right')
    plt.show()



# def draw(C):
#     Xw = []  # x坐标列表
#     Yw = []  # y坐标列表
#     for i in range(len(C)):
#         for j in range(len(C[i])):
#             Xw.append(C[i][0])
#             Yw.append(C[i][1])
#     plt.xlim(xmax=50, xmin=0)
#     plt.ylim(ymax=150, ymin=0)
#     plt.plot(Xw, Yw, 'ro')
#     plt.show()
C = DBSCAN(dataset, 5 ,10)
draw(C)
