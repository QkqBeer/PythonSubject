# import sys
# line = sys.stdin.readline().strip()
# value = list(map(int, line.split()))
# n = value[0]
# a = value[1]
# xLine = sys.stdin.readline().strip()
# x = list(map(int, xLine.split()))
# x.sort()
# Min = x[0]
# Max = x[len(x) - 1]
# if a >= Max:
#     print(abs(a - x[1]))
# if a <= Min:
#     print(abs(x[len(x) - 2] - a))
# if abs(a - Min) > abs(a - Max):
#     print(abs(a - Max) + abs(Max - x[1]))
# else:
#     print(abs(a - Min) + abs(Min - x[len(x) - 2]))


# import sys
# lines = int(sys.stdin.readline().strip())
# res = []
# for i in range(lines):
#     res.append(int(sys.stdin.readline().strip()))
# l = [0] * (lines + 1)
# if lines <= 2:
#     print(0)
# l[0] = 0
# l[1] = res[1]
# l[3] = res[3] if res[0] + res[1] > res[3] else res[3]
# for i in range(3, lines):
#     if res[i] > res[i - 1] + res[i - 2]:
#         l[i] = l[i - 3] + res[i]
#     else:
#         l[i] = l[i - 1]

# import sys
# lines = int(sys.stdin.readline().strip())
# res = [i + 1 for i in range(lines)]
# r = []
# while len(res) > 0:
#     s = res.pop(0)
#     r.append(str(s))
#     if len(res) > 0:
#         t = res.pop(0)
#         res.append(t)
#     else:
#         break
# print(' '.join(r))



