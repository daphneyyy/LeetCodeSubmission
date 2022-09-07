// Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

// It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution {
public:
    void backtrack(vector<int>& candidates, const int target, vector<vector<int>> &res,
        vector<int> queue, int idx) {
        if (target == 0) {
            res.push_back(queue);
        } else if (target < 0) {
            return;
        }
        int prev = -1;
        for (unsigned int i = idx; i < candidates.size(); i++) {
            if (candidates[i] == prev) {
                continue;
            }
            queue.push_back(candidates[i]);
            backtrack(candidates, target-candidates[i], res, queue, i);
            prev = candidates[i];
            queue.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> cur_vec;
        sort(candidates.begin(), candidates.end());
        backtrack(candidates, target, res, cur_vec, 0);
        return res;
    }
};
