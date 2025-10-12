class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        i = 0
        for j in range(1, len(prices)):
            max_prof = max(prices[j] - prices[i], max_prof)
            if prices[i] > prices[j]:
                i = j
        return max_prof
