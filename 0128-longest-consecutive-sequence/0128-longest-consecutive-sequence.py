class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = 0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                count = 0
                j = i
                while j in nums:
                    count += 1
                    j += 1
                output = max(output, count)
        return output     