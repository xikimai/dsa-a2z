/*
 * Warmup 2: Bubble Sort
 * =========================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Implement bubble sort with early termination. If no swaps
 *   occur in a pass, the array is already sorted -- stop early.
 *
 * EXAMPLES:
 *   solve({64,34,25,12,22,11,90}) -> {11,12,22,25,34,64,90}
 *   solve({1,2,3,4})             -> {1,2,3,4}
 *   solve({2,1})                 -> {1,2}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^4
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Use a "swapped" flag for early termination.
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return arr;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
