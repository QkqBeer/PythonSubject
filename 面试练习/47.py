__author__ = "那位先生Beer"


# def permuteUnique( nums ):
#     ans = [[]]
#     for n in nums:
#         ans = [l[:i] + [n] + l[i:]
#         for l in ans
#         for i in range( (l + [n]).index( n ) + 1 )]
#         print(ans)
#     # 排除重复排列
#     return ans
# print(permuteUnique([1, 1, 3]))

def permuteUnique( nums ):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    helper( nums, res, [] )
    return res


def helper( nums, res, path ):
    if not nums and path not in res:
        res.append( path )
    else:
        for i in range( len( nums ) ):
            print(nums[:i] + nums[i + 1:], res, path + [nums[i]])
            helper( nums[:i] + nums[i + 1:], res, path + [nums[i]] )
print(permuteUnique([1,2,1]))