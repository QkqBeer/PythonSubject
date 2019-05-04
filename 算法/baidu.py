__author__ = "那位先生Beer"
def solution(M, nums):
    dic = [0 for _ in range(M + 1)]
    for i in range(len(nums)):
        for j in range(nums[i][1] - 1, nums[i][0] - 1, -1):
            print(j)
            dic[j] += 1
    dic.sort()
    return dic[M]
def main():
    nums = []
    N = int(input())
    M = 0
    for i in range(N):
        li = input()
        l = list(map(int, li.strip().split(' ')))
        if l[1] > M:
            M = l[1]
        nums.append(l)
    print(solution(M, nums))
main()
