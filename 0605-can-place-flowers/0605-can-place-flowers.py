class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        fb = len(flowerbed)
        for i in range(fb):
                if flowerbed[i] == 0:
                    le = (i == 0) or flowerbed[i-1] == 0 
                    re = (i == fb - 1) or flowerbed[i+1] == 0
                    if le and re:
                        flowerbed[i] = 1
                        n -= 1
                        if n <= 0: return True

        return n <= 0


