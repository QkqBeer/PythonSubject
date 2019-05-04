__author__ = "那位先生Beer"
def choose_sort(data):
    for i in range(len(data)-1):
        for j in range(i,len(data)):
            if  data[i]>data[j]:
                temp = data[j]
                data[j] = data[i]
                data[i] = temp
d=[2,1,3,2,9,5,6,7,3,8]
choose_sort(d)
print(d)
