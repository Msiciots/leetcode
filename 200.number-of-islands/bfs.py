class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        q = []
        q.append([i, j])
        n = len(grid)
        m = len(grid[0])
        while q:
            ci, cj = q.pop(0)
            grid[ci][cj] = "0"
            if (ci - 1) >= 0 and grid[ci - 1][cj] == "1":
                    q.append([ci - 1, cj])
                    grid[ci-1][cj]="0"
            if (ci + 1) < n and grid[ci + 1][cj] == "1":
                    q.append([ci + 1, cj])
                    grid[ci + 1][cj] = "0"
            if (cj - 1) >= 0 and grid[ci][cj - 1] == "1":
                    q.append([ci, cj - 1])
                    grid[ci][cj-1] = "0"
            if (cj + 1) < m and grid[ci][cj + 1] == "1":
                    q.append([ci, cj + 1])
                    grid[ci][cj+1] = "0"
        

if __name__ == "__main__":
    s = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(s.numIslands(grid))
