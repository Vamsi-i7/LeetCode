import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        # use max heap concept, import heapq
        heap = []
        for num in nums: 
            heapq.heappush(heap,-num)
        original_sum = sum(nums)
        curr_sum = original_sum
        ans = 0
        while curr_sum > original_sum / 2:
            ans += 1
            top = -heapq.heappop(heap)
            curr_sum -= top / 2
            heapq.heappush(heap,-top/2)
        return ans
        