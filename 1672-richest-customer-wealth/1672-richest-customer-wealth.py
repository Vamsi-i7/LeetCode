class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            res = 0
            for j in accounts[i]:
                res += j
            if res > ans:
                ans = res
        return ans


        