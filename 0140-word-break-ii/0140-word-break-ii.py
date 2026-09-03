class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        curr = []
        ans = []
        def fun(idx):
            if idx == len(s):
                ans.append(" ".join(curr))
                return
            for j in range(idx , len(s)):
                temp = s[idx: j+1]
                if temp in wordDict:
                    curr.append(temp)
                    fun(j+1)
                    curr.pop()
        fun(0)
        return ans
