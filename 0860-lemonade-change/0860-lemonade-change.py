class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        # f = 1
        # t = 1
        # tt = 1
        # a = 0
        # for i in bills:
        #     if a < 0: return False
        #     if i == 5: 
        #         a += 1
        #     elif i == 10: 
        #         a -= 1
        #         a += 1
        #     else: 
        #         a -= 3
        #     return True
        # res = []
        # if bills[0] != 5: return False
        # for i in range(len(bills)):
        #     if sum(res) <= bills[i]: return False

        #     if i == 5:

        five=0
        ten=0
        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                if five==0:
                    return False 
                five-=1
                ten+=1
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False 
        return True 

        

        
