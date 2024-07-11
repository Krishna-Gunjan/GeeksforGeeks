from typing import List

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        def dfs(grid, visited, x, y, n):
            stack = [(x, y)]
            visited[x][y] = True
            size = 0
            
            while stack:
                cx, cy = stack.pop()
                size += 1
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            
            return size
        
        n = len(grid)
        if n == 0:
            return 0
        
        visited = [[False] * n for _ in range(n)]
        component_sizes = []
        component_ids = [[-1] * n for _ in range(n)]
        component_id = 0
        max_size = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    size = dfs(grid, visited, i, j, n)
                    component_sizes.append(size)
                    max_size = max(max_size, size)
                    for x in range(n):
                        for y in range(n):
                            if visited[x][y] and component_ids[x][y] == -1:
                                component_ids[x][y] = component_id
                    component_id += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_components = set()
                    combined_size = 1
                    
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            comp_id = component_ids[ni][nj]
                            if comp_id not in unique_components:
                                unique_components.add(comp_id)
                                combined_size += component_sizes[comp_id]
                    
                    max_size = max(max_size, combined_size)
        
        return max_size
