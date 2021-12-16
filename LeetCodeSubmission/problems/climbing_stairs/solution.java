class Solution {
    public int climbStairs(int n) {
        int second = 1;
        int total = 1;
        for (int i = 1; i < n; i++) {
            int tempA = total;
            total += second;
            second = tempA;
        }
        return total;
    }
}