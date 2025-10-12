class Solution {
    public int[] plusOne(int[] digits) {
         int addOne = 0;
        for(int i = digits.length - 1; i >= 0; i--) {
            if(digits[i] < 9) {
                digits[i] = digits[i] + 1;
                addOne = 0;
                break;
            } else {
                digits[i] = 0;
                addOne = 1;
           }
        } 
        if(addOne == 1) {
            int[] newDigits = new int[digits.length + 1];
            newDigits[0] = 1;
            System.arraycopy( digits, 0, newDigits, 1, digits.length );
            return newDigits;
        }
        return digits;
    }
}