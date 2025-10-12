class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myList = []
        for i in range(len(nums) + 1):
            myList.append(1)
        
        for i in nums:
            myList[i] = 0
        
        for i in range(len(myList)):
            if myList[i] == 1:
                return i 
        