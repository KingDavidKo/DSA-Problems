class Solution:
    def largestVariance(self, s: str) -> int:
        myLetters = [0]*26
        for i in s:
            print(ord(i)-97)
            myLetters[ord(i)-97] += 1
        global_max = 0
        
        for i in range(26):
            for j in range(26):
                if (i == j or myLetters[i] == 0 or myLetters[j] == 0):
                    continue
                major = chr(i+97)
                minor = chr(j+97)
                major_count = 0
                minor_count = 0
                rest_minor = myLetters[j]

                for char in s:
                    if char == major:
                        major_count += 1
                    if char == minor:
                        minor_count += 1
                        rest_minor -= 1
                    if minor_count > 0:
                        global_max = max(global_max, major_count - minor_count)
                    if major_count - minor_count < 0 and rest_minor > 0:
                        major_count = 0
                        minor_count = 0
                
        return global_max

