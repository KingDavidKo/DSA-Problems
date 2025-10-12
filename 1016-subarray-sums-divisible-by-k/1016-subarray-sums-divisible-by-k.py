class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = []

        total = 0
        for i in nums:
            total += i
            prefix.append(total)
        


        freq = {
            0: 1
        }
        output = 0
        print (prefix)
        for i in range(len(prefix)):
            
            if prefix[i] % k in freq:
                output += freq[prefix[i] % k]

            if prefix[i] % k in freq:
                freq[prefix[i] % k ] += 1
            else:
                freq[prefix[i] % k] = 1
        print(freq)
        return output

        