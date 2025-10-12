class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = False
        stringList1 = list(s)
        stringList2 = list(s)
        n1 = len(stringList1) - 1
        i1 = 0
        i2 = 0

        for i in range(len(s)//2):
            if stringList1[i] != stringList1[n1]:
                deleted = True
                i1 = i
                i2 = n1
                break
            else:
                n1 -= 1
        stringList1.pop(i)
        stringList2.pop(n1)
        success1 = True
        success2 = True
        for i in range((len(s)-1)//2):
            if stringList1[i] != stringList1[len(s)-2-i]:
                success1 = False
                break
        for i in range((len(s)-1)//2):
            if stringList2[i] != stringList2[len(s)-2-i]:
                success2 = False
                break
        return success1 or success2
        




