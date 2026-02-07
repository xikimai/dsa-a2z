/*
 * Warmup 1: Selection Sort
 * =========================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Implement selection sort. Repeatedly find the minimum element
 *   from the unsorted portion and place it at the beginning.
 *
 * EXAMPLES:
 *   solve({64,25,12,22,11}) -> {11,12,22,25,64}
 *   solve({1,2,3,4,5})      -> {1,2,3,4,5}
 *   solve({5,4,3,2,1})      -> {1,2,3,4,5}
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
