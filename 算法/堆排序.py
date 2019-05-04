# __author__ = "那位先生Beer"
# #构建堆
# # def build_heap(data):
# #     i=0
# #     while 2*i+1<len(data):
# #         if 2*(i+1)<len(data): #判断右子是否存在
# #             if data[2*i+1]<data[2*(i+1)]:
# #                 temp=data[2*(i+1)]
# #             else:
# #                 temp = data[2*i+1]
# #         else:
# #             if data[2*i+1]>data[i]:
# #                 temp=data[2*i+1]
# #             else:
# #                 temp=data[i]
# #         data[i]=temp
# #         i+=1
# #
# #
# # d=[5,3,4,6,3,7,1,2,9,0]
# #
# # build_heap(d)
# # print(d)
#
#
#
# # def fixDown( a, k, n ):  # 自顶向下堆化，从k开始堆化
# #     N = n - 1
# #     while 2 * k <= N:
# #         j = 2 * k
# #         if j < N and a[j] < a[j + 1]:  # 选出左右孩子节点中更大的那个
# #             j += 1
# #         if a[k] < a[j]:
# #             a[k], a[j] = a[j], a[k]
# #             k = j
# #         else:
# #             break
# #
# #
# # def heapSort( l ):
# #     n = len( l ) - 1
# #     for i in range( n // 2, 0, -1 ):
# #         fixDown( l, i, len( l ) )
# #     while n > 1:
# #         l[1], l[n] = l[n], l[1]
# #         fixDown( l, 1, n )
# #         n -= 1
# #     return l[1:]
# #
# #
# # l = [-1, 26, 5, 77, 1, 61, 11, 59, 15, 48, 19]  # 第一个元素不用，占位
# # res = heapSort( l )
# # print( res )
#
#
# #建堆的过程
# import random
#
# # def insert(li, i):
# #     tmp = li[i]
# #     j = i - 1
# #     while j >= 0 and li[j] > tmp:
# #         li[j + 1] = li[j]
# #         j = j - 1
# #     li[j + 1] = tmp
# #
# # def insert_sort(li):
# #     for i in range(1, len(li)):
# #         insert(li, i)
# #
#
# # def topk(li, k):
# #     top = li[0:k + 1]
# #     insert_sort(top)
# #     for i in range(k+1, len(li)):
# #         top[k] = li[i]
# #         insert(top, k)
# #     return top[:-1]
#
#
# def sift(data, low, high):
#     i = low
#     j = 2 * i + 1
#     tmp = data[i]
#     while j <= high:    #孩子在堆里
#         if j + 1 <= high and data[j] < data[j+1]:   #如果有右孩子且比左孩子大
#             j += 1  #j指向右孩子否则还是指向左孩子
#         if data[j] > tmp:   #孩子比最高领导大
#             data[i] = data[j]   #孩子填到父亲的空位上
#             i = j               #孩子成为新父亲
#             j = 2 * i + 1        #新孩子
#         else:
#             break
#     data[i] = tmp           #最高领导放到父亲位置
#
# def topn(li, n):
#     heap = li[0:n]
#     for i in range(n // 2 - 1, -1, -1):
#         sift(heap, i, n - 1)
#     #遍历
#     for i in range(n, len(li)):
#         if li[i] < heap[0]:
#             heap[0] = li[i]
#             sift(heap, 0, n - 1)
#     for i in range(n - 1, -1, -1):  # i指向堆的最后
#         heap[0], heap[i] = heap[i], heap[0]  # 领导退休，刁民上位
#         sift(heap, 0, i - 1)  # 调整出新领导
#     return heap
#
# data = list(range(10000))
# random.shuffle(data)
# print(topn(data, 10))


