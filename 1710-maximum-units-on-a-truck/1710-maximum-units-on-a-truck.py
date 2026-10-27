class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: x[1],reverse = True)
        ts = truckSize
        total = 0
        for b,u in boxTypes:
            take = min(ts,b)

            total += take * u 
            ts -= take

            if ts <= 0: 
                break
        return total
            





        