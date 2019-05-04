__author__ = "那位先生Beer"


def findRelativeRanks(nums):
    sort = sorted( nums )[::-1]
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map( str, range( 4, len( nums ) + 1 ) )
    return map( dict(zip(sort, rank)).get, nums)