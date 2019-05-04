# class Solution( object ):
#     def longestIncreasingPath( self, matrix ):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         m = len( matrix )
#
#         if m == 0:
#             return 0
#
#         n = len( matrix[0] )
#
#         dp = [[1] * n for i in range( m )]
#
#         slist = sorted( [(i, j, val)
#                          for i, row in enumerate( matrix )
#                          for j, val in enumerate( row )], key = operator.itemgetter( 2 ) )
#
#         for x, y, val in slist:
#             for dx, dy in zip( [1, 0, -1, 0], [0, 1, 0, -1] ):
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
#                     dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
#         return max( max( x ) for x in dp )
