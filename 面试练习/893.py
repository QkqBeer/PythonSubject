__author__ = "那位先生Beer"
# def numSpecialEquivGroups(A):
#     """
#     :type A: List[str]
#     :rtype: int
#     """
#     B = set()
#     for a in A:
#         B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
#     print(B)
#     return len(B)
# print(numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))


def numSpecialEquivGroups( A ):
    def count( A ):
        ans = [0] * 52
        for i, letter in enumerate( A ):
            ans[ord( letter ) - ord( 'a' ) + 26 * (i % 2)] += 1
        return tuple( ans )
    return {count( word ) for word in A}
print(numSpecialEquivGroups(["a","b","c","a","c","c"]))


