class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        p = 0
        for i in range(n):
            for j in range(len(mat[0])):
                if i == j or i + j == n -1:
                    p += mat[i][j]
        return p
        