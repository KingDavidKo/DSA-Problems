class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0, currElement, valCount = 0;
        if(nums.length == 0) {
            return 0;
        } else if(nums.length == 1) {
            return nums[0] == val ? 0 : 1;
        } 
        for(int i = 0; i < nums.length; i++) {
            currElement = nums[i];
            if(currElement == val) {
                valCount++;
            } else {
                nums[i - valCount] = nums[i];
                k++;
            }
        }
        return k;
    }
}