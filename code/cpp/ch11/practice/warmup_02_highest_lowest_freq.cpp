/*
 * Warmup 2: Highest and Lowest Frequency
 * ========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array of integers, return a vector {highest_freq_element,
 *   lowest_freq_element}. Test inputs guarantee that each element has a
 *   unique frequency.
 *
 * EXAMPLES:
 *   solve({1,2,2,3,3,3})        -> {3,1}
 *   solve({10,10,10,20,20,30})  -> {10,30}
 *   solve({5})                  -> {5,5}
 *
 * CONSTRAINTS:
 *   - 1 <= arr.size() <= 10^5
 *   - Each element has a unique frequency
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

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return {0, 0};
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
