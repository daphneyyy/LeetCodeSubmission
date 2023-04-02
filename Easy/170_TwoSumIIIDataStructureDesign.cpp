// Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

// Implement the TwoSum class:

// TwoSum() Initializes the TwoSum object, with an empty array initially.
// void add(int number) Adds number to the data structure.
// boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.


#include<vector>
#include <unordered_map>

class TwoSum {
private:
    vector<int> arr;
    unordered_map<int, bool> sums;

public:
    TwoSum() {
        arr = vector<int>();
        sums = unordered_map<int, bool>();
    }
    
    void add(int number) {
        for (auto i: this->arr) {
            sums[i + number] = true;
        }
        this->arr.push_back(number);
    }
    
    bool find(int value) {
        return this->sums.count(value) > 0;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
