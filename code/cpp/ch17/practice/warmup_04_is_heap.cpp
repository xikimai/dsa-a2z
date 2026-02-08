/*
 * Warmup 4: Check if Array is a Min-Heap
 * =========================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an array of integers, return true if it satisfies the
 *   min-heap property: every parent <= both its children.
 *
 * EXAMPLES:
 *   solve({1,3,2,7,6,5,4})    -> true
 *   solve({7,3,2,1,6,5,4})    -> false
 *   solve({})                  -> true
 *
 * CONSTRAINTS:
 *   - 0 <= arr.size() <= 10^5
 *   - Elements can be any integer
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr) {
    // TODO: Replace this with your solution
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
