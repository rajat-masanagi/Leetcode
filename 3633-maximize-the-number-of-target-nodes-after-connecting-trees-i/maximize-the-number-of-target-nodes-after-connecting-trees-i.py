class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(edges, k):
            length = len(edges) + 1
            ans = [0] * length
            tree = [[] for _ in range(length)]
            for edge in edges:
                u, v = edge[0], edge[1]
                tree[u].append(v)
                tree[v].append(u)
            for x in range(length):                
                stk = [(x, -1, 0)]
                while stk:
                    u, p, d = stk.pop()
                    if d > k:
                        continue
                    ans[x] += 1
                    for v in tree[u]:
                        if v != p:
                            stk.append((v, u, d+1))
            return ans
                            
        most = max(dfs(edges2, k-1))
        return [x+most for x in dfs(edges1, k)]


