/*
 * Solution for Challenge 1: Reorganize String
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Use a max-heap of (count, char). Greedily place the most frequent
 *           char. After placing, set it aside (prev). Place next most frequent,
 *           then push prev back if it still has count > 0.
 * TIME:  O(n log 26) = O(n)
 * SPACE: O(26) = O(1) auxiliary
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

string solve(string s) {
    int freq[26] = {};
    for (char c : s) freq[c - 'a']++;

    // Check feasibility
    int maxCount = *max_element(freq, freq + 26);
    if (maxCount > ((int)s.size() + 1) / 2) return "";

    // Max-heap of (count, char_index)
    priority_queue<pair<int,int>> pq;
    for (int i = 0; i < 26; i++) {
        if (freq[i] > 0) pq.push({freq[i], i});
    }

    string result;
    pair<int,int> prev = {0, -1};

    while (!pq.empty()) {
        auto [cnt, ch] = pq.top();
        pq.pop();
        result += (char)(ch + 'a');

        // Push previous character back if it still has remaining count
        if (prev.first > 0) {
            pq.push(prev);
        }

        // Update prev to current with decremented count
        prev = {cnt - 1, ch};
    }

    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    cin >> s;
    cout << solve(s) << endl;
    return 0;
}
