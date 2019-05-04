__author__ = "那位先生Beer"
#coding:utf-8
#一维问题的分类
#导入画图和 矩阵的包
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#设定两类数据的 期望 和方差(特征分别为 长度 和 宽)
mu1_1= 3; sigma1_1=0.6; mu1_2= 3.5; sigma1_2=0.4;
mu2_1= 6; sigma2_1=1.2; mu2_2= 7.5; sigma2_2=1.2;
N=5000;
#生成服从分布的数据
S1=np.random.normal(mu1_1, sigma1_1, N ) #5000条鲈鱼长度
S2=np.random.normal(mu1_2, sigma1_2, N ) #鲈鱼宽度
L1=np.random.normal(mu2_1, sigma2_1, N ) #鲑鱼长度
L2=np.random.normal(mu2_2, sigma2_2, N ) #鲑鱼宽度
#存储生成的数据 并且加标签(0为鲈鱼，1为鲑鱼)
S=np.array([S1,S2]);Z=np.zeros((1,5000));S=np.vstack((S,Z));S=S.T;
L=np.array([L1,L2]);O=np.ones((1,5000));L=np.vstack((L,O));L=L.T;
import xlwt
w = xlwt.Workbook() #创建一个工作簿
ws = w.add_sheet('1')
counti=0
countj=0
for i in S:
    for j in i:
        ws.write(counti,countj,j)
        countj=countj+1
    countj=0
    counti=counti+1
for i in L:
    for j in i:
        ws.write(counti,countj,j)
        countj=countj+1
    countj=0
    counti=counti+1
w.save('xqtest.xls')
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
#根据生成的数据画出图像（横坐标为长度，纵坐标为亮度）
plt.figure(figsize=(8,6))
plt.title("生成的鲈鱼和鲑鱼数据的散点图",fontproperties=font_set)
plt.xlabel("长度",fontproperties=font_set)
plt.ylabel("宽度",fontproperties=font_set)
plt.scatter(S[:,0],S[:,1],marker="o",label="鲈鱼")
plt.scatter(L[:,0],L[:,1],marker="s",label="鲑鱼")
plt.legend()
plt.show()
