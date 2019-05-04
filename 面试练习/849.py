__author__ = "那位先生Beer"

#
# def maxDistToClosest( seats ):
#     """
#     :type seats: List[int]
#     :rtype: int
#     """
#     maxCount = 0
#     count = 1
#     for i in range( 1, len( seats ) ):
#         if seats[i] == seats[i - 1] == 0:
#             count += 1
#         else:
#             maxCount = max(maxCount, count)
#             count = 1
#     count0 = 1
#     if seats[0] == 0:
#         for i in range(1,len(seats)):
#             if seats[i] == 0:
#                 count0 += 1
#             else:
#                 break
#     countL= 1
#     if seats[len(seats) - 1] == 0:
#         for j in range(len(seats) - 2, -1, -1):
#             if seats[j] == 0:
#                 countL += 1
#             else:
#                 break
#
#     return max(max(count0, countL),maxCount // 2 + 1)
# print(maxDistToClosest([1,0,0,0,1,0,1]))