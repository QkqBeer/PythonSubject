__author__ = "那位先生Beer"
def exist(board, word ):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    # 递归
    x = len( board )
    y = len( board[0] )

    def select( board, i, j, word ):
        # 上下左右
        if board[i][j] == word[0] and len( word ) > 1:
            board[i][j] = '0'
            if j - 1 >= 0:
                flag1 = select( board, i, j - 1, word[1:] )
            else:
                flag1 = False
            if j + 1 < y:
                flag2 = select( board, i, j + 1, word[1:] )
            else:
                flag2 = False
            if i - 1 >= 0:
                flag3 = select( board, i - 1, j, word[1:] )
            else:
                flag3 = False
            if i + 1 < x:
                flag4 = select( board, i + 1, j, word[1:] )
            else:
                flag4 = False
            board[i][j] = word[0]
            return (flag1 or flag2 or flag3 or flag4)
        elif board[i][j] == word[0] and len( word ) == 1:
            return True
        else:
            return False

    # 确定起始点
    for i in range( x ):
        for j in range( y ):
            if board[i][j] == word[0]:
                print(select( board, i, j, word))

exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB")