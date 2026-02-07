/*
 * Solution -- Practice 2: Upper Bound
 * =====================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Binary search for the first index where arr[index] > target.
 *           If arr[mid] > target, it's a candidate -- search left.
 *           If arr[mid] <= target, search right.
 * TIME:  O(log n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size();  // hi = n (past-the-end)
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] > target) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
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
