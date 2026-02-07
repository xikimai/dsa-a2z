/*
 * Solution -- Practice 4: Search in Rotated Sorted Array
 * ========================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Binary search. At each step, one half is always sorted.
 *           Determine which half is sorted, then check if target is in
 *           that half to decide which way to go.
 * TIME:  O(log n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;

        // Left half is sorted
        if (arr[lo] <= arr[mid]) {
            if (target >= arr[lo] && target < arr[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (target > arr[mid] && target <= arr[hi]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }
    return -1;
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
