/*
 * Challenge 4: Candy Distribution
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Min candies with neighbor rating constraints.
 * EXAMPLES: solve({1,0,2}) -> 5
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<int> ratings) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> ratings(n);
    for (int i = 0; i < n; i++) cin >> ratings[i];
    cout << solve(ratings) << endl;
    return 0;
}
