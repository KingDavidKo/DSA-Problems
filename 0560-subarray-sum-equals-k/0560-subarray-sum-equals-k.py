class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}

        prefixsums = []

        output = 0
        for i in nums:
            output += i
            prefixsums.append(output)
        output = 0
        
        for i in range(len(prefixsums)):
            
            if prefixsums[i] - k in freq:
                output += freq[prefixsums[i] - k]
            if prefixsums[i] in freq:
                freq[prefixsums[i]] += 1
            else:
                freq[prefixsums[i]] = 1
        return output
        