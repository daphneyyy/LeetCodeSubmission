// 704. Binary Search
// Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

class Solution {
    public int search(int[] nums, int target) {
        return binarySearch(0, nums.length, nums, target);
    }
    
    public int binarySearch(int left, int right, int[] nums, int target) {
        int middle = (right+left)/2;
        if (left+1== right) {
            if ((nums[left] != target) && (nums[right-1] != target)) {
                return -1;
            } else if (nums[left] == target) {
                return left;
            } else {
                return right-1;
            }
        }
        if (nums[middle] == target) {
            return middle;
        } else if (nums[middle] > target) {
            return binarySearch(left, middle, nums, target);
        } else {
            return binarySearch(middle, right, nums, target);
        }
    }
}
