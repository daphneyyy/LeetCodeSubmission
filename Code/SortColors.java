// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

class Solution {
    public void sortColors(int[] nums) {
        int countSorted = nums.length - 1;
        while (countSorted > 0) {
            int maxIdx = 0;
            int max = nums[maxIdx];
            for (int i = 0; i < countSorted + 1; i++) {
                if (nums[i] > max) {
                    max = nums[i];
                    maxIdx = i;
                }
            }
            int temp = nums[countSorted];
            nums[countSorted] = max;
            nums[maxIdx] = temp;
            countSorted -= 1;
        }
    }
}
