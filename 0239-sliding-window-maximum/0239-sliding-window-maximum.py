class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        i = 0
        window = deque()
        for i in range(len(nums)):
            while (window and window[-1] < nums[i]):
                window.pop()
            window.append(nums[i])

            if i >= k and nums[i - k] == window[0]:
                window.popleft()

            if (i >= k-1):
                output.append(window[0])
        return output
