__author__ = "那位先生Beer"


def search( nums, target ):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def Bsearch(nums, low, high):
        if len(nums[low:high]) > 1:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return Bsearch(nums, low, mid)
            else:
                return Bsearch(nums, mid, high)
        else:
            return -1
    return Bsearch(nums, 0, len(nums) - 1)
print(search([-1,0,3,5,9,12], 9))