/*
 * Solution -- Practice 3: Count Occurrences
 * ============================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Helper function with index parameter.
 *           Base case: idx == arr.size() returns 0.
 *           Count = (arr[idx]==target ? 1 : 0) + helper(idx+1).
 * TIME:  O(n)
 * SPACE: O(n) call stack
 */

#include <iostream>
#include <vector>
using namespace std;

int helper(const vector<int>& arr, int target, int idx) {
    if (idx == (int)arr.size()) return 0;
    int count = (arr[idx] == target) ? 1 : 0;
    return count + helper(arr, target, idx + 1);
}

int solve(vector<int> arr, int target) {
    return helper(arr, target, 0);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    cout << solve(arr, target) << endl;
    return 0;
}
