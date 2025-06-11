from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [row[:] for row in grid]
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        drow = [0, -1, 0, 1]
        dcol = [-1, 0, 1, 0]#where to move
        t = 0

        while q:
            node_i, node_j, t = q.popleft()
            for i in range(4):
                n_i = node_i + drow[i]
                n_j = node_j + dcol[i]
                if 0 <= n_i < m and 0 <= n_j < n:
                    if visited[n_i][n_j] == 1:
                        visited[n_i][n_j] = 2
                        q.append((n_i, n_j, t + 1))

        for r in visited:
            if 1 in r:
                return -1

        return t



                        





        