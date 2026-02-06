/*
 * Solution — Practice 4: Statistics
 * ==================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Write three helper functions that each do one scan through the data.
 *   find_min and find_max initialize with the first element and compare
 *   against the rest. find_average sums all elements and divides.
 *
 * TIME COMPLEXITY:  O(n) — three passes, still linear
 * SPACE COMPLEXITY: O(1) for helpers; O(1) extra for the result vector
 */

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int find_min(vector<int>& nums) {
    int result = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        if (nums[i] < result) {
            result = nums[i];
        }
    }
    return result;
}

int find_max(vector<int>& nums) {
    int result = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        if (nums[i] > result) {
            result = nums[i];
        }
    }
    return result;
}

double find_average(vector<int>& nums) {
    double sum = 0;
    for (int val : nums) {
        sum += val;
    }
    return sum / nums.size();
}

vector<double> solve(vector<int> nums) {
    if (nums.empty()) return {};

    double mn = (double)find_min(nums);
    double mx = (double)find_max(nums);
    double avg = round(find_average(nums) * 100.0) / 100.0;

    return {mn, mx, avg};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    vector<double> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
