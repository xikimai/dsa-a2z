/*
 * Solution — Challenge 2: Apply Operations
 * =========================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Write a helper function for each operation. Loop through the
 *   operations list and dispatch to the matching helper.
 *   Unknown operations are silently skipped.
 *
 * TIME COMPLEXITY:  O(m * n log n) worst case, where m = number of operations
 *                   and n = nums.size(). The sort operation is O(n log n);
 *                   other operations are O(n).
 * SPACE COMPLEXITY: O(1) extra (all modifications are in-place on the copy)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void op_double(vector<int>& nums) {
    for (int& x : nums) {
        x *= 2;
    }
}

void op_negate(vector<int>& nums) {
    for (int& x : nums) {
        x *= -1;
    }
}

void op_sort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
}

void op_reverse(vector<int>& nums) {
    reverse(nums.begin(), nums.end());
}

void op_square(vector<int>& nums) {
    for (int& x : nums) {
        x = x * x;
    }
}

vector<int> solve(vector<int> nums, vector<string> operations) {
    for (const string& op : operations) {
        if (op == "double")       op_double(nums);
        else if (op == "negate")  op_negate(nums);
        else if (op == "sort")    op_sort(nums);
        else if (op == "reverse") op_reverse(nums);
        else if (op == "square")  op_square(nums);
        // Unknown operations: silently ignored
    }
    return nums;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    int m;
    cin >> m;
    vector<string> operations(m);
    for (int i = 0; i < m; i++) {
        cin >> operations[i];
    }
    vector<int> result = solve(nums, operations);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
