// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int i : nums) {
            if (cnts.get(i) == null) {
                cnts.put(i, 1);
            } else {
                return true;
            }
        }
        return false;
    }
}
