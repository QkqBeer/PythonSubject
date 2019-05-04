__author__ = "那位先生Beer"
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import xlrd
import numpy as np
print('输入鲈鱼的先验概率例如：70，对应70%')
a=input('输入鲈鱼的先验概率（鲑鱼对应的1减去剩余的）：')
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
#根据生成的数据画出图像（横坐标为长度，纵坐标为亮度）
data=xlrd.open_workbook('xqtest.xls')
shxrange=range(data.nsheets)
sh=data.sheet_by_name("1")
L=[]
for i in range(0,(int(a))*50):
    rowa_data=sh.row_values(i)
    L.append(rowa_data)
L=np.array(L)
L=L[:,0:2]

G=[]
for j in range(5000,5000+(100-int(a))*50):
    rowa_data = sh.row_values(j)
    G.append(rowa_data)
G=np.array(G)
G=G[:,0:2]
plt.figure(figsize=(8,6))
plt.title("生成的鲈鱼和鲑鱼数据的散点图",fontproperties=font_set)
plt.xlabel("长度",fontproperties=font_set)
plt.ylabel("宽度",fontproperties=font_set)
plt.scatter(L[:,0],L[:,1],marker="o",label="鲈鱼")
plt.scatter(G[:,0],G[:,1],marker="s",label="鲑鱼")
# 分类模型
x = np.linspace(0,8)
y = -x+9
plt.plot(x,y, color="red")
plt.legend()
plt.show()


#模拟的数据鲈鱼比较小，可得出其在直线下面，即y+x<=9：
#计算准确率
count=0
for i in L:
    if i[0]+i[1]<=9:
        count=count+1
q=(count/((int(a))*50))
print('鲈鱼准确率：%s'%(count/((int(a))*50)))
countG=0
for i in G:
    if i[0]+i[1]>=9:
        countG=countG+1
p=(countG/((100-int(a))*50))
print('鲑鱼准确率：%s'%(countG/((100-int(a))*50)))

#p(b)=p(b|a)*p(a) + p(b|-a)p(-a)
pb=(int(a)/100)*q + (1-(int(a)/100))*p
print(pb)
#p(ab)=p(b|a)*p(a)
pab=(int(a)/100)*q
print(pab)
print(pab/pb)
