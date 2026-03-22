class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(numbers)):
            if target - numbers[i] in freq:
                return [freq[target - numbers[i]] + 1, i + 1]
            freq[numbers[i]] = i
        