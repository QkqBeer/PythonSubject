__author__ = "那位先生Beer"
def insert_sort(data):
    for i in range(1,len(data)):
        j=i-1
        while j>=0:  #因为生成的已经是有序的，所以利用类似冒泡的方式继续排列一次
            if data[i]<=data[j]:
                data[i],data[j]=data[j],data[i]
                j-=1
                i-=1
            else:
                break


def insert_sort_plus(data):
    for i in range(1,len(data)):
        temp=data[i]
        j=i-1
        while j>=0 and data[j]>temp:
            data[j+1]=data[j]
            j-=1
        data[j+1]=temp

d=[2,1,3,2,9,5,6,7,3,8]
#insert_sort(d)
insert_sort_plus(d)
print(d)
