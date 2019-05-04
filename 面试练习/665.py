__author__ = "那位先生Beer"


def checkPossibility(nums ):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = 0
    for i in range( len( nums ) ):
        for j in range( i + 1, len( nums ) ):
            if nums[i] > nums[j]:
                count += 1
                print(count)
                break
        if count >= 2:
            return False
    return True
print(checkPossibility([2,3,3,2,4]))