// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

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
