class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i in range(len(nums)):
            j,k  = i + 1,len(nums) - 1

            while (j < k):
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif total > 0:
                    k -=1
                else:
                    j += 1
        return list(output)
        