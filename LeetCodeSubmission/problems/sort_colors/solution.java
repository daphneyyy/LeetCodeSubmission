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