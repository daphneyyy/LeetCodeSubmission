// An array is monotonic if it is either monotone increasing or monotone decreasing.
// An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
// Given an integer array nums, return true if the given array is monotonic, or false otherwise.
class Solution {
    public boolean checkIncreasing(int[] nums) {
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (prev > nums[i]) {
                return false;
            }
            prev = nums[i];
        }
        return true;
    }

    public boolean checkDecreasing(int[] nums) {
        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (prev < nums[i]) {
                return false;
            }
            prev = nums[i];
        }
        return true;
    }

    public boolean isMonotonic(int[] nums) {
        if (nums.length == 1) {
            return true;
        }
        int prev = nums[0];
        int cur = nums[1];
        if (prev < cur) {
            return checkIncreasing(nums);
        } else if (prev > cur) {
            return checkDecreasing(nums);
        } else {
            return checkIncreasing(nums) || checkDecreasing(nums);
        }
    }
}