__author__ = "那位先生Beer"


def convert(s, numRows ):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    news = [''] * numRows
    change = -1
    i = 0
    for c in s:
        news[i] += c
        if i == 0 or i == (numRows - 1):
            change = -1 * change
        i += change
    return ('').join(news)
print(convert("PAYPALISHIRING", 3))
