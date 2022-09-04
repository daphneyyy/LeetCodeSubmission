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