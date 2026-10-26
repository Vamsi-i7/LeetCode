class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m*n != len(original): return []
        k = 0
        ans = []
        for i in range(m):
            res = []
            for j in range(n):
                res.append(original[k])
                k += 1
            ans.append(res)
        return ans
