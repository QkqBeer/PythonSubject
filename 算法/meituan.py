# __author__ = "那位先生Beer"
# # def func():
# #     try:
# #         a = 35/0
# #     except NameError:
# #         print("A")
# # try:
# #     func()
# # except TypeError:
# #     print("B")
# # except ZeroDivisionError:
# #     print("C")
# # finally:
# #     print("D")
# def solution(nums):
#     count = 0
#     x = len(nums)
#     y = len(nums[0])
#     for i in range(x):
#         for j in range(y):
#             if(i - 1 >=0  and i + 1 < x):
#                 if nums[i][j] == nums[i - 1][j] == nums[i + 1][j]:
#                     nums[i - 1][j] = -1
#                     nums[i + 1][j] = -1
#                 elif nums[i + 1][j] == nums[i][j]:
#                     nums[i + 1][j] = nums[i - 1][j]
#             elif(i - 1 < 0 and i + 1 < x):
#                 if nums[i + 1][j] == nums[i][j]:
#                     nums[i + 1][j] = -1
#             elif(i - 1 >= 0 and i + 1 >= x):
#                 if nums[i - 1][j] == nums[i][j]:
#                     nums[i - 1][j] = -1
#
#
#
#
# n = int(input())
# result = []
# while n:
#     L = list(map(int,input().split(" ")))
#     if L[0] == L[2]:
#         if L[1] > L[3]:
#             L[1],L[3] = L[3],L[1]
#         result = result + [(L[0], i) for i in range(L[1],L[3]+1)]
#     if L[1] == L[3]:
#         if L[0] > L[2]:
#             L[0],L[2] = L[2],L[0]
#         result = result + [(i, L[1]) for i in range(L[0], L[2]+1)]
#     n = n -1
# print(len(set(result)))

n = int(input())
result = []
while n:
    L = list(map(int,input().split(" ")))
    if L[0] == L[2]:
        if L[1] > L[3]:
            L[1],L[3] = L[3],L[1]
        for i in range(L[1],L[3]+1):
            result.append((L[0], i))
    if L[1] == L[3]:
        if L[0] > L[2]:
            L[0],L[2] = L[2],L[0]
        for i in range(L[0], L[2]+1):
            result.append((i, L[1]))
    n -= 1
print(len(set(result)))
