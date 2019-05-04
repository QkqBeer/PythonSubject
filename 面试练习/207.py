__author__ = "那位先生Beer"
'''
d = [[1,2],[3,4]]
for k, v in d:
    print(k)
    print(v) 
#学习到了新的List for 循环的用法
    '''
import collections
class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                indegrees[node] -= 1
        return True
#方法二

class Solution( object ):
    def canFinish( self, N, prerequisites ):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict( list )
        for u, v in prerequisites:
            graph[u].append( v )
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * N
        for i in range( N ):
            if not self.dfs( graph, visited, i ):
                return False
        return True

    # Can we add node i to visited successfully?
    def dfs( self, graph, visited, i ):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs( graph, visited, j ):
                return False
        visited[i] = 2
        return True
