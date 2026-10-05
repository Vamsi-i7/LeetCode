from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for start in range(n):
            if visited[start]:
                continue
            # Found a new province — BFS to mark its whole component
            provinces += 1
            queue = deque([start])
            visited[start] = True

            while queue:
                city = queue.popleft()
                for neighbor in range(n):
                    if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        return provinces