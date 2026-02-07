/*
 * Practice 3: Dutch National Flag
 * =================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Given an array containing only 0s, 1s, and 2s, sort it in-place
 *   in O(n) time and O(1) extra space.
 *   This is Dijkstra's Dutch National Flag problem.
 *
 * EXAMPLES:
 *   solve({2,0,2,1,1,0}) -> {0,0,1,1,2,2}
 *   solve({2,0,1})       -> {0,1,2}
 *   solve({0,0,0})       -> {0,0,0}
 *   solve({})            -> {}
 *   solve({1})           -> {1}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   arr[i] is 0, 1, or 2
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Use three pointers: low, mid, high.
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
