class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = 0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                j = i + 1
                while j in nums:
                    j += 1
                output = max(output, j - i)
        return output     