/*
 * Solution for Warmup 5: Intersection of Two Arrays
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Insert first array into an unordered_set, then iterate
 *           second array and collect common elements in a result set.
 *           Sort the result before returning.
 * TIME:  O(n + m + k log k) where k = intersection size
 * SPACE: O(n + m)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> solve(vector<int> a, vector<int> b) {
    unordered_set<int> set_a(a.begin(), a.end());
    unordered_set<int> found;
    for (int x : b) {
        if (set_a.count(x)) {
            found.insert(x);
        }
    }
    vector<int> result(found.begin(), found.end());
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, m;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) cin >> b[i];
    vector<int> result = solve(a, b);
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}
