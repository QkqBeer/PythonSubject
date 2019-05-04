__author__ = "那位先生Beer"
# def solution(nums):
#     res = []
#     buffer = []
#     def build(s, buffer, res):
#         if len(s) == 0:
#             res.append(buffer)
#         else:
#             for i in range(len(s)):
#                 build(s[:i] + s[i + 1:], buffer + [s[i]], res)
#     build(nums, buffer, res)
#     print(res)
# solution([1,2,3])





#确定第一个数字的位置
def quanpailie(nums):
    res = []
    path = []
    def build(nums, res, path):
        if len(nums) == 0:
            res.append(path)
        else:
            for i in range(len(nums)):
                build(nums[:i] + nums[i + 1:], res, path + [nums[i]])
    build(nums, res, path)
    print(res)
quanpailie([1, 2, 3])































