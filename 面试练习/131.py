class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        if self.is_palindrome(s): #判断s是否为回文字符串
            res.append([s])
        n = len(s)
        self.d = {}
        for i in range(1, n):
            if not self.is_palindrome(s[:i]):
                continue
            r_pas = self.get_palindromes(i, n, s)
            for r_pa in r_pas:
                res.append([s[:i]]+r_pa)
        return res

    def get_palindromes(self, i, j, s):
        l = j - i
        seq = s[i:j]
        if l == 1:
            return [[seq]]
        if (i, j) in self.d:
            return self.d[(i, j)]
        res = []
        if self.is_palindrome(seq):
            res.append([seq])
        for x in range(i + 1, j):
            if not self.is_palindrome(s[i: x]):
                continue
            r_pas = self.get_palindromes(x, j, s)
            for r_pa in r_pas:
                res.append([s[i: x]]+r_pa)
        self.d[(i, j)] = res
        return res

    def is_palindrome(self, s): #该函数判断该字符串是否为回文字符串
        n = len(s)
        for i in range(int(n / 2)):
            if s[i] != s[n - 1 - i]:
                return False
        return True
obj = Solution()
print(obj.partition('aab'))