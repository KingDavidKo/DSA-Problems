class Solution {
    public int removeDuplicates(int[] nums) {
        int currElement, duplCount = 0, k = 0;
        if(nums.length == 0) {
            return 0;
        } else if(nums.length == 1) {
            return 1;
        }

        for(int i = 0; i < nums.length - 1; i++) {
            currElement = nums[i];
            if(currElement == nums[i+1]) {
                duplCount++;
            } else {
                nums[i - duplCount + 1] = nums[i+1];
                k++;
            }
        }
        k++;
        /*
        for(int j = nums.length - 1; j >= nums.length - k; j--) {
            nums[j] = '_';
        } */
        return k;
    }
}