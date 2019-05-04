__author__ = "那位先生Beer"
def bubble_sort(data):
    count=len(data)-1
    exchange=False
    while count>=1:
        for i in range(count):
            if data[i]>data[i+1]:
                temp=data[i]
                data[i]=data[i+1]
                data[i+1]=temp
                exchange=True
        count-=1
        if not exchange:#代码优化，避免无用排序
            break
d=[2,1,3,2,9,5,6,7,3,8]
bubble_sort(d)
print(d)