# def sift(data, low, high):
#     i = low
#     j = low * 2 + 1 #左孩子
#     tep = data[i]
#     while j <= high: #孩子在堆里
#         if j + 1 <= high and data[j + 1] > data[j]: #如果有右孩子，且右孩子大于左孩子
#             j += 1 #j指向右孩子
#         if data[j] > tep:
#             data[i] = data[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             break
#     data[i] = tep
# def heap_sort(data):
#     n = len(data)
#     for i in range(n // 2 - 1, -1, -1):
#         sift(data, i, n - 1)
#     #堆建好
#     for i in range(n - 1, -1, -1):
#         data[0], data[i] = data[i], data[0]
#         sift(data, 0, i - 1)
#     return data
#
# print(heap_sort([3,5,3,12,4,5,67,7]))

#
# def buildHeap(data, low, high):
#     i = low
#     j = 2 * i + 1 #左子
#     tmp = data[i] #取下最高节点，准备开始调整
#     while j <= high: #在右边界内
#         if j < high and data[j + 1] > data[j]: #j < high 表示存在右子，data[j + 1] > data[j] 表示右子大于左子
#             j += 1 #j将成为原先节点右子
#         if tmp < data[j]: #如果最高点大于当前节点，进行交换，再进行一次向下遍历查找
#             data[i] = data[j]
#             i = j
#             j = 2 * i + 1
#         else:
#             break
#     data[i] = tmp
# def heapSort(data):
#     n = len(data)
#     for i in range(n // 2, -1, -1): #从最后一个有子节点的节点，从最后一颗子树开始调整
#         buildHeap(data, i, n - 1)
#     #出堆
#     for i in range(n - 1, -1, -1):
#         data[0], data[i] = data[i], data[0]
#         buildHeap(data, 0, i - 1)
#     return data
# print(heapSort([3,5,3,12,4,5,67,7,6]))
def buildHeap(start, end, data):
    i = start
    leftOrRight = start * 2 + 1
    tmp = data[i]
    while leftOrRight < end:
        if leftOrRight < end and data[leftOrRight] < data[leftOrRight + 1]:
            leftOrRight += 1
        if tmp < data[leftOrRight]:
            data[i] = data[leftOrRight]
            i = leftOrRight
            leftOrRight = 2 * i + 1
        else:
            break
    data[i] = tmp

def heapSort(data):
    n = len(data)
    for i in range(n // 2, -1, -1):
        buildHeap(i, n - 1, data)

    for j in range(n - 1, -1, -1):
        data[j], data[0] = data[0], data[j]
        buildHeap(0, j - 1, data)
    print(data)
#heapSort([3,5,3,12,4,5,67,7,6])



# def build(start, end, data):
#     low = start
#     leftOrRight =  2 * low + 1
#     tmp = data[low]
#     while leftOrRight < end:
#         if leftOrRight < end and data[leftOrRight] < data[leftOrRight + 1]:
#             leftOrRight += 1
#         if data[leftOrRight] > tmp:
#             data[low] = data[leftOrRight]
#             low = leftOrRight
#             leftOrRight = 2 * leftOrRight + 1
#         else:
#             break
#     data[low] = tmp
# def heap(data):
#     n = len(data)
#     for i in range(n // 2, -1, -1):
#         buildHeap(i, n - 1, data)
#     for j in range(n - 1, -1, -1):
#         data[j], data[0] = data[0], data[j]
#         build(0, j - 1, data)
#     print(data)
# heap([3,5,3,12,4,5,67,7,6])



def build(start, end, data):
    low = start
    j = 2 * low + 1
    tmp = data[low]
    while j < end:
        if j < end and data[j + 1] > data[j]:
            j += 1
        if data[j] > tmp:
            data[low] = data[j]
            low = j
            j = 2 * low + 1
        else:
            break
    data[low] = tmp
def sort(data):
    n = len(data)
    for i in range(n // 2, -1, -1):
        build(i, n, data)

    for j in range(n - 1, -1, -1):
        data[0], data[j] = data[j], data[0]
        build(0, j - 1, data)
    return data

print(sort([3,5,3,12,4,5,67,7,6]))









