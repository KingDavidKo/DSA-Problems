class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        output = 1
        unique = set(nums)
        while unique:
            i = unique.pop()
            low = i - 1
            high = i + 1
    
            while low in unique or high in unique:
                if low in unique:
                    unique.discard(low)
                    low -=1
                if high in unique:
                    unique.discard(high)
                    high +=1
            high -=1
            low += 1
            output = max(high-low + 1, output)
        return output
            
            

        

        