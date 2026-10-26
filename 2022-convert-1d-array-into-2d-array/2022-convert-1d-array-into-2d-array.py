class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:

        if m*n != len(original): return []
        nn = len(original)
        mat = []
        for st in range(0,nn,n):
            row = []
            for j in range(st,st+n):
                row.append(original[j])
            mat.append(row)
        return mat
