class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0;
        int right = 0;
        for (int i = 1; i < nums.length; i++) {
            right += nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            if (left == right) {
                return i;
            }
            left += nums[i];
            if (i == nums.length - 1) {
                right = 0;
            } else {
                right -= nums[i+1];
            }
        }
        return -1;
    }
}