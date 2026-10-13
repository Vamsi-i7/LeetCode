class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)

        def solv(n,dp):
            if n == 1 or n == 0: return 1
            if dp[n] != -1: return dp[n]
            dp[n] = solv(n-1,dp) + solv(n-2,dp)
            return dp[n]
        return solv(n,dp)

