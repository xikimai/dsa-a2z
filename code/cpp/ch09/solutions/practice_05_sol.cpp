/*
 * Solution -- Practice 5: Find Minimum in Rotated Sorted Array
 * ==============================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Binary search. Compare arr[mid] with arr[hi].
 *           If arr[mid] > arr[hi], min is in right half.
 *           Otherwise, min is in left half (including mid).
 * TIME:  O(log n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] > arr[hi]) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return arr[lo];
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
