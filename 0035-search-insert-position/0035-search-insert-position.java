class Solution {
    public int searchInsert(int[] nums, int target) {
        // Solution 1
        /*
        if(nums.length == 0) {
            return 0;
        }
        if(nums.length == 1) {
            return nums[0] == target || nums[0] > target ? 0 : 1;
        }
        for(int i = 1; i < nums.length; i++) {
            if((nums[i] == target) || (nums[i] > target && nums[i-1] < target)) {
                return i;
            }
        }
        return nums.length; */

        // Solution 2
        if(nums.length == 0) {
            return 0;
        }
        int start = 0, end = nums.length - 1, mid;

        while(start != end) {
            mid = (end - start) == 1 ? start : (end - start)/2 + start;
            if(nums[mid] == target) {
                return mid;
            } else if(nums[mid + 1] == target) {
                return mid + 1;
            } else if(nums[mid] < target && nums[mid + 1] > target) {
                return mid + 1;
            } else if(nums[mid] < target) {
                start = mid + 1;
            } else if(nums[mid] > target) {
                end = mid;
            }
        }
        return nums[start] >= target ? 0 : start + 1;
    }
}