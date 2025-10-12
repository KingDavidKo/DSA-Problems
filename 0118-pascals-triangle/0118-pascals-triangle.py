
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        myList = []
        for i in range(numRows):
            if i == 0:
                myList.append([1])
            else:
                myList.append([1])
                for j in range(i - 1):
                    myList[i].append(myList[i-1][j] + myList[i-1][j + 1])
                myList[i].append(1)

        return myList