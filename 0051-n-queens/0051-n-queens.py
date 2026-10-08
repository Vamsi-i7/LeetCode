class Solution:
    def solve(self,col,board,ans,leftrow,upperDia,lowerDia,n):
        if col == n:
            ans.append(board[:])
            return
        for row in range(n):
            if (
                leftrow[row] == 0
                and lowerDia[col + row] == 0
                and upperDia[n-1 + col - row] == 0):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                leftrow[row] = 1
                lowerDia[col + row] = 1
                upperDia[n-1+col-row] = 1
                self.solve(col + 1, board,ans,leftrow,upperDia,lowerDia,n)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                leftrow[row] = 0
                lowerDia[col + row] = 0
                upperDia[n-1+col-row] = 0



    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        upperDia = [0] * (2*n - 1)
        lowerDia = [0] * (2*n - 1)
        self.solve(0,board,ans,leftrow,upperDia,lowerDia,n)
        return ans
        