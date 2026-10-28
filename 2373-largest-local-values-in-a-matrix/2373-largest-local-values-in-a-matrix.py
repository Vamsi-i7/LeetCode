class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ans = []
        def maxx(r,c):
            max_val = 0
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] > max_val:
                        max_val = grid[i][j]
            return max_val
        
        row = n - 2
        col = n - 2


        for p in range(row):
            res = []
            for q in range(col):
                res.append(maxx(p,q))
            ans.append(res)

        return ans
