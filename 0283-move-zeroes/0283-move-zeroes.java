class Solution {
    public void moveZeroes(int[] nums) {
        int zCount = 0, currNum;
        for(int i = 0; i < nums.length; i++) {
            currNum = nums[i];
            if(nums[i] == 0) {
                zCount++;
            } else {
                nums[i - zCount] = currNum;
            }
        }
        for(int j = nums.length - 1; j >= nums.length - zCount; j--) {
            nums[j] = 0;
        }
    }
}