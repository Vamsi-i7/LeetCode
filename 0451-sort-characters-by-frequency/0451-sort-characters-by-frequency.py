from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        x = Counter(s).most_common()
        arr = []
        for ch, f in x:
            arr.append(ch * f)
        print(arr)
        return "".join(arr)

        