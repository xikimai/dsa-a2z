/*
 * Solution -- Challenge 1: Find Duplicates (Multiple Approaches)
 * ===============================================================
 * Chapter 5: Collections
 *
 * Three approaches:
 *   1. solve_brute — O(n^2) nested loops
 *   2. solve_sort  — O(n log n) sort then adjacent check
 *   3. solve_set   — O(n) using unordered_set
 *
 * solve() calls solve_set (the best approach).
 *
 * TIME COMPLEXITY:  O(n) for solve_set
 * SPACE COMPLEXITY: O(n)
 */

#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> solve_brute(vector<int>& nums) {
    unordered_set<int> dups;
    for (int i = 0; i < (int)nums.size(); i++) {
        for (int j = i + 1; j < (int)nums.size(); j++) {
            if (nums[i] == nums[j]) {
                dups.insert(nums[i]);
            }
        }
    }
    vector<int> result(dups.begin(), dups.end());
    sort(result.begin(), result.end());
    return result;
}

vector<int> solve_sort(vector<int>& nums) {
    if (nums.empty()) return {};
    vector<int> sorted_nums = nums;
    sort(sorted_nums.begin(), sorted_nums.end());

    unordered_set<int> dups;
    for (int i = 1; i < (int)sorted_nums.size(); i++) {
        if (sorted_nums[i] == sorted_nums[i - 1]) {
            dups.insert(sorted_nums[i]);
        }
    }
    vector<int> result(dups.begin(), dups.end());
    sort(result.begin(), result.end());
    return result;
}

vector<int> solve_set(vector<int>& nums) {
    unordered_set<int> seen;
    unordered_set<int> dups;
    for (int x : nums) {
        if (seen.count(x)) {
            dups.insert(x);
        }
        seen.insert(x);
    }
    vector<int> result(dups.begin(), dups.end());
    sort(result.begin(), result.end());
    return result;
}

vector<int> solve(vector<int>& nums) {
    return solve_set(nums);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
