__author__ = "那位先生Beer"

#超时
def largestPalindrome( n ):
    maxNum = 10 ** n - 1
    minNum = 10 ** (n - 1)
    s = maxNum * maxNum
    while s >= minNum * minNum and s <= maxNum * maxNum:
        if str(s) == str(s)[::-1]:
            if is_vaild(s,maxNum, minNum) == True:
                return s % 1337
            else:
                s -= 1
        else:
            s -= 1
import math
def is_vaild(num,m,n):
    for i in range(n,math.sqrt(m)):
        if num % i == 0:
            t = num // i
            if t >= n and t <= m:
                return True
    return False

# print(largestPalindrome(2))
# print(is_vaild(9009,99,10))
#

# def largestPalindrome( n ):
#     if n == 1: return 9
#     for z in range( 2, 2 * (9 * 10 ** n) - 1 ):
#         left = 10 ** n - z
#         right = int( str( left )[::-1] )
#         root_1, root_2 = 0, 0
#
#         if z ** 2 - 4 * right < 0:
#             continue
#         else:
#             root_1 = 1 / 2 * (z + (z ** 2 - 4 * right) ** 0.5)
#             root_2 = 1 / 2 * (z - (z ** 2 - 4 * right) ** 0.5)
#             if root_1.is_integer() or root_2.is_integer():
#                 return (10 ** n * left + right) % 1337
# print(largestPalindrome(5))