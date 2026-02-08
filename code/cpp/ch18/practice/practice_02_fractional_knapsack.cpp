/*
 * Practice 2: Fractional Knapsack
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Max value with fractional items.
 * EXAMPLES: solve(50, {{10,60},{20,100},{30,120}}) -> 240.0
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

double solve(int capacity, vector<pair<int,int>> items) {
    // TODO: Replace this with your solution
    return 0.0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int cap, n; cin >> cap >> n;
    vector<pair<int,int>> items(n);
    for (int i = 0; i < n; i++) cin >> items[i].first >> items[i].second;
    cout << fixed << setprecision(4) << solve(cap, items) << endl;
    return 0;
}
