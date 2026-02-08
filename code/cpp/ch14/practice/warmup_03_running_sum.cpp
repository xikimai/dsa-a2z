/*
 * Warmup 3: Running Sum of Array
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Return running_sum where running_sum[i] = arr[0]+...+arr[i].
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    auto result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
