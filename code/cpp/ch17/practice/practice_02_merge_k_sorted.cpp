/*
 * Practice 2: Merge K Sorted Arrays
 * ====================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given K sorted arrays, merge them into one sorted array.
 *
 * EXAMPLES:
 *   solve({{1,4,7},{2,5,8},{3,6,9}})  -> {1,2,3,4,5,6,7,8,9}
 *   solve({{1,3,5},{2,4,6}})          -> {1,2,3,4,5,6}
 *
 * CONSTRAINTS:
 *   - 0 <= K <= 100
 *   - 0 <= arrays[i].size() <= 10^4
 *   - Each array is sorted in ascending order
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;

vector<int> solve(vector<vector<int>> arrays) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int k;
    cin >> k;
    vector<vector<int>> arrays(k);
    for (int i = 0; i < k; i++) {
        int n;
        cin >> n;
        arrays[i].resize(n);
        for (int j = 0; j < n; j++) cin >> arrays[i][j];
    }
    vector<int> result = solve(arrays);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
