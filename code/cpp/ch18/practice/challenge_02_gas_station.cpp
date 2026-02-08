/*
 * Challenge 2: Gas Station
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Find starting station for circular trip. -1 if impossible.
 * EXAMPLES: solve({1,2,3,4,5}, {3,4,5,1,2}) -> 3
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<int> gas, vector<int> cost) {
    // TODO: Replace this with your solution
    return -1;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> gas(n), cost(n);
    for (int i = 0; i < n; i++) cin >> gas[i];
    for (int i = 0; i < n; i++) cin >> cost[i];
    cout << solve(gas, cost) << endl;
    return 0;
}
