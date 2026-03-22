class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = [0]*26
        tFreq = [0]*26
        for i in s:
            sFreq[ord(i)-ord('a')] += 1
        for i in t:
            tFreq[ord(i)-ord('a')] += 1
        return sFreq == tFreq