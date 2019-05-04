__author__ = "那位先生Beer"


class Solution( object ):
    def findKthLargest( self, nums, k ):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 堆排序,复习一下堆排序
        n = len( nums )
        for i in range( n // 2, -1, -1 ):
            self.buildHeap( nums, i, n - 1 )
        for j in range( n - 1, n - k - 1, -1 ): #出堆，将第一个数和最后一个叶子结点进行交换，再排序。
            nums[0], nums[j] = nums[j], nums[0]
            self.buildHeap( nums, 0, j - 1 )
        return nums[n - k]

    def buildHeap( self, nums, low, high ):
        i = low
        j = 2 * i + 1
        tmp = nums[i]
        while j <= high:
            if j < high and nums[j + 1] > nums[j]:
                j += 1
            if tmp < nums[j]:
                nums[i] = nums[j]
                i = j
                j = 2 * i + 1
            else:
                break
        nums[i] = tmp