__author__ = "那位先生Beer"
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        return s[::-1][:len(s) - j] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]