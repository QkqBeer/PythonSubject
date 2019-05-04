__author__ = "那位先生Beer"


# def networkDelayTime( self, times, N, K ):
#     """
#     :type times: List[List[int]]
#     :type N: int
#     :type K: int
#     :rtype: int
#     """
#
#     INF = 0x7FFFFFFF  # 无穷大标记
#     edge = [[INF for _ in range( N + 1 )] for _ in range( N + 1 )]
#     dist = [INF] * (N + 1)
#     visit = [False] * (N + 1)
#
#     for time in times:  # 对图的邻接矩阵进行初始化
#         edge[time[0]][time[1]] = time[2]
#     dist[K] = 0  # 对距离数组进行初始化
#
#     for i in range( N ):
#         MIN = INF
#         index = None
#         for j in range( 1, N + 1 ):
#             if visit[j] == False and dist[j] < MIN:
#                 MIN = dist[j]
#                 index = j  # 挑选出一个可确定的节点
#         if index == None: return -1
#         visit[index] = True
#         for j in range( 1, N + 1 ):
#             if visit[j] == False and MIN + edge[index][j] < dist[j]:
#                 dist[j] = MIN + edge[index][j]  # 用该节点更新数组
#
#     return max( dist[1:] )

#实现Dijkstra算法 time = (u, v, w)
def solution(times, N, K):
    INF = 0x7FFFFFFF  # 无穷大标记
    edge = [[INF for _ in range( N + 1 )] for _ in range( N + 1 )] #初始化
    for time in times:
        edge[time[0]][time[1]] = time[2]

solution([[2,1,1],[2,3,1],[3,4,1]],4,2)