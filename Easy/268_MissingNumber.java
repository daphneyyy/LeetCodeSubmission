/* Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array. */

class Solution {
    public int missingNumber(int[] nums) {
        boolean[] contains = new boolean[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            contains[nums[i]] = true;
        }
        for (int i = 0; i < nums.length + 1; i++) {
            if (!contains[i]) {
                return i;
            }
        }
        return 0;
    }
}
