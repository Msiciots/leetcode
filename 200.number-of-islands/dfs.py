class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1

        return count 

    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        grid[i][j] = "0"
        if i > 0 and grid[i - 1][j] == "1":
            self.dfs(grid, i - 1, j)
        if i + 1 <= n - 1 and grid[i + 1][j] == "1":
            self.dfs(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == "1":
            self.dfs(grid, i, j - 1)
        if j + 1 <= m - 1 and grid[i][j + 1] == "1":
            self.dfs(grid, i, j + 1)

if __name__ == "__main__":
    s = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(s.numIslands(grid))
