class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        output = 1
        m -= 1
        n -= 1
        for i in range(m+n, max(m,n), -1):
            output *= i
        for i in range(1,min(m,n)+1):
            output = output // i
        return output