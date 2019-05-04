__author__ = "那位先生Beer"


def getMoneyAmount( n ):
    """
    :type n: int
    :rtype: int
    """
    # dp[i][j]代表从i到j范围内猜数字至少要拥有的现金
    dp = [[0] * n for i in range( n )]
    for i in range( 1, n ):
        for j in range( n - i ):
            res = []
            for x in range( j, i + j + 1 ):
                if x == j:
                    res.append( j + 1 + dp[j + 1][i + j] )
                elif x == i + j:
                    res.append( i + j + 1 + dp[j][i + j - 1] )
                else:
                    res.append( x + 1 + max( dp[j][x - 1], dp[x + 1][i + j] ) )
            dp[j][i + j] = min( res )
    print(dp)
    #return dp[0][n - 1]
getMoneyAmount(10)