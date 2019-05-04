# # # __author__ = "那位先生Beer"
# # def sum1(n):
# #     sum2=0
# #     # for i in range(n+1):
# #     #     bin1=bin(i)
# #     #     strbin1=str(bin1)
# #     #     #print(strbin1)
# #     #     l=strbin1.find("11")
# #     #     if l!=-1:
# #     #         sum2=sum2+1
# #     # return n+1-sum2
# #     for i in range (1,n+1):
# #          m=(i&(i>>1))>0
# #          if m==False:
# #              sum2=sum2+1
# #     if n>0:
# #         return sum2+1
# #     if n==0:
# #         return sum2
# #
# # if __name__=="__main__":
# #     N=int(input())
# #
# #     print(sum1(N))
# #
# #
# def sum1( n ):
#     if n < 2:
#         return n + 1
#     string = bin( n )
#     str = string.replace( "0b", "" )
#     str = str[::-1]
#     k = len( str )
#
#     f = [0] * k
#     f[0] = 1
#     f[1] = 2
#     for i in range(2, k):
#         f[i] = f[i - 1] + f[i - 2]
#     ans = 0
#     for i in range( k - 1, -1, -1 ):
#         if str[i] == "1":
#             ans += f[i]
#             if i < k - 1 and str[i + 1] == "1":
#                 return ans
#     ans += 1
#     return ans
#
#
# if __name__ == "__main__":
#     N = int( input() )
#     print( sum1( N ) )
# def sum1( n ):
#     if n < 2:
#         return n + 1
#     string = bin( n )
#     string1 = string.replace( "0b", "" )
#
#     string1 = string1[::-1]
#     number = len( string1 )
#
#     num1 = [0] * len( string1 )
#     num1[0] = 1;
#     num1[1] = 2
#     for i in range( 2, len( string1 ) ):
#         num1[i] = num1[i - 1] + num1[i - 2]
#     sum2 = 0
#     for i in range( len( string1 ) - 1, -1, -1 ):
#         if string1[i] == "1":
#             sum2 = sum2 + num1[i]
#             if i < len( string1 ) - 1 and string1[i + 1] == "1":
#                 return sum2
#     sum2 = sum2 + 1
#     return sum2
#
#
# if __name__ == "__main__":
#     N = int( input() )
#     print( sum1( N ) )

# def adder(x):
#     def wrapper(y):
#         return x + y
#     return wrapper
# adder5 = adder(5)
# print(adder5(adder5(6)))
