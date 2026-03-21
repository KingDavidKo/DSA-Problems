class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A,B = nums1, nums2
        if len(A) > len(B):
            B, A = A, B
        
        l = 0
        r = len(A) - 1
        while True:
            mid = (r + l) // 2
            j = half - mid - 2
            ALeft = -1000000000
            ARight = 1000000000
            if mid >= 0:
                ALeft = A[mid]
            if mid < len(A)-1:
                ARight = A[mid+1]
            BLeft = -1000000000  
            BRight = 1000000000
            if j < len(B)-1:
                BRight = B[j+1]
            if j >= 0:
                BLeft = B[j]

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return min(BRight, ARight)
                return (max(ALeft, BLeft) + min(ARight, BRight))/2
            if ALeft > BRight:
                r = mid - 1
            else:
                l = mid + 1
            


