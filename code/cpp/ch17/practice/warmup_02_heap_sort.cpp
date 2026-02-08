/*
 * Warmup 2: Sort Using Heap (Heapsort)
 * ======================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an array of integers, return it sorted in ascending order
 *   using a heap (priority queue).
 *
 * EXAMPLES:
 *   solve({5,3,8,1,2})  -> {1,2,3,5,8}
 *   solve({})            -> {}
 *
 * CONSTRAINTS:
 *   - 0 <= arr.size() <= 10^5
 *   - Elements can be any integer
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
