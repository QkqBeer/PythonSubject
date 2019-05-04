__author__ = "那位先生Beer"


# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         '''
#         maxNum = nums[0]
#         cur = nums[0]
#         for i in range(1, len(nums)):
#             cur = cur * nums[i]
#             if cur < nums[i]:
#                 cur = nums[i]
#             maxNum = max(maxNum, cur)
#         return maxNum
#         这道题需要考虑负数的情况，这是一道垃圾题。
#         '''
#         newList = []
#         first = 0
#         maxNum = max(nums)
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 newList.append(nums[first:i])
#                 first = i + 1
#         for temp in newList:
#             m = 1
#             isT = self.isEven(temp)
#             if isT[0]:
#                 for j in range(len(temp)):
#                     m *= temp[j]
#             else:
#负数个数为奇数的情况，不能解答
#             maxNum = max(maxNum, m)
#         return maxNum
#     def isEven(self, n):
#         count = 0
#         minF = 0
#         for i in range(len(n)):
#             if n[i] < 0:
#                 count += 1
#                 minF = min(abs(minF), abs(n[i]))
#         return True if count % 2 == 0 else False
'''
本题要求连续子数组的最大乘积，思路与求连续子数组的最大和相似，
都是采用动态规划，maxvalue[i]maxvalue[i]表示以a[i]a[i]为结尾的子数组中最大乘积，
同时维护一个全局最大值globalmaxglobalmax，记录maxvalue[i]maxvalue[i]中的最大值。
与求子数组的最大和不同的是，还需要维记录子数组最小乘积minvalue[i]minvalue[i]，
因为可能会出现 负 × 负 = 正的情况。并且最大最小乘积只可能出现在 
(maxvalue[i−1]×a[i],minvalue[i−1]×a[i],a[i])(maxvalue[i−1]×a[i],minvalue[i−1]×a[i],a[i])三者之间。
'''
class Solution( object ):
    def maxProduct( self, nums ):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxvalue = minvalue = nums[0]
        globalmax = nums[0]
        for i in range( 1, len( nums ) ):
            lastmax = maxvalue
            maxvalue = max( minvalue * nums[i], lastmax * nums[i], nums[i] )
            minvalue = min( minvalue * nums[i], lastmax * nums[i], nums[i] )
            globalmax = max( globalmax, maxvalue )
        return globalmax