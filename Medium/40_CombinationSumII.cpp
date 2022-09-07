// Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

// Each number in candidates may only be used once in the combination.

// Note: The solution set must not contain duplicate combinations.

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
            backtrack(candidates, target-candidates[i], res, queue, i+1);
            prev = candidates[i];
            queue.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> cur_vec;
        sort(candidates.begin(), candidates.end());
        backtrack(candidates, target, res, cur_vec, 0);
        return res;
    }
};
