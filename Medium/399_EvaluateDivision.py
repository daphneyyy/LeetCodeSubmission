# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def backtrack(cur, target, pro, visited):
            visited.add(cur)
            res = -1.0
            if target in graph[cur]:
                res = pro * graph[cur][target]
            else:
                for i in graph[cur]:
                    if i in visited:
                        continue
                    res = backtrack(i, target, pro * graph[cur][i], visited)
                    if res != -1.0:
                        break
            visited.remove(cur)
            return res

        results = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                res = -1.0
            elif q[0] == q[1]:
                res = 1.0
            else:
                visited = set()
                res = backtrack(q[0], q[1], 1, visited)
            results.append(res)

        return results
