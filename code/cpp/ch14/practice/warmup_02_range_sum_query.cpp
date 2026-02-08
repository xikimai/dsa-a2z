/*
 * Warmup 2: Range Sum Query
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Given array and queries [l, r], return sum of arr[l..r] for each.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr, vector<vector<int>> queries) {
    // TODO: Replace this with your solution
    return vector<long long>(queries.size(), 0);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int q;
    cin >> q;
    vector<vector<int>> queries(q, vector<int>(2));
    for (int i = 0; i < q; i++) cin >> queries[i][0] >> queries[i][1];
    auto result = solve(arr, queries);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
