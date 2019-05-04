__author__ = "那位先生Beer"
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #复杂度是n ** 2
    # dic = {}
    # for num in nums:
    #     dic[num] = dic.get(num, 0) + 1
    # print(dic)

    nums.sort()
    reList = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                reList.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s > 0:
                r -= 1
            else:
                l += 1
    return reList
print(threeSum([-1, 0, 1, 2, -1, -4]))