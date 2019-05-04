__author__ = "那位先生Beer"
def longestWord(words):
    """
    :type words: List[str]
    :rtype: str
    """
    dic = {}
    result = []
    t = set(words)
    for i in range(len(words)):
        if len(words[i]) not in dic:
            dic[len(words[i])] = []
            dic[len(words[i])].append(words[i])
        else:
            dic[len(words[i])].append(words[i])
    for s in sorted(dic, reverse=True):
        for j in range(len(dic[s])):
            test = set()
            for i in range(len(dic[s][j]), 0, -1):
                test.add(dic[s][j][0: i])
            if len(test & t) == len(test):
                result.append(dic[s][j])
    maxLength = 0
    maxLengthStack = []
    for i in range(len(result)):
        if len(result[i]) > maxLength:
            maxLengthStack = []
            maxLengthStack.append(result[i])
            maxLength = len(result[i])
        elif len(result[i]) == maxLength:
            maxLengthStack.append( result[i] )
    sorted(maxLengthStack)
    print(maxLengthStack)
    print(maxLengthStack[0])
longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
