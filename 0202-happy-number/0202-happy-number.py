class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        for i in range(1000):
            temp = 0
            while (n>0):
                temp += (n%10)**2
                n = n//10
            n = temp
            if n in seen:
                return False
            if n == 1:
                return True
            else:
                seen.add(n)
        return False

        