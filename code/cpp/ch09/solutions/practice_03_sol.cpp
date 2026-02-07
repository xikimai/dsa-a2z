/*
 * Solution -- Practice 3: Floor and Ceil
 * ========================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH:
 *   Floor: largest element <= target. Binary search, track candidate.
 *   Ceil:  smallest element >= target. Binary search, track candidate.
 * TIME:  O(log n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr, int target) {
    int n = (int)arr.size();
    int floor_val = -1, ceil_val = -1;

    // Find floor: largest element <= target
    {
        int lo = 0, hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] <= target) {
                floor_val = arr[mid];
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }

    // Find ceil: smallest element >= target
    {
        int lo = 0, hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= target) {
                ceil_val = arr[mid];
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
    }

    return {floor_val, ceil_val};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    vector<int> result = solve(arr, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
