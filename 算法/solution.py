#
# def findUnsortedSubarray(nums):
#     all_same=[a==b for (a,b) in zip(nums,sorted(nums))]
#     print(all_same)
#     print(all_same.index(False),all_same[::-1].index(False))
#     return 0 if all(all_same) else len(nums)-all_same.index(False)-all_same[::-1].index(False)
#
#
# n=findUnsortedSubarray([2,4,6,4,8,10,9,15])
# print(n)



# def findAnagrams( s, p ):
#     """
#
#     :type s: str
#     :type p: str
#     :rtype: List[int]
#     """
#     left = 0
#     right = len( p ) - 1
#     dic1 = dict()
#     res = []
#     for i in p:
#         dic1[i] = dic1.get(i,0)+1
#     while right < len( s ):
#         dic2 = {}
#         for i in s[left:right + 1]:
#             dic2[i] = dic2.get( i, 0 ) + 1
#         if dic1 == dic2:
#             res.append( left )
#         left += 1
#         right += 1
#     return res
#
# print(findAnagrams("cbaebabacd",'abc'))

def a():
    s="aabdcc"
    dic={}
    for i in s:
        dic[i]=dic.get(i,0)+1
    dic['a']=dic['a']-2
    print(dic)

a()