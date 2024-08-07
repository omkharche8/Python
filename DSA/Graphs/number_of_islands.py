# Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land).
# Find the number of islands.
#
# Note: An island is either surrounded by water or boundary of grid
# and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

# Input:
# grid = {{0,1},{1,0},{1,1},{1,0}}
# Output:
# 1
# Explanation:
# The grid is-
# 0 1
# 1 0
# 1 1
# 1 0
# All lands are connected.

# grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
# Output:
# 2
# Explanation:
# The grid is-
# 0 1 1 1 0 0 0
# 0 0 1 1 0 1 0


def numofislands(grid):
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(i, j):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
        stack = [(i, j)]
        visited[i][j] = True

        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    num_of_islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                num_of_islands += 1

    return num_of_islands

# Test case
grid = [[0, 1], [1, 0], [1, 1], [1, 0]]
print(numofislands(grid))  # Output should be 1
