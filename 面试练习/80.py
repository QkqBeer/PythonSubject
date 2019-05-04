__author__ = "那位先生Beer"
def solution(nums):
    if len( nums ) <= 2:
        return nums
    first = 0
    second = 0
    temp = nums[second]
    flag = 0
    while first < len(nums):
        if temp == nums[first]:
            flag += 1
            if flag <= 2:
                nums[second] = nums[first]
                first += 1
                second += 1
            else:
                first += 1
        else:
            temp = nums[first]
            flag = 0
        print(nums[:second])
solution([1,1,2,2,2,2,3,3,5])

