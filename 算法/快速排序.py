__author__ = "那位先生Beer"
'''def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList
myList = [49,38,65,97,76,13,27,49]
print("Quick Sort: ")
QuickSort(myList,0,len(myList)-1)
print(myList)'''

#自己写的快速排序
# def quick_sort(data, left, right):
#     start = left
#     end = right
#     temp = data[left]
#     if left < right:
#         while left < right:
#             while left < right and data[right] > temp:
#                 right -= 1
#             data[left] = data[right]
#             while left < right and data[left] <= temp:
#                 left += 1
#             data[right] = data[left]
#         data[left] = temp
#         quick_sort(data, start, left - 1)
#         quick_sort(data, left + 1, end)
#     return data
# data = [49,38,65,97,76,13,27,49]
# print(quick_sort(data, 0, len(data) - 1))

#
# def kuaipai(data, left, right):
#     low = left
#     high = right
#     tmp = data[left]
#     if left < right:
#         while left < right:
#             while left < right and data[right] > tmp:
#                 right -= 1
#             data[left] = data[right]
#             while left < right and data[left] <= tmp:
#                 left += 1
#             data[right] = data[left]
#         data[left] = tmp
#         kuaipai(data, low, left - 1)
#         kuaipai(data, left + 1, high)
#     return data
# data = [49,38,65,97,76,13,27,49]
# print(kuaipai(data, 0, len(data) - 1))



def k(left, right, data):
    low = left
    high = right
    tmp = data[left]
    if left < right:
        while left < right:
            while left < right and data[right] > tmp:
                right -= 1
            data[left] = data[right]
            while left < right and data[left] <= tmp:
                left += 1
            data[right] = data[left]
        data[left] = tmp
        k(low, left - 1, data)
        k(left + 1, high, data)

data = [49,38,65,97,76,13,27,49]
k(0, len(data) - 1, data)
print(data)
















