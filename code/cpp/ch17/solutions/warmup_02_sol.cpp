/*
 * Solution for Warmup 2: Sort Using Heap (Heapsort)
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Push all elements into a min-heap, then pop them all.
 *           Each pop gives the next smallest element.
 * TIME:  O(n log n)
 * SPACE: O(n)
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    priority_queue<int, vector<int>, greater<int>> pq(arr.begin(), arr.end());
    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top());
        pq.pop();
    }
    return result;
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
