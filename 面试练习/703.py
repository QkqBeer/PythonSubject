__author__ = "那位先生Beer"
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool) #将列表进行调整，默认是小顶堆
        while self.size > k:
            heapq.heappop(self.pool) #heappop()方法，将对顶元素弹出，返回的就是堆顶
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val) #将val添加到heap中
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val) #先pop再加入
        return self.pool[0]
