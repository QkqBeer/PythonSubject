__author__ = "那位先生Beer"

#
# def letterCasePermutation( S ):
#     """
#     :type S: str
#     :rtype: List[str]
#     """
#     def switch_capital(s):
#         if s.isupper():
#             return s.lower()
#         else:
#             return s.upper()
#     newList = []
#     newList.append(S)
#     for i in range(len(S)):
#         if ord(S[i]) >= 65:
#             tmp = []
#             for j in range(len(newList)):
#                 tmp.append(newList[j][0:i] + switch_capital(newList[j][i]) + newList[j][i + 1 :])
#         else:
#             continue
#         newList += tmp
#     print(newList)


def letterCasePermutation( S ):
    """
    :type S: str
    :rtype: List[str]
    """

    res = [""]
    for s in S:
        print(res)
        if not s.isalpha():
            for i in range( len( res ) ):
                res[i] += s
        else:
            for i in range( len( res ) ):
                tmp = res[i]
                res[i] += s.lower()
                res.append( tmp + s.upper() )

    return res

print(letterCasePermutation('1abc'))

