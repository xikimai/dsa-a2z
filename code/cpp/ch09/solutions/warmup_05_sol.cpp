/*
 * Solution -- Warmup 5: Count Occurrences
 * =========================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Find first and last occurrence using binary search.
 *           Count = last - first + 1 (if found).
 * TIME:  O(log n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int target) {
    int n = (int)arr.size();
    if (n == 0) return 0;

    // Find first occurrence
    int lo = 0, hi = n - 1;
    int first = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) {
            first = mid;
            hi = mid - 1;
        } else if (arr[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    if (first == -1) return 0;

    // Find last occurrence
    lo = 0;
    hi = n - 1;
    int last = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) {
            last = mid;
            lo = mid + 1;
        } else if (arr[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    return last - first + 1;
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
