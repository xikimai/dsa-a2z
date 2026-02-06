/*
 * Solution -- Challenge 1: Two Sum Three Ways
 * =============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * Three approaches:
 *   1. solve_brute — O(n^2) check all pairs
 *   2. solve_sort  — O(n log n) sort + two pointers
 *   3. solve_hash  — O(n) hash map
 *
 * solve() calls solve_hash (the best approach).
 *
 * TIME COMPLEXITY:  O(n) for solve_hash
 * SPACE COMPLEXITY: O(n)
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve_brute(vector<int>& nums, int target) {
    int n = (int)nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

vector<int> solve_sort(vector<int>& nums, int target) {
    int n = (int)nums.size();
    // Create index pairs, sort by value
    vector<pair<int, int>> indexed(n);
    for (int i = 0; i < n; i++) {
        indexed[i] = {nums[i], i};
    }
    sort(indexed.begin(), indexed.end());

    int left = 0;
    int right = n - 1;
    while (left < right) {
        int sum = indexed[left].first + indexed[right].first;
        if (sum == target) {
            int i = indexed[left].second;
            int j = indexed[right].second;
            if (i > j) swap(i, j);
            return {i, j};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {-1, -1};
}

vector<int> solve_hash(vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {-1, -1};
}

vector<int> solve(vector<int>& nums, int target) {
    return solve_hash(nums, target);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int target;
    cin >> target;
    vector<int> result = solve(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
