/*
 * Solution -- Challenge 1: Find Peak Element
 * =============================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH:
 *   Linear: scan for first element greater than its right neighbor.
 *   Binary: if arr[mid] < arr[mid+1], peak is to the right; else left.
 * TIME:  O(n) linear, O(log n) binary
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve_linear(vector<int> arr) {
    int n = (int)arr.size();
    if (n == 1) return 0;
    for (int i = 0; i < n; i++) {
        bool leftOk = (i == 0) || (arr[i] > arr[i - 1]);
        bool rightOk = (i == n - 1) || (arr[i] > arr[i + 1]);
        if (leftOk && rightOk) return i;
    }
    return 0;  // should not reach here
}

int solve_binary(vector<int> arr) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] < arr[mid + 1]) {
            lo = mid + 1;  // peak is to the right
        } else {
            hi = mid;  // peak is here or to the left
        }
    }
    return lo;
}

int solve(vector<int> arr) {
    return solve_binary(arr);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
