class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # input 1 nums = [3,5,2,3]
        # input 2 nums = [3,5,4,2,4,6]
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(len(nums)//2):
            res = []
            res.append((nums[i],nums[n-i-1]))
            ans.append(res)
        fin = []
        for i in ans:
            s = sum(i[0])
            fin.append(s)

        return max(fin)

            
