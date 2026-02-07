/*
 * Solution -- Warmup 4: Check If Sorted
 * =======================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Linear scan checking arr[i] <= arr[i+1] for all consecutive pairs.
 * TIME:  O(n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr) {
    for (int i = 0; i + 1 < (int)arr.size(); i++) {
        if (arr[i] > arr[i + 1]) return false;
    }
    return true;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << (solve(arr) ? "true" : "false") << endl;
    return 0;
}
