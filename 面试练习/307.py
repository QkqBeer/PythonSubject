__author__ = "那位先生Beer"


class NumArray( object ):
    def __init__( self, nums ):
        self.l = len( nums )
        self.nums = [0] * self.l
        for i in nums:
            self.nums.append( i )
        i = self.l - 1
        while (i > 0):
            self.nums[i] = self.nums[2 * i] + self.nums[2 * i + 1]
            i -= 1

    def update( self, i, val ):
        i += self.l
        diff = val - self.nums[i]
        while (i > 0):
            self.nums[i] += diff
            i //= 2

    def sumRange( self, i, j ):
        sum = 0
        i += self.l
        j += self.l
        while (i <= j):
            if i % 2 == 1:
                sum += self.nums[i]
                i += 1
            if j % 2 == 0:
                sum += self.nums[j]
                j -= 1
            i = i // 2
            j = j // 2
        return sum




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
obj = NumArray([1,2,3,4,5])
print(obj.nums)
obj.update(1,3)