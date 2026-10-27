class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # fe = position[0]
        # e = 0
        # o = 0
        # if fe % 2 == 0:
        #     for i in range(1,len(position)):
        #         if position[i]%2 != 0: e += 1
        #     return e
        # else:
        #     for i in range(1,len(position)):
        #         if position[i]%2 == 0: o += 1
        #     return o
        e = 0
        o = 0
        for i in position:
            if i % 2 ==0: e += 1
            else:
                o += 1
        return min(e,o)
        



        