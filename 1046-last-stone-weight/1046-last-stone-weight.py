class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        output = 0
        while True:
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]
            diff = abs(heapq.heappop_max(stones) - heapq.heappop_max(stones))
            if diff != 0:
                heapq.heappush_max(stones, diff)


        
        