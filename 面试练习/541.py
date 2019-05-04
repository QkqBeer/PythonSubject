__author__ = "那位先生Beer"


def reverseStr( s, k ):
    print(len(s))
    if len( s ) <= k:
        return s[::-1]
    if k == 1:
        return s
    newStr = ''
    for i in range(len(s)):
        if i % (2 * k) == 0:
            flag = i
        if i % (2 * k) < k and flag + k <= len(s):
            newStr += s[flag + k - (i % (2 * k)) - 1]
        elif i % (2 * k) < k and flag + k > len(s):
            newStr += s[len(s) - (i % (2 * k)) - 1]
        else:
            newStr += s[i]
    return newStr

print(reverseStr('hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsg',39))