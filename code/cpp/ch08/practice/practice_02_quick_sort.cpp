/*
 * Practice 2: Quick Sort
 * =========================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Implement quick sort using the Lomuto partition scheme.
 *   Pick the last element as the pivot, partition so that all
 *   elements <= pivot are on the left, then recurse.
 *
 * EXAMPLES:
 *   solve({10,7,8,9,1,5}) -> {1,5,7,8,9,10}
 *   solve({3,2,1})        -> {1,2,3}
 *   solve({1})            -> {1}
 *   solve({})             -> {}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Implement a partition helper function!
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
