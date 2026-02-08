/*
 * Solution for Practice 3: Longest Subarray with Sum K
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Prefix sum + hash map. Store the first occurrence of each
 *           prefix sum. For each position, check if (prefix_sum - k)
 *           has been seen before — that gives a subarray with sum k.
 * TIME:  O(n)
 * SPACE: O(n)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int solve(vector<int> arr, int k) {
    unordered_map<long long, int> first_seen;
    first_seen[0] = -1;  // empty prefix at index -1
    long long prefix_sum = 0;
    int max_len = 0;
    for (int i = 0; i < (int)arr.size(); i++) {
        prefix_sum += arr[i];
        long long need = prefix_sum - k;
        if (first_seen.count(need)) {
            max_len = max(max_len, i - first_seen[need]);
        }
        if (!first_seen.count(prefix_sum)) {
            first_seen[prefix_sum] = i;
        }
    }
    return max_len;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr, k) << endl;
    return 0;
}
