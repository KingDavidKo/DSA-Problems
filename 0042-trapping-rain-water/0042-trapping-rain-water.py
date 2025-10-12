class Solution:
    def trap(self, height: List[int]) -> int:

        water_trapped = 0

        left = 0
        right = len(height) - 1

        lmax = height[0]
        rmax = height[-1]


        while (left < right):
            if (height[left] <= height[right]):
                lmax = max(lmax, height[left])
                water_trapped += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax, height[right])
                water_trapped += rmax - height[right]
                right -= 1
        return water_trapped



        