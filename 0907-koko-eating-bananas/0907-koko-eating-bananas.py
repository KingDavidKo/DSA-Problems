class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        upper = max(piles)
        lower = max(sum(piles)//h, 1)
        while lower <= upper:
            count = 0
            k = (lower + upper) //2
            for i in piles:
                if i % k != 0:
                    count += i//k + 1
                else:
                    count += i//k
            if count > h:
                lower = k + 1
            else:
                upper = k - 1
        return lower



        
        