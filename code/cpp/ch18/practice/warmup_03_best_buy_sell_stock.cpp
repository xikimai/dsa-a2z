/*
 * Warmup 3: Best Time to Buy and Sell Stock
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Max profit from one buy-sell. Return 0 if no profit.
 * EXAMPLES: solve({7,1,5,3,6,4}) -> 5
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> prices) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) cin >> prices[i];
    cout << solve(prices) << endl;
    return 0;
}
