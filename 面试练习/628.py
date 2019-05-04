__author__ = "那位先生Beer"


def maximumProduct(nums ):
    """
    :type nums: List[int]
    :rtype: int
    """
    t = len( nums )
    nums.sort()
    print(nums)
    s = nums[t - 1] * nums[t - 2] * nums[t - 3]
    p = nums[0] * nums[1] * nums[t - 1]
    return s if s > p else p
print(maximumProduct([9,1,5,6,7,2]))