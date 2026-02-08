/*
 * Solution for Warmup 1: Frequency Count
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Use unordered_map to count frequencies, then collect
 *           into a vector of {value, count} pairs and sort by value.
 * TIME:  O(n log n) — n for counting, n log n for sorting
 * SPACE: O(n) — hash map storage
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> arr) {
    unordered_map<int, int> freq;
    for (int x : arr) {
        freq[x]++;
    }
    vector<vector<int>> result;
    for (auto& [val, cnt] : freq) {
        result.push_back({val, cnt});
    }
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<int>> result = solve(arr);
    for (auto& p : result) {
        cout << p[0] << " " << p[1] << endl;
    }
    return 0;
}
