import xlrd
import math
from pylab import *
from sklearn import preprocessing
import numpy as np
import scipy.stats as cs
data=xlrd.open_workbook('xqtest.xls')
shxrange=range(data.nsheets)
try:
    sh=data.sheet_by_name("1")
except:
    print("no sheeet")

print('输入先验概率70%，例如：70')
x=input('请输入先验概率：')
lu=int(x)
Arowlist=[]
for i in range(0,lu*50):
    rowa_data=sh.row_values(i)
    Arowlist.append(rowa_data)
A=np.array(Arowlist)
A=A[:,0:2]
Browlist=[]
for i in range(5000,5000+((100-lu)*50)):
    rowa_data=sh.row_values(i)
    Browlist.append(rowa_data)
B=np.array(Browlist)
B=B[:,0:2]
Amean=(A.mean(axis=0))#对鲈鱼数据按列求均值
Avar=A.var(axis=0)#对鲈鱼数据求方差
Bmean=B.mean(axis=0)#对鲑鱼数据按列求均值
Bvar=B.var(axis=0)#对鲑鱼数据求方差
pa=[];pb=[]

for j in A:
       #鲈鱼数据做鲈鱼的后验概率
       pluyu1 =( 1/sqrt(2*np.pi*Avar[0])*np.exp(-((j[0]-Amean[0])**2)/(2*Avar[0])))
       pluyu2 =(1/sqrt(2*np.pi*Avar[1] )*np.exp(-((j[1]-Amean[1])**2)/(2*Avar[1])))
       # 鲈鱼第一类数据做鲑鱼的后验概率
       pguiyu1= ( 1/sqrt(2*np.pi*Bvar[0]))*np.exp(-((j[0]-Bmean[0])**2)/(2*Bvar[0]))
       pguiyu2= ( 1/sqrt(2*np.pi*Bvar[1]))*np.exp(-((j[1]-Bmean[1])**2)/(2*Bvar[1]))
       pa.append([pluyu1,pluyu2])
       pb.append([pguiyu1,pguiyu2])
for j in B:
       #鲑鱼数据做鲈鱼的后验概率
       pluyu1 =( 1/sqrt(2*np.pi*Avar[0])*np.exp(-((j[0]-Amean[0])**2)/(2*Avar[0])))
       pluyu2= ( 1/sqrt(2*np.pi*Avar[1])*np.exp(-((j[1]-Amean[1])**2)/(2*Avar[1])))
       #鲑鱼数据做鲑鱼的后验概率
       pguiyu1 =(1/sqrt(2*np.pi*Bvar[0]))*np.exp(-((j[0]-Bmean[0])**2)/(2* Bvar[0]))
       pguiyu2= ( 1/sqrt(2*np.pi*Bvar[1]))*np.exp(-((j[1]-Bmean[1])**2)/(2*Bvar[1]))
       pa.append([pluyu1,pluyu2])
       pb.append([pguiyu1,pguiyu2])
p1=(lu/100)
p2=(1-p1)
lph=[]
gph=[]
count=0
#计算两种数据的后验概率乘积，实现归类
for j in range(len(pb)):
       ply = np.prod(pa[j])*p1; #prod()累乘函数
       pgy = np.prod(pb[j])*p2;
       if ply>pgy:
           lph.append(pa[j])
       else:
           gph.append(pb[j])


lph=np.array(lph)


#数据，数组，颜色，颜色深浅，组宽，显示频率
plt.hist(lph, bins =7, color =['r','g'] ,alpha=0.5,rwidth= 0.5)

plt.title('A posteriori probability')
plt.xlabel('probability ')
plt.ylabel('number')
plt.show()
