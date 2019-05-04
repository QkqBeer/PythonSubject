__author__ = "那位先生Beer"


# def canConstruct( ransomNote, magazine ):
#     dir1 = {}
#     for i in range( len( ransomNote ) ):
#         if ransomNote[i] not in dir1:
#             dir1[ransomNote[i]] = 1
#         else:
#             dir1[ransomNote[i]] += 1
#     dir2 = {}
#     for i in range( len( magazine ) ):
#         if magazine[i] not in dir2:
#             dir2[magazine[i]] = 1
#         else:
#             dir2[magazine[i]] += 1
#     print(dir1)
#     print(dir2)
#     for key in dir1:
#         if key in dir2:
#             if dir1[key] <= dir2[key]:
#                 pass
#             else:
#                 return False
#         else:
#             return False
#     return True
# canConstruct('qq','qqw')

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    for i in range( len( s ) ):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
    print(dic)
    for key in dic:
        if dic[key] == 1:
            flag = key
            break
    for i in range( len( s ) ):
        if s[i] == flag:
            return i
print(firstUniqChar('loveleetcode'))