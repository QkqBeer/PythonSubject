__author__ = "那位先生Beer"
#实现全排列,利用递归，确定第一个字符，对后面的n-1个字符进行全排列，确定第二个，在对后面的n - 2个字符进行全排列
# def solution(s, start, end):
#     if start == end:
#         print(s)
#         #返回的话self.result.append(s[:]),不能self.result.append(s)
#     else:
#         for i in range(start, end):
#             s[start], s[i] = s[i], s[start]
#             solution(s, start + 1,end)
#             s[start], s[i] = s[i], s[start]
# solution([1,2,3], 0, 3)

#利用深度优先算法实现全排列,回溯法
def permute( nums ):
    mark = [False] * len( nums )
    outcome = []
    curr = []
    core( mark, nums, curr, outcome )
    return outcome


def core( mark, nums, curr, outcome ):
    if sum( mark ) == len( nums ):
        print(curr)
        outcome.append( curr[:] )
    for i in range( len( nums ) ):
        if mark[i]:
            continue
        curr.append( nums[i] )
        mark[i] = True
        core( mark, nums, curr, outcome )
        mark[i] = False
        curr.pop()
permute([1,2,3])





