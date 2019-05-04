__author__ = "那位先生Beer"
from copy import deepcopy as copy
# def imageSmoother( M ):
#     x_len = len( M )
#     y_len = len( M[0] ) if x_len else 0
#     res = copy( M )
#     for x in range( x_len ):
#         for y in range( y_len ):
#             neibors = [
#                 M[_x][_y]
#                 for _x in (x - 1, x, x + 1)
#                 for _y in (y - 1, y, y + 1)
#                 if 0 <= _x < x_len and 0 <= _y < y_len]
#             res[x][y] = sum( neibors ) // len( neibors )
#     return res
def imageSmoother(M):
    x_len = len( M )
    y_len = len( M[0] ) if x_len else 0
    res = copy( M )
    for i in range( x_len ):
        for j in range( y_len ):
            neibors = [
                M[_x][_y]
                for _x in (i - 1, i, i + 1)
                for _y in (j - 1, j, j + 1)
                if 0 <= _x < x_len and 0 <= _y < y_len]
            res[i][j] = sum(neibors) // len(neibors)
    return res
print(imageSmoother([[1,1,1],
 [1,0,1],
 [1,1,1]]))
# m = [[1,1,1],
#      [1,0,1],
#      [1,1,1]]
# newList = [ m[x,y]
#             for x in range(len(m))
#             for y in range(len(m[0]))
#             ]
# print(newList)
#
