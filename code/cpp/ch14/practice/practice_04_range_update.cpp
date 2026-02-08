/*
 * Practice 4: Range Update with Difference Array
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Start with n zeros. Apply updates [l, r, val]. Return final array.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(int n, vector<vector<int>> updates) {
    // TODO: Replace this with your solution
    return vector<long long>(n, 0);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<int>> updates(q, vector<int>(3));
    for (int i = 0; i < q; i++) cin >> updates[i][0] >> updates[i][1] >> updates[i][2];
    auto result = solve(n, updates);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
