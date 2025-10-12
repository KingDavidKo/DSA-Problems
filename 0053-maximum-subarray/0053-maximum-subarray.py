class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        max_sum = nums[0]

        for i in nums:
            if sums < 0:
                sums = 0
            sums += i
            max_sum = max(max_sum, sums)
        return max_sum
            



        