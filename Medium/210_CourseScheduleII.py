# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        def explore(v, visited, neigh, stack):
            visited[v] = 'pending'
            nonlocal isDAG
            if v in neigh:
                for u in neigh[v]:
                    if visited[u] == 'pending':
                        isDAG = False
                        return
                    if isDAG and visited[u] == 'unvisited':
                        explore(u, visited, neigh, stack)
            visited[v] = 'visited'
            stack.append(v)

        if numCourses == 1 and prerequisites == []: return [0]
        visited = defaultdict(str)
        neigh = defaultdict(list)
        isDAG = True    
        stack = []
        for i in range(numCourses):
            visited[i] = 'unvisited'
        for v in prerequisites:
            if v[0] in neigh:
                if v[1] in neigh[v[0]]:
                    return []
            neigh[v[1]].append(v[0])
        for v in range(numCourses):
            if visited[v] == 'unvisited':
                explore(v, visited, neigh, stack)
        if not isDAG:
            return []
        else:
            return stack[::-1]