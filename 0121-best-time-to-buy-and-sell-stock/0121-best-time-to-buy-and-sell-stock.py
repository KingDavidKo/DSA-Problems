class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        hold = 10000000
        for i in prices:
            if i < hold:
                hold = i
            else:
                maxProf = max(maxProf,  i - hold)
        return maxProf