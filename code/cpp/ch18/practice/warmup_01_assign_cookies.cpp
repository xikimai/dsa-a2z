/*
 * Warmup 1: Assign Cookies
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Maximize content children. Cookie >= greed means content.
 * EXAMPLES: solve({1,2,3}, {1,1}) -> 1
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> greed, vector<int> cookies) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, m;
    cin >> n;
    vector<int> greed(n);
    for (int i = 0; i < n; i++) cin >> greed[i];
    cin >> m;
    vector<int> cookies(m);
    for (int i = 0; i < m; i++) cin >> cookies[i];
    cout << solve(greed, cookies) << endl;
    return 0;
}
