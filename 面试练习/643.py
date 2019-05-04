__author__ = "那位先生Beer"


def findMaxAverage(nums, k ):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    average = -10000.0
    for i in range( len( nums ) - k ):
        average = float( max( average, sum( nums[i:i + k] ) / k ) )
    return average
print(findMaxAverage([1,12,-5,-6,50,3],4))