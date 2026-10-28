from collections import Counter;
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        removed = 0
        ans = 0
        for ele,f in Counter(arr).most_common():
            # print(ele,f)
            removed += f
            ans += 1
            if removed >= len(arr) / 2: break
        return ans