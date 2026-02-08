/*
 * Example 02: Priority Queue Usage Patterns
 * ============================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * Demonstrates:
 *   Part 1: Custom comparators with lambda
 *   Part 2: ER triage simulation with pairs
 *   Part 3: Top-K elements
 *   Part 4: Merging sorted arrays with a PQ
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

// ── Part 1: Custom Comparators ──────────────────────────────────────

void part1_custom_comparators() {
    cout << "=== Part 1: Custom Comparators ===" << endl;

    // Min-heap with greater<>
    priority_queue<int, vector<int>, greater<int>> minPQ;
    for (int x : {5, 3, 8, 1, 2}) minPQ.push(x);
    cout << "  Min-heap: ";
    while (!minPQ.empty()) { cout << minPQ.top() << " "; minPQ.pop(); }
    cout << endl;

    // Custom lambda comparator for pairs (min by first element)
    auto cmp = [](const pair<int,string>& a, const pair<int,string>& b) {
        return a.first > b.first;  // greater = min-heap
    };
    priority_queue<pair<int,string>, vector<pair<int,string>>, decltype(cmp)> pq(cmp);
    pq.push({3, "low"});
    pq.push({1, "high"});
    pq.push({2, "medium"});

    cout << "  Custom min by first: ";
    while (!pq.empty()) {
        cout << "(" << pq.top().first << "," << pq.top().second << ") ";
        pq.pop();
    }
    cout << endl;
}

// ── Part 2: ER Triage ──────────────────────────────────────────────

void part2_er_triage() {
    cout << "\n=== Part 2: ER Triage Simulation ===" << endl;

    auto cmp = [](const pair<int,string>& a, const pair<int,string>& b) {
        return a.first > b.first;  // lower number = higher urgency
    };
    priority_queue<pair<int,string>, vector<pair<int,string>>, decltype(cmp)> er(cmp);

    er.push({3, "scraped knee"});
    er.push({1, "chest pain"});
    er.push({5, "headache"});
    er.push({2, "broken arm"});
    er.push({1, "allergic reaction"});

    cout << "  Doctor sees:" << endl;
    while (!er.empty()) {
        auto [priority, condition] = er.top();
        er.pop();
        cout << "    Priority " << priority << ": " << condition << endl;
    }
}

// ── Part 3: Top-K Elements ─────────────────────────────────────────

void part3_top_k() {
    cout << "\n=== Part 3: Top-K Elements ===" << endl;

    vector<int> scores = {85, 92, 78, 95, 88, 76, 99, 82, 91, 73};
    int k = 3;

    // Min-heap of size k for top-k largest
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int s : scores) {
        pq.push(s);
        if ((int)pq.size() > k) pq.pop();
    }

    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top());
        pq.pop();
    }
    sort(result.rbegin(), result.rend());
    cout << "  Top " << k << " scores: ";
    for (int x : result) cout << x << " ";
    cout << endl;
}

// ── Part 4: Merge Sorted Arrays ────────────────────────────────────

void part4_merge_sorted() {
    cout << "\n=== Part 4: Merging 3 Sorted Arrays ===" << endl;

    vector<vector<int>> arrays = {{1,4,7}, {2,5,8}, {3,6,9}};

    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) > get<0>(b);
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);

    for (int i = 0; i < (int)arrays.size(); i++) {
        if (!arrays[i].empty()) {
            pq.push({arrays[i][0], i, 0});
        }
    }

    cout << "  Merged: ";
    while (!pq.empty()) {
        auto [val, ai, ei] = pq.top();
        pq.pop();
        cout << val << " ";
        if (ei + 1 < (int)arrays[ai].size()) {
            pq.push({arrays[ai][ei+1], ai, ei+1});
        }
    }
    cout << endl;
}

// ── Main ────────────────────────────────────────────────────────────

int main() {
    part1_custom_comparators();
    part2_er_triage();
    part3_top_k();
    part4_merge_sorted();
    return 0;
}
