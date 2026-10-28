from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # arr = [ch * f for ch, f in Counter(s).most_common()]
        return "".join([ch * f for ch, f in Counter(s).most_common()])

        