/*
 * Solution for Practice 4: Count Subarrays with Sum K
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Prefix sum + frequency map. For each prefix sum, check
 *           how many times (prefix_sum - k) has appeared before.
 *           Initialise map with {0: 1} for the empty prefix.
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
    unordered_map<long long, int> prefix_count;
    prefix_count[0] = 1;
    long long prefix_sum = 0;
    int count = 0;
    for (int x : arr) {
        prefix_sum += x;
        long long need = prefix_sum - k;
        if (prefix_count.count(need)) {
            count += prefix_count[need];
        }
        prefix_count[prefix_sum]++;
    }
    return count;
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
