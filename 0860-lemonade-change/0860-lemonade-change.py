class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fc = 0
        tc = 0
        for i in bills:
            if i == 5: fc += 1
            elif i == 10:
                if fc == 0:
                    return False
                fc -= 1
                tc += 1
            else:
                if fc > 0 and tc > 0:
                    fc -= 1
                    tc -= 1
                elif fc >= 3:
                    fc -= 3
                else:
                    return False
        return True



        
