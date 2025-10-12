class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        output = [False] * (n + 1)
        output[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if output[j] and s[j:i] in wordDict:
                    output[i] = True
                    break
        return output[n]
