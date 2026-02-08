/*
 * Warmup 1: Frequency Count
 * ==========================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array of integers, return a sorted list of {value, count}
 *   pairs sorted by value in ascending order.
 *
 * EXAMPLES:
 *   solve({1,2,2,3,3,3})  -> {{1,1},{2,2},{3,3}}
 *   solve({5})             -> {{5,1}}
 *   solve({})              -> {}
 *   solve({3,1,2,1})       -> {{1,2},{2,1},{3,1}}
 *
 * CONSTRAINTS:
 *   - 0 <= arr.size() <= 10^5
 *   - Elements can be any integer
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return {};
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
