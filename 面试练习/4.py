__author__ = "那位先生Beer"
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L = []
        L1 = len(nums1)
        L2 = len(nums2)
        count = 0
        i = j = 0
        while count < (L1 + L2):
            if i < L1 and j < L2:
                if nums1[i] < nums2[j]:
                    L.append(nums1[i])
                    i += 1
                    count += 1
                else:
                    L.append(nums2[j])
                    j += 1
                    count += 1
            else:
                if i == L1:
                    L += nums2[j:]
                    break
                else:
                    L += nums1[i:]
                    break
        print (L)
        if (L1 + L2) % 2 == 0:
            n = int((L1 + L2) // 2)
            return (L[n] + L[n - 1]) / 2
        else:
            n = int((L1 + L2) // 2)
            return L[n]
obj = Solution()
print(obj.findMedianSortedArrays([1],[2]))