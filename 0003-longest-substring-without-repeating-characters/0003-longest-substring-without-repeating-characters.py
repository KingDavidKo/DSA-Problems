class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        count = 0
        max_length = 0
        ptr = 0
        string = ''
        for i in range(len(s)):
            if s[i] not in seen:
                count += 1
                seen[s[i]] = 0
                if count > max_length:
                    max_length = count  
            else:
                while (ptr != i):
                    if s[ptr] == s[i]:
                        ptr += 1
                        break
                    else:
                        del seen[s[ptr]]
                        count -= 1
                        ptr += 1
        return max_length


        