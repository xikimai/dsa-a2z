/*
 * Solution for Warmup 2: Highest and Lowest Frequency
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count frequencies with unordered_map, then find the
 *           elements with the highest and lowest frequencies.
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

vector<int> solve(vector<int> arr) {
    unordered_map<int, int> freq;
    for (int x : arr) {
        freq[x]++;
    }
    int high_elem = 0, high_cnt = 0;
    int low_elem = 0, low_cnt = INT_MAX;
    for (auto& [val, cnt] : freq) {
        if (cnt > high_cnt) {
            high_cnt = cnt;
            high_elem = val;
        }
        if (cnt < low_cnt) {
            low_cnt = cnt;
            low_elem = val;
        }
    }
    return {high_elem, low_elem};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
