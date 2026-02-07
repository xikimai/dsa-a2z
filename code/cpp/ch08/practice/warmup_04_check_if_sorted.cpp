/*
 * Warmup 4: Check If Sorted
 * =========================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Given a vector of integers, return true if it is sorted in
 *   non-decreasing order (each element <= the next), false otherwise.
 *   An empty array or single-element array is considered sorted.
 *
 * EXAMPLES:
 *   solve({1,2,3,4,5}) -> true
 *   solve({1,3,2,4,5}) -> false
 *   solve({})          -> true
 *   solve({7})         -> true
 *   solve({1,1,1})     -> true
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace "return false;" with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return false;
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
