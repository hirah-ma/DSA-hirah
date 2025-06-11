from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)

        visited = [0] * n
        stack = []
        count = 0

        for i in range(n):
            if visited[i] != 1:
                nodes = []
                edge_count = 0

                stack.append(i)
                visited[i] = 1
                while stack:
                    node = stack.pop()
                    nodes.append(node)
                    for neighbor in d[node]:
                        edge_count += 1
                        if visited[neighbor] == 0:
                            visited[neighbor] = 1
                            stack.append(neighbor)

                size = len(nodes)
                edge_count = edge_count // 2  # undirected graph formula 
                if edge_count == size * (size - 1) // 2:
                    count += 1

        return count

        