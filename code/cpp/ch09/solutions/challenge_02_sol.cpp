/*
 * Solution -- Challenge 2: Single Element in Sorted Array
 * =========================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Before the single element, pairs start at even indices.
 *           After it, pairs start at odd indices.
 *           Binary search on even indices: if arr[mid] == arr[mid+1],
 *           the single element is to the right; otherwise to the left.
 * TIME:  O(log n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr) {
    int n = (int)arr.size();
    if (n == 1) return arr[0];

    int lo = 0, hi = n - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        // Ensure mid is even so we can compare pairs
        if (mid % 2 == 1) mid--;

        if (arr[mid] == arr[mid + 1]) {
            // Pair is intact, single element is to the right
            lo = mid + 2;
        } else {
            // Pair is broken, single element is here or to the left
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
