class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @cache
        def go(u, p):
            u_sum = 0
            u_count = 1
            for v in graph[u]:
                if v == p:
                    continue
                v_sum, v_count = go(v, u)
                u_sum += v_sum + v_count
                u_count += v_count
            return u_sum, u_count
        
        return [go(u, -1)[0] for u in range(n)]