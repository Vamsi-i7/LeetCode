class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        c = 0
        while len(g) and len(s):
            gk = g[-1]
            sk = s[-1]
            if sk >= gk:
                c += 1
                s.pop()
            g.pop()

        return c

        