class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])

        ans = []
        for i in range(n):
            for j in range(m):
                cur = matrix[i][j]
                h = True
                l = True

                for k in range(m):
                    if matrix[i][k] < cur:
                        h = False

                for p in range(n):
                    if matrix[p][j] > cur: 
                        l = False
                if h and l: 
                    ans.append(cur)

        return ans


        