class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        capacity = 0
        station = 0
        for i in range(len(gas)):
            capacity += gas[i]
            capacity -= cost[i]
            if capacity < 0:
                station = i+1
                capacity = 0
        return station

        