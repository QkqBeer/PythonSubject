# -*- coding: utf-8 -*-

'''
====================
3D plots as subplots
====================

Demonstrate including 3D plots as subplots.
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
import numpy as np
import scipy.stats as cs
from sklearn import preprocessing
import math
import xlrd
import scipy.io as sio
from scipy import *
from pylab import *
data=xlrd.open_workbook('xqtest.xls')
shxrange=range(data.nsheets)
try:
    sh=data.sheet_by_name("1")
except:
    print("no sheeet")
nrows=sh.nrows#获取行数
ncols=sh.ncols-1#获取列数
Arowlist=[]
for i in range(0,nrows//2):
    rowa_data=sh.row_values(i)
    Arowlist.append(rowa_data)
A=np.array(Arowlist)
A=A[:,0:2]
Browlist=[]
for i in range(nrows//2,nrows):
    rowa_data=sh.row_values(i)
    Browlist.append(rowa_data)
B=np.array(Browlist)
B=B[:,0:2]
#A中存储的为鲈鱼，B中存储的为鲑鱼
Amean=(A.mean(axis=0))
Avar=cov(A.T)
Bmean=B.mean(axis=0)
Bvar=cov(B.T)
# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

#===============
#  First subplot
#===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# plot a 3D surface like in the example mplot3d/
# 生成三维坐标轴的X轴和Y轴，并生成网格
X = np.arange(0, 5, 0.25)
Y = np.arange(0, 5, 0.25)
X, Y = np.meshgrid(X, Y)

# 生成标准正态分布的概率分布模型
gass = cs.multivariate_normal(
    Amean[:],
    Avar[:,:],
)

# 将X Y的大小变成1*1600， 并转成列表
X1 = X.reshape((1,400)).tolist()
Y1 = Y.reshape((1,400)).tolist()

# 通过列表的形式将X Y 合并，并转回数组
Zz = np.array([X1[0], Y1[0]])

# 因为gass.pdf函数需要的是 （1600， 2） 的输入格式，所以这里将数组进行转置
Z = gass.pdf(Zz.T)

# 将计算得到的X Y对应坐标的Z值数组 变回（60， 60）这样就可以和初始的X Y网格进行对应
Z = Z.reshape((20,20))

# 调用三维画曲面图的函数，绘制图形
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# 在图像旁边显示颜色条，标注不同颜色代表的数值
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.title("luyu")
ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D surface like in the example mplot3d/
# 生成三维坐标轴的X轴和Y轴，并生成网格
X = np.arange(2, 12, 0.25)
Y = np.arange(2, 12, 0.25)
X, Y = np.meshgrid(X, Y)

# 生成标准正态分布的概率分布模型
gass = cs.multivariate_normal(
    Bmean[:],
    Bvar[:, :],
)

# 将X Y的大小变成1*1600， 并转成列表
X1 = X.reshape((1,1600)).tolist()
Y1 = Y.reshape((1,1600)).tolist()

# 通过列表的形式将X Y 合并，并转回数组
Zz = np.array([X1[0], Y1[0]])

# 因为gass.pdf函数需要的是 （1600， 2） 的输入格式，所以这里将数组进行转置
Z = gass.pdf(Zz.T)

# 将计算得到的X Y对应坐标的Z值数组 变回（40， 40）这样就可以和初始的X Y网格进行对应
Z = Z.reshape((40,40))

# 调用三维画曲面图的函数，绘制图形
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot',
                       linewidth=0, antialiased=False)

# 在图像旁边显示颜色条，标注不同颜色代表的数值
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.title("guiyu")
# 显示图像
plt.show()