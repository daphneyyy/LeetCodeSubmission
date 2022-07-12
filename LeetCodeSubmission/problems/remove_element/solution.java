class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) {
            return 0;
        }
        int cnt = 0;
        int right = nums.length - 1;
        while (right >= 0) {
            if (nums[right] == val) {
                right--;
                cnt++;
            } else {
                break;
            }
        }
        int i = 0;
        while (i < right) {
            if ((nums[i] == val) & (i != right)) {
                nums[i] = nums[right];
                nums[right] = val;
                right--;
                cnt++;
            }
            i++;
            // if (i == right) {
            //     if (nums[i] == val) {
            //         cnt++;
            //     }
            // }
            while (right >= 0) {
                if (nums[right] == val) {
                    right--;
                    cnt++;
                } else {
                    break;
                }
            }
        }
        return nums.length-cnt;
    }
}