/*
 * Solution -- Practice 1: Union of Two Arrays
 * =============================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Insert all elements from both arrays into an unordered_set
 *   (removes duplicates automatically). Then copy to a vector and sort.
 *
 * TIME COMPLEXITY:  O((n+m) * log(n+m)) — dominated by the sort
 * SPACE COMPLEXITY: O(n+m)
 */

#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& a, vector<int>& b) {
    unordered_set<int> seen;
    for (int x : a) seen.insert(x);
    for (int x : b) seen.insert(x);

    vector<int> result(seen.begin(), seen.end());
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int m;
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) cin >> b[i];
    vector<int> result = solve(a, b);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
