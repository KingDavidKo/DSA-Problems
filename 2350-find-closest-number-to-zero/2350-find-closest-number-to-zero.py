class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        val = 1000000000
        absval = 10000000000

        for i in nums:
            if abs(i) < absval or (abs(i) == absval and i > val):
                val = i
                absval = abs(i)
        return val


        