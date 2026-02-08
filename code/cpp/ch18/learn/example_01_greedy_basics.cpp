/*
 * Example 01: Greedy Basics — Activity Selection Step by Step
 * ============================================================
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * Demonstrates:
 *   Part 1: Activity Selection: sort by end time, pick greedily
 *   Part 2: When Greedy Fails: coin change counterexample
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    // ── Part 1: Activity Selection ──
    cout << "=== Part 1: Activity Selection ===" << endl;

    struct Activity { string name; int start, end; };
    vector<Activity> acts = {
        {"A", 9, 10}, {"B", 9, 12}, {"C", 10, 11},
        {"D", 11, 14}, {"E", 11, 12}, {"F", 13, 15}
    };

    cout << "  Original:" << endl;
    for (auto& a : acts)
        cout << "    " << a.name << ": [" << a.start << ", " << a.end << ")" << endl;

    sort(acts.begin(), acts.end(), [](auto& a, auto& b) { return a.end < b.end; });

    cout << "\n  Sorted by end time:" << endl;
    for (auto& a : acts)
        cout << "    " << a.name << ": [" << a.start << ", " << a.end << ")" << endl;

    cout << "\n  Greedy selection:" << endl;
    int lastEnd = 0, count = 0;
    for (auto& a : acts) {
        if (a.start >= lastEnd) {
            cout << "    PICK " << a.name << " [" << a.start << ", " << a.end << ")" << endl;
            lastEnd = a.end;
            count++;
        } else {
            cout << "    SKIP " << a.name << " [" << a.start << ", " << a.end << ")" << endl;
        }
    }
    cout << "  Selected: " << count << " activities\n" << endl;

    // ── Part 2: When Greedy Fails ──
    cout << "=== Part 2: Coin Change — Greedy Fails ===" << endl;
    vector<int> coins = {4, 3, 1};
    int target = 6, rem = 6;
    vector<int> used;
    for (int c : coins) {
        while (rem >= c) { used.push_back(c); rem -= c; }
    }
    cout << "  Coins: {4, 3, 1}, target: " << target << endl;
    cout << "  Greedy: ";
    for (int u : used) cout << u << " ";
    cout << "= " << used.size() << " coins" << endl;
    cout << "  Optimal: 3 + 3 = 2 coins" << endl;
    cout << "  Greedy is WRONG!" << endl;

    return 0;
}
