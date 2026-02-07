/*
 * Warmup 3: Insertion Sort
 * =========================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Implement insertion sort. For each element, insert it into
 *   its correct position among the already-sorted elements to its left.
 *
 * EXAMPLES:
 *   solve({12,11,13,5,6}) -> {5,6,11,12,13}
 *   solve({1,2,3})        -> {1,2,3}
 *   solve({3,2,1})        -> {1,2,3}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^4
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
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
