__author__ = "那位先生Beer"
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newL = s.split() #split()函数不加任何参数可以默认将单词中任意个空格去掉，分割。
        return ' '.join(newL[::-1]) if len(newL) > 0 else ''

s = Solution()
print(s.reverseWords('the '))