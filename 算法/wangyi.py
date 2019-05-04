# def solution( data ):
#     flag = 0;
#     temp = 1
#     if len( data ) >= 3:
#         for i in range( len( data ) ):
#             if i == 0:
#                 t = data[i] * data[i + 1]
#             elif i == len( data ) - 1:
#                 t = data[i - 1] * data[i]
#             else:
#                 t = data[i - 1] * data[i] * data[i + 1]
#             if t > temp:
#                 temp = t
#                 flag = i
#         return flag, temp
#     elif len(data) == 2:
#         return 0, data[0] * data[1]
#     elif len(data) == 1:
#         return 0, data[0]
#     else:
#         return 0, 0
#
#
#
# import sys
#
# data = sys.stdin.readline().strip().split( ' ' )
# values = list( map( int, data ) )
# count = 0
# while(len(data) > 0):
#     flag, temp = solution(values)
#     if flag == 0 and temp == 0:
#         break
#     count = count + temp
#     values = values[:flag] + values[flag + 1:]
# print(count)
#
#
#
#
#
#
# def solution(N, c):
#     s = [N]
#     n = 0
#     count = 0
#     while c >= 2 ** n:
#         c = c - 2 ** n
#         for i in range(len(s)):
#             if s[i] > 1:
#                 if s[i] % 2 == 0:
#                     s[i] = s[i] / 2
#                     s.append(s[i])
#                 else:
#                     s[i] = s[i] // 2
#                     s.append(s[i] + 1)
#         n += 1
#         count += 1
#     m = max(s)
#     print(m + count)
# solution(5, 2)

# def solution(len, k, nums):
#     nums.sort()
#     nums = list(set(nums))
#     print(nums[0])
#     for i in range(1, k):
#         print(nums[i] - nums[i - 1])
#
# solution(2,2,[4,6])


# def solution(nums):
#     newNums = [nums[0]]
#     for i in range(1, len(nums)):
#         cur = newNums[i - 1] + nums[i]
#         if cur < nums[i]:
#             newNums.append(cur)
#         else:
#             newNums.append(nums[i])
#     left = 0
#     right = 1
#     res = []
#     while right < len(newNums):
#         if newNums[right - 1] > newNums[right]:
#             right += 1
#         else:
#             res.append(newNums[left:right])
#             left = right
#             right += 1
#     res.append(newNums[left:right])
#     r = []
#     for i in range(len(res)):
#         r.append(res[i][len(res[i]) - 1])
#     r.sort()
#     return r[0] + r[1]
# print(solution([2,-2,5,6,-7]))

#
# def solution(N):
#     if N <= 6:
#         return 1
#     else:
#         return (2 ** (N - 6)) % 666666666

def solution(nums, k):
    nums.sort()
    secondMax = nums[len(nums) - 1] + k
    for i in range(len(nums)):
        c = nums[len(nums) - 1] - nums[i]
        if k > 0 and k >= c:
            nums[i] += c
            k -= c
        elif k > 0 and k < c:
            nums[i] += k
            k = 0
            break
    if k > 0:
        cishu = k // len(nums)
        yushu = k % len(nums)
        if yushu > 0:
            firstMax = nums[len(nums) - 1] + cishu + 1
        else:
            firstMax = nums[len( nums ) - 1]
    else:
        firstMax = nums[len(nums) - 1]
    return [secondMax, firstMax]
print(solution([1,1,1,7], 7))











