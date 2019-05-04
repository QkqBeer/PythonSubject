__author__ = "那位先生Beer"


def findShortestSubArray(nums ):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for i in range( len( nums ) ):
        if nums[i] in dic:
            dic[nums[i]] += 1
        else:
            dic[nums[i]] = 1
    if max(list(dic.values())) == 1:
        return 1
    record = []
    p = 0
    for i in dic:
        if dic[i] > p:
            record = []
            record.append( i )
            p = dic[i]
        elif dic[i] == p:
            record.append(i)
    minCount = len(nums)
    for i in range(len(record)):
        start = 0
        end = len(nums)
        for j in range(len(nums)):
            if nums[j] == record[i]:
                start = j
                break
        for k in range(len(nums) - 1, -1, -1):
            if nums[k] == record[i]:
                end = k
                break
        minCount = min(minCount, end - start + 1)
    return minCount

findShortestSubArray([1,2])