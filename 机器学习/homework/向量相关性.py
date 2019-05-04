__author__ = "那位先生Beer"
import math
#计算特征和类的平均值
def calcMean(x,y):
   sum_x = sum(x)
   sum_y = sum(y)
   n = len(x)
   x_mean = float(sum_x+0.0)/n
   y_mean = float(sum_y+0.0)/n
   return x_mean,y_mean

#计算Pearson系数
def calcPearson(x,y):
    x_mean,y_mean = calcMean(x,y)   #计算x,y向量平均值
    n = len(x)
    sumTop = 0.0
    x_pow = 0.0
    y_pow = 0.0
    for i in range(n):
        sumTop += (x[i]-x_mean)*(y[i]-y_mean)
    for i in range(n):
        x_pow += math.pow(x[i]-x_mean,2)
    for i in range(n):
        y_pow += math.pow(y[i]-y_mean,2)
    sumBottom = math.sqrt(x_pow*y_pow)
    p = sumTop/sumBottom
    return p


f1=input('输入第一个向量')
x=f1.split()
f2=input('输入第二个向量')
y=f2.split()
q=[]
p=[]
for i in x:
    j=int(i)
    q.append(j)

for i in y:
    j=int(i)
    p.append(j)
#画图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x1 = np.linspace( 0,q[0])
y1 = np.linspace(0,q[1])
z1 = np.linspace(0,q[2])
x2 = np.linspace( 0,p[0])
y2 = np.linspace(0,p[1])
z2 = np.linspace(0,p[2])
# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D( fig )

# 绘制线型图
ax.plot( x1, y1, z1 )
ax.plot( x2, y2, z2 )
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('两个向量之间的相关系数为'+str(calcPearson(q,p)))

# 显示图
plt.show()


