/*
 * Solution -- Warmup 1: Linear Search
 * =====================================
 * Chapter 9: Finding Needles -- The Power of Searching
 *
 * APPROACH: Scan every element left to right. Return index on match.
 * TIME:  O(n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int target) {
    for (int i = 0; i < (int)arr.size(); i++) {
        if (arr[i] == target) return i;
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
