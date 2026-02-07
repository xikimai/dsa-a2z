/*
 * Practice 1: Merge Sort
 * =========================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Implement merge sort. Divide the array in half, recursively sort
 *   each half, then merge the two sorted halves together.
 *
 * EXAMPLES:
 *   solve({38,27,43,3,9,82,10}) -> {3,9,10,27,38,43,82}
 *   solve({5,4,3,2,1})         -> {1,2,3,4,5}
 *   solve({1})                  -> {1}
 *   solve({})                   -> {}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Implement a merge helper function!
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
