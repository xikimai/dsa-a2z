/*
 * Solution for Practice 1: Top K Frequent Elements
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Build frequency map, then use a min-heap of size k keyed by
 *           frequency. Return the k elements with highest frequency, sorted.
 * TIME:  O(n + m log k) where m = unique elements
 * SPACE: O(n) for the frequency map
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums, int k) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;

    // Min-heap of (frequency, value) — keeps top k by frequency
    auto cmp = [](const pair<int,int>& a, const pair<int,int>& b) {
        return a.first > b.first;  // min-heap by frequency
    };
    priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);

    for (auto& [val, cnt] : freq) {
        pq.push({cnt, val});
        if ((int)pq.size() > k) pq.pop();
    }

    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top().second);
        pq.pop();
    }
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cin >> k;
    vector<int> result = solve(nums, k);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
