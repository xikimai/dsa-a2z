/*
 * Warmup 4: Lemonade Change
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Each lemonade costs $5. Can you make change for everyone?
 * EXAMPLES: solve({5,5,5,10,20}) -> true
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> bills) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> bills(n);
    for (int i = 0; i < n; i++) cin >> bills[i];
    cout << (solve(bills) ? "true" : "false") << endl;
    return 0;
}
