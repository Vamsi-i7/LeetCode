from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        dis = {}

        for i in s:
            if i in dis:
                dis[i] += 1
            else:
                dis[i] = 1

        arr =[]
        for ch,f in dis.items():
            arr.append([f,ch])
        arr.sort(reverse = True)
        
        res = []
        for f,ch in arr:
            res.append(ch * f)
        return "".join(res)
        