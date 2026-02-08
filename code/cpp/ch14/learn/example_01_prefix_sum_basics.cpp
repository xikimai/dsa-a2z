/*
 * Example 01: Prefix Sum Basics
 * ==============================
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * Demonstrates:
 *   Part 1: Building a 1D prefix sum array
 *   Part 2: Answering range sum queries in O(1)
 *   Part 3: Difference array for range updates
 */

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // ── Part 1: Building a Prefix Sum Array ──
    cout << "=== Part 1: Building a Prefix Sum Array ===" << endl;
    vector<int> arr = {3, 1, 4, 1, 5, 9, 2, 6};
    int n = arr.size();
    vector<long long> prefix(n + 1, 0);

    cout << "  arr = [";
    for (int i = 0; i < n; i++) cout << arr[i] << (i < n-1 ? ", " : "");
    cout << "]" << endl;

    for (int i = 1; i <= n; i++) {
        prefix[i] = prefix[i-1] + arr[i-1];
        cout << "  prefix[" << i << "] = prefix[" << i-1 << "] + arr[" << i-1
             << "] = " << prefix[i-1] << " + " << arr[i-1] << " = " << prefix[i] << endl;
    }

    cout << "  prefix = [";
    for (int i = 0; i <= n; i++) cout << prefix[i] << (i < n ? ", " : "");
    cout << "]" << endl << endl;

    // ── Part 2: Range Sum Queries ──
    cout << "=== Part 2: Range Sum Queries in O(1) ===" << endl;
    vector<pair<int,int>> queries = {{0,7}, {2,5}, {0,0}, {4,7}, {3,3}};
    for (auto [l, r] : queries) {
        long long result = prefix[r+1] - prefix[l];
        cout << "  sum(" << l << ", " << r << ") = prefix[" << r+1
             << "] - prefix[" << l << "] = " << prefix[r+1] << " - "
             << prefix[l] << " = " << result << endl;
    }
    cout << endl;

    // ── Part 3: Difference Array ──
    cout << "=== Part 3: Difference Array for Range Updates ===" << endl;
    int sz = 6;
    vector<long long> diff(sz + 1, 0);
    vector<tuple<int,int,int>> updates = {{1,3,5}, {2,4,3}};

    for (auto [l, r, val] : updates) {
        diff[l] += val;
        if (r + 1 < sz) diff[r + 1] -= val;
        cout << "  Add " << val << " to [" << l << ", " << r << "]" << endl;
    }

    vector<long long> result(sz);
    long long running = 0;
    for (int i = 0; i < sz; i++) {
        running += diff[i];
        result[i] = running;
    }

    cout << "  Final array: [";
    for (int i = 0; i < sz; i++) cout << result[i] << (i < sz-1 ? ", " : "");
    cout << "]" << endl;

    return 0;
}
