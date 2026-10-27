class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr.append(mat[i][j])
        if r * c != len(arr): return mat
        new_mat = []
        for l in range(r):
            res= []
            for k in range(c):
                res.append(arr[l * c + k])
            new_mat.append(res)
        return new_mat

