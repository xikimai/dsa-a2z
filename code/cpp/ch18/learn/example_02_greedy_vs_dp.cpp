/*
 * Example 02: Greedy vs DP — Fractional vs 0/1 Knapsack
 * =======================================================
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * Demonstrates:
 *   Part 1: Fractional Knapsack (greedy works)
 *   Part 2: 0/1 Knapsack counterexample (greedy fails)
 *   Part 3: Exchange argument idea
 */

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // ── Part 1: Fractional Knapsack ──
    cout << "=== Part 1: Fractional Knapsack (Greedy) ===" << endl;

    vector<pair<int,int>> items = {{10,60}, {20,100}, {30,120}};
    int capacity = 50;
    cout << "  Items (weight, value): ";
    for (auto& [w,v] : items) cout << "(" << w << "," << v << ") ";
    cout << endl << "  Capacity: " << capacity << endl;

    sort(items.begin(), items.end(), [](auto& a, auto& b) {
        return (double)a.second/a.first > (double)b.second/b.first;
    });

    double total = 0;
    int rem = capacity;
    for (auto& [w, v] : items) {
        if (rem <= 0) break;
        int take = min(w, rem);
        double val = take * ((double)v / w);
        total += val;
        rem -= take;
        cout << "  Take " << take << "/" << w << " of (w=" << w << ",v=" << v
             << "), value=" << fixed << setprecision(1) << val << endl;
    }
    cout << "  Total: " << total << endl << endl;

    // ── Part 2: 0/1 Knapsack Fails ──
    cout << "=== Part 2: 0/1 Knapsack (Greedy Fails!) ===" << endl;
    cout << "  Items: (6,8), (5,5), (5,5). Capacity: 10" << endl;
    cout << "  Ratios: 1.33, 1.00, 1.00" << endl;
    cout << "  Greedy: takes (6,8) -> value 8. Can't fit more." << endl;
    cout << "  Optimal: (5,5)+(5,5) -> value 10" << endl;
    cout << "  Greedy is WRONG for 0/1 knapsack!" << endl << endl;

    // ── Part 3: Exchange Argument ──
    cout << "=== Part 3: Exchange Argument ===" << endl;
    cout << "  1. Greedy picks earliest-ending activity" << endl;
    cout << "  2. Optimal may pick a different one" << endl;
    cout << "  3. Swap optimal's choice with greedy's: still valid!" << endl;
    cout << "  4. Repeat until optimal = greedy" << endl;
    cout << "  Therefore greedy is optimal!" << endl;

    return 0;
}
