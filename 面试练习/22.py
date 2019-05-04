__author__ = "那位先生Beer"


def generateParenthesis( n ):
    """
    :type n: int
    :rtype: List[str]
    """
    # 自己本来打算单独进行判断，括号是否合理，利用栈
    # 答案提示left  < right 聪明啊！ 相当nice
    def buildList(state):
        for j in range(len(state)):
            newState = []
            if state[j][1] > state[j][2]:
                newState.append([state[j][0] + ')', state[j][1], state[j][2] + 1])
            if state[j][1] < n:
                newState.append([state[j][0] + '(', state[j][1] + 1, state[j][2]])
        return newState
    state = [['(', 1, 0]]
    i = 0
    while i < 2 * n:
        temp = buildList(state)
        print(temp)
        state.clear()
        print(state)
        state = temp
        i += 1
    reList = []
    for item in state:
        reList.append( item[0] )
    return reList
print(generateParenthesis(3))