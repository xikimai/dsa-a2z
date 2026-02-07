/*
 * Solution -- Challenge 3: Search in Rotated Sorted Array II
 * ============================================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Like P4 but handles duplicates. When arr[lo] == arr[mid]
 *           == arr[hi], we can't tell which half is sorted, so we
 *           shrink both ends (lo++, hi--). Average O(log n), worst O(n).
 * TIME:  O(log n) average, O(n) worst case
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr, int target) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return true;

        // Handle ambiguous case: can't determine sorted half
        if (arr[lo] == arr[mid] && arr[mid] == arr[hi]) {
            lo++;
            hi--;
            continue;
        }

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
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    cout << (solve(arr, target) ? "true" : "false") << endl;
    return 0;
}
