class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def fun(idx):
            if idx == len(s):
                return [""]
            if idx in memo:
                return memo[idx]
            ans = []
            for i in range(idx + 1, len(s) + 1):
                word = s[idx:i]
                if word in words:
                    for sub in fun(i):
                        if sub:
                            ans.append(word + " " + sub)
                        else:
                            ans.append(word)
            memo[idx] = ans
            return ans

        return fun(0)
