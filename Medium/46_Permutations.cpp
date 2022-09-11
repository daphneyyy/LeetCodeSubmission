// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution {
public:    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> queue;
        vector<vector<int>> res;
        backtrack(nums, queue, res);
        return res;
    }
    
    void backtrack(vector<int>& nums, vector<int>& queue, vector<vector<int>>& res) {
        if (queue.size() == nums.size()) {
            vector<int> vec{queue};
            res.push_back(vec);
            return;
        }
        vector<int> v1{nums};
        sort(v1.begin(), v1.end());
        vector<int> v2{queue};
        sort(v2.begin(), v2.end());
        vector<int> diff;
        set_difference(v1.begin(), v1.end(), v2.begin(), v2.end(),
                      inserter(diff, diff.begin()));
        for (int i = 0; i < diff.size(); i++) {
            queue.push_back(diff[i]);
            backtrack(nums, queue, res);
            queue.pop_back();
        }
    }
};
