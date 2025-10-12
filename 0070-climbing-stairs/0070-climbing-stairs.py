tracker = {
}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n not in tracker:
            tracker[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return tracker[n]


