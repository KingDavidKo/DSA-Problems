class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Boolean> numsMap = new HashMap<Integer, Boolean>();
        int currNum;
        for(int i = 0; i < nums.length; i++) {
            currNum = nums[i];
            if(numsMap.get(currNum) == null) {
                numsMap.put(currNum, true);
            } else { 
                return true;
            }
        }
        return false;
    }
}