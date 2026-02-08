/*
 * Solution for Practice 4: Power Set Using Bitmasks
 * TIME: O(n * 2^n)   SPACE: O(n * 2^n)
 */
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    int n = nums.size();
    vector<vector<int>> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                subset.push_back(nums[i]);
            }
        }
        result.push_back(subset);
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    auto result = solve(nums);
    for (auto& s : result) {
        cout << "[";
        for (int j = 0; j < (int)s.size(); j++) {
            if (j > 0) cout << ",";
            cout << s[j];
        }
        cout << "]" << endl;
    }
    return 0;
}
