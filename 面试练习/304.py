class NumMatrix( object ):
    def __init__( self, matrix ):
        """
        :type matrix: List[List[int]]
        """
        x = len( matrix )
        y = 0
        if x != 0:
            y = len( matrix[0] )
        for i in range( x ):
            for j in range( y ):
                left = 0
                top = 0
                leftTop = 0
                if j - 1 >= 0:
                    left = matrix[i][j - 1]
                if i - 1 >= 0:
                    top = matrix[i - 1][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    leftTop = matrix[i - 1][j - 1]
                matrix[i][j] = matrix[i][j] + left + top - leftTop
        self.matrix = matrix

    def sumRegion( self, row1, col1, row2, col2 ):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        top = 0
        left = 0
        leftTop = 0
        if row1 - 1 >= 0:
            top = self.matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            left = self.matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            leftTop = self.matrix[row1 - 1][col1 - 1]
        return self.matrix[row2][col2] - left - top + leftTop




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)