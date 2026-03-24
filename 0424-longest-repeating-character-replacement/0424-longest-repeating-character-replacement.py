class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        maxLength = 0
        maxFreq = 0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0
            freq[s[right]] += 1
            maxFreq = max(freq[s[right]], maxFreq)
            if right-left + 1 - maxFreq > k:
                freq[s[left]] -= 1                
                left += 1
            else:
                maxLength = max(maxLength, right-left + 1)
        return maxLength
            


            
             


        