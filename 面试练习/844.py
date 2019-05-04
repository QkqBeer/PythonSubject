__author__ = "那位先生Beer"


def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """

    def helpFunc(s):
        stack = []
        for i in range(len(s)):
            if s[i] == '#' and len(stack) > 0:
                stack.pop()
            elif s[i] != '#':
                stack.append(s[i])
        return ''.join(stack)
    return helpFunc( S ) == helpFunc( T )
print(backspaceCompare("y#fo##f","y#f#o##f"))