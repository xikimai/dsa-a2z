/*
 * Solution for Warmup 3: Last Stone Weight
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Use a max-heap (C++ default). Pop two largest stones each turn.
 *           If they differ, push the difference back.
 * TIME:  O(n log n)
 * SPACE: O(n)
 */

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<int> stones) {
    priority_queue<int> pq(stones.begin(), stones.end());  // Max-heap
    while (pq.size() > 1) {
        int first = pq.top(); pq.pop();
        int second = pq.top(); pq.pop();
        if (first != second) {
            pq.push(first - second);
        }
    }
    return pq.empty() ? 0 : pq.top();
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> stones(n);
    for (int i = 0; i < n; i++) cin >> stones[i];
    cout << solve(stones) << endl;
    return 0;
}
